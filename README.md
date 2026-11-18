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
A bilingual cybersecurity awareness platform helping individuals
recognize online threats, understand cyber fraud, and access practical
cybercrime support resources.
```{=html}
</p>
```
```{=html}
<p align="center">
```
`<img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Project Status" />`{=html}
`<img src="https://img.shields.io/badge/Frontend-React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React" />`{=html}
`<img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />`{=html}
`<img src="https://img.shields.io/badge/Database-PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />`{=html}
`<img src="https://img.shields.io/badge/Deployment-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />`{=html}
```{=html}
</p>
```

------------------------------------------------------------------------

## 🌐 About CyberMitra

The internet creates endless opportunities, but it also exposes people
to increasingly sophisticated cyber threats.

**CyberMitra -- Cyber Security Solutions** aims to make cybersecurity
awareness accessible, understandable, and actionable.

Built as a bilingual platform for English- and Hindi-speaking users,
CyberMitra brings together cyber safety education, fraud awareness,
reporting guidance, and useful emergency resources in one place.

Our mission is simple:

> **Make digital safety knowledge accessible to everyone.**

## ✨ What Makes CyberMitra Special?

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td width="50%">
```
```{=html}
<h3>
```
🔍 Fraud Awareness
```{=html}
</h3>
```
Learn to recognize suspicious messages, calls, links, and common online
scams.
```{=html}
</td>
```
```{=html}
<td width="50%">
```
```{=html}
<h3>
```
🚨 Cybercrime Support
```{=html}
</h3>
```
Find useful guidance and resources when dealing with cybercrime.
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td width="50%">
```
```{=html}
<h3>
```
📋 Complaint Assistance
```{=html}
</h3>
```
Access complaint-related information and FIR preparation resources.
```{=html}
</td>
```
```{=html}
<td width="50%">
```
```{=html}
<h3>
```
📞 Emergency Resources
```{=html}
</h3>
```
Find important cybercrime reporting contacts and emergency numbers.
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td width="50%">
```
```{=html}
<h3>
```
🌏 Bilingual Experience
```{=html}
</h3>
```
Explore cybersecurity awareness content in English and Hindi.
```{=html}
</td>
```
```{=html}
<td width="50%">
```
```{=html}
<h3>
```
📱 Responsive Interface
```{=html}
</h3>
```
Access the platform through desktop, tablet, and mobile devices.
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
## 🖥️ Platform Preview

```{=html}
<p align="center">
```
`<em>`{=html}CyberMitra --- Designed to make cybersecurity awareness
simple and accessible.`</em>`{=html}
```{=html}
</p>
```
```{=html}
<!-- Add your actual application screenshots here -->
```
     English Experience       Hindi Experience
  ------------------------ ----------------------
   Add English screenshot   Add Hindi screenshot

## ⚙️ Technology Behind CyberMitra

CyberMitra combines modern frontend technologies, a Python-powered
backend, and containerized deployment.

```{=html}
<p align="center">
```
`<img src="https://skillicons.dev/icons?i=react,js,python,fastapi,postgres,docker,nginx,git,github,vite" alt="Technology Stack" />`{=html}
```{=html}
</p>
```
  Layer              Technology
  ------------------ -------------------------
  Frontend           React, JavaScript, Vite
  Backend            Python, FastAPI
  Database           PostgreSQL
  ORM                SQLAlchemy
  Reverse Proxy      Nginx
  Containerization   Docker
  Orchestration      Docker Compose
  Version Control    Git, GitHub

## 🏗️ Project Architecture

``` text
CyberMitra/
│
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   ├── utils/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── context/
│   │   ├── data/
│   │   └── styles/
│   └── Dockerfile
│
├── deploy/
├── nginx/
├── docker-compose.yml
├── docker-compose.https.yml
├── .env.example
├── .gitignore
└── README.md
```

## 🚀 Getting Started

Want to run CyberMitra locally? Follow these steps.

### Prerequisites

Make sure you have installed:

-   [Docker Desktop](https://www.docker.com/products/docker-desktop/)
-   [Git](https://git-scm.com/)
-   Docker Compose (included with Docker Desktop)

### 1. Clone the Repository

``` bash
git clone https://github.com/rohitrksingh1920/CyberMitra.git
cd CyberMitra
```

### 2. Configure Environment Variables

Create your environment configuration file.

**Windows PowerShell:**

``` powershell
Copy-Item .env.example .env
```

**Linux / macOS:**

``` bash
cp .env.example .env
```

Open `.env` and configure the required credentials, database settings,
security keys, and other environment variables.

> 🔐 **Security First:** Never upload your actual `.env` file,
> passwords, API keys, or production credentials to GitHub.

### 3. Build and Launch CyberMitra

``` bash
docker compose --env-file .env up -d --build
```

### 4. Verify Running Containers

``` bash
docker compose ps
```

### 5. Monitor Application Logs

``` bash
docker compose logs -f
```

### 6. Stop the Application

``` bash
docker compose down
```

## ☁️ Deployment

CyberMitra is containerized using Docker Compose, making it suitable for
deployment on cloud-based Linux servers.

Potential deployment environments include:

-   **AWS EC2** -- Run the complete Docker Compose application on a
    Linux instance.
-   **Microsoft Azure** -- Deploy using suitable container hosting
    services.
-   **Other Linux VPS providers** -- Run the application with Docker and
    Nginx.

### Production Deployment Checklist

-   [ ] Prepare a Linux server.
-   [ ] Install Docker and Docker Compose.
-   [ ] Configure production environment variables.
-   [ ] Configure PostgreSQL and persistent storage.
-   [ ] Connect your domain and configure DNS.
-   [ ] Configure HTTPS using Let's Encrypt and Certbot.
-   [ ] Configure firewall rules and security settings.
-   [ ] Launch the Docker Compose services.
-   [ ] Verify frontend, backend, database, and HTTPS connectivity.

## 🔒 Security & Privacy

Security is an important part of CyberMitra.

-   Environment variables are excluded from version control.
-   Production secrets should be strong and private.
-   API access should be restricted to configured origins.
-   Application traffic should use HTTPS in production.
-   Database backups and private certificates should never be committed.
-   Dependencies and container images should be maintained regularly.

## 🧪 Testing & Verification

Before deploying changes, verify:

-   Frontend production build.
-   Backend API availability.
-   Database connectivity.
-   Application navigation and responsiveness.
-   English and Hindi content.
-   Complaint and reporting workflows.
-   Docker container health.
-   HTTPS configuration.

## 🗺️ Project Roadmap

Our vision is to continuously improve the CyberMitra experience.

-   [x] Bilingual English and Hindi interface
-   [x] Cybersecurity awareness content
-   [x] Responsive frontend
-   [x] Docker-based application setup
-   [x] PostgreSQL integration
-   [x] Legal and privacy information pages
-   [ ] Production cloud deployment
-   [ ] Further cybersecurity awareness features
-   [ ] Continuous improvements based on user feedback

## 🤝 Contributing

We believe a safer internet is a collective responsibility.

Contributions, suggestions, bug reports, and improvements are welcome.

1.  Fork the repository or create an authorized feature branch.
2.  Create a new branch for your contribution.
3.  Make your changes.
4.  Test your implementation.
5.  Submit a pull request with a clear description.

## 📜 License

Refer to the repository's `LICENSE` file for licensing information.

## 📬 Connect With Us

Have suggestions, questions, or feedback?

Open an issue in the repository or contact the project maintainers.

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
`<em>`{=html}Building awareness today for a safer digital
tomorrow.`</em>`{=html}
```{=html}
</p>
```
