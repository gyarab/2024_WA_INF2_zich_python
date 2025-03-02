# My Django CMS

This is a simple Content Management System (CMS) built with Django. The application allows users to view a list of articles and access detailed views of each article.

## Project Structure

```
my-django-cms
├── cms
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── templates
│   │   ├── base.html
│   │   ├── article_list.html
│   │   └── article_detail.html
│   ├── urls.py
│   ├── views.py
│   └── migrations
│       └── __init__.py
├── my_django_cms
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── articles.json
├── manage.py
└── README.md
```

## Features

- **Homepage**: Displays a list of articles with links to their detail pages.
- **Article Detail Page**: Shows the content of a selected article.
- **Template Inheritance**: Utilizes Django's template inheritance for a consistent layout.

## Getting Started

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-django-cms
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```
   python manage.py runserver
   ```

4. Access the application at `http://127.0.0.1:8000/`.

## Data Source

The articles are stored in a JSON file (`articles.json`) which the application reads to display the articles on the homepage and their details.

## License

This project is licensed under the MIT License.