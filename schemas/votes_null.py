from pydantic import BaseModel

class VotesNullBase(BaseModel):
    pass

class VotesNullCreate(VotesNullBase):
    pass

class VotesNull(VotesNullBase):
    # id: int
    null_votes: int
    blank_votes: int

    class Config:
        orm_mode = True