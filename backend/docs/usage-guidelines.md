# Usage Guidelines

## Overview

This document provides usage guidelines for interacting with the backend API. It includes examples of how to make requests to the API endpoints and handle responses.

## API Endpoints

The backend exposes the following API endpoints:

- **GET /items**: Fetches a list of items.
- **POST /items**: Creates a new item.

## Examples

### Fetching Items

To fetch a list of items, make a GET request to the `/items` endpoint. Below is an example using `curl`:

```sh
curl -X GET "http://localhost:8000/items" -H "accept: application/json"
```

### Creating an Item

To create a new item, make a POST request to the `/items` endpoint with the item data in the request body. Below is an example using `curl`:

```sh
curl -X POST "http://localhost:8000/items" -H "accept: application/json" -H "Content-Type: application/json" -d '{"name":"New Item","description":"Description of the new item"}'
```

## Handling Responses

The API responses are in JSON format. Below are examples of the expected responses for each endpoint.

### GET /items Response

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

### POST /items Response

```json
{
  "name": "New Item",
  "description": "Description of the new item"
}
```

## Error Handling

The API may return error responses in case of invalid requests or server issues. Below are examples of possible error responses.

### 400 Bad Request

```json
{
  "detail": "Invalid request data"
}
```

### 500 Internal Server Error

```json
{
  "detail": "Internal server error"
}
```

## Conclusion

These usage guidelines provide examples of how to interact with the backend API. For more detailed information on the available endpoints and their usage, refer to the API specifications document.
