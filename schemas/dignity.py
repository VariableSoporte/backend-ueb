from pydantic import BaseModel


class DignityBase(BaseModel):
    dignity: str


class DignityCreate(DignityBase):
    pass


class Dignity(DignityBase):
    id: int

    class Config:
        orm_mode = True
