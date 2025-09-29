# Eelarve VOCO

A modern, minimal budget tracking application built with Django and Tailwind CSS. Track your income and expenses with a clean, intuitive interface.

## Features

- 💰 **Transaction Management**: Add, edit, and delete income and expense transactions
- 📊 **Real-time Dashboard**: View your balance, total income, expenses, and transaction count
- 🎨 **Modern UI**: Clean, responsive design with Tailwind CSS
- 📱 **Mobile Friendly**: Works perfectly on desktop and mobile devices
- 🏷️ **Categories**: Predefined categories for better organization
- 💾 **Persistent Storage**: SQLite database for data storage

## Screenshots

The application features a clean dashboard with:
- Summary cards showing balance, income, expenses, and transaction count
- Transaction list with color-coded income (green) and expenses (red)
- Modal forms for adding and editing transactions
- Confirmation dialogs for deleting transactions

## Tech Stack

- **Backend**: Django 5.2.6
- **Frontend**: HTML5, Tailwind CSS, Vanilla JavaScript
- **Database**: SQLite
- **Styling**: Tailwind CSS (via CDN)

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### 1. Clone the Repository

```bash
git clone https://github.com/rasmus-antsi/Eelarve-VOCO.git
cd Eelarve-VOCO
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Database Migrations

```bash
python manage.py migrate
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

### 7. Access the Application

Open your browser and go to: `http://127.0.0.1:8000/`

## Usage

### Adding a Transaction

1. Click the "Lisa Tehing" button in the top-right corner
2. Fill in the transaction details:
   - **Kirjeldus**: Description of the transaction
   - **Summa**: Amount in euros
   - **Kuupäev**: Date of the transaction
   - **Kategooria**: Select from predefined categories
   - **Sissetulek**: Check if it's income, leave unchecked for expenses
3. Click "Salvesta" to save

### Editing a Transaction

1. Click the edit icon (pencil) next to any transaction
2. Modify the details in the modal
3. Click "Salvesta" to update

### Deleting a Transaction

1. Click the delete icon (trash) next to any transaction
2. Confirm the deletion in the popup dialog

## Project Structure

```
Eelarve-VOCO/
├── _core/                 # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── a_main/               # Main application
│   ├── migrations/       # Database migrations
│   ├── models.py        # Transaction model
│   ├── views.py         # View functions
│   ├── urls.py          # URL patterns
│   └── admin.py         # Admin configuration
├── templates/           # HTML templates
│   └── index.html       # Main template
├── venv/               # Virtual environment
├── db.sqlite3          # SQLite database
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Database Schema

The application uses a single `transaction` model with the following fields:

- `id`: UUID primary key
- `amount`: Float field for transaction amount
- `description`: Text field for transaction description
- `date`: Date field for transaction date
- `category`: Char field for transaction category
- `is_income`: Boolean field (True for income, False for expense)
- `created_at`: DateTime field (auto-generated)
- `updated_at`: DateTime field (auto-updated)

## Customization

### Adding New Categories

Edit the category options in `templates/index.html` around line 250:

```html
<option value="Your New Category">Your New Category</option>
```

### Styling Changes

The application uses Tailwind CSS. You can modify the styling by editing the classes in `templates/index.html`.

## Development

### Running Tests

```bash
python manage.py test
```

### Creating Migrations

After modifying models:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Admin Interface

Access the Django admin at `http://127.0.0.1:8000/admin/` (you'll need to create a superuser first):

```bash
python manage.py createsuperuser
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Created by [Rasmus Antsi](https://github.com/rasmus-antsi)

## Support

If you encounter any issues or have questions, please open an issue on GitHub.
