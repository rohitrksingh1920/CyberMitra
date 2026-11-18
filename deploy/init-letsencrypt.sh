#!/usr/bin/env bash
# One-time HTTPS setup with Let's Encrypt, for the Docker Compose stack in this repo.
#
#   1. Point your domain's A records (@ and www) at this server and open ports 80 + 443.
#   2. Create .env (see .env.example).
#   3. Run:   DOMAIN=example.com EMAIL=you@example.com ./deploy/init-letsencrypt.sh
#      (first try with STAGING=1 in front to test without using up Let's Encrypt's rate limits)
#
# What it does: swaps nginx/conf.d/app.conf for the HTTPS version, starts nginx with a throw-away
# certificate, asks Let's Encrypt for a real one, reloads nginx and starts everything.
# Safe to re-run; pass --force to issue a new certificate.

set -euo pipefail
cd "$(dirname "$0")/.."

DOMAIN="${DOMAIN:-}"
EMAIL="${EMAIL:-}"
STAGING="${STAGING:-0}"
FORCE=0; [[ "${1:-}" == "--force" ]] && FORCE=1

if [[ -z "$DOMAIN" || -z "$EMAIL" ]]; then
  echo "Usage: DOMAIN=example.com EMAIL=you@example.com ./deploy/init-letsencrypt.sh"; exit 1
fi
[[ -f .env ]] || { echo "Missing .env - copy .env.example to .env and fill it in first."; exit 1; }

COMPOSE="docker compose -f docker-compose.yml -f docker-compose.https.yml"
CONF="./deploy/certbot-data/conf"
WWW="./deploy/certbot-data/www"
LIVE="$CONF/live/$DOMAIN"
mkdir -p "$CONF" "$WWW"

echo ">> Installing the HTTPS nginx config for $DOMAIN"
[[ -f nginx/conf.d/app.conf && ! -f nginx/conf.d/app.http.conf.bak ]] && cp nginx/conf.d/app.conf nginx/conf.d/app.http.conf.bak
sed "s/__DOMAIN__/${DOMAIN}/g" nginx/https/app.conf.template > nginx/conf.d/app.conf

if [[ -e "$LIVE/fullchain.pem" && $FORCE -eq 0 ]]; then
  echo ">> A certificate for $DOMAIN already exists - starting the stack (use --force to re-issue)."
  $COMPOSE up -d --build
  grep -q '^COMPOSE_FILE=' .env || echo 'COMPOSE_FILE=docker-compose.yml:docker-compose.https.yml' >> .env
  exit 0
fi

echo ">> Creating a temporary self-signed certificate so nginx can start..."
mkdir -p "$LIVE"
docker run --rm -v "$(pwd)/$CONF:/etc/letsencrypt" --entrypoint openssl certbot/certbot \
  req -x509 -nodes -newkey rsa:2048 -days 1 -subj "/CN=localhost" \
  -keyout "/etc/letsencrypt/live/$DOMAIN/privkey.pem" -out "/etc/letsencrypt/live/$DOMAIN/fullchain.pem"

echo ">> Starting the stack with the temporary certificate..."
$COMPOSE up -d --build

echo ">> Requesting the real certificate from Let's Encrypt..."
rm -rf "$LIVE" "$CONF/archive/$DOMAIN" "$CONF/renewal/$DOMAIN.conf"
STAGING_ARG=""; [[ "$STAGING" == "1" ]] && STAGING_ARG="--staging"
$COMPOSE run --rm --entrypoint certbot certbot certonly --webroot -w /var/www/certbot \
  -d "$DOMAIN" -d "www.$DOMAIN" --email "$EMAIL" --agree-tos --no-eff-email --non-interactive $STAGING_ARG

echo ">> Reloading nginx with the real certificate..."
$COMPOSE exec proxy nginx -s reload

# From now on a plain `docker compose up -d` should include the HTTPS files too
grep -q '^COMPOSE_FILE=' .env || echo 'COMPOSE_FILE=docker-compose.yml:docker-compose.https.yml' >> .env

echo
echo "Done: https://$DOMAIN"
[[ "$STAGING" == "1" ]] && echo "(That was a STAGING certificate - browsers will warn. Re-run with --force and without STAGING=1.)"
