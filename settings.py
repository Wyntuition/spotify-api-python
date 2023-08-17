from pydantic_settings import BaseSettings


class RuntimeSettings(BaseSettings):
    CLIENT_ID = "<.ENV>"
    CLIENT_SECRET = "<.ENV-SECRET>"
