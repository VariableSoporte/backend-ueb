from pydantic import BaseModel


class VoteNullBase(BaseModel):
    pass


class VoteNullCreate(VoteNullBase):
    pass


class VoteNull(VoteNullBase):
    null_votes: int
    blank_votes: int
    null_votes_morning: int
    blank_votes_morning: int
    null_votes_afternoon: int
    blank_votes_afternoon: int

    class Config:
        orm_mode = True
