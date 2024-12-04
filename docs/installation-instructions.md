# Installation Instructions

## Frontend Setup

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

## Backend Setup

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

## Additional Notes

- Ensure that you have Python 3.10, 3.11, or 3.12 installed for the backend. (3.13 not yet supported)
- The frontend will be available at `http://localhost:3000` and the backend at `http://localhost:8000`.
