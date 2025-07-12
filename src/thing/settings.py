"""thing Settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for thing."""

    model_config = SettingsConfigDict(
        env_prefix="THING",
        env_file=".env-thing",
    )
    debug: bool = False
