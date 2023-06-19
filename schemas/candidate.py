from pydantic import BaseModel
from .student import Student
from .dignity import Dignity
# from .list import List


class CandidateBase(BaseModel):
    photo: str
    student_id: int
    


class CandidateCreate(CandidateBase):
    dignity_id: int
    list_id: int
    pass


class Candidate(CandidateBase):
    student: Student
    dignity: Dignity
    # list: List

    class Config:
        orm_mode = True
