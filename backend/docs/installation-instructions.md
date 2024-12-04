# Backend Installation Instructions

## Prerequisites

Before setting up the backend, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment tool (venv)

## Setup Steps

### 1. Clone the Repository

Clone the repository to your local machine:

```sh
git clone https://github.com/pkuppens/genai-hackathon.git
cd genai-hackathon/backend
```

### 2. Create a Virtual Environment

Create a virtual environment to manage dependencies:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install the required dependencies using pip:

```sh
pip install -r requirements.txt
```

### 4. Start the FastAPI Server

Start the FastAPI server to handle API requests:

```sh
uvicorn main:app --reload
```

## Additional Configuration

### Environment Variables

You may need to set environment variables for configuration. Create a `.env` file in the `backend` directory and add your variables there. For example:

```sh
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your_secret_key
```

### Database Setup

If your application uses a database, ensure it is set up correctly. For example, if using SQLite, the database file will be created automatically. For other databases, refer to their specific setup instructions.

### Running Migrations

If your application uses database migrations, run the necessary commands to apply them. For example, using Alembic:

```sh
alembic upgrade head
```

## Testing

To run tests, use the following command:

```sh
pytest
```

Ensure all tests pass before deploying the application.

## Deployment

For deployment, consider using a production-ready server like Gunicorn along with a reverse proxy like Nginx. Refer to the FastAPI deployment documentation for detailed instructions.
