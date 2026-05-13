import os


class Settings:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_USER = os.getenv("DB_USER", "username")
    DB_PASSWORD = os.getenv("DB_NAMEL_PASSWORD", "fQnyLZSu2-KhV!c0=6am")
    DB_NAME = os.getenv("DB_NAME", "reigor")
    def database_url(self):
        return (
    f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}"
    f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    )


settings = Settings()
