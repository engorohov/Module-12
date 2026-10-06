from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_host: str = "localhost"
    db_port: int = 5432
    debug: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
print(settings.db_host, type(settings.db_port))
print(settings.debug, type(settings.debug))
