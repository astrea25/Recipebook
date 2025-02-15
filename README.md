# Recipebook

A web application for managing and sharing recipes, built with Django.

## Features

- Create, read, update, and delete recipes
- User authentication and authorization
- Recipe categorization
- Search functionality
- Responsive design for mobile and desktop

## Prerequisites

- Python 3.8+
- Django 4.0+
- pip (Python package installer)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/astrea25/Recipebook.git
cd recipebook
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(f'SECRET_KEY={get_random_secret_key()}')" > .env
```
This command will generate a secure secret key and save it to the .env file.

6. Start the development server:
```bash
python manage.py runserver
```

7. Open your browser and navigate to `http://localhost:8000/recipes/list` to see the application in action.

## Environment Variables

The application uses a `.env` file to store sensitive information. The installation process will create a `.env` file containing your secret key. Make sure to never commit the `.env` file to version control.


