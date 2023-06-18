from pydantic import BaseModel
from .student import Student
from .dignity import Dignity


class CandidateBase(BaseModel):
    photo: str
    student_id: int
    


class CandidateCreate(CandidateBase):
    dignity_id: int
    pass


class Candidate(CandidateBase):
    student: Student
    dignity: Dignity

    class Config:
        orm_mode = True
