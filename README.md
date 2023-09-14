# User Management and Profile Picture Upload

This repository contains a Python application for performing CRUD (Create, Read, Update, Delete) operations on user data and allows users to upload and retrieve profile pictures. The application is built using [FastAPI](https://fastapi.tiangolo.com/) and MongoDB, making it a versatile solution for managing user data and profile pictures in a database.

## Prerequisites

Before deploying this application, ensure that you have the following prerequisites installed on your system:

- Python 3.11
- MongoDB (Make sure the MongoDB server is running)
- Docker (optional, if you prefer using Docker for deployment)

## Getting Started

Follow these steps to deploy the application:

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/axrav/assignment.git
   cd assignment
   ```
2. Edit the .env file to configure the application settings, such as the MongoDB URI and any other environment-specific variables.
    ```# MongoDB URI
    MONGO_URI=mongodb://username:password@localhost:27017/your-database-name
    # Other environment variables...
    ```
3. Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```
4. Run the application:
    ```
    Run the application:
    ```
This command will start the FastAPI application, and it will be accessible at http://localhost:{port} in your web browser, where {port} is the port specified in your .env file.

## Using Docker (Optional)

If you prefer using Docker for deployment, follow these steps:

1. Build a Docker image from the project directory (replace `{sample_tag}` with your desired image tag):

   ```shell
   docker build -t {sample_tag} .
    ```
2. Run the Docker container, specifying the port mapping (replace {port} with the desired port):
    ```
    docker run -p {port}:{port} {sample_tag}
    ```
This will start the application inside a Docker container, and it will be accessible at http://localhost:{port} in your web browser.

## Application Features

- **User CRUD Operations**:
  - `POST /user`: Create a new user.
  - `GET /user/{user_id}`: Retrieve user details by ID.
  - `PUT /user/{user_id}`: Update user details by ID.
  - `DELETE /user/{user_id}`: Delete a user by ID.
  - `GET /users`: Retrieve a list of all users.

- **Profile Picture Endpoints**:
  - `POST /upload_profile_pic`: Upload a profile picture for a user.
  - `GET /get_profile_pic/{user_id}`: Retrieve the profile picture of a user.
