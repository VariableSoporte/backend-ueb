from pydantic import BaseModel


class StudentBase(BaseModel):
    identification_card: str
    patern_lastname: str
    matern_lastname: str
    first_name: str
    second_name: str
    can_vote: bool
    course_id: int


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True


class CourseBase(BaseModel):
    level: str
    parallel: str


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int
    students: list[Student] = []

    class Config:
        orm_mode = True
