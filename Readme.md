# Full-Stack Flask & MongoDB Application By Fazal Ahmed

A clean, decoupled full-stack web application featuring a frontend user interface and a backend API service that interacts with MongoDB Atlas.

---

## 🚀 Features

* **Decoupled Architecture:** Frontend and backend run independently on different ports (`8000` and `9000`).
* **File I/O API:** Backend serves a clean JSON list read directly from a local text file.
* **MongoDB Atlas Integration:** Safely captures frontend form submissions, forwards them via API, and inserts them into a cloud database.
* **Graceful Error Handling:** Form validation errors or database connection issues are captured dynamically and displayed on the user interface without crashing or breaking redirection rules.

---

## 📂 Project Structure

```text
flask_tutorial/
│
├── .gitignore               # Protects sensitive environment variables
├── README.md                # Project documentation
│
├── backend/
│   ├── app.py               # Backend Flask API (Port 9000)
│   ├── .env                 # Local environment config (Hidden/Ignored)
│   └── requirements.txt     # Backend dependencies (pymongo, python-dotenv, etc.)
│
└── frontend/
    ├── app.py               # Frontend UI Server (Port 8000)
    ├── requirements.txt     # Frontend dependencies (requests, etc.)
    ├── templates/
    │   └── index.html       # Dynamic HTML Form (Jinja2)
    └── static/
        └── style.css        # Modern UI styling