import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Settings:
    PROJECT_NAME: str = "Airline Microservice"
    API_V1_STR: str = "/api/v1"
    MYSQL_USER: str = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD")
    MYSQL_SERVER: str = os.getenv("MYSQL_SERVER", "localhost")  # Default to localhost
    MYSQL_PORT: str = os.getenv("MYSQL_PORT", "3306")  # Default to 3306
    MYSQL_DB: str = os.getenv("MYSQL_DB")

    SQLALCHEMY_DATABASE_URI: str = ""

    def assemble_db_connection(self) -> str:
        return f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_SERVER}:{self.MYSQL_PORT}/{self.MYSQL_DB}"

settings = Settings()
settings.SQLALCHEMY_DATABASE_URI = settings.assemble_db_connection()