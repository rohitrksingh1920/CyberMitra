# 🛡️ CyberMitra --- Cyber Security Solutions

```{=html}
<p align="center">
```
`<img src="frontend/public/cybermitra-logo.png" alt="CyberMitra Logo" width="180" />`{=html}
```{=html}
</p>
```
```{=html}
<h3 align="center">
```
Spot the Scam Before It Spots You.
```{=html}
</h3>
```
```{=html}
<p align="center">
```
`<strong>`{=html}Your digital safety companion for a safer
internet.`</strong>`{=html}
```{=html}
</p>
```
```{=html}
<p align="center">
```
A bilingual cybersecurity awareness and assistance platform helping
people recognize online threats, understand cyber fraud, and access
practical cybercrime support resources.
```{=html}
</p>
```
```{=html}
<p align="center">
```
`<img src="https://img.shields.io/badge/Project-CyberMitra-2563EB?style=for-the-badge" alt="CyberMitra" />`{=html}
`<img src="https://img.shields.io/badge/Frontend-React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React" />`{=html}
`<img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />`{=html}
`<img src="https://img.shields.io/badge/Database-PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />`{=html}
`<img src="https://img.shields.io/badge/Deployment-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />`{=html}
```{=html}
</p>
```

------------------------------------------------------------------------

## 🌐 About CyberMitra

The internet creates opportunities for learning, communication, and
business, but it also exposes people to increasingly sophisticated cyber
threats. Many users are unsure how to identify scams, what to do after a
cyber incident, or where to find reliable reporting guidance.

**CyberMitra -- Cyber Security Solutions** is designed to make digital
safety knowledge easier to understand and act on. It brings
cybersecurity awareness, fraud-prevention information, complaint
assistance, and emergency resources together in one accessible platform.

The platform is designed with English- and Hindi-speaking users in mind.

> **Our mission: Make digital safety knowledge accessible to everyone.**

## ✨ Key Features

  -----------------------------------------------------------------------
  Feature                             Description
  ----------------------------------- -----------------------------------
  🔍 Fraud Awareness                  Learn to recognize suspicious
                                      messages, calls, links, phishing
                                      attempts, and common online scams.

  🚨 Cybercrime Support               Find practical guidance and
                                      resources for responding to
                                      cybercrime incidents.

  📋 Complaint Assistance             Access complaint-related
                                      information and guidance for
                                      preparing incident details.

  📞 Emergency Resources              Find useful cybercrime reporting
                                      contacts and support information.

  🌏 Bilingual Experience             Access cybersecurity awareness
                                      content in English and Hindi.

  📱 Responsive Interface             Use the platform across desktop,
                                      tablet, and mobile screen sizes.

  🛡️ Security-focused design          Uses a backend API,
                                      environment-based configuration,
                                      and reverse-proxy deployment
                                      architecture.
  -----------------------------------------------------------------------

*Feature availability may depend on the current application build and
deployment configuration.*

## 🖥️ Platform Preview

Add screenshots of the running application to the table below when
available.

      English Experience          Hindi Experience
  --------------------------- -------------------------
   Add English UI screenshot   Add Hindi UI screenshot

## 🧰 Technology Stack

CyberMitra combines a modern web frontend, a Python API, a relational
database, and container-based deployment.

  Layer               Technology
  ------------------- -------------------------
  Frontend            React, JavaScript, Vite
  Backend             Python, FastAPI
  Database            PostgreSQL
  ORM / Data Access   SQLAlchemy
  Reverse Proxy       Nginx
  Containerization    Docker
  Orchestration       Docker Compose
  Version Control     Git and GitHub

## 🏗️ Project Structure

