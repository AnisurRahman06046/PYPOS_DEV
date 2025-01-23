# auth/auth.py
import requests
from ..database import save_user_data, get_user_data

class Auth:
    @staticmethod
    def login(email, password):
        if not email or not password:
            raise ValueError("Email and password cannot be empty.")
        
        try:
            response = requests.post(
                "https://anzaar-api.bitcommerz.com/api/v1/auth/admin/pos/login", 
                json={"email": email, "password": password}
            )
            if response.status_code == 201:
                data = response.json()
                save_user_data(data)  # Save to DB
                return True, data
            else:
                return False, "Invalid credentials."
        except Exception as e:
            return False, f"Failed to connect to the server: {e}"
    
    @staticmethod
    def is_logged_in():
        user = get_user_data()
        return user is not None and user[7] is not None  # Check if token exists
