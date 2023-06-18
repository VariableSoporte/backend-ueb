from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    identification_card = Column(String(10), unique=True, index=True)
    patern_lastname = Column(String(50))
    matern_lastname = Column(String(50))
    first_name = Column(String(50))
    second_name = Column(String(50))
    can_vote = Column(Boolean, default=True)

    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship('Course', back_populates='students')

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    level = Column(String(50))
    parallel = Column(String(2))

    students = relationship('Student', back_populates='course')



    