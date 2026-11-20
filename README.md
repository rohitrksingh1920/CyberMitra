# 🛡️ CyberMitra – Cyber Security Awareness & Assistance Platform

> **Spot the Scam Before It Spots You.**  
> Your digital safety companion for a safer internet.

<p align="center">
  <img src="https://img.shields.io/badge/Project-CyberMitra-2563EB?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Frontend-Vercel-000000?style=for-the-badge&logo=vercel" />
  <img src="https://img.shields.io/badge/Backend-Render-46E3B7?style=for-the-badge&logo=render&logoColor=black" />
  <img src="https://img.shields.io/badge/Database-Neon_PostgreSQL-00E699?style=for-the-badge&logo=postgresql&logoColor=black" />
  <img src="https://img.shields.io/badge/Framework-React-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
  <img src="https://img.shields.io/badge/API-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
</p>

<p align="center">
  <a href="https://cybermitra-frontend.vercel.app/">
    <img src="https://img.shields.io/badge/🚀_Live_Demo-CyberMitra-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Live"/>
  </a>
</p>

<p align="center">
  **🌐 Live Application:**  
  <a href="https://cybermitra-frontend.vercel.app/">CyberMitra – Try It Now</a>
</p>
## 🌐 Project Overview

**CyberMitra** is a bilingual (English and Hindi) cybersecurity awareness, assistance, and reporting platform developed to help citizens recognize online threats, understand cyber fraud, and access essential cybercrime support resources.

The project is developed under the community service initiative in coordination with **Shree Durga Samajik Sansthan**, following the organization's approval for the project titled:

**"Cyber Security Awareness, Assistance and Reporting Platform."**

The platform aims to promote digital literacy, encourage responsible internet usage, and make cybersecurity information more accessible to citizens.

CyberMitra brings together cybersecurity awareness resources, suspicious activity checking, complaint assistance, and practical safety guidance through a user-friendly web application.

## 🎯 Project Objectives

- Promote cybersecurity awareness and digital literacy among citizens.
- Educate users about phishing, online scams, identity theft, and digital fraud.
- Provide accessible guidance for cybercrime reporting and complaint assistance.
- Help users identify suspicious phone numbers, UPI IDs, and website links through community reports.
- Make cybersecurity resources available in both English and Hindi.
- Encourage safe and responsible digital practices.

## ✨ Key Features

| Feature | Description |
|---|---|
| 🛡️ Fraud Awareness | Learn about phishing, online scams, identity theft, and common cyber threats. |
| 🔍 Suspicious Activity Checker | Check phone numbers, UPI IDs, and website links against reports submitted by other CyberMitra users. |
| 📝 Cybercrime Reporting | Access cybercrime reporting resources and assistance. |
| 📄 FIR Format Assistance | Access guidance and formats to help prepare cybercrime complaint information. |
| 📌 Complaint Tracking | Track submitted CyberMitra complaint drafts using a unique reference code. |
| 🚨 Emergency Resources | Access important cybercrime helplines and official reporting resources. |
| 🌐 Bilingual Interface | Access platform information in English and Hindi. |
| 📱 Responsive Design | Use the platform across desktop, tablet, and mobile devices. |
| ⚖️ Legal & Privacy Information | Access the platform's available Terms, Privacy, Refund, Shipping, and Contact information. |

**Important:** Community suspicious-activity reports are user-submitted information, not an official government blacklist or confirmation of criminal activity. CyberMitra complaint tracking refers to submissions within the application and does not independently verify official police FIR registration.

## 🖥️ Platform Preview

CyberMitra provides a user-friendly interface designed to make cybersecurity awareness and assistance accessible to citizens.

Add screenshots of the deployed application in `docs/screenshots/`:

```text
docs/
└── screenshots/
    ├── homepage.png
    ├── dashboard.png
    ├── cybercrime-reporting.png
    ├── suspicious-checker.png
    └── complaint-tracking.png
```

Example:

```markdown
![CyberMitra Homepage](docs/screenshots/homepage.png)
```

## 🧰 Technology Stack

CyberMitra uses a modern full-stack architecture with separate frontend, backend, and cloud database services.

| Layer | Technology | Purpose |
|---|---|---|
| Frontend | React | User interface and application experience |
| Backend | FastAPI | REST API and application logic |
| Database | PostgreSQL | Persistent application data |
| Database Hosting | Neon | Cloud-hosted PostgreSQL database |
| Frontend Hosting | Vercel | Frontend deployment and hosting |
| Backend Hosting | Render | Backend API deployment and hosting |
| Containerization | Docker | Local development and containerized services |
| Local Orchestration | Docker Compose | Running application services locally |
| Web Server | Nginx | Reverse proxy configuration where applicable |

## ☁️ Cloud Deployment Architecture

CyberMitra is deployed using three cloud services that work together to provide a complete application.

