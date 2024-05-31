# Aldo Cafe Website

This project is a website for Aldo Cafe, where users can view the menu, leave feedback, and contact the cafe. It is built using Django, a Python web framework.

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/aldo-cafe.git
```


2. Create a virtual environment:

```
py -m venv venv
```

3. Activate the virtual environment:

On Windows:
```
venv\Scripts\activate
```

On macOS and Linux:
```
source venv/bin/activate
```

4. Install the required dependencies:

```
pip install -r requirements.txt
```

5. Apply migrations:

```
py manage.py migrate
```

## Usage

1. Run the development server:

```
py manage.py runserver
```

2. Open your web browser and navigate to [http://localhost:8000/](http://localhost:8000/) to view the website.

## Features

- **Menu:** View the menu items categorized by type (e.g., breakfast, coffee, drinks).
- **Feedback:** Leave feedback for the cafe.
- **Contact:** Contact the cafe via email.

## File Structure

- `aldo/`: Main project directory.
- `products/`: Django app for managing products and categories.
- `templates/`: HTML templates for rendering views.
  - `layout.html`: Base template for all pages.
  - `items/`: Subdirectory for item-related templates.
    - `feedback.html`: Template for the feedback form.
    - `index.html`: Template for the homepage.
- `static/`: Static files (CSS, JavaScript, images).
- `media/`: Media files uploaded by users (e.g., product images).

## Technologies Used

- **Django**: Web framework for building the backend.
- **HTML/CSS**: Frontend markup and styling.
- **JavaScript**: Client-side scripting for interactivity.
- **Bootstrap**: Frontend framework for responsive design.

## Contributors

- [Your Name](https://github.com/your-username)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
