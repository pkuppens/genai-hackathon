# genai-hackathon
Code for the 2024 GenAI Works Hackathon #BuildWithAI

## Project Overview

This project is designed to facilitate the creation, submission, and management of generative AI prompts and their templates. It consists of a frontend built with React and TypeScript, and a backend that includes API endpoints, language model implementations, request handling, data management, security, and comprehensive documentation.

## Frontend

The frontend is built using React and TypeScript. It includes components for viewing and submitting generative AI prompts and their templates. The frontend communicates with the backend via API calls.

## Backend

The backend is built using FastAPI and includes the following components:

- **API Endpoints**: The backend exposes RESTful APIs for the frontend to interact with. These endpoints handle HTTP requests from the frontend and return appropriate responses.
- **Language Model Implementations**: The core functionality of the backend involves implementing and managing the language models. These models are containerized and can be either local Ollama models or generalized to cloud versions like OpenAI, Gemini, or Claude.
- **Request Handling**: The backend processes incoming requests, performs necessary actions using the language models, and returns the results to the frontend.
- **Data Management**: The backend manages data related to generative AI prompts and their templates, ensuring that the data is stored, retrieved, and processed efficiently.
- **Security**: The backend implements security measures to protect the API endpoints and data, including authentication and authorization mechanisms.
- **Documentation**: The backend provides clear and comprehensive documentation, including API specifications, installation instructions, and usage guidelines.

## Installation

### Frontend Setup

1. **Clone the repository**:
   ```sh
   git clone https://github.com/pkuppens/genai-hackathon.git
   cd genai-hackathon/frontend
   ```

2. **Install dependencies**:
   ```sh
   npm install
   ```

3. **Start the development server**:
   ```sh
   npm start
   ```

### Backend Setup

1. **Navigate to the backend directory**:
   ```sh
   cd ../backend
   ```

2. **Create a virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Start the FastAPI server**:
   ```sh
   uvicorn main:app --reload
   ```

## Frontend-Backend Communication

The frontend communicates with the backend via API calls. The backend exposes RESTful APIs that the frontend can use to interact with the language models and manage data related to generative AI prompts and their templates.

## Documentation

Detailed documentation is available in the `docs/` directory, including:

- Project description
- Design
- Installation instructions
- API specifications
- Usage guidelines

## Acknowledgements

This project acknowledges the use of the following Code Generative AI tools and libraries:

- **Code Generative AI Tools**: bolt.new, GitHub Copilot
- **Libraries**: LangChain, DSPy.ai
