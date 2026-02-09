from abc import ABC, abstractmethod

class AuthInterface(ABC):
    @abstractmethod
    def register(self, username: str, password: str) -> bool:
        pass

    @abstractmethod
    def login(self, username: str, password: str) -> str:
        pass

    @abstractmethod
    def logout(self, token: str) -> bool:
        pass
    
    @abstractmethod
    def refresh_token(self, refresh_token: str) -> str:
        pass        
    
    @abstractmethod
    def reset_password(self, username: str) -> bool:
        pass
    
    @abstractmethod
    def confirm_registration(self, username: str, confirmation_code: str) -> bool:
        pass
    
    @abstractmethod
    def change_password(self, username: str, old_password: str, new_password: str) -> bool:
        pass