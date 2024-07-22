Setup Instructions
Prerequisites
Python 3.8+: Ensure Python is installed.
pip: Python package installer.

1. Clone the Repository
   Clone the repository to your local machine:
   git clone https://github.com/yourusername/django-blog-app.git
   cd django-blog-app
2. Create and Activate a Virtual Environment
   python -m venv venv
3. Active venv
   source venv/bin/activate
4. Install Dependencies
   pip install -r requirements.txt
5. Database Setup
   python3 manage.py makemigrations
   python3 manage.py migrate
6. Create a superuser to access the Django admin interface
   python manage.py createsuperuser
7. python manage.py runserver
    8. API Documentation
       Interactive API documentation is available at:

       Swagger UI: http://127.0.0.1:8000/swagger/

9. Authentication
   JWT Authentication
   Obtain Access and Refresh Tokens:

          Endpoint: /api/token/
          Method: POST
          Body:
          {
          "username": "your_username",
          "password": "your_password"
          }
11. Refresh Access Token:

           Endpoint: /api/token/refresh/
           Method: POST
           Body:

          {
          "refresh": "your_refresh_token"
          }

Include the JWT token in the Authorization header for authenticated requests:

Authorization: Bearer <your-access-token>

12. CSRF Token
    For POST requests, include the CSRF token in the request headers. Retrieve the CSRF token by making a GET request to
    any endpoint with CSRF protection enabled.

Example:

vbnet
Copy code
curl -X 'POST' \
'http://127.0.0.1:8000/api/posts/' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-H 'X-CSRFToken: <your-csrf-token>' \
-d '{
"title": "Today news",
"content": "India won the world cup",
"author": 1
}'

13Testing

python manage.py test