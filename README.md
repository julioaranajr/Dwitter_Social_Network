# Dwitter Social Network

Dwitter - Your tiny social network built with Django This web app models the basic functionality of Twitter.  
You can:

- Post short text-based messages
- View all users on the platform
- Follow and unfollow other users
- Inspect a feed of messages from users that you follow

## Prerequisites

To complete this tutorial series, you should be comfortable with the following concepts:

- Using object-oriented programming in Python
- Setting up a basic Django project
- Managing routing and redirects, view functions, templates, models, and migrations in Django
- Using and customizing the Django admin interface
- Reading and writing HTML with class attributes

## Step 1: Set Up the Base Project

You’ll tackle a few steps one after another:

    - Create a virtual environment and install Django
    - Create a Django project and app
    - Customize the Django admin interface
    - Create users for your app

Before doing anything else, you’ll first create a virtual environment and install Django.

## Create a Virtual Environment and Install Django

Start by creating a new project root folder where you’ll put all the files that you’ll make while working on this project, then navigate into that folder:

```bash
$ mkdir django-social
$ cd django-social
```
After navigating to the parent folder where you’ll develop your project, you can create and activate a virtual environment and install Django from the Python Packaging Index (PyPI):

```bash
$ python3 -m venv venv --prompt=social
```

Activate the virtual environment:

```bash
$ source ./venv/bin/activate
```

Navigate to the folder for the step you're currently on.

Install the dependencies for this project if you haven't installed them yet:

```bash
$ python -m pip install -r requirements.txt
```

These commands create a new virtual environment named social, activate this environment, and install Django.

## Create a Django Project and App

Once the installation is complete, then you can start a new Django project named social. The name of your project doesn’t have to align with the name of your virtual environment, but this way, it’ll be more straightforward to remember.

After creating the Django project, create a new Django app called dwitter to go along with it:

```bash
(social) $ django-admin startproject social .
(social) $ python manage.py startapp dwitter
```
You’ll also need to register your new dwitter app to INSTALLED_APPS in social/settings.py:

```python
# social/settings.py
INSTALLED_APPS = [
    # ...
    'dwitter',
]
```

## Customize the Django Admin Interface

We need to set up Django’s default SQLite database and create a superuser so we can log in to the Django admin portal:

```bash
(social) $ python manage.py migrate
(social) $ python manage.py createsuperuser
Username: admin
Email address: admin@example.com
Password:
Password (again):

```

Create a superuser that allows us to log in to your Django admin portal:

After running these two commands and entering information for the superuser account, you can start Django’s development server:

```bash
(venv) $ python manage.py runserver
```

Navigate to `http://localhost:8000/admin` and log in with your superuser credentials.

We can create users through the Django admin and explore your social media platform with multiple users.

## Tutorial

This project is part of a tutorial series that teaches you how to build a social network with Django.

You’ll implement the project in a series of steps spread out over four parts.
There’s a lot to cover, and you’ll go into detail along the way:

### 📍 Part 1: Models and Relationships

- Step 1: Set Up the Base Project
- Step 2: Extend the Django User Model
- Step 3: Implement a Post-Save Hook

### ⏭ Part 2: Templates and Front-End Styling

- Step 4: Create a Base Template With Bulma
- Step 5: List All User Profiles
- Step 6: Access Individual Profile Pages

### ⏭ Part 3: Follows and Dweets

- Step 7: Follow and Unfollow Other Profiles
- Step 8: Create the Back-End Logic For Dweets
- Step 9: Display Dweets on the Front End

### ⏭ Part 4: Forms and Submissions

- Step 10: Submit Dweets Through a Django Form
- Step 11: Prevent Double Submissions and Handle Errors
- Step 12: Improve the Front-End User Experience
