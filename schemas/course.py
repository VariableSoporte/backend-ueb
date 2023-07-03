from pydantic import BaseModel

from schemas.student import Student


class CourseBase(BaseModel):
    level: str
    parallel: str

    class Config:
        orm_mode = True


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int
    data_file: str
    students: list[Student] = []

    class Config:
        orm_mode = True


class CourseList(BaseModel):
    id: int
    level: str
    parallel: str
    journal: str

    class Config:
        orm_mode = True


class CourseStudents(BaseModel):
    students: list[Student] = []

    class Config:
        orm_mode = True
