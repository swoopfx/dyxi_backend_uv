import os
from dotenv import load_dotenv

envpath = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=envpath)



class Settings:
    db_url = os.getenv("DB_URL", "sqlite+aiosqlite:///./test.db")
    jwt_secret = os.getenv("JWT_SECRET")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MIN = int(os.getenv("ACCESS_TOKEN_EXPIRE_MIN", "30"))
    
    
    APP_DEBUG = os.getenv("APP_DEBUG", "False").lower() == "true" 
    

settings = Settings()
