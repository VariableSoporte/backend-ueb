from sqlalchemy.orm import Session
import pandas as pd
from models import models
from config.database import engine
from schemas.course import CourseCreate
from sqlalchemy.orm import aliased
from sqlalchemy.sql import exists


def get_courses(db: Session):
    return db.query(models.Course).all()


def create_course(db: Session, course: CourseCreate):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()


def update_course_data_file(db: Session, course_id: int, file: str):
    db.query(models.Course).filter(models.Course.id ==
                                   course_id).update({"data_file": file})
    db.commit()
    return db.query(models.Course).filter(models.Course.id == course_id).first()


def add_students(db: Session, course_id: int):
    db_course = get_course(db, course_id)
    df = pd.read_excel(
        f'data/courses/{db_course.data_file}', dtype={'identification_card': str})
    df = df.assign(course_id=course_id)
    df = df.assign(can_vote=True)
    df.to_sql('students', con=engine, if_exists='append', index=False)
    db.commit()
    return {True}


def concate_columns(row):
    return f'{row["course"]}-{row["parallel"]}-{row["journal"]}'


def add_students_and_courses(db: Session):
    file_route = 'data/carga_masiva.xlsx'
    data = pd.read_excel(file_route, dtype={'identification_card': str})
    courses = [(row['course'], row['parallel'], row['journal']) for _, row in data.iterrows()]
    courses = list(set(courses))
    courses_list = [models.Course(level=course[0], parallel=course[1], journal=course[2]) for course in courses]
    data['course_id'] = data.apply(concate_columns, axis=1)
    data = data.drop(columns=['course', 'parallel', 'journal'])
    data['course_id'] = pd.factorize(data['course_id'])[0] + 1
    students = [models.Student(identification_card=row['identification_card'], patern_lastname=row['patern_lastname'], matern_lastname=row['matern_lastname'], first_name=row['first_name'], second_name=row['second_name'], course_id=row['course_id']) for _, row in data.iterrows()]
    db.add_all(students)
    db.add_all(courses_list)
    db.commit()

def get_students_by_course(db: Session, course_id: int):
    return db.query(models.Student).filter(models.Student.course_id == course_id).all()


def delete_students_by_course(db: Session, course_id: int):
    db.query(models.Student).filter(
        models.Student.course_id == course_id).delete()
    db.commit()
    return True


def delete_course(db: Session, course_id: int):
    db.query(models.Course).filter(models.Course.id == course_id).delete()
    db.commit()
    return {True}


def delete_candidates_by_course(db: Session, course_id: int):
    aux = db.query(models.Candidate).join(models.Student).filter(
        models.Student.course_id == course_id).delete()
    db.commit()
    # db.commit()
    return True
