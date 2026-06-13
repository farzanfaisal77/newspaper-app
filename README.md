# 📰 Newspaper App

## <a href="https://newspaper-app-0ql6.onrender.com">LINK TO THE APP</a>
<br />

A modern, secure, and production-ready newspaper and blogging platform built with **Django** using **PostgreSQL** (SQLite locally). This application features a custom user model, full CRUD capabilities for articles, interactive article comments, and a complete REST API wrapper.

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

- **🔌 Fully-Featured REST API:**
  - Endpoints for users, articles, and article-specific comments.
  - Secure token and session authentication.
  - Granular, object-level permissions ensuring data integrity.
  - Interactive browser-based documentation.

- **🎨 Responsive Design:**
  - Crafted with a modern **Bootstrap 5** framework.
  - Clean forms using `django-crispy-forms` with the Bootstrap 5 template pack etc.

- **🚀 Cloud & Deployment Ready:**
  - Secure environment configuration using `environs`.
  - Production-ready static asset pipeline using **WhiteNoise**.
  - Flexible database routing supporting SQLite locally and PostgreSQL in production using `dj-db-url`.
  - Configured for effortless deployment on platforms like **Render** (check for my deployment checklist below).
  - PostgreSQL using Neon cloud database, and SQLite for local deployment.
 
---

## 🛠️ Tech Stack & Dependencies

- **Core Web Framework:** Django 6.0+
- **API Framework:** Django REST Framework (DRF) 3.15+
- **REST Auth & Registration:** `dj-rest-auth` & `django-allauth`
- **API Documentation:** `drf-spectacular` (OpenAPI 3.0)
- **CORS Management:** `django-cors-headers`
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
├── apis/               # Django REST Framework views, serializers, permissions, and URL routing
├── articles/           # Article and Comment CRUD models, custom mixins, forms, and views
├── pages/              # Static page layouts and homepage rendering views
├── django_project/     # Project configuration, URLs, CORS setups, and production settings
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

## 🔌 REST API & Integrations

The `apis` app brings a modern API layer to the application, leveraging **Django REST Framework (DRF)** and several specialized packages:

### 1. Key API Packages Used
* **`djangorestframework`**: Powers the serialization of models and provides standard Class-Based Views for CRUD operations.
* **`django-cors-headers`**: Configured to whitelist clients (like frontend React applications on `localhost:3000`) for cross-origin resource requests.
* **`dj-rest-auth` & `django-allauth`**: Expose ready-to-use REST endpoints for user authentication, registration, password change, and password reset.
* **`drf-spectacular`**: Auto-generates an OpenAPI 3.0 schema directly from the Django codebase, powering interactive documentation.

### 2. Interactive Documentation Portals
The app is self-documenting. Developers and testers can run the application locally and browse the API:
* **Swagger UI**: Accessible at `http://127.0.0.1:8000/apis/schema/swagger-ui/` for an interactive playground.
* **ReDoc**: Accessible at `http://127.0.0.1:8000/apis/schema/redoc/` for a clean, structural outline of the schema.
* **Raw Schema**: Fetch the YAML schema file directly at `http://127.0.0.1:8000/apis/schema/`.

### 3. API Endpoints Map
All API routes are grouped under the `/apis/` prefix.

#### 🔑 Authentication & Users
| Endpoint | HTTP Method | Description | Access Level |
| :--- | :--- | :--- | :--- |
| `/apis/dj-rest-auth/registration/` | `POST` | Register a new user | Public |
| `/apis/dj-rest-auth/login/` | `POST` | Login user & return Auth Token | Public |
| `/apis/dj-rest-auth/logout/` | `POST` | Log out active user | Authenticated |
| `/apis/dj-rest-auth/password/change/` | `POST` | Change active user password | Authenticated |
| `/apis/dj-rest-auth/password/reset/` | `POST` | Trigger password reset email | Public |
| `/apis/dj-rest-auth/password/reset/confirm/` | `POST` | Confirm reset with email token | Public |
| `/apis/dj-rest-auth/user/` | `GET`/`PUT`/`PATCH` | Retrieve or edit active profile | Authenticated |
| `/apis/users/` | `GET` | List all custom users in system | Admin Only |
| `/apis/users/<int:pk>/` | `GET`/`PUT`/`PATCH`/`DELETE` | CRUD user details | Admin Only |

#### 📝 Articles & Comments
| Endpoint | HTTP Method | Description | Access Level |
| :--- | :--- | :--- | :--- |
| `/apis/articles/` | `GET` | List all articles | Public |
| `/apis/articles/` | `POST` | Publish a new article | Authenticated |
| `/apis/articles/<int:pk>/` | `GET` | Retrieve single article details | Public |
| `/apis/articles/<int:pk>/` | `PUT`/`PATCH` | Update an existing article | Article Author / Admin |
| `/apis/articles/<int:pk>/` | `DELETE` | Delete an article | Article Author / Admin |
| `/apis/articles/<int:article_pk>/comments/` | `GET` | Get all comments under article | Authenticated |
| `/apis/articles/<int:article_pk>/comments/` | `POST` | Add comment to article | Authenticated |
| `/apis/articles/<int:article_pk>/comments/<int:comment_pk>/` | `GET` | Detail comment | Authenticated |
| `/apis/articles/<int:article_pk>/comments/<int:comment_pk>/` | `PUT`/`PATCH` | Update a comment | Comment Author / Admin |
| `/apis/articles/<int:article_pk>/comments/<int:comment_pk>/` | `DELETE` | Delete comment | Comment Author / Admin |

### 4. API Security & Permission Model
* **Object-Level Security**:
  * `IsAuthorElseRead`: Prevents unauthenticated changes. Allows modification (`PUT`, `PATCH`, `DELETE`) of an article **only** if the request is from the article's author or an administrator.
  * `RWifAuthenticated`: Comments require authentication to read or write, but modification is strictly limited to the comment author or an administrator.
* **No Author Impersonation**:
  * In the API serializers, `author` is marked as a `ReadOnlyField`.
  * During creation (`perform_create`), the backend automatically associates the resource (`Article` or `Comment`) with the logged-in request user (`self.request.user`), keeping authors securely authenticated and verified.

---

## 🚀 Refer here for my Render or other production deployment checklist
## <a href="https://app.notion.com/p/Deployment-Checklist-Update-37be213526548062a81af4d1a27b1f21">My Render Deployment checklist on notion</a>

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
Visit **`http://127.0.0.1:8000/apis/`** to view the api endpoints and documentation!

---

## 🔒 Security & Deployment Notes

- **Secret Keys:** Never commit your production `.env` files. `environs` parses and keeps them out of source control.
- **Allowed Hosts:** Production domains like Render (`.onrender.com`) are configured inside `settings.py` for immediate deployment.

<div align="center">
  <sub>Built with ❤️ and 🚀 by <a href="https://github.com/farzanfaisal77" target="_blank" rel="noopener noreferrer">Farzan Faisal</a> as part of a Python Django Learning Journey.</sub>
</div>