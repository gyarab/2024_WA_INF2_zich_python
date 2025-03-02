# 2024_WA_INF2_zich_python

# Django CMS

This is a basic Content Management System (CMS) built with Django. The project is structured to provide a clear separation of concerns, with dedicated files for models, views, and URLs.

## Project Structure

- **cms/**: Contains the core application files for the CMS.
  - `__init__.py`: Indicates that this directory is a Python package.
  - `admin.py`: Register models with the Django admin site.
  - `apps.py`: Configuration for the cms application.
  - `models.py`: Defines the data models for the CMS.
  - `tests.py`: Contains tests for the application.
  - `urls.py`: Defines URL patterns for the cms application.
  - `views.py`: Contains view functions for the CMS.

- **django_cms/**: Contains the main project files.
  - `__init__.py`: Indicates that this directory is a Python package.
  - `asgi.py`: ASGI configuration for handling asynchronous requests.
  - `settings.py`: Project settings, including database configuration and installed apps.
  - `urls.py`: URL patterns for the entire Django project.
  - `wsgi.py`: WSGI configuration for serving HTTP requests.

- `manage.py`: Command-line utility for interacting with the Django project.

- `requirements.txt`: Lists all dependencies required for the project.

## Setup Instructions

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required packages using:
   ```
   pip install -r requirements.txt
   ```
4. Run the migrations:
   ```
   python manage.py migrate
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```

## Features

- Create, read, update, and delete articles.
- Admin interface for managing articles.
- URL routing for accessing different views.

## License

This project is licensed under the MIT License.