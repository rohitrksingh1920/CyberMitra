# ðŸ›¡ï¸ CyberMitra â€” Cyber Security Solutions

> **Spot the Scam Before It Spots You.**
> Your digital safety companion for a safer internet.

![Project](https://img.shields.io/badge/Project-CyberMitra-2563EB?style=for-the-badge)
![Frontend](https://img.shields.io/badge/Frontend-React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Backend](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Database](https://img.shields.io/badge/Database-PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Deployment](https://img.shields.io/badge/Deployment-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

CyberMitra is a bilingual cybersecurity awareness and assistance platform designed to help people recognize online threats, understand cyber fraud, and access practical cybercrime support resources. It brings essential digital-safety information together in one accessible place, with an experience for both English- and Hindi-speaking users.

---

## ðŸŒ About the Project

The internet creates opportunities for learning, communication, and business, but it also exposes people to scams, identity theft, phishing, and other cyber threats.

**CyberMitra â€” Cyber Security Solutions** aims to make cybersecurity knowledge easier to understand and act upon. The platform focuses on awareness, guidance, and access to useful support information.

> **Our mission:** Make digital safety knowledge accessible to everyone.

## âœ¨ Key Features

| Feature | What it offers |
| --- | --- |
| ðŸ” Fraud Awareness | Learn to identify suspicious messages, calls, links, and common online scams. |
| ðŸš¨ Cybercrime Support | Find guidance and useful resources when dealing with cybercrime. |
| ðŸ“‹ Complaint Assistance | Access complaint-related information and FIR preparation resources. |
| ðŸ“ž Emergency Resources | Find important cybercrime reporting contacts and emergency numbers. |
| ðŸŒ Bilingual Experience | Explore cybersecurity awareness information in English and Hindi. |
| ðŸ“± Responsive Interface | Use the platform across desktop, tablet, and mobile screens. |
| ðŸ“„ Legal & Privacy Pages | Access the platform's terms, privacy, refund, shipping, and contact information where applicable. |

## ðŸ–¥ï¸ Platform Preview

The screenshots below can be added when final application screenshots are available.

| English Experience | Hindi Experience |
| --- | --- |
| _Add `docs/images/english-home.png`_ | _Add `docs/images/hindi-home.png`_ |

To display your own screenshots, create a `docs/images/` folder, add the images, and replace the placeholders above with:

```md
![CyberMitra English interface](docs/images/english-home.png)
![CyberMitra Hindi interface](docs/images/hindi-home.png)
```

## ðŸ§° Technology Stack

| Layer | Technology |
| --- | --- |
| Frontend | React, JavaScript, Vite |
| Backend | Python, FastAPI |
| Database | PostgreSQL |
| ORM / Data access | SQLAlchemy |
| Reverse proxy | Nginx |
| Containerization | Docker |
| Orchestration | Docker Compose |
| Version control | Git and GitHub |

<p align="center">
  <img src="https://skillicons.dev/icons?i=react,js,python,fastapi,postgres,docker,nginx,git,github,vite" alt="Technology stack icons" />
</p>

## ðŸ—ï¸ Project Structure

```text
CyberMitra/
â”œâ”€â”€ backend/
â”‚   â”œâ”€â”€ app/
â”‚   â”‚   â”œâ”€â”€ routers/
â”‚   â”‚   â”œâ”€â”€ utils/
â”‚   â”‚   â”œâ”€â”€ main.py
â”‚   â”‚   â”œâ”€â”€ config.py
â”‚   â”‚   â”œâ”€â”€ database.py
â”‚   â”‚   â”œâ”€â”€ models.py
â”‚   â”‚   â””â”€â”€ schemas.py
â”‚   â”œâ”€â”€ Dockerfile
â”‚   â””â”€â”€ requirements.txt
â”œâ”€â”€ frontend/
â”‚   â”œâ”€â”€ public/
â”‚   â”œâ”€â”€ src/
â”‚   â”‚   â”œâ”€â”€ components/
â”‚   â”‚   â”œâ”€â”€ context/
â”‚   â”‚   â”œâ”€â”€ data/
â”‚   â”‚   â””â”€â”€ styles/
â”‚   â””â”€â”€ Dockerfile
â”œâ”€â”€ deploy/
â”œâ”€â”€ nginx/
â”œâ”€â”€ docker-compose.yml
â”œâ”€â”€ docker-compose.dev.yml
â”œâ”€â”€ docker-compose.https.yml
â”œâ”€â”€ .env.example
â”œâ”€â”€ .gitignore
â””â”€â”€ README.md
```

## ðŸš€ Run Locally with Docker

### Prerequisites

Install the following tools:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Git](https://git-scm.com/)

Docker Compose is included with current Docker Desktop installations.

### 1. Clone the repository

```bash
git clone https://github.com/rohitrksingh1920/CyberMitra.git
cd CyberMitra
```

### 2. Create your environment file

**Windows PowerShell:**

```powershell
Copy-Item .env.example .env
```

**Linux / macOS:**

```bash
cp .env.example .env
```

Open `.env` and configure the values required by your local environment. Use a strong database password and a private API/admin key where required.

**Security:** Never commit your real `.env` file, passwords, API keys, private certificates, or production credentials. The repository includes `.env.example` as a safe template.

### 3. Build and start the application

```bash
docker compose --env-file .env up -d --build
```

### 4. Check container status

```bash
docker compose ps
```

### 5. View application logs

```bash
docker compose logs -f
```

### 6. Stop the application

```bash
docker compose down
```

To stop the containers without deleting persistent database volumes, use the command above. **Do not add `-v`** unless you intentionally want to remove the associated volumes and their stored data.

## âš™ï¸ Configuration

The root `.env.example` documents the environment variables expected by the Docker Compose deployment. Review it before starting the application and provide appropriate values in your local `.env`.

For deployment, configure domain-specific CORS origins, strong credentials, persistent storage, and any required application secrets. Do not share secret values in screenshots, issues, or chat messages.

## â˜ï¸ Deployment

CyberMitra uses Docker Compose and Nginx, making it suitable for deployment on a Linux virtual machine such as **AWS EC2** or another Docker-capable server.

A typical production deployment involves:

1. Provision a Linux server and restrict inbound access using its firewall/security group.
2. Install Docker Engine and the Docker Compose plugin.
3. Clone the repository onto the server.
4. Create and securely configure the production `.env` file.
5. Configure the domain's DNS records to point to the server.
6. Configure HTTPS using the supplied Nginx and Certbot deployment files.
7. Start the production Compose services.
8. Verify the frontend, API, database connectivity, and HTTPS configuration.
9. Configure database backups, monitoring, and a certificate-renewal reload process.

The HTTPS setup requires a real domain with the required DNS records already pointing to the server. Review the deployment scripts and Compose files for your environment before running them. Do not treat HTTPS as configured until certificate issuance, Nginx configuration validation, renewal, and browser access have all been tested.

## ðŸ” Security & Privacy

- Keep `.env` files and production credentials out of version control.
- Use strong, unique passwords and secret keys.
- Restrict database access to the application network; do not expose the database publicly.
- Configure CORS with only the trusted frontend origins.
- Use HTTPS for production traffic.
- Keep Docker images and application dependencies updated.
- Back up persistent data securely.
- Never commit private keys, certificates, database dumps, or user data.

## ðŸ§ª Testing & Verification

Before a release or deployment, verify:

- Frontend production build completes successfully.
- Backend starts and its API endpoints respond as expected.
- Backend can connect to PostgreSQL.
- English and Hindi content displays correctly.
- Navigation and responsive layouts work on supported screen sizes.
- Complaint-assistance and reporting-related workflows behave as expected.
- Docker containers remain healthy.
- Nginx routing and HTTPS work correctly in the target environment.

## ðŸ—ºï¸ Project Roadmap

- [x] English and Hindi user experience
- [x] Cybersecurity awareness content
- [x] Responsive frontend
- [x] Docker-based application setup
- [x] PostgreSQL integration
- [x] Legal and information pages
- [ ] Production cloud deployment
- [ ] Expanded cybersecurity awareness resources
- [ ] Further improvements based on user feedback

## ðŸ¤ Contributing

Suggestions, bug reports, and improvements are welcome.

1. Fork the repository or create an authorized feature branch.
2. Create a branch for your change.
3. Make your changes and test them.
4. Commit with a clear message.
5. Open a pull request describing the change.

Please do not include secrets, personal information, or real complaint data in issues or pull requests.

## ðŸ“œ License

Refer to the repository's `LICENSE` file for licensing terms, if present.

## ðŸ“¬ Contact & Support

For questions, suggestions, or feedback, open an issue in the [CyberMitra GitHub repository](https://github.com/rohitrksingh1920/CyberMitra).

---

<p align="center">

**ðŸ›¡ï¸ CyberMitra â€” Your Safety. Your Awareness. Your Digital Future.**

_Building awareness today for a safer digital tomorrow._

</p>
