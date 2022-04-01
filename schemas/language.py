from pydantic import BaseModel
from typing import Optional


class LanguageBase(BaseModel):
    lang_code: str
    en_des: str
    cn_des: str


class LanguageCreate(LanguageBase):
    pass


class Language(LanguageBase):
    id: int

    class Config:
        orm_mode = True
