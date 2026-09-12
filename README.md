Live Demo Link -----> https://veerababu-foodie-hub.onrender.com/

🍔 Foodie Hub
===============

Foodie Hub is a simple Django-based food ordering / restaurant menu web app. It lets visitors browse a restaurant's menu, while a logged-in user (admin/staff) can manage the menu items — add new dishes, edit existing ones, and remove items that are no longer available.

This project was built as a learning project to practice Django fundamentals — models, forms, templates, authentication, and CRUD operations.

✨ Features
=============

Home page with a welcoming landing view for visitors
About and Contact Us pages
User Authentication
Sign up (registration) with username, email, name and password
Login / Logout using Django's built-in django.contrib.auth views
Navbar dynamically shows Login/SignUp or Profile/Logout depending on whether the user is authenticated
Menu Management (CRUD)
View all menu items in a clean, tabular "Manage Menu" dashboard
Add a new menu item (name, category, price, image)
Edit/Update an existing menu item
Delete a menu item (with a confirmation prompt before deleting)
Authorization
The "Manage Menu" dashboard is protected using @login_required — only logged-in users can view it
Django Admin Panel support for MenuItem (list view, search by name, filter by category)
Category-based menu items: Biryani, Pizza, Noodles, Starters, Dessert
Static assets (CSS, images) served via WhiteNoise, ready for simple deployment
🛠️ Tech Stack
Backend: Python, Django 5.2
Database: SQLite (default, easy to swap for PostgreSQL/MySQL in production)
Frontend: Django Templates, HTML, CSS
Static file serving: WhiteNoise
Server (production-ready): Gunicorn

📁 Project Structure
=====================
Foodie_Hub/
├── Foodie_Hub/            # Project settings, urls, wsgi/asgi
├── testapp/               # Main app — models, views, forms, admin
│   ├── models.py          # MenuItem model
│   ├── views.py           # All view logic (home, auth, menu CRUD)
│   ├── forms.py           # SignUpForm, MenuItemForm
│   ├── admin.py           # Admin panel registration
│   └── migrations/
├── design/
│   └── table_design.excalidraw   # Database/table design diagram (open at excalidraw.com)
├── templates/              # HTML templates
│   ├── navbar.html         # Base template with navbar
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
============
1. Clone the project
bash
git clone <your-repo-url>
cd Foodie_Hub
2. Create a virtual environment & activate it
bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
3. Install dependencies
bash
pip install -r requirements.txt
4. Apply migrations
bash
python manage.py migrate
5. Create a superuser (for admin panel / to manage menu)
bash
python manage.py createsuperuser
6. Run the development server
bash
python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser 🎉

🔗 Available Routes
====================
URL	Description	Access
/	Home page	Public
/about/	About page	Public
/contactus/	Contact Us page	Public
/signup/	User registration	Public
/accounts/login/	Login	Public
/logout/	Logout	Logged-in users
/managemenu/	View all menu items	Logged-in users
/managemenu/add/	Add a new menu item	Logged-in users*
/editmenu/<id>/	Edit an existing menu item	Logged-in users*
/deletemenu/<id>/	Delete a menu item	Logged-in users*
/admin/	Django admin panel	Superuser/Staff

* Currently add, edit, and delete views don't have the @login_required decorator applied yet (only /managemenu/ does). See Known Limitations below.

⚠️ Known Limitations / Next Steps
=================================

A few things worth improving as the project grows:

Add @login_required (and ideally @staff_member_required or a custom permission check) to add_menu_item, edit_menu_item, and delete_menu_item views — right now only the menu listing page is protected, so the add/edit/delete URLs can technically be hit directly without logging in.
SignUpForm saves the raw password field and then calls set_password() on it — this works, but using Django's UserCreationForm (or hashing the password before the first save) is the more standard approach.
Menu item images are currently referenced by a manually-typed static path (e.g. images/mc1.png) instead of an actual ImageField upload — fine for a demo, but a real image upload would be more user-friendly.
No cart / order-placing flow yet — right now it's a menu management app rather than a full ordering system.
DEBUG = True and a hardcoded SECRET_KEY are fine for local development, but should be moved to environment variables before deploying anywhere public.

🗂️ Design
===========
The database/table structure for this project was planned out beforehand and is available as an Excalidraw file at design/table_design.excalidraw. You can open it by:

Uploading it at excalidraw.com (File → Open), or
Opening it directly in VS Code with the Excalidraw extension

This is useful as a quick visual reference before diving into models.py, especially if you plan to add more models (e.g. Orders, Cart, Category) later.

📌 Notes
=============
Default LOGIN_REDIRECT_URL is set to /, so after logging in, users land on the home page.
The MenuItem model supports 5 categories out of the box — add more by extending CATEGORY_CHOICES in models.py.


