from pydantic import BaseModel
from .student import Student


class DignityBase(BaseModel):
    dignity: str


class DignityCreate(DignityBase):
    pass


class Dignity(DignityBase):
    id: int
    # candidates: list[Candidate] = []

    class Config:
        orm_mode = True
