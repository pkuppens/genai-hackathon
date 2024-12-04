# API Specifications

## Overview

This document provides the API specifications for the backend of the project. The backend exposes RESTful APIs for the frontend to interact with. These endpoints handle HTTP requests from the frontend and return appropriate responses.

## Endpoints

### GET /items

Fetches a list of items.

- **URL**: `/items`
- **Method**: `GET`
- **Response**:
  - `200 OK`: Returns a list of items.
  - `Content-Type`: `application/json`
  - **Example**:
    ```json
    [
      {
        "name": "Item 1",
        "description": "Description of Item 1"
      },
      {
        "name": "Item 2",
        "description": "Description of Item 2"
      }
    ]
    ```

### POST /items

Creates a new item.

- **URL**: `/items`
- **Method**: `POST`
- **Request Body**:
  - `Content-Type`: `application/json`
  - **Example**:
    ```json
    {
      "name": "New Item",
      "description": "Description of the new item"
    }
    ```
- **Response**:
  - `201 Created`: Returns the created item.
  - `Content-Type`: `application/json`
  - **Example**:
    ```json
    {
      "name": "New Item",
      "description": "Description of the new item"
    }
    ```

### POST /recognize-speech

Recognizes speech from an audio file.

- **URL**: `/recognize-speech`
- **Method**: `POST`
- **Request Body**:
  - `Content-Type`: `multipart/form-data`
  - **Example**:
    ```sh
    curl -X POST "http://localhost:8000/recognize-speech" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@path_to_audio_file" -F "model=base"
    ```
- **Response**:
  - `200 OK`: Returns the recognized speech transcript and language.
  - `Content-Type`: `application/json`
  - **Example**:
    ```json
    {
      "transcript": "This is a sample transcript.",
      "language": "en"
    }
    ```

## Usage

To interact with the API, you can use tools like `curl`, Postman, or any HTTP client library in your preferred programming language. Below are some examples of how to use the API.

### Example: Fetching Items

```sh
curl -X GET "http://localhost:8000/items" -H "accept: application/json"
```

### Example: Creating an Item

```sh
curl -X POST "http://localhost:8000/items" -H "accept: application/json" -H "Content-Type: application/json" -d '{"name":"New Item","description":"Description of the new item"}'
```

### Example: Recognizing Speech

```sh
curl -X POST "http://localhost:8000/recognize-speech" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@path_to_audio_file" -F "model=base"
```

## Further Documentation

For further API documentation and testing, refer to the `/docs` endpoint provided by FastAPI.
