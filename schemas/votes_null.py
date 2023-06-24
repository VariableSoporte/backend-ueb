from pydantic import BaseModel


class VoteNullBase(BaseModel):
    pass


class VoteNullCreate(VoteNullBase):
    pass


class VoteNull(VoteNullBase):
    null_votes: int
    blank_votes: int

    class Config:
        orm_mode = True
