and paste everything below.

# 🔐 Login Register App

This project is a simple **Login & Register Authentication System** built using **Flask** during my B.Tech journey.

I originally created this project while learning backend development and understanding authentication systems. Recently, I found this project again in my workspace and decided to clean it up, improve the structure, and push it to GitHub as part of my learning progress.

---

## 🚀 Features

### 👤 User Module
- User Registration
- Login / Logout
- Secure Password Hashing
- User Dashboard
- Profile Page
- Update Password

### 🛡 Admin Module
- Admin Login
- View All Users
- View User Details
- Delete Users
- Role-Based Access Control

---

## 🧠 Tech Stack

- **Backend:** Flask
- **Database:** SQLite (SQLAlchemy)
- **Authentication:** Flask-Login
- **Security:** Flask-Bcrypt
- **Forms:** Flask-WTF
- **Frontend:** HTML + Bootstrap 5
- **Environment Management:** python-dotenv

---

## 📂 Project Structure


app/
│
├── auth/ # Login & Register logic
├── dashboard/ # User dashboard
├── admin/ # Admin module
├── models/ # Database models
├── templates/ # HTML templates
├── static/ # CSS / JS
│
├── config.py
├── extensions.py
└── init.py


---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/shesamsetti-vamsi/login-register-app.git
cd login-register-app
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Application
python run.py

Open browser:

http://127.0.0.1:5000
👑 Default Admin Login

An admin user is automatically created when the app runs for the first time.

Email: admin@email.com
Password: admin123
🎯 Project Purpose

This was one of my first backend projects during my B.Tech.

The main goal at that time was to:

Learn how authentication works

Understand Flask project structure

Work with databases

Practice building real-world features

Later, after improving my skills, I revisited this project and upgraded it with:

Better architecture

Admin module

Role-based access control

Improved dashboard and navigation

This repository represents part of my learning journey as a developer.

📈 Future Improvements

Email verification system

Password reset via email

JWT authentication

Improved admin analytics

Docker deployment



⭐ This project is part of my learning journey — feedback and suggestions are always welcome.


---

Now just:

```bash
git add README.md
git commit -m "Added README"
git push

## 👨‍💻 Author

**Vamsi Shesamsetti**

GitHub:  
https://github.com/shesamsetti-vamsi

---

## ⭐ If you like this project

Feel free to fork it, use it, or give it a star ⭐
