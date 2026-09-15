# ⚡ Instant Meeting Summariser

<p align="center">
  <img src="https://img.shields.io/badge/Django-6.1.1-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-18-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Google%20Gemini-AI-4285F4?style=for-the-badge&logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/WhiteNoise-Static%20Files-222222?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Render-Deployed-46E3B7?style=for-the-badge&logo=render&logoColor=black" />
</p>

<p align="center">
  <b>🎙️ Turn meetings into structured intelligence.</b>
</p>

<p align="center">
  Record. Transcribe. Summarise. Extract decisions. Track action items.
</p>

<p align="center">
  <a href="https://instant-meeting-summariser.onrender.com">
    <img src="https://img.shields.io/badge/🚀%20Live%20Demo-Visit%20App-000000?style=for-the-badge" />
  </a>
</p>

---

## 🧠 What is Instant Meeting Summariser?

**Instant Meeting Summariser** is an AI-powered web application designed to transform long and messy meetings into concise, structured, actionable information.

Instead of going through an entire meeting transcript manually, the application helps users extract the information that actually matters:

* 📝 Meeting summaries
* 🎯 Key decisions
* ✅ Action items
* 💬 Transcripts
* ⭐ Important meetings
* 🏷️ Meeting tags
* 💭 Meeting chat history
* 👤 User-specific meeting data

The goal is simple:

> **Spend less time remembering meetings and more time acting on them.**

---

# ✨ Core Features

<table>
<tr>
<td width="50%">

### 🎙️ Meeting Management

* Create and manage meetings
* Store meeting metadata
* Track meeting transcripts
* Mark important meetings
* Organise meetings with tags

</td>

<td width="50%">

### 🤖 AI-Powered Intelligence

* Generate intelligent summaries
* Identify important information
* Extract decisions
* Generate actionable tasks
* Process meeting content with Gemini

</td>
</tr>

<tr>
<td>

### 📄 Transcript Management

* Store meeting transcripts
* Keep meeting content organised
* Connect transcripts with meetings
* Retrieve previous meeting information

</td>

<td>

### 💬 Meeting Intelligence

* Meeting chat history
* Decision tracking
* Action-item tracking
* Structured meeting information

</td>
</tr>
</table>

---

# 🚀 Live Application

### 🌐 Production

