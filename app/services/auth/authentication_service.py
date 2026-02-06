from passlib.context import CryptContext
from services.service import Service

# from bcrypt import bcrypt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthenticatonService(Service):
    
    """
    Docstring for AuthenticatonService
    Authentication service to handle user authentication and registration.
    """
    
    """authenticatoin
       
    
    """
    def authenticate(self, username: str, password: str) -> bool:
        # Implement authentication logic here
        return True
    
    
    
    
    
    def phase_one_register(self, email: str) -> str:
        """Phase one of registration, 
        used to hydrate the user email
        on a pahse level registration

        Args:
            email (str): _description_

        Returns:
            str: _description_
        """
        # Implement phase one registration logic here
        return "phase_one_token"
    
    
    
        
    def register_user(self, user_data: dict) -> dict:
        """Registers the user 

        Args:
            user_data (dict): _description_

        Returns:
            dict: _description_
        """
        # Implement user registration logic here
        return {}
    
    
    
    
    def encrypt_password(self, password: str) -> str:
        """Used to encrypt the ppassword

        Args:
            password (str): _description_

        Returns:
            str: _description_
        """
        # Implement password encryption logic here
        return pwd_context.hash(password)
    
    
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """used to verify the password

        Args:
            plain_password (str): _description_
            hashed_password (str): _description_

        Returns:
            bool: _description_
        """
        return True
    
    
    def run(self):
        return super().run()
    
    def setup(self, data: dict = {}):
        return super().setup(data)
    
