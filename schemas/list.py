from pydantic import BaseModel
from .candidate import Candidate

class ListBase(BaseModel):
    name: str
    logo: str

class ListCreate(ListBase):
    pass

class List(ListBase):
    id: int
    candidates: list[Candidate] = []

    class Config:
        orm_mode = True