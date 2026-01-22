# Movie Database Project

A Django-based application for managing a movie database, including information about movies, directors, and their addresses.

## Technologies Used

- **Python**: Programming language.
- **Django**: Web framework.
- **SQLite**: Database engine.

## Project Structure

```text
.
├── .gitignore
├── db.sqlite3
├── manage.py
├── movies
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_movie_director_movie_winner_oscar_alter_movie_rating.py
│   │   ├── 0003_director_alter_movie_director.py
│   │   ├── 0004_address_director_address.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── setup
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## How to Execute the Project

To run this project locally, follow these steps:

### 1. Requirements

Ensure you have Python installed. It is recommended to use a virtual environment.

### 2. Set up Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Linux/macOS
# .venv\Scripts\activate   # On Windows
```

### 3. Install Dependencies

Install the necessary packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

Prepare the database:

```bash
python manage.py migrate
```

### 5. Run the Server

Start the Django development server:

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.
