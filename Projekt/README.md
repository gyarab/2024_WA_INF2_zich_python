# README.md

# Django CMS Project: Engines

This project is a simple Content Management System (CMS) built with Django, designed to manage and display information about various engines. The application allows users to view a list of engines on the homepage and access detailed information about each engine.

## Project Structure

The project is organized as follows:

```
2024_WA_INF1_foltin_python/
├── cms/                  # Django project configuration
├── content/              # Application for managing engine data
├── manage.py             # Command-line utility for Django
├── media/                # Directory for user-uploaded files
├── README.md             # Project documentation
├── requirements.txt      # Project dependencies
└── static/               # Static files (CSS, JS, images)
```

## Features

- **Homepage**: Displays a list of engines with links to their detail pages.
- **Detail Page**: Shows detailed information about a selected engine.
- **Template Inheritance**: Utilizes Django's template inheritance for a clean and maintainable design.

## Data Source

The application uses a JSON file located at `content/data.json` to source engine data. This file contains an array of engine objects, each with relevant attributes such as name, type, and specifications.

## Setup Instructions

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd 2024_WA_INF1_foltin_python
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the development server:
   ```
   python manage.py runserver
   ```

5. Open your web browser and navigate to `http://127.0.0.1:8000/` to view the homepage.

## License

This project is licensed under the MIT License - see the LICENSE file for details.