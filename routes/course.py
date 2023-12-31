from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from config.database import SessionLocal
from schemas import course as course_schema
import os
from sqlalchemy.sql import text

from repositories import courses as crud

course_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@course_router.get('/', response_model=list[course_schema.CourseList])
def get_courses(db: Session = Depends(get_db)):
    return crud.get_courses(db)


@course_router.get('/{course_id}', response_model=course_schema.CourseStudents)
def get_students_by_course(course_id: int, db: Session = Depends(get_db)):
    return crud.get_course(db, course_id)


@course_router.post('/', response_model=course_schema.CourseList)
def create_course(course: course_schema.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db, course)


@course_router.get('/file/{course_id}')
def get_course_data_file(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db=db, course_id=course_id)
    file_path = f"data/courses/{db_course.data_file}"
    return FileResponse(file_path, media_type="application/octet-stream", filename=db_course.data_file)


@course_router.post('/masive/')
def add_students_and_courses(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Directorio del xlsx
    xlsx_directory = "data/"
    # Crea el directorio de xlsx si no existe
    os.makedirs(xlsx_directory, exist_ok=True)
    # Obtén la extensión del archivo
    extension = os.path.splitext(file.filename)[1]
    file.filename = f"carga_masiva{extension}".replace(" ", "_").lower()
    # Guardar el archivo en la ruta especificada
    with open(os.path.join(xlsx_directory, file.filename), "wb") as buffer:
        buffer.write(file.file.read())
    # Carga masiva de estudiantes y cursos
    crud.add_students_and_courses(db=db)
    return True


@course_router.get('/masive/')
def get_masive():
    if os.path.exists("data/carga_masiva.xlsx"):
        return FileResponse("data/carga_masiva.xlsx", media_type="application/octet-stream", filename="carga_masiva.xlsx")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontró el archivo")


@course_router.put('/masive/')
def edit_masive(file: UploadFile = File(...), db: Session = Depends(get_db)):
    crud.delete_students(db=db)
    crud.delete_courses(db=db)
    # db.execute('ALTER TABLE courses AUTO_INCREMENT = 1')
    db.execute(text('ALTER TABLE courses AUTO_INCREMENT = 1'))
    # db.execute('ALTER TABLE students AUTO_INCREMENT = 1')
    db.execute(text('ALTER TABLE students AUTO_INCREMENT = 1'))
    return add_students_and_courses(file=file, db=db)


@course_router.post("/{course_id}", response_model=course_schema.Course)
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
    file.filename = f"{level}-{parallel}{extension}".replace(" ", "_").lower()

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


@course_router.delete('/{course_id}')
def delete_course(course_id: int, db: Session = Depends(get_db)):
    # crud.delete_candidates_by_course(db=db, course_id=course_id)
    crud.delete_students_by_course(db=db, course_id=course_id)
    crud.delete_course(db=db, course_id=course_id)
    return True



