from pydantic import BaseModel
from .student import Student


class CourseBase(BaseModel):
    id: int
    level: str
    parallel: str

    class Config:
        orm_mode = True


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    # id: int
    students: list[Student] = []
    data_file: str

    class Config:
        orm_mode = True

class CourseStudents(BaseModel):
    students: list[Student] = []

    class Config:
        orm_mode = True
