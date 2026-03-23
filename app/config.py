from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    user_id: str
    school_no: str
    name: str
    authorization: str
    cron: str
    location_name: str
    location_lon: float
    location_lat: float
    sign_any_time: bool = False


# noinspection PyArgumentList
settings = Settings()

