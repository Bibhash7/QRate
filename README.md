# QRate - Share Code Instantly via QR

**QRate** is a minimalist Django-based web app that lets users paste code, generate a QR code for the link, and access the code by scanning the QR. It’s simple, fast, and the QR and code expire shortly to ensure privacy.

## 🌟 Features

- Paste code and generate a shareable QR code.
- View code by scanning the QR.
- QR codes auto-expire after 20 seconds.
- Auto-delete database entries after 100 records to reduce bloat.
- Copy button for easy code copying from shared page.
- Responsive UI with modern gradient background.
- Error handling for server issues and unknown routes.
- Hosted on PythonAnywhere with MySQL support.

---

## 📂 Folder Structure

```
qrateProject/
│
├── qrateApp/
│ ├── migrations/
│ ├── templates/
│ │ └── qrateApp/
│ │ ├── home.html
│ │ ├── view_code.html
│ │ ├── unknown_routes.html
│ │ └── internal_server_error.html
│ ├── services/
│ │ ├── create_qr.py
│ │ ├── delete_qr.py
│ │ └── clear_db.py
│ ├── init.py
│ ├── models.py
│ ├── views.py
│ ├── admin.py
│ └── apps.py
│
├── media/
│ └── qrcodes/
│
├── manage.py
├── requirements.txt
└── README.md
```

## 🛠 Technologies Used

1. Django
2. Python 3
3. MySQL
4. HTML/CSS/JS (Vanilla)
5. PythonAnywhere (Hosting)

## 👨‍💻 Developer
Bibhash Ghosh
© 2025 All Rights Reserved.

