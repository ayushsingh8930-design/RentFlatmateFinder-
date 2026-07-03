from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Rent & Flatmate Finder API"
    APP_VERSION: str = "1.0.0"

    DATABASE_URL: str = "sqlite:///./rent_flatmate.db"

    SECRET_KEY: str = "your_super_secret_key_here_change_this_2026"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    EMAIL_HOST: str = "smtp.gmail.com"
    EMAIL_PORT: int = 587
    EMAIL_USERNAME: str = ""
    EMAIL_PASSWORD: str = ""

    GEMINI_API_KEY: str = ""

    class Config:
        env_file = ".env"


settings = Settings()