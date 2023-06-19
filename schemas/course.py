from pydantic import BaseModel
from .student import Student


class CourseBase(BaseModel):
    level: str
    parallel: str


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int
    students: list[Student] = []
    data_file: str

    class Config:
        orm_mode = True