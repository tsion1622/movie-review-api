🎬 Movie Review API

A Django REST Framework API to manage movies and their reviews.
This is my ALX Backend Engineering Capstone Project – it demonstrates building a fully functional REST API with authentication, CRUD operations, and deployment on Render.

 Project Overview

The Movie Review API allows users to:

 View a list of movies

 Create reviews for a specific movie

 Edit or delete reviews

 Authenticate users (JWT authentication)

This API can be used as the backend for a movie rating or recommendation system.

Tech Stack

Backend: Django 5, Django REST Framework

Authentication: JWT (djangorestframework-simplejwt)

Database: PostgreSQL (via dj-database-url)

Deployment: Render (with Gunicorn + Whitenoise)

 Live Demo

Base URL: https://movie-review-api-qemt.onrender.com
Example Endpoints

GET /movies/ → List all movies

POST /movies/ → Create a new movie

GET /movies/<id>/reviews/ → List reviews for a movie

POST /movies/<id>/reviews/ → Add a review for a movie

Setup & Installation

Clone the repository:
git clone https://github.com/tsion1622/movie-review-api.git
cd movie-review-api

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

🔑 Environment Variables

The following environment variables are required for production:

Variable	Example Value	Description
SECRET_KEY	django-insecure-123abcxyz	Django secret key
DEBUG	False	Set to False in production
ALLOWED_HOSTS	movie-review-api-qemt.onrender.com	