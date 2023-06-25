from pydantic import BaseModel


class StudentBase(BaseModel):
    identification_card: str
    patern_lastname: str
    matern_lastname: str
    first_name: str
    second_name: str
    course_id: int


class StudentCreate(StudentBase):
    pass


class StudentEdit(StudentBase):
    pass


class Student(StudentBase):
    id: int
    can_vote: bool

    class Config:
        orm_mode = True
