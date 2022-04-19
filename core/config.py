from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:11231325@192.168.105.12:3306/workcore'
    API_V1_STR: str = "/api/v1"
