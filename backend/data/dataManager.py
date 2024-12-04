import json
from typing import List, Dict, Any

class DataManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self) -> List[Dict[str, Any]]:
        """Load data from the JSON file."""
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self) -> None:
        """Save data to the JSON file."""
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_prompt(self, prompt: Dict[str, Any]) -> None:
        """Add a new prompt to the data."""
        self.data.append(prompt)
        self.save_data()

    def get_prompts(self) -> List[Dict[str, Any]]:
        """Retrieve all prompts from the data."""
        return self.data

    def update_prompt(self, index: int, updated_prompt: Dict[str, Any]) -> None:
        """Update an existing prompt in the data."""
        if 0 <= index < len(self.data):
            self.data[index] = updated_prompt
            self.save_data()

    def delete_prompt(self, index: int) -> None:
        """Delete a prompt from the data."""
        if 0 <= index < len(self.data):
            self.data.pop(index)
            self.save_data()
