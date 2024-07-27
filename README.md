# Bookstore Project

## Overview

The Bookstore Project is a web application built using Django, Docker, and PostgreSQL. 

This project is developed following the "Django for Professionals" book by William S. Vincent, and it showcases best practices for building a production-ready web application. 

The application provides a fully-featured online bookstore with functionalities like user registration, book reviews, advanced authentication, and more.

## Features

- **User Authentication and Registration**
  - Secure user registration with email verification.
  - Customizable permissions to control user access.
  - Oauth2 integration for social login.(implemented google and github)

- **Book Management**
  - CRUD operations for managing books.
  - Admin tools for managing books, authors .etc.

- **Review System**
  - Users can leave reviews and ratings for books.
  - Admin tools for managing reviews.

- **Filter Functionality**
  - Filter books by any combination of author, title, price.

- **Optimized performance**
  - Used 3rd party libraries like django-debug-toolbar to monitor performance.
  - Optimized database queries for faster performance. (prefetch_related, select_related)



## Technologies Used

- **Django**: The primary web framework used for development.
- **Docker**: Containerization tool used to create consistent development and production environments.
- **PostgreSQL**: Relational database system used for data storage.
- **HTML/CSS**: Front-end technologies used for the user interface.
- **Bootstrap**: Front-end framework used for responsive design.


## Getting Started

To get started with the project, clone the repository and follow the setup instructions:

```bash
git clone https://github.com/yaaa3ser/django-bookstore-app.git
cd django-bookstore-app
```

### Setting Up Docker

Ensure Docker is installed on your machine. Then, build and run the Docker containers:

```bash
docker-compose up --build
```


### Creating a Superuser

To access the Django admin interface, create a superuser:

```bash
docker-compose exec web python manage.py createsuperuser
```

### Running the Development Server

Start the development server and access the application at `http://localhost:8000`:

```bash
docker-compose up
```
