from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal
from repositories import candidates as crud
import schemas.candidate as candidate_schema
from fastapi import UploadFile, File
from fastapi.responses import FileResponse
import os

candidate_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@candidate_router.post("/", response_model=candidate_schema.Candidate)
async def add_candidate(candidate: candidate_schema.CandidateCreate, db: Session = Depends(get_db)) -> any:
    aux = crud.student_is_candidate(db=db, student_id=candidate.student_id)
    if aux:
        raise HTTPException(status_code=400, detail="El estudiante ya es candidato")
    db_candidate = crud.create_candidate(db=db, candidate=candidate)
    return db_candidate

# @candidate_router.options


@candidate_router.post("/photo/{candidate_id}")
def upload_photo(file: UploadFile = File(...), candidate_id: int = 0, db: Session = Depends(get_db)):
    # Directorio de imágenes
    image_directory = "images/candidates"
    # Crea el directorio de imágenes si no existe
    os.makedirs(image_directory, exist_ok=True)
    # Obtén la extensión del archivo
    extension = os.path.splitext(file.filename)[1]
    # Crea la ruta donde se almacenará la imagen en el directorio de imágenes
    file_path = os.path.join(image_directory, file.filename)
    # Guarda la imagen en la ruta especificada
    with open(file_path, "wb") as image:
        image.write(file.file.read())

    # Actualiza la ruta de la imagen en la base de datos
    file_path = f"images/candidates/{file.filename}"
    db_candidate = crud.update_candidate(
        db=db, candidate_id=candidate_id, file=file_path)
    print(db_candidate)
    return db_candidate
    # return file_path


@candidate_router.get("/image/{candidate_id}")
async def get_image(candidate_id: str, db: Session = Depends(get_db)):
    # Obtener la ruta de la imagen desde la bd
    db_candidate = crud.get_candidate(db=db, candidate_id=candidate_id)
    image_directory = db_candidate.photo
    # Ruta completa de la imagen
    file_path = os.path.join(image_directory)
    # Verificar si el archivo existe
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        return file_path


@candidate_router.put("/image/{candidate_id}", response_model=candidate_schema.Candidate)
async def update_image(candidate_id: int, db: Session = Depends(get_db), file: UploadFile = File(...)):
    # Directorio de imágenes
    image_directory = "images/candidates"
    # Crea el directorio de imágenes si no existe
    os.makedirs(image_directory, exist_ok=True)
    # Obtén la extensión del archivo
    extension = os.path.splitext(file.filename)[1]
    # Crea la ruta donde se almacenará la imagen en el directorio de imágenes
    file_path = os.path.join(image_directory, file.filename)
    # Guarda la imagen en la ruta especificada
    with open(file_path, "wb") as image:
        image.write(file.file.read())

    # Actualiza la ruta de la imagen en la base de datos
    file_path = f"images/candidates/{file.filename}"
    db_candidate = crud.update_candidate(
        db=db, candidate_id=candidate_id, file=file_path)
    print(db_candidate)
    return db_candidate
    # return file_path


@candidate_router.put("/{candidate_id}", response_model=candidate_schema.Candidate)
async def update_candidate(candidate_id: int, candidate: candidate_schema.CandidateCreate, db: Session = Depends(get_db)):
    db_candidate = crud.update_candidate_by_id(
        db=db, candidate_id=candidate_id, candidate=candidate)
    return db_candidate
