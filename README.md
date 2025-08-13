# 🗺️ TripApp - Travel Memory Tracker

A Django-based web application that helps you keep track of all your adventures and never forget the amazing memories. TripApp allows users to create, manage, and organize their trips with detailed notes, ratings, and images.

## ✨ Features

- **User Authentication**: Secure login/signup system
- **Trip Management**: Create, edit, and delete trips with city, country, and date information
- **Note System**: Add detailed notes for each trip including:
  - Event details
  - Dining experiences
  - Adventure experiences
  - General notes
- **Image Support**: Upload and store images for your trip memories
- **Rating System**: Rate your experiences on a 1-5 scale
- **Responsive Design**: Modern UI built with Tailwind CSS
- **User Dashboard**: Personalized view of all your trips and notes

## 🛠️ Technology Stack

- **Backend**: Django 5.2.5
- **Database**: SQLite (development)
- **Frontend**: HTML, Tailwind CSS
- **Forms**: Django Crispy Forms with Tailwind styling
- **Authentication**: Django's built-in user authentication system
- **Image Handling**: Pillow for image processing

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd Trip-App
```

### 2. Create and Activate Virtual Environment
```bash
# On Linux/Mac
python3 -m venv env
source env/bin/activate

# On Windows
python -m venv env
env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 📱 Usage

### Getting Started
1. **Sign Up**: Create a new account to get started
2. **Login**: Access your personalized dashboard
3. **Create Trips**: Add new trips with city, country, and dates
4. **Add Notes**: Create detailed notes for each trip experience
5. **Upload Images**: Add photos to preserve your memories
6. **Rate Experiences**: Give ratings to your favorite moments

### Features Overview
- **Home Page**: Landing page with app introduction
- **Trip List**: View all your trips in one place
- **Trip Detail**: See trip information and associated notes
- **Note Management**: Create, edit, and delete trip notes
- **User Dashboard**: Centralized view of all your travel data

## 🏗️ Project Structure

```
Trip-App/
├── config/                 # Django project configuration
│   ├── settings.py        # Project settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── trip/                  # Main Django app
│   ├── models.py         # Database models (Trip, Note)
│   ├── views.py          # View logic and business logic
│   ├── urls.py           # App-specific URL routing
│   ├── admin.py          # Django admin configuration
│   └── templates/        # HTML templates
│       └── trip/         # Trip-related templates
├── templates/             # Global templates
│   └── registration/     # Authentication templates
├── media/                 # User-uploaded files
├── requirements.txt       # Python dependencies
├── manage.py             # Django management script
└── README.md             # This file
```

## 🗄️ Database Models

### Trip Model
- `city`: City name (max 50 characters)
- `country`: Country code (2 characters)
- `start_date`: Trip start date (optional)
- `end_date`: Trip end date (optional)
- `owner`: Foreign key to User model

### Note Model
- `trip`: Foreign key to Trip model
- `name`: Note title (max 100 characters)
- `description`: Detailed note content
- `type`: Note category (event, dining, experience, general)
- `img`: Optional image upload
- `rating`: Experience rating (1-5 scale)

## 🧪 Testing

Run the test suite with:
```bash
python manage.py test
```

## 📦 Dependencies

- `Django==5.2.5` - Web framework
- `crispy-tailwind==1.0.3` - Tailwind CSS integration for forms
- `django-crispy-forms==2.4` - Form rendering
- `pillow==11.3.0` - Image processing
- `asgiref==3.9.1` - ASGI utilities
- `sqlparse==0.5.3` - SQL parsing