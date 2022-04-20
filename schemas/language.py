from pydantic import BaseModel


class LanguageBase(BaseModel):
    lang_code: str
    en_des: str
    cn_des: str


class LanguageCreate(LanguageBase):
    pass


class Language(LanguageBase):
    id: int
    create_date: str
    last_modified: str

    class Config:
        orm_mode = True
