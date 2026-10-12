from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = "sqlite:///./notes.db"
    ENVIRONMENT: str = "development"

    class Config:
        env_file = ".env"


def get_settings() -> Settings:
    return Settings()