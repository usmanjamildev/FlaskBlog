# Flask Blog

A blog web application built with **Flask**, **SQLAlchemy**, and **Bootstrap 5**.  
It allows users to create accounts, log in, write blog posts, and manage their profiles.

## 🚀 Features
- User registration and authentication (Flask-Login & Bcrypt)
- Create, read, update, and delete blog posts
- User profile with profile picture
- Responsive UI with Bootstrap 5
- SQLite database (can be extended to PostgreSQL/MySQL)
- Secure password hashing

## 🛠️ Tech Stack
- **Backend**: Flask, Flask-SQLAlchemy, Flask-Login, Flask-Bcrypt  
- **Frontend**: Bootstrap 5, Jinja2 templates  
- **Database**: SQLite (default), easily swappable with other SQL databases  

## 📂 Project Structure
flaskblog/
│
├── init.py # App factory and extensions
├── models.py # Database models (User, Post)
├── routes.py # Application routes
├── templates/ # HTML templates
├── static/ # CSS, JS, images
└── site.db # SQLite database
run.py # Entry point to run the app

## ⚡ Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flask-blog.git
   cd flask-blog
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Linux/Mac
pip install -r requirements.txt
python
>>> from flaskblog import db, app
>>> with app.app_context():
...     db.create_all()
python run.py
