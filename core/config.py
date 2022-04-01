from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:11231325@localhost:3306/workcore'
