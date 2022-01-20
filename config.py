from dataclasses import dataclass
from os import getenv


@dataclass
class Config:
    """
    Maciej, put here all your config.
    """
    SECRET_KEY = "Nie zgdadniesz"
    SQLALCHEMY_DATABASE_URI: getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False