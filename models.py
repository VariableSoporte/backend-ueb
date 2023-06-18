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

    candidate = relationship('Candidate', uselist=False,
                             back_populates='student')


class Course(Base):

    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    level = Column(String(50))
    parallel = Column(String(2))

    students = relationship('Student', back_populates='course')


class Dignity(Base):

    __tablename__ = 'dignities'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dignity = Column(String(50), unique=True, index=True)

    candidate = relationship('Candidate', back_populates='dignity')


class Candidate(Base):

    __tablename__ = 'candidates'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    photo = Column(String(200), nullable=True)

    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship('Student', back_populates='candidate')

    dignity_id = Column(Integer, ForeignKey('dignities.id'))
    dignity = relationship('Dignity', back_populates='candidate')

    list_id = Column(Integer, ForeignKey('lists.id'))
    list = relationship('List', back_populates='candidate')


class List(Base):

    __tablename__ = 'lists'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))
    logo = Column(String(200))

    candidate = relationship('Candidate', back_populates='list')
    votes = relationship('Votes', back_populates='list')


class Votes(Base):

    __tablename__ = 'votes'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    votes = Column(Integer, default=0)

    list_id = Column(Integer, ForeignKey('lists.id'))
    list = relationship('List', back_populates='votes')
