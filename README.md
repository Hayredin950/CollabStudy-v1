<div align="center">
  <img src="static/images/logo.svg" alt="CollabStudy Logo" width="120" height="120" style="border-radius: 20px;">
  <h1 align="center">CollabStudy v1</h1>
  <p align="center">
    <strong>Real-time Study Collaboration Platform</strong>
    <br>
    Build meaningful connections, share knowledge, and grow together
  </p>
  
  <p align="center">
    <a href="https://collabstudy750.onrender.com" target="_blank">
      <img src="https://img.shields.io/badge/Live_Demo-Access_Now-brightgreen?style=for-the-badge&logo=render" alt="Live Demo">
    </a>
    <a href="https://github.com/Hayredin950/CollabStudy-v1" target="_blank">
      <img src="https://img.shields.io/badge/GitHub-View_Repository-181717?style=for-the-badge&logo=github" alt="GitHub">
    </a>
    <a href="LICENSE" target="_blank">
      <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
    </a>
  </p>

  <div align="center">
    <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white" alt="Django">
    <img src="https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat&logo=tailwind-css&logoColor=white" alt="Tailwind CSS">
    <img src="https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white" alt="PostgreSQL">
  </div>
</div>

<br>

## 📖 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Tech Stack](#️-tech-stack)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Screenshots](#-screenshots)
- [Architecture](#-architecture)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## 🎯 About

CollabStudy v1 is a sophisticated collaboration platform engineered for students, researchers, and developers to create focused study spaces, exchange ideas in real-time, and foster academic growth. Built as a production-ready Django monolith, it serves as the foundation for the upcoming v2 microservices architecture with AI-powered features.

## ✨ Features

| Feature | Description |
|---------|-------------|
| **🔐 Secure Authentication** | User registration, login, and profile management with avatar support |
| **🏠 Study Rooms** | Create, join, and manage topic-specific study rooms |
| **💬 Real-time Messaging** | Instant communication within study rooms |
| **📊 Activity Feed** | Stay updated with platform-wide discussions and activities |
| **🏷️ Topic Discovery** | Explore rooms by subjects and interests |
| **🎨 Premium UI/UX** | Modern dark theme with responsive design powered by Tailwind CSS |
| **👥 User Profiles** | Customizable profiles with bios and contribution tracking |
| **🔧 Admin Dashboard** | Full Django admin panel for platform management |

## 🛠️ Tech Stack

### Backend
- **Framework**: Django 5.x
- **Language**: Python 3.x
- **Database**: PostgreSQL (Production) / SQLite (Development)
- **API**: Django REST Framework
- **Security**: Django's built-in authentication & CSRF protection

### Frontend
- **Styling**: Tailwind CSS
- **Interactivity**: Vanilla JavaScript
- **Icons**: Custom SVG icons
- **Fonts**: Inter Font Family

### Deployment
- **Hosting**: Render
- **WSGI Server**: Gunicorn
- **Static Files**: Whitenoise
- **HTTPS**: Auto SSL via Let's Encrypt

### One-click deploy (Render Blueprint)

This repo ships a [`render.yaml`](render.yaml) blueprint that provisions the web
service **and** a managed PostgreSQL database automatically:

1. Push this repo to GitHub.
2. Go to **Render Dashboard → New → Blueprint** and connect the repository.
3. Render creates the `collabstudy` web service + `collabstudy-db` Postgres and
   sets `SECRET_KEY`, `DEBUG=false` and the `DATABASE_URL` for you. Static files
   are collected during the build; database migrations run automatically at
   startup (free tier doesn't support pre-deploy commands).

Required environment variables (all set by the blueprint, but needed if you
create the service manually):

| Variable | Example | Purpose |
|----------|---------|---------|
| `SECRET_KEY` | `<random 50+ chars>` | Django signing/security key |
| `DEBUG` | `false` | Must be `false` in production |
| `ALLOWED_HOSTS` | `.onrender.com` | Allowed request hosts |
| `CSRF_TRUSTED_ORIGINS` | `https://*.onrender.com` | HTTPS origins allowed for POST |
| `DATABASE_URL` | `postgres://…` | Managed PostgreSQL connection |

> ⚠️ **Note:** Render's *free* PostgreSQL instances expire after ~30 days.
> Upgrade the database plan before that if you want the data to persist.
> Uploaded avatars live on the instance disk and are wiped on redeploys — for
> permanent storage, move uploads to Cloudinary/S3 (planned for v2).

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip package manager
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Hayredin950/CollabStudy-v1.git
   cd CollabStudy-v1
   ```

2. **Set up virtual environment**
   ```bash
   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   Create a `.env` file in the root directory:
   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional but recommended)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Open your browser**
   Navigate to `http://localhost:8000` to see the application!

## 📱 Usage

### For Students
1. **Sign Up**: Create your account with a custom avatar
2. **Explore Rooms**: Browse study rooms by topics or search
3. **Join Discussions**: Participate in real-time conversations
4. **Create Rooms**: Start your own study space for specific subjects

### For Admins
1. Access the admin panel at `http://localhost:8000/admin`
2. Manage users, rooms, messages, and topics
3. Monitor platform activity and moderate content

## 📸 Screenshots

<div align="center">
  <p><em>Coming Soon</em></p>
</div>

## 🏗️ Architecture

CollabStudy v1 follows Django's classic Model-View-Template (MVT) architecture:

```
CollabStudy-v1/
├── base/                   # Main application
│   ├── api/               # REST API endpoints
│   ├── migrations/        # Database migrations
│   ├── templates/         # HTML templates
│   ├── admin.py           # Admin configuration
│   ├── models.py          # Database models
│   ├── views.py           # Request handlers
│   └── urls.py            # URL routing
├── static/                # Static files (CSS, JS, images)
├── staticfiles/           # Collected static files for production
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

### Version 2 Preview

This v1 serves as a proof of concept. Version 2 will feature:
- **Microservices**: NestJS, FastAPI, and standalone services
- **AI Integration**: LangChain-powered study assistants
- **Vector Search**: Semantic search using pgvector
- **Real-time**: WebSocket-based communication
- **Modern UI**: Next.js with React

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place! Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📬 Contact

**Hayredin** - [hayredin.950@gmail.com](mailto:hayredin.950@gmail.com)

Project Link: [https://github.com/Hayredin950/CollabStudy-v1](https://github.com/Hayredin950/CollabStudy-v1)

---

<div align="center">
  <p>
    Built with ❤️ by <a href="https://github.com/Hayredin950">Hayredin</a>
  </p>
  <p>
    © 2026 CollabStudy. All rights reserved.
  </p>
</div>
