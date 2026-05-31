# 📰 Newspaper App

## <a href="https://newspaper-app-0ql6.onrender.com">LINK TO THE APP</a>
<br />

A modern, secure, and production-ready newspaper and blogging platform built with **Django** using **PostgreSQL**(SQLite locally). This application features a custom user model, full CRUD capabilities for articles, and interactive article comments.

---

## ✨ Features

- **🔐 Robust Authentication**
  - Complete authentication flows: Sign Up, Log In, Log Out, and Password Change.
  - Production-ready Password Reset flow integrated with **SendGrid** SMTP.

- **✍️ Article Management (CRUD):**
  - Create, view, update, and delete newspaper articles.
  - Restricted operations: Only the original author of an article can edit or delete it (enforced via custom `UserPassesTestMixin` checks).
  - Secure page guards requiring authentication (`LoginRequiredMixin`).

- **💬 Comments:**
  - Viewers can leave comments on individual articles.

- **🎨 Responsive Design:**
  - Crafted with a modern **Bootstrap 5** framework.
  - Clean forms using `django-crispy-forms` with the Bootstrap 5 template pack etc.

- **🚀 Cloud & Deployment Ready:**
  - Secure environment configuration using `environs`.
  - Production-ready static asset pipeline using **WhiteNoise**.
  - Flexible database routing supporting SQLite locally and PostgreSQL in production using `dj-db-url`.
  - Configured for effortless deployment on platforms like **Render** (check for my deployment checklist below).
  - PostgreSQL using Neon cloud database. and SQLite for local deployment.
 
---

## 🛠️ Tech Stack & Dependencies

- **Framework:** Django 6.0+
- **Database:** PostgreSQL (SQLite locally)
- **Styling:** Bootstrap 5, Vanilla CSS
- **Static Assets:** WhiteNoise
- **WSGI Server:** Gunicorn
- **Cloud Deployment:** Render
- **Cloud Database:** Neon PostgreSQL

---

## 📂 Project Structure

```text
├── accounts/           # Custom user models, registration forms, views, and tests
├── articles/           # Article and Comment CRUD models, custom mixins, forms, and views
├── pages/              # Static page layouts and homepage rendering views
├── django_project/     # Project configuration, URLs, and production settings
├── templates/          # Global HTML templates with block-based layout inheritance
├── db.sqlite3          # Local database file
├── manage.py           # Django CLI utility
├── requirements.txt    # Project dependencies
└── .env.example        # Template for setting up local environment variables
```

---

## 🏗️ Database Schema

### `CustomUser` (inherits from `AbstractUser`)
- `username` (string)
- `email` (string)
- `age` (positive integer)

### `Article`
- `title` (string, max 255 chars)
- `body` (text)
- `date` (datetime, auto-added)
- `author` (foreign key to `CustomUser`, cascades on delete)

### `Comment`
- `article` (foreign key to `Article`, cascades on delete)
- `comment` (string, max 200 chars)
- `author` (foreign key to `CustomUser`, cascades on delete)

---

## 🚀 Refer here for my Render or other production deployment checklist
<a href="https://app.notion.com/p/Deployment-CheckList-for-Render-365e2135265480ceafbaf96bb1d11768">Deployment checklist</a>

## Local Deployment

Follow these steps to run the application locally on your computer.

### 1. Prerequisites
Make sure you have **Python 3.10+** and `pip` installed.

### 2. Clone the Repository
```bash
git clone https://github.com/farzanfaisal77/newspaper-app.git
cd newspaper-app
```

### 3. Create and Activate a Virtual Environment
```bash
# On Linux/macOS
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Create a file named `.env` in the root of your project directory and add the following keys:
```env
DJANGO_SECRET_KEY=your-super-secret-django-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_HOST_PASSWORD=your_sendgrid_api_key_or_smtp_password
```

### 6. Run Migrations & Apply Database Schema
```bash
python manage.py migrate
```

### 7. Create a Superuser (Admin account)
```bash
python manage.py createsuperuser
```

### 8. Run the Development Server
```bash
python manage.py runserver
```
Visit **`http://127.0.0.1:8000`** in your browser to view the application!
Visit **`http://127.0.0.1:8000/admin/`** to view the django admin panel!

---

## 🔒 Security & Deployment Notes

- **Secret Keys:** Never commit your production `.env` files. `environs` parses and keeps them out of source control.
- **Allowed Hosts:** Production domains like Render (`.onrender.com`) are configured inside `settings.py` for immediate deployment.

<div align="center">
  <sub>Built with ❤️ and 🚀 by <a href="https://github.com/farzanfaisal77" target="_blank" rel="noopener noreferrer">Farzan Faisal</a> as part of a Python Django Learning Journey.</sub>
</div>