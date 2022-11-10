from pydantic import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    algorithm: str
    access_token_expiry_minutes: int
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str

    class Config:
        env_file = ".env"

settings = Settings()