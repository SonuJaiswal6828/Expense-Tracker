# 💸 Expense Tracker

A modern and secure **Flask-based Web Application** designed to manage your daily expenses on the cloud. This project is integrated with an **Aiven Cloud MySQL** database and is live-hosted on **Render**.

---

## 🚀 Live Demo
Check out the live application here:
👉 [https://your-app-name.onrender.com](https://your-app-name.onrender.com)

---

## ✨ Features

* **Expense Management**: Easily add, view, and delete your financial records.
* **Cloud Integration**: Data is persistently stored and secured using Aiven MySQL.
* **User System Ready**: Includes a `users` table schema for future authentication and login features.
* **Production Optimized**: Configured with Gunicorn and SSL for stable deployment on Render.

---

## 🛠️ Tech Stack

* **Backend**: Python 3.13 / Flask
* **Database**: MySQL (Aiven Cloud)
* **Deployment**: Render (Web Service)
* **Libraries**: PyMySQL, Flask-SQLAlchemy, Python-Dotenv

---

## 📦 Local Setup & Installation

1.  **Clone the Repository**:
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Configuration**:
    Create a `.env` file in the root folder and add your credentials (Do NOT share this file):
    ```env
    DB_HOST=your_aiven_host_here
    DB_USER=your_username
    DB_PASSWORD=your_secure_password
    DB_NAME=defaultdb
    DB_PORT=your_port
    ```

4.  **Run the App**:
    ```bash
    python app.py
    ```

---

## 🗄️ Database Schema

The system utilizes two primary tables within the `defaultdb`:
* **`expenses`**: Tracks `id`, `amount`, `category`, `note`, and `timestamp`.
* **`users`**: Manages `id`, `username`, `email`, and `password` for authentication.

---

## 🛡️ Security Best Practices

* **Environment Variables**: All sensitive credentials are managed via `.env` and excluded from version control using `.gitignore`.
* **SSL Encryption**: Secure connection strings (SSL) are required to communicate with the Aiven MySQL instance.

---

### Developed by [Your Name]
