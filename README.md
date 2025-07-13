# KPA Form Data API

This project implements two REST APIs for the KPA form data assignment using Django REST Framework and PostgreSQL. The APIs correspond to:

- **Wheel Specifications Form** (POST and GET with filters)
- **Bogie Checksheet Form** (POST)

---

## 📋 Table of Contents

- [Project Setup](#project-setup)  
- [API Endpoints](#api-endpoints)  
- [Postman Collection](#postman-collection)  
- [Testing](#testing)  
- [Environment Variables](#environment-variables)  
 

---

## 🚀 Project Setup

### Prerequisites

- Python 3.8+
- PostgreSQL
- pip

### Steps

1. Clone the repo:

   ```bash
   git clone https://github.com/AnupamJain2003/anupam_api_assigment
   cd kpa_project
   ```
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies: pip install -r requirements.txt

4. Setup PostgreSQL database and update your `settings.py` with correct DB credentials.

5. Run migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

---

## 🛠️ API Endpoints

| Method | URL                                    | Description                                  |
|--------|----------------------------------------|----------------------------------------------|
| POST   | `/api/forms/wheel-specifications`      | Create a new wheel specifications form       |
| GET    | `/api/forms/wheel-specifications`      | Retrieve wheel specifications (supports filters: `formNumber`, `submittedBy`, `submittedDate`) |
| POST   | `/api/forms/bogie-checksheet`          | Create a new bogie checksheet form           |

---

## 📦 Postman Collection

Import the included Postman collection to test the APIs quickly:

- File: `KPA_API_Local.postman_collection.json`
- Import it via **Postman > Import > File**

---

## 🧪 Testing

You can test APIs using:

- **Postman** with the imported collection.
- **Curl commands** (see examples below):

### Examples:

```bash
curl -X POST http://127.0.0.1:8000/api/forms/wheel-specifications -H "Content-Type: application/json" -d '{...}'
curl "http://127.0.0.1:8000/api/forms/wheel-specifications?formNumber=WHEEL-2025-001"
curl -X POST http://127.0.0.1:8000/api/forms/bogie-checksheet -H "Content-Type: application/json" -d '{...}'
```

---

## ⚙️ Environment Variables

Add your database credentials and other secrets in `.env` or `settings.py` securely.

Example:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```


*Happy coding! 🚀*
