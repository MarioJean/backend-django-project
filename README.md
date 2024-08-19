# Django Backend Project

## Overview

This project a Django-based API with user authentication, role management, and an admin feature that allows exporting user data in CSV format. The project uses PostgreSQL as the database, Redis for caching, and JWT (JSON Web Tokens) for authentication.

## Features

1. **User Authentication**
   - Register new users with email and password.
   - Log in and obtain a JWT token for authenticated requests.
   - Secure endpoints using JWT, requiring a valid token for access.

2. **Role Management**
   - Role-based access control to secure resources based on user roles.
   - Manage roles and permissions via the Django Admin Dashboard.

3. **CSV Export in Admin**
   - Admins can export user data to a CSV file directly from the Django admin interface.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- PostgreSQL
- Redis
- Django
- Django REST Framework (DRF)
- Django JWT Authentication packages
- Django-Redis (for caching)

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/username/django-interview-project.git
   cd django-interview-project
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   - Create a `.env` file in the project root with the following variables:
     ```plaintext
     SECRET_KEY=your_secret_key
     DEBUG=True
     DATABASE_URL=postgres://user:password@localhost:5432/dbname
     REDIS_URL=redis://localhost:6379/0
     ```

5. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

## Usage Instructions

### 1. **Accessing the Admin Dashboard:**

- Navigate to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

### 2. **Testing User Authentication:**

- Register a new user at `http://127.0.0.1:8000/api/register/`.
- Log in with the registered user at `http://127.0.0.1:8000/api/login/` to obtain a JWT token.
- Use the JWT token to access secured endpoints.

### 3. **Role Management:**

- Assign roles to users via the Django Admin interface and test role-based access control on secure endpoints.

### 4. **Export Users to CSV:**

- In the Admin Dashboard, go to the Users model.
- Select users and choose the "Export Selected Users to CSV" action from the dropdown.
- Click "Go" to download the CSV file.

---