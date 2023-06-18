from pydantic import BaseModel
from .list import List

class VotesBase(BaseModel):
    votes: int

class VotesCreate(VotesBase):
    pass

class Votes(VotesBase):
    id: int
    list: List

    class Config:
        orm_mode = True