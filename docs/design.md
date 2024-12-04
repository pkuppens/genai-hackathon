# Design

## Directory Structure

The project is organized into the following directories:

- `frontend/`: Contains the React + TypeScript frontend application.
- `backend/`: Contains the FastAPI backend application.
  - `api/`: Contains FastAPI endpoints for handling requests from the frontend.
  - `llm/`: Contains Large Language Model interaction code.
  - `models/`: Contains implementations for local containerized Ollama models and placeholders for cloud versions.
  - `data/`: Manages data related to generative AI prompts and their templates.
  - `docs/`: Contains markdown files with API specifications, installation instructions, and usage guidelines.

## Frontend Structure

The frontend is built using React and TypeScript. It includes components for viewing and submitting generative AI prompts and their templates. The frontend communicates with the backend via API calls.

## Backend Structure

The backend is built using FastAPI and includes the following components:

- **API Endpoints**: The backend exposes RESTful APIs for the frontend to interact with. These endpoints handle HTTP requests from the frontend and return appropriate responses.
- **Language Model Implementations**: The core functionality of the backend involves implementing and managing the language models. These models are containerized and can be either local Ollama models or generalized to cloud versions like OpenAI, Gemini, or Claude.
- **Request Handling**: The backend processes incoming requests, performs necessary actions using the language models, and returns the results to the frontend.
- **Data Management**: The backend manages data related to generative AI prompts and their templates, ensuring that the data is stored, retrieved, and processed efficiently.
- **Security**: The backend implements security measures to protect the API endpoints and data, including authentication and authorization mechanisms.
- **Documentation**: The backend provides clear and comprehensive documentation, including API specifications, installation instructions, and usage guidelines.