**[Launch Instant Meeting Summariser](https://instant-meeting-summariser.onrender.com)**

> The application is deployed using **Render** with PostgreSQL as the production database.

---

# 🏗️ Application Architecture

```text
                         ┌──────────────────────┐
                         │      👤 USER         │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     🌐 DJANGO        │
                         │     WEB APPLICATION   │
                         └──────────┬───────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 │                  │                  │
                 ▼                  ▼                  ▼
        ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
        │   👤 ACCOUNTS  │ │  🎙️ MEETINGS  │ │   ⚙️ CORE      │
        │                │ │                │ │                │
        │ Authentication │ │ Meeting Data   │ │ Application    │
        │ User Sessions  │ │ Transcripts    │ │ Logic          │
        └────────────────┘ │ Decisions      │ └────────────────┘
                           │ Action Items   │
                           │ Chat History   │
                           └───────┬────────┘
                                   │
                                   ▼
                         ┌──────────────────────┐
                         │     🤖 GEMINI AI     │
                         │                      │
                         │  Summarisation       │
                         │  Analysis            │
                         │  Intelligence        │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    🐘 POSTGRESQL     │
                         │                      │
                         │ Persistent Data      │
                         └──────────────────────┘
```

---

# 🔄 How It Works

```text
        Meeting
           │
           ▼
    ┌──────────────┐
    │   Capture    │
    │   Meeting    │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │  Transcript  │
    │   Storage    │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │   Gemini AI  │
    │   Processing  │
    └──────┬───────┘
           │
           ▼
   ┌─────────────────┐
   │ Structured Data │
   ├─────────────────┤
   │ 📝 Summary      │
   │ 🎯 Decisions    │
   │ ✅ Action Items │
   │ 💬 Insights     │
   └────────┬────────┘
            │
            ▼
      User Dashboard
```

---

# 🧰 Tech Stack

## Backend

| Technology          | Purpose                    |
| ------------------- | -------------------------- |
| 🐍 Python           | Core programming language  |
| 🎯 Django 6.1.1     | Web framework              |
| 🗄️ PostgreSQL      | Production database        |
| 🧩 SQLite           | Local development database |
| 🔐 Django Auth      | Authentication & sessions  |
| 🤖 Google Gemini    | AI-powered processing      |
| 🐘 Psycopg          | PostgreSQL connectivity    |
| 🗃️ dj-database-url | Database configuration     |

## Frontend

| Technology       | Purpose                 |
| ---------------- | ----------------------- |
| HTML5            | Structure               |
| CSS3             | Styling                 |
| JavaScript       | Client-side interaction |
| Django Templates | Dynamic rendering       |

## Production

| Technology           | Purpose                 |
| -------------------- | ----------------------- |
| 🚀 Render            | Application hosting     |
| 🐘 Render PostgreSQL | Production database     |
| ⚡ Gunicorn           | WSGI application server |
| 🛡️ WhiteNoise       | Static file serving     |

---

# 📁 Project Structure

```text
Instant_Meeting_Summariser/
│
├── 📂 accounts/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── 📂 meetings/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── 📂 core/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── 📂 config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── 📂 static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── 📂 templates/
│
├── 📂 media/
│
├── 📂 staticfiles/
│
├── 📄 manage.py
├── 📄 build.sh
├── 📄 requirements.txt
├── 📄 .gitignore
└── 📄 README.md
```

---

# ⚙️ Local Development

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/aryanbindal89/Instant_Meeting_Summariser.git
```

```bash
cd Instant_Meeting_Summariser
```

---

## 2️⃣ Create a Virtual Environment

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file in the project root.

```env
DJANGO_SECRET_KEY=your-secret-key
DEBUG=True
GEMINI_API_KEY=your-gemini-api-key
```

For local development, PostgreSQL is optional because the application can fall back to SQLite.

If you want to use PostgreSQL locally:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
```

---

## 5️⃣ Run Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

## 6️⃣ Collect Static Files

```bash
python manage.py collectstatic --noinput
```

---

## 7️⃣ Start the Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# 🔐 Environment Variables

| Variable            | Description                 |
| ------------------- | --------------------------- |
| `DJANGO_SECRET_KEY` | Django secret key           |
| `DEBUG`             | Enables/disables debug mode |
| `GEMINI_API_KEY`    | Google Gemini API key       |
| `DATABASE_URL`      | PostgreSQL connection URL   |

### Production

Never commit your `.env` file.

Add secrets through your hosting provider's environment-variable system.

---

# 🗄️ Database

The application supports two database configurations.

### Development

```text
SQLite
```

### Production

```text
PostgreSQL
```

The application automatically checks whether `DATABASE_URL` exists.

```python
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    # PostgreSQL
else:
    # SQLite
```

This makes local development simple while allowing production deployments to use PostgreSQL.

---

# 🚀 Deployment

The project is configured for deployment on **Render**.

### Build Command

```bash
pip install -r requirements.txt && bash build.sh
```

### Start Command

```bash
gunicorn config.wsgi:application
```

### Build Script

```bash
#!/usr/bin/env bash
set -o errexit

python manage.py collectstatic --no-input
python manage.py migrate
```

---

# 🛡️ Production Configuration

The project includes several production-focused configurations:

### WhiteNoise

Static files are served through WhiteNoise.

```python
"whitenoise.middleware.WhiteNoiseMiddleware",
```

### PostgreSQL

Production database support is handled through:

```python
dj_database_url
```

### Gunicorn

The Django application runs through:

```bash
gunicorn config.wsgi:application
```

### HTTPS

Render provides HTTPS for the deployed application.

Django is configured to recognise Render's HTTPS proxy:

```python
SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)
```

---

# 📊 Current Database Models

The meeting system currently handles information such as:

```text
Meeting
   │
   ├── Transcript
   │
   ├── Decisions
   │
   ├── Action Items
   │
   ├── Chat History
   │
   ├── Tags
   │
   └── Important Status
```

This allows a single meeting to become a structured knowledge unit instead of just a block of text.

---

# 🧠 AI Integration

The project integrates **Google Gemini** for meeting intelligence.

The AI layer can be used to transform raw meeting information into structured outputs.

Conceptually:

```text
Raw Meeting Content
        │
        ▼
   Gemini Model
        │
        ├───────────────┐
        ▼               ▼
    Summary         Decisions
        │               │
        └───────┬───────┘
                ▼
          Action Items
```

This architecture makes it possible to extend the AI layer with additional capabilities without rebuilding the entire application.

---

# 🗺️ Roadmap

The project is being developed toward a more complete AI meeting assistant.

### ✅ Completed

* [x] Django project setup
* [x] User authentication foundation
* [x] Meeting management
* [x] Meeting transcripts
* [x] Meeting decisions
* [x] Action items
* [x] Meeting tags
* [x] Important meeting support
* [x] Meeting chat history
* [x] Gemini API integration
* [x] PostgreSQL production support
* [x] WhiteNoise static file configuration
* [x] Gunicorn production server
* [x] Render deployment

### 🔨 Future Improvements

* [ ] 🎙️ Direct browser audio recording
* [ ] 🗣️ Automatic speech-to-text pipeline
* [ ] 🤖 Advanced AI meeting analysis
* [ ] 📌 Automatic task assignment
* [ ] ⏰ Action-item deadlines
* [ ] 📧 Email notifications
* [ ] 📊 Meeting analytics dashboard
* [ ] 🔎 Full-text meeting search
* [ ] 🧠 Personal meeting knowledge base
* [ ] 📤 Export summaries as PDF
* [ ] 📄 Export meeting reports
* [ ] 🔗 Calendar integration
* [ ] 👥 Team collaboration
* [ ] 🔐 Advanced permissions
* [ ] 📱 Mobile-friendly improvements

---

# 🔥 Why This Project?

Meetings generate enormous amounts of information, but most of that information disappears into:

> transcripts → documents → forgotten tabs → digital archaeology

Instant Meeting Summariser is built around a different idea:

```text
              BEFORE

Meeting
   ↓
Long Transcript
   ↓
Manual Reading
   ↓
"Wait... what did we decide?"
```

versus:

```text
              AFTER

Meeting
   ↓
AI Processing
   ↓
┌───────────────────────┐
│ 📝 Summary            │
│ 🎯 Decisions          │
│ ✅ Action Items       │
│ 💬 Important Insights │
└───────────────────────┘
```

The application focuses on turning **conversation into action**.

---

# 🧪 Development Philosophy

This project follows a few important principles:

### 🧩 Modular

Separate Django apps keep functionality organised.

### 🔐 Environment-driven

Secrets and production configuration are handled through environment variables.

### 📈 Scalable

The database layer supports PostgreSQL for production.

### 🤖 AI-ready

The architecture allows additional AI capabilities to be introduced without rebuilding the core application.

### 🚀 Deployment-ready

The repository contains the configuration required to run the project in a production environment.

---

# 🧑‍💻 Developer

## Aryan Agrawal

**B.Tech Computer Science Engineering**

Interested in:

```text
Software Engineering
       │
       ├── Backend Development
       ├── AI / Generative AI
       ├── Cybersecurity
       ├── Java & DSA
       └── Full-Stack Development
```

### GitHub

**[@aryanbindal89](https://github.com/aryanbindal89)**

---

# 📌 Project Links

| Resource             | Link                                                        |
| -------------------- | ----------------------------------------------------------- |
| 🚀 Live Application  | https://instant-meeting-summariser.onrender.com             |
| 💻 GitHub Repository | https://github.com/aryanbindal89/Instant_Meeting_Summariser |

---

# ⭐ Support

If you find this project interesting, consider giving the repository a ⭐.

It helps the project get noticed and motivates further development.

---

<p align="center">

### ⚡ Built to make meetings shorter after they're over.

**Instant Meeting Summariser**

</p>

<p align="center">
Made with 🐍 Python · 🎯 Django · 🤖 Gemini · 🐘 PostgreSQL
</p>
```

This version is intentionally **product-style rather than tutorial-style**. It makes the repository look like something you could actually hand to a recruiter and say, *“Here’s one of the systems I built.”* 🚀
