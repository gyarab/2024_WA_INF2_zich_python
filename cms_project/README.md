# Content Management System (CMS) in Django

This project is a simple Content Management System (CMS) built using Django. It allows users to view a list of articles and access detailed views for each article. The articles are sourced from a JSON file, making it easy to manage and update content without needing to modify the database directly.

## Features

- **Homepage**: Displays a list of articles with links to their detail pages.
- **Article Detail Page**: Shows the content of a selected article.
- **Template Inheritance**: Utilizes Django's template inheritance to maintain a consistent layout across pages.

## Data

The articles are stored in a JSON file (`articles.json`) and include fields such as:

- **Title**: The title of the article.
- **Content**: The main content of the article.
- **Publication Date**: The date when the article was published.

## Setup Instructions

1. **Clone the Repository**:
   ```
   git clone <repository-url>
   cd cms_project
   ```

2. **Install Dependencies**:
   Ensure you have Python and pip installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Development Server**:
   ```
   python manage.py runserver
   ```

4. **Access the Application**:
   Open your web browser and go to `http://127.0.0.1:8000/` to view the homepage.

## License

This project is open-source and available under the MIT License.