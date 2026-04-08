import requests

class LoginSystem:
    def __init__(self,baseUrl):
        self.url = f"{baseUrl}/login"

    def check(self, username, password):
            try:
                response = requests.post(self.url, json={
                    "username": username, 
                    "password": password
                })
                if response.status_code == 200:
                    return True, response.json()
                return False, "Invalid Credentials"
            except Exception as e:
                return False, str(e)

    def forgotPassword():
        pass

class RegisterSystem:
    def __init__(self,baseUrl):
        self.url = f"{baseUrl}/register"

    def addUser(self, username, gmail, phone, password, confirmPassword):
            if password != confirmPassword:
                return False, "Passwords do not match!"
    
            if not username or not gmail or not password:
                return False, "Fields cannot be empty!"
            payload = {
                "username": username,     
                "gmail": gmail,
                "phone": phone,
                "password": password,
                "id": 999,           
                "rooms": []          
            }
            try:
    
                response = requests.post(self.url, json=payload, timeout=5)

                if response.status_code == 200:
                    return True, response.json()
                error_data = response.json()
                return False, error_data.get("detail", "Registration failed")
                
            except Exception as e:
                return False, f"Connection failed: {str(e)}"
            
class ForgetPasswordSystem:
    def __init__(self):
        pass

    def setNewPassword(char,int):
        pass


class UserLoginDetails:
    def __init__(self):
        self.password = " "

    def setPassword():
        pass

    def setUsername():
        pass
