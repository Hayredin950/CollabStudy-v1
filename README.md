# CollabStudy v1 — Real-time Study Network 🚀

CollabStudy is a professional collaboration platform designed for students and developers to create study rooms, share knowledge, and engage in real-time discussions. This is **Version 1** of the platform, built as a robust Django monolith.

### 🟢 Live Demo
Check out the live application here: [https://collabstudy750.onrender.com](https://collabstudy750.onrender.com)

---

## 🌟 Features

- **Real-time Study Rooms**: Create and join dedicated rooms for specific topics.
- **Dynamic Messaging**: Engage in instant discussions with participants.
- **User Profiles**: Custom avatars, bios, and contribution tracking.
- **Activity Feed**: Stay updated with the latest discussions across the platform.
- **Topic Discovery**: Easily browse and filter rooms by subject.
- **Premium UI**: Modern, responsive dark-themed interface built with Tailwind CSS.

## 🛠️ Tech Stack

- **Backend**: Python, Django 5.x
- **Frontend**: Tailwind CSS, JavaScript (Inter font)
- **Database**: SQLite (Development), PostgreSQL (Production ready)
- **Deployment**: Render, Gunicorn, Whitenoise
- **Architecture**: Monolithic Model-View-Template (MVT)

---

## 🚀 Architectural Evolution

This project represents the **initial phase** of CollabStudy. It demonstrates a complete, production-ready monolithic architecture. 

> **Note**: I am currently rebuilding this platform from the ground up as a **Microservices Architecture (v2)** using NestJS, Next.js, FastAPI, and LangChain to implement advanced AI-powered study features and vector search.

---

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/HayreKhan750/CollabStudy-v1.git
   cd CollabStudy-v1
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

---

## 👨‍💻 Developed By
**Hayredin** — *Transforming ideas into high-performance digital solutions.*
