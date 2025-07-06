from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_uri: str = "mysql+aiomysql://localhost:5432/tournaments"
    secret_key: str = "qwerty"
    exp_time_minutes: int = 30


settings = Settings()