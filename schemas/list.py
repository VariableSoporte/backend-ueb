from pydantic import BaseModel
from schemas.candidate import Candidate
from schemas.list_documents import ListDocument


class ListBase(BaseModel):
    pass


class ListCreate(ListBase):
    name: str


class List(ListBase):
    id: int
    name: str
    logo: str
    votes: int
    candidates: list[Candidate] = []
    list_documents: list[ListDocument] = []

    class Config:
        orm_mode = True
