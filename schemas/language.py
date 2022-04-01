from pydantic import BaseModel
from typing import Optional


class LanguageBase(BaseModel):
    id: int
    lang_code: str
    en_des: str
    cn_des: str


class LanguageCreate(LanguageBase):
    pass


class Language(LanguageBase):

    class Config:
        orm_mode = True

