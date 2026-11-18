# CyberMitra - Cyber Security Solutions

> **Spot the Scam Before It Spots You.**\
> Your digital safety companion for a safer internet.

![Project](https://img.shields.io/badge/Project-CyberMitra-2563EB?style=for-the-badge)
![Frontend](https://img.shields.io/badge/Frontend-React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Backend](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Database](https://img.shields.io/badge/Database-PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Deployment](https://img.shields.io/badge/Deployment-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

CyberMitra is a bilingual cybersecurity awareness and assistance
platform designed to help people recognize online threats, understand
cyber fraud, and find practical cybercrime support resources. It brings
essential digital-safety information together in one accessible place
for English- and Hindi-speaking users.

------------------------------------------------------------------------

## About the Project

The internet creates opportunities for learning, communication, and
business, but it also exposes people to scams, identity theft, phishing,
and other cyber threats.

CyberMitra aims to make cybersecurity knowledge easier to understand and
act upon. The platform presents awareness resources, guidance for common
cyber-fraud situations, and links to relevant support channels.

## Key Features

  -----------------------------------------------------------------------
  Feature                             Description
  ----------------------------------- -----------------------------------
  Fraud Awareness                     Learn about suspicious messages,
                                      online scams, phishing, and common
                                      digital threats.

  Cybersecurity Support               Access practical guidance for safer
                                      online activity and responding to
                                      cyber risks.

  Complaint Assistance                Find guidance and relevant
                                      resources for reporting cybercrime.

  Emergency Resources                 Access important cybercrime support
                                      information and reporting
                                      resources.

  Bilingual Experience                Access platform information in
                                      English and Hindi.

  Responsive Interface                Use the platform across desktop and
                                      mobile screen sizes.

  Legal and Privacy Pages             Review the platform's Terms,
                                      Privacy, Refund, Shipping, and
                                      Contact information where provided.
  -----------------------------------------------------------------------

## Platform Preview

The application includes a user-facing web interface for browsing
cybersecurity awareness content and support resources.

> Add screenshots of the running application to `docs/screenshots/` and
> link them here when available.

```{=html}
<!-- Example:
![CyberMitra Home Page](docs/screenshots/homepage.png)
-->
```
## Technology Stack

  Layer                        Technology
  ---------------------------- ---------------------------
  Frontend                     React
  Backend API                  FastAPI
  Database                     PostgreSQL
  Containerization             Docker and Docker Compose
  Web Server / Reverse Proxy   Nginx

## Project Structure

``` text
CyberMitra/
├── backend/                 # FastAPI backend
├── frontend/                # React frontend
├── deploy/                  # Deployment-related files
├── nginx/                   # Nginx configuration
├── docker-compose.yml       # Main application services
├── docker-compose.https.yml # HTTPS deployment override
├── .env.example             # Environment variable template
├── .gitignore
└── README.md
```

The exact contents may vary as the project evolves.

## Run Locally with Docker

### Prerequisites

-   Git
-   Docker Desktop
-   Docker Compose (included with current Docker Desktop releases)

### 1. Clone the repository

``` bash
git clone https://github.com/rohitrksingh1920/CyberMitra.git
cd CyberMitra
```

### 2. Create the environment file

On Windows Command Prompt:

``` bat
copy .env.example .env
```

On macOS or Linux:

``` bash
cp .env.example .env
```

Open `.env` and configure the required values. Set a strong PostgreSQL
password and a strong `ADMIN_API_KEY`. Do not commit `.env` or share its
secrets.

### 3. Build and start the application

``` bash
docker compose up --build -d
```

### 4. Check container status

``` bash
docker compose ps
```

### 5. View application logs

``` bash
docker compose logs -f
```

### 6. Stop the application

``` bash
docker compose down
```

To remove the containers and the associated named database volume, use
`docker compose down -v` only when you intentionally want to delete the
local database data.

## Deployment

CyberMitra includes Docker Compose and Nginx configuration intended to
support deployment on a Linux server, such as an AWS EC2 instance.

Before enabling HTTPS:

1.  Point your domain and any required subdomain records to the server.
2.  Configure the production environment variables securely.
3.  Restrict inbound server access to the required ports using the cloud
    firewall/security group.
4.  Verify the HTTP deployment before requesting certificates.
5.  Configure and test certificate renewal and Nginx reload behavior.

The HTTPS configuration requires a domain that resolves to the server.
Do not run the certificate initialization script until DNS and server
access are configured.

## Security and Privacy

-   Keep `.env` files and credentials out of version control.
-   Use strong, unique production secrets.
-   Do not expose database ports publicly unless there is a specific
    secured requirement.
-   Configure CORS for the actual production domains.
-   Keep Docker images and application dependencies updated.
-   Do not publish private keys, certificates, database dumps, or user
    data.
-   Review the application's legal and privacy pages before public
    release.

## Testing and Verification

Before deployment, verify that:

-   The frontend loads successfully.
-   Backend API requests reach the FastAPI service through Nginx.
-   The database connection is healthy.
-   Environment variables are configured for the target environment.
-   The application works on desktop and mobile layouts.
-   HTTPS and certificate renewal are tested on the target server.

## Project Roadmap

-   [ ] Continue improving English and Hindi content.
-   [ ] Expand cybersecurity awareness resources.
-   [ ] Improve the reporting and support guidance.
-   [ ] Complete production deployment.
-   [ ] Verify HTTPS renewal and operational monitoring.
-   [ ] Improve accessibility and mobile experience.

## Contributing

Contributions, suggestions, and bug reports are welcome.

1.  Fork the repository.
2.  Create a feature branch.
3.  Make your changes.
4.  Test the changes locally.
5.  Open a pull request with a clear description.

Please do not include passwords, API keys, private certificates,
database backups, or personal data in commits.

## License

Refer to the repository's `LICENSE` file for licensing terms, if
present.

## Contact and Support

For project questions, suggestions, or feedback, open an issue in the
[CyberMitra GitHub
repository](https://github.com/rohitrksingh1920/CyberMitra).

------------------------------------------------------------------------

**CyberMitra - Your Safety, Your Awareness, Your Digital Future.**

*Building awareness today for a safer digital tomorrow.*
