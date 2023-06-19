from fastapi import APIRouter, Depends
import schemas.course as course_schema
from database import SessionLocal
from repositories import courses_repository as crud
from sqlalchemy.orm import Session
from fastapi import UploadFile, File
from fastapi.responses import FileResponse
import os

course_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@course_router.post("/", response_model=course_schema.Course)
def create_course(course: course_schema.CourseCreate, db: Session = Depends(get_db)):
    db_course = crud.create_course(db=db, course=course)
    return db_course


@course_router.get("/", response_model=list[course_schema.Course])
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses


@course_router.put("/{course_id}", response_model=course_schema.Course)
def update_course_data_file(file: UploadFile = File(...), course_id: int = 0, db: Session = Depends(get_db)):
    # Obtenemos el curso de la base de datos
    db_course = crud.get_course(db=db, course_id=course_id)
    # Obtenemos el nivel y paralelo del curso
    id = db_course.id
    level = db_course.level
    parallel = db_course.parallel
    # Directorio de imágenes
    image_directory = "data/courses"
    # Crea el directorio de imágenes si no existe
    os.makedirs(image_directory, exist_ok=True)
    # Obtén la extensión del archivo
    extension = os.path.splitext(file.filename)[1]
    file.filename = f"{level}-{parallel}{extension}".replace(" ","_").lower()
    
    # Crea la ruta donde se almacenará la imagen en el directorio de imágenes
    file_path = os.path.join(image_directory, file.filename)
    # Guarda la imagen en la ruta especificada
    with open(file_path, "wb") as image:
        image.write(file.file.read())

    # Actualiza la ruta de la imagen en la base de datos
    file_path = f"{file.filename}"
    db_course = crud.update_course_data_file(
        db=db, course_id=course_id, file=file_path)
    crud.add_students(db=db, course_id=course_id)
    return db_course
