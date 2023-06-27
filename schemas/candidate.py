from pydantic import BaseModel
from schemas.dignity import Dignity
from schemas.student import StudentCourse


class CandidateBase(BaseModel):
    pass


class CandidateCreate(CandidateBase):
    student_id: int
    dignity_id: int
    list_id: int


class Candidate(CandidateBase):
    id: int
    photo: str
    student: StudentCourse
    dignity: Dignity

    class Config:
        orm_mode = True
