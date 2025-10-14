# SSD — Flask CRUD App

This is a simple Flask application demonstrating CRUD operations using Flask-SQLAlchemy and SQLite.

Files:
- app.py                : Main Flask application
- requirements.txt      : Python dependencies
- templates/index.html  : Home page with Add/List functionality
- templates/update.html : Update form
- instance/firstapp.db  : SQLite database (created at first run)
- static/               : Static files (empty)

How to run:
1. (Optional) Create and activate a virtual environment:
    python -m venv env
    source env/bin/activate   # Linux/Mac
    env\Scripts\activate    # Windows (PowerShell)

2. Install dependencies:
    pip install -r requirements.txt

3. Run the app:
    python app.py

4. Open your browser at:
    http://127.0.0.1:5000/

Notes:
- The database is created automatically on first request.
- This example uses minimal validation for demonstration purposes. For production, add input validation and CSRF protection.
