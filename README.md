
# 🎬  MOVIE_HUB

A Django-based movie management and discovery web application where users can browse movies, search by title, explore movies by category, view movie details, and contribute new movies to the platform.



## 📸 Screenshots

### 🏠 Home Page

![Home Page](screenshots/home.png)

### 🔐 Login Page

![Login Page](screenshots/login.png)

### 📝 Registration Page

![Registration Page](screenshots/register.png)

### 🎬 Movie Details

![Movie Details](screenshots/movie-detail.png)

## ✨ Features

### 🔐 User Authentication
- User registration and login
- Secure logout
- Django authentication system
- User profile management
- Profile editing

### 🎥 Movie Management
- Add new movies
- View movie details
- Edit movies
- Delete movies
- Movie ownership-based editing and deletion
- Movie posters
- YouTube trailer links

### 🔎 Search & Categories
- Search movies by title
- Browse movies by category/genre
- View filtered movie results
- Easy navigation through the movie collection

### 🎞️ Movie Details
Each movie can contain:
- Movie title
- Poster
- Description
- Release date
- Actors
- Rating
- Category
- YouTube trailer

### 🎨 User Interface
- Responsive Bootstrap design
- Bootstrap Icons
- Reusable `base.html`
- Shared navigation bar and footer
- Custom background images
- Responsive movie cards
- Clean and user-friendly layout

## 🛠️ Technologies Used

- **Python**
- **Django**
- **HTML5**
- **CSS3**
- **Bootstrap 5**
- **Bootstrap Icons**
- **SQLite**
- **Git & GitHub**

## 📁 Project Structure

```text
MOVIE_HUB/
│
├── movie_project/
│   │
│   ├── accounts/
│   │   ├── migrations/
│   │   ├── static/
│   │   │   └── accounts/
│   │   │       └── images/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── tests.py
│   │
│   ├── movie_project/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── templates/
│   │   └── accounts/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── profile.html
│   │       ├── edit_profile.html
│   │       ├── add_movie.html
│   │       ├── edit_movie.html
│   │       ├── delete_movie.html
│   │       ├── movie_detail.html
│   │       ├── category_movies.html
│   │       └── search_results.html
│   │
│   ├── media/
│   ├── manage.py
│   └── ...
│
├── .gitignore
└── README.md
