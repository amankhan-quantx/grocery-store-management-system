import os

class Config:
    SECRET_KEY = "change-this-later"
    DATABASE = os.path.join("database", "grocery.db")