```text
              USERS / CITIZENS
                     |
                     v
          +----------------------+
          |       VERCEL         |
          |    React Frontend    |
          +----------------------+
                     |
                     | API Requests
                     v
          +----------------------+
          |       RENDER         |
          |    FastAPI Backend   |
          +----------------------+
                     |
                     | PostgreSQL Connection
                     v
          +----------------------+
          |        NEON          |
          |  PostgreSQL Database |
          +----------------------+
```

### Deployment Services

**1. Frontend – Vercel**

- Hosts the React frontend.
- Provides a publicly accessible application URL.
- Handles frontend deployment and production builds.

**2. Backend – Render**

- Hosts the FastAPI backend.
- Handles API requests and application logic.
- Communicates with the PostgreSQL database.

**3. Database – Neon**

- Provides managed cloud PostgreSQL hosting.
- Stores application data persistently.
- Allows the backend to connect through a secure database connection string.

### 🌍 Application Access

**Live Application:** Add your Vercel production URL here.

**Backend API:** Add your Render service URL here.

**API Documentation:** `<Render Backend URL>/docs`

The Vercel frontend URL is the primary link to share with users who want to access CyberMitra.

## 📂 Project Structure

```text
CyberMitra/
│
├── backend/                  # FastAPI backend
│   ├── app/
│   ├── requirements.txt
│   └── ...
│
├── frontend/                 # React frontend
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── deploy/                   # Deployment configurations
├── nginx/                    # Nginx configuration
├── docker-compose.yml        # Local application services
├── docker-compose.https.yml  # HTTPS deployment override
├── .env.example              # Environment variable template
├── .gitignore
└── README.md
```

*Note: The actual directory structure may vary depending on the current project version.*

## 🚀 Run Locally

### Prerequisites

- Git
- Docker Desktop
- Docker Compose

### 1. Clone the repository

```bash
git clone https://github.com/rohitrksingh1920/CyberMitra.git

cd CyberMitra
```

### 2. Configure environment variables

For Windows:

```bash
copy .env.example .env
```

For macOS/Linux:

```bash
cp .env.example .env
```

Configure the required environment variables in `.env`.

Use secure credentials and never commit secret keys, database URLs, or passwords to GitHub.

### 3. Build and start the application

```bash
docker compose up --build -d
```

### 4. Check running containers

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

To remove containers and the associated named database volume:

```bash
docker compose down -v
```

**Warning:** This command can permanently delete your local database data.

## 🔐 Security and Privacy

CyberMitra follows important security practices to help protect application data and user information.

- Keep environment files and credentials out of version control.
- Store production secrets securely in deployment environment settings.
- Never expose database credentials or private API keys to the frontend.
- Use HTTPS for production communication.
- Configure CORS for authorized frontend domains.
- Restrict database access to trusted services.
- Validate and sanitize user inputs.
- Keep application dependencies and deployment environments updated.
- Review privacy policies and legal information before public release.

## 🧪 Testing and Verification

Before releasing changes, verify the following:

- [ ] Frontend loads successfully through Vercel.
- [ ] Backend API responds successfully through Render.
- [ ] Backend connects successfully to Neon PostgreSQL.
- [ ] User-submitted reports are stored persistently.
- [ ] Suspicious number, UPI ID, and link checking works.
- [ ] Complaint reference codes are generated correctly.
- [ ] Complaint tracking retrieves the correct submission.
- [ ] FIR assistance functionality works as expected.
- [ ] English and Hindi interfaces work correctly.
- [ ] Application is responsive across desktop and mobile devices.

## 🗺️ Project Roadmap

- [ ] Expand cybersecurity awareness resources.
- [ ] Improve English and Hindi educational content.
- [ ] Enhance suspicious activity reporting and verification.
- [ ] Improve complaint assistance and tracking.
- [ ] Conduct cybersecurity awareness activities with the NGO.
- [ ] Improve accessibility and mobile experience.
- [ ] Strengthen application security and monitoring.
- [ ] Continue improving the production deployment.

## 🤝 Community Service Collaboration

CyberMitra is being developed as part of a community service initiative in coordination with:

**Shree Durga Samajik Sansthan**

**Approved Project Title:** Cyber Security Awareness, Assistance and Reporting Platform.

The initiative focuses on spreading cybersecurity awareness, educating citizens about online threats, and helping people access appropriate cybercrime assistance and reporting resources.

The project aims to contribute towards a safer and more digitally aware community.

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

1. Fork the repository.
2. Create a new feature branch.
3. Make your changes.
4. Test your implementation.
5. Submit a pull request with a clear description.

Please do not include passwords, API keys, private certificates, database backups, or personal information in commits.

## 📜 License

Refer to the repository's `LICENSE` file for licensing terms, if present.

## 📬 Contact & Support

For project-related questions, suggestions, or feedback, please open an issue in the GitHub repository.

**GitHub Repository:**  
https://github.com/rohitrksingh1920/CyberMitra

---

<p align="center">

**🛡️ CyberMitra – Your Safety, Your Awareness, Your Digital Future.**

*Building awareness today for a safer digital tomorrow.*

</p>

**© 2026 CyberMitra. All Rights Reserved. Created by GentEch.**
