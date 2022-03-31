from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/workcore'
