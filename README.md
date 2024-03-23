##GymFitness Project


## Overview
The GymFitness project is a web application designed to manage gym memberships, workouts, and fitness-related activities. It provides features for both users and administrators to interact with the system.

## Technologies Used

Backend: Django (Python)
Frontend: HTML, CSS (Bootstrap can be integrated for styling)
Database: Django's default database (SQLite in development, can be switched to other databases like PostgreSQL, MySQL, etc., for production)
Authentication: JWT (JSON Web Tokens) for authorization and authentication

## Project Structure
/accounts: Contains authentication-related views, serializers, and URLs.
/workouts: Manages workout-related functionalities such as creating, editing, and deleting workouts.
/memberships: Handles membership-related operations like membership plans, subscriptions, etc.
/templates: Contains HTML templates for rendering frontend views.
/static: Stores static files such as CSS, JavaScript, images, etc.

## Usage
User Registration/Login: Users can register for an account and log in using their credentials.
Membership Management: Users can view available membership plans and subscribe to them.
Workout Tracking: Users can create, edit, and delete their workout routines.
Admin Panel: Administrators can access the admin panel (/admin) to manage users, memberships, workouts, etc.