``` text
CyberMitra/
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   ├── utils/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── limiter.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── .dockerignore
│   ├── Dockerfile
│   └── requirements.txt
├── deploy/
│   └── init-letsencrypt.sh
├── frontend/
│   ├── partials/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── context/
│   │   ├── data/
│   │   └── styles/
│   ├── Dockerfile
│   └── legal.config.json
├── nginx/
│   ├── conf.d/
│   ├── https/
│   │   └── app.conf.template
│   └── nginx.conf
├── docker-compose.yml
├── docker-compose.dev.yml
├── docker-compose.https.yml
├── .env.example
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Install the following tools:

-   [Git](https://git-scm.com/)
-   [Docker Desktop](https://www.docker.com/products/docker-desktop/) on
    Windows or Docker Engine on Linux
-   Docker Compose v2 (included with current Docker Desktop
    installations)

### 1. Clone the repository

``` bash
git clone https://github.com/rohitrksingh1920/CyberMitra.git
cd CyberMitra
```

### 2. Configure environment variables

Create your local environment file from the example.

**Windows PowerShell**

``` powershell
Copy-Item .env.example .env
```

**Linux / macOS**

``` bash
cp .env.example .env
```

Open `.env` and configure the values required by your environment. At
minimum, review the database credentials, allowed frontend origins, and
administrative API key.

Use strong, unique values for secrets. Do not copy production
credentials into documentation or commit your `.env` file.

### 3. Build and start the application

``` bash
docker compose --env-file .env up -d --build
```

### 4. Check container status

``` bash
docker compose ps
```

### 5. View application logs

``` bash
docker compose logs -f
```

To inspect one service:

``` bash
docker compose logs -f backend
docker compose logs -f frontend
docker compose logs -f proxy
docker compose logs -f db
```

### 6. Stop the application

``` bash
docker compose down
```

To stop the application and remove its containers and network while
retaining named database volumes:

``` bash
docker compose down
```

**Note:** Do not add `-v` unless you intentionally want to remove the
named volumes and understand the data-loss implications.

## 🧪 Development Configuration

The repository includes a development Compose configuration. Review
`docker-compose.dev.yml` before using it, then start the development
stack with:

``` bash
docker compose -f docker-compose.yml -f docker-compose.dev.yml --env-file .env up -d --build
```

The exact services, ports, and environment variables are defined in the
Compose files. Check the effective configuration before starting:

``` bash
docker compose --env-file .env -f docker-compose.yml config
```

## ☁️ Deployment

CyberMitra is packaged for deployment on a Linux server using Docker
Compose and Nginx. An AWS EC2 instance is one possible hosting target.

### Production deployment outline

1.  Provision a Linux server and restrict inbound access using its
    firewall / security group.
2.  Install Docker Engine and the Docker Compose plugin.
3.  Clone the repository onto the server.
4.  Create and securely configure the production `.env` file.
5.  Configure PostgreSQL persistence and take a backup plan into
    account.
6.  Point your domain's DNS records to the server.
7.  Configure the domain and HTTPS settings in the deployment
    configuration.
8.  Validate the Nginx and Docker Compose configuration.
9.  Start the application and verify frontend, API, database, and HTTPS
    connectivity.

### HTTPS / Let's Encrypt

The repository includes an HTTPS Compose override
(`docker-compose.https.yml`) and a certificate initialization script
(`deploy/init-letsencrypt.sh`).

Before using the initialization script:

-   Own or control the domain you intend to use.
-   Point the domain and any configured `www` hostname to the server.
-   Ensure ports 80 and 443 are reachable from the internet.
-   Configure the required environment variables on the server.
-   Review the script and Nginx template for your domain before
    execution.

Do not run certificate initialization with placeholder domains. After
certificate issuance, verify the Nginx configuration and confirm that
certificate renewal is followed by an Nginx reload so renewed
certificates are actually served.

## 🔐 Security and Privacy

-   Keep `.env` files and production secrets out of version control.
-   Use strong database passwords and administrative keys.
-   Restrict CORS origins to the trusted application domains.
-   Serve production traffic over HTTPS.
-   Keep database storage persistent and establish regular, tested
    backups.
-   Do not commit private keys, certificates, database dumps, or user
    data.
-   Keep dependencies and container images updated.
-   Review access controls, rate limits, logs, and error handling before
    production use.

## ✅ Testing and Verification

Before releasing a change, verify the areas relevant to that change:

-   Frontend production build.
-   Backend startup and API health.
-   Database connectivity and persistence.
-   Frontend-to-backend communication.
-   English and Hindi content.
-   Complaint and reporting workflows.
-   Responsive layout and navigation.
-   Docker Compose configuration and container health.
-   HTTP-to-HTTPS redirection and certificate validity in production.

Useful configuration validation:

``` bash
docker compose --env-file .env config --quiet
docker compose --env-file .env -f docker-compose.yml -f docker-compose.https.yml config --quiet
```

## 🗺️ Project Roadmap

-   [x] English and Hindi user experience
-   [x] Cybersecurity awareness content
-   [x] Responsive frontend
-   [x] Docker-based application setup
-   [x] PostgreSQL integration
-   [x] Legal and privacy information pages
-   [x] Production-oriented Compose and Nginx configuration
-   [ ] Complete cloud deployment
-   [ ] Verify production HTTPS and certificate renewal
-   [ ] Continue expanding cybersecurity awareness and assistance
    features

## 🤝 Contributing

Contributions and suggestions that improve digital safety are welcome.

1.  Fork the repository or create an authorized feature branch.
2.  Create a focused branch for your change.
3.  Make the change and test it.
4.  Commit with a clear message.
5.  Open a pull request describing the change and its verification.

## 📜 License

Refer to the repository's `LICENSE` file for licensing terms. If no
license file is present, contact the project maintainers before reusing
or distributing the code.

## 📬 Contact and Support

For questions, suggestions, or bug reports, open an issue in the
[CyberMitra GitHub
repository](https://github.com/rohitrksingh1920/CyberMitra) or use the
contact information published on the project website.

------------------------------------------------------------------------

```{=html}
<p align="center">
```
`<strong>`{=html}🛡️ CyberMitra --- Your Safety. Your Awareness. Your
Digital Future.`</strong>`{=html}
```{=html}
</p>
```
```{=html}
<p align="center">
```
Building awareness today for a safer digital tomorrow.
```{=html}
</p>
```
