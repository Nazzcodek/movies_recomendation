# Movie API and User Management Documentation

## Overview

This Django project provides an API for searching and retrieving movie details using the Free movies API via RapidAPI. Additionally, it includes user management functionalities such as account creation, profile editing, profile picture uploading, and account deletion.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [User API Endpoints](#user-api-endpoints)
  - [Movie API Endpoints](#movie-api-endpoints)
- [Authentication](#authentication)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Users should be able to create an account and login.
- Users should be able to edit their profile.
- Users should be able to upload their profile picture, and the link should be returned as part of their profile information.
- Users should be able to delete their account.
- Users should be able to search for a movie and get details of a single movie using the [Free movies API](https://rapidapi.com/rapidapi/api/movie-database-alternative/).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Nazzcodek/movie-api.git
   cd movie-api
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   Create a `.env` file in the project root and add the following:

   ```ini
   MOVIE_API_TOKEN=your_rapidapi_token
   ```

   Replace `your_rapidapi_token` with your actual RapidAPI key.

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

### User API Endpoints

#### Create User

- **Endpoint:** `/api/users/create/`
- **Method:** POST
- **Description:** Create a new user.
- **Parameters:**
  - `username`: The username for the new user.
  - `email`: The email for the new user.
  - `password`: The password for the new user.

Example:
```bash
curl -X POST -d "username=new_user&email=new_user@example.com&password=secure_password" http://127.0.0.1:8000/api/users/create/
```

#### Login

- **Endpoint:** `/api/token/`
- **Method:** POST
- **Description:** Obtain a user token for authentication.
- **Parameters:**
  - `username`: The username of the user.
  - `password`: The password of the user.

Example:
```bash
curl -X POST -d "username=your_username&password=your_password" http://127.0.0.1:8000/api/token/
```

#### Get User Profile

- **Endpoint:** `/api/users/profile/`
- **Method:** GET
- **Description:** Get the profile of the authenticated user.

Example:
```bash
curl -H "Authorization: Token YOUR_TOKEN" http://127.0.0.1:8000/api/users/profile/
```

#### Update User Profile

- **Endpoint:** `/api/users/profile/`
- **Method:** PUT
- **Description:** Update the profile of the authenticated user.
- **Parameters:**
  - `username` (optional): The new username for the user.
  - `email` (optional): The new email for the user.
  - `password` (optional): The new password for the user.

Example:
```bash
curl -X PUT -H "Authorization: Token YOUR_TOKEN" -d "username=new_username&email=new_email@example.com&password=new_password" http://127.0.0.1:8000/api/users/profile/
```

#### Delete User

- **Endpoint:** `/api/users/profile/`
- **Method:** DELETE
- **Description:** Delete the profile of the authenticated user.

Example:
```bash
curl -X DELETE -H "Authorization: Token YOUR_TOKEN" http://127.0.0.1:8000/api/users/profile/
```

### Movie API Endpoints

#### Search Movies

- **Endpoint:** `/movies_api/search/`
- **Method:** GET
- **Description:** Search for movies using the Free movies API.
- **Parameters:**
  - `query` (optional): The search query for movies.

Example:
```bash
curl -H "Authorization: Token YOUR_TOKEN" http://127.0.0.1:8000/movies_api/search/?query=endgame
```

#### Get Movie Details

- **Endpoint:** `/movies_api/details/<int:movie_id>/`
- **Method:** GET
- **Description:** Get details of a single movie using the Free movies API.
- **Parameters:**
  - `movie_id`: The ID of the movie.

Example:
```bash
curl -H "Authorization: Token YOUR_TOKEN" http://127.0.0.1:8000/movies_api/details/123/
```

## Authentication

All endpoints require authentication using a user token. Obtain a token by making a POST request to `/api/token/`.

Example:
```bash
curl -X POST -d "username=your_username&password=your_password" http://127.0.0.1:8000/api/token/
```

## Configuration

The project uses environment variables for configuration. See the [Installation](#installation) section for details on setting up environment variables.

## Contributing

If you'd like to contribute to this project, please follow the [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
```

Note: Make sure to replace placeholders such as `your_rapidapi_token`, `YOUR_TOKEN`, `your_username`, and `your_password` with the actual values relevant to your project. Also, create the necessary files, such as `requirements.txt`, `.env`, `CONTRIBUTING.md`, and `LICENSE`, if they don't already exist.