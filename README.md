Live Demo Link -----> https://veerababu-foodie-hub.onrender.com/

🍔 Foodie_Hub
===============

A simple Django-based restaurant menu web app with authentication and full menu CRUD (Create, Read, Update, Delete) functionality.

📖 About the Project
========================

Built using Django to practice real-world concepts: models, forms, templates, authentication & authorization, and CRUD operations.
Lets visitors browse a restaurant's menu.
Lets a logged-in user manage the menu (add / edit / delete items).

✨ Features
================

Home Page
Landing page for all visitors.
About Page
Static info page about Foodie Hub.
Contact Us Page
Static contact page.
User Authentication
Sign Up page (username, email, first name, last name, password).
Login page (Django's built-in auth view).
Logout functionality.
Navbar changes dynamically:
Shows Login / SignUp if user is not logged in.
Shows Profile (username) / Logout if user is logged in.
Authorization
manage_menu page is protected with @login_required.
Only logged-in users can view the "Manage Menu" dashboard.
Menu Management (CRUD)
Create – Add a new menu item (name, category, price, image).
Read – View all menu items in a table with image preview.
Update – Edit an existing menu item.
Delete – Remove a menu item (asks for confirmation before deleting).
Django Admin Panel
MenuItem model registered in admin.
Search by name.
Filter by category.
Categories Supported
Biryani
Pizza
Noodles
Starters
Dessert
Static File Handling
CSS and images served via WhiteNoise (deployment-ready).

🛠️ Tech Stack
===============

Language: Python
Framework: Django 5.2
Database: SQLite (default)
Frontend: Django Templates + HTML + CSS
Static Files: WhiteNoise
Deployment Server: Gunicorn

📁 Project Structure
======================

Foodie_Hub/
├── Foodie_Hub/                     # Project settings, urls, wsgi/asgi
├── testapp/                        # Main app
│   ├── models.py                   # MenuItem model
│   ├── views.py                    # All views (home, auth, menu CRUD)
│   ├── forms.py                    # SignUpForm, MenuItemForm
│   ├── admin.py                    # Admin panel config
│   └── migrations/
├── design/
│   └── table_design.excalidraw     # Database/table design diagram
├── templates/
│   ├── navbar.html                 # Base template with navbar
│   ├── home.html
│   ├── about.html
│   ├── contactus.html
│   ├── signup.html
│   ├── manage_menu.html
│   ├── add_menu_item.html
│   ├── edit_menu_item.html
│   ├── logout.html
│   └── registration/login.html
├── static/
│   ├── css/
│   └── images/
├── requirements.txt
└── manage.py

🚀 Getting Started
Clone the project
bash
   git clone <your-repo-url>
   cd Foodie_Hub
Create a virtual environment
bash
   python -m venv venv
Activate the virtual environment
bash
   source venv/bin/activate     # On Windows: venv\Scripts\activate
Install dependencies
bash
   pip install -r requirements.txt
Apply database migrations
bash
   python manage.py migrate
Create a superuser (to access admin panel / manage menu)
bash
   python manage.py createsuperuser
Run the development server
bash
   python manage.py runserver
Open in browser
Go to http://127.0.0.1:8000/
🔗 Routes / URLs
URL	Description	Access
/	Home page	Public
/about/	About page	Public
/contactus/	Contact Us page	Public
/signup/	User registration	Public
/accounts/login/	Login	Public
/logout/	Logout	Logged-in users
/managemenu/	View all menu items	Logged-in users
/managemenu/add/	Add a menu item	Logged-in users*
/editmenu/<id>/	Edit a menu item	Logged-in users*
/deletemenu/<id>/	Delete a menu item	Logged-in users*
/admin/	Django admin panel	Superuser/Staff

* Add/Edit/Delete views don't yet have @login_required applied — see Known Limitations.

🗂️ Design
===========

Database/table structure planned before coding.
Available at design/table_design.excalidraw.
Open it by:
Uploading to excalidraw.com → File → Open, OR
Using the Excalidraw extension in VS Code.
Useful reference before adding new models (e.g. Orders, Cart).

⚠️ Known Limitations / Next Steps
====================================
add_menu_item, edit_menu_item, delete_menu_item views don't have @login_required yet — only manage_menu is protected.
SignUpForm saves the raw password first, then calls set_password() — works, but UserCreationForm is the more standard Django approach.
image_path is a plain text field (manually typed path like images/mc1.png) instead of a real ImageField upload.
No cart / order placement flow yet — currently a menu management app, not a full ordering system.
DEBUG = True and hardcoded SECRET_KEY — fine for local dev, should move to environment variables before deploying.

📌 Notes
=============
LOGIN_REDIRECT_URL is set to / — user lands on home page after login.
MenuItem model supports 5 categories by default — extend CATEGORY_CHOICES in models.py to add more.
