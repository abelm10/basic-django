# basic-django# Django Test Project

This is a simple Django project called **`testproject`** with a single app named **`welcomeapp`**.  
The app displays a basic “Hello world!” message to verify that Django is set up and routing correctly.

---

## Setup

1. Open your terminal (or VS Code terminal).
2. Navigate to the folder where you want the project:

   ```bash
   cd ..   # move to your desired directory

   
Create the Django project:
django-admin startproject testproject


Move into the project folder:
cd testproject


Create the application:
python manage.py startapp welcomeapp

App View (welcomeapp/views.py)

Defines a simple view called members that returns "Hello world!" in the browser.

This view handles the request when a user visits the URL mapped to it.

(Code for this view will be added in the file directly.)

App URLs (welcomeapp/urls.py)

This file:
Imports path from django.urls.
Imports views from the current app.

Running the Project
From inside the testproject folder, run:

python manage.py runserver

Defines a URL pattern list:
welcomeapp/ → handled by views.members
Assigns the name "welcomeapp" to this route.

So when you visit:
http://127.0.0.1:8000/welcomeapp/
