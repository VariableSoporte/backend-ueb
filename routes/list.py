from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal
from repositories import lists as crud
import schemas.list as list_schema
from fastapi import UploadFile, File
from fastapi.responses import FileResponse
import os

list_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@list_router.get("/", response_model=list[list_schema.List])
def get_lists(db: Session = Depends(get_db)):
    try:
        lists = crud.get_lists(db)
        return lists
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@list_router.get("/unorder", response_model=list[list_schema.List])
def get_lists_unorder(db: Session = Depends(get_db)):
    try:
        lists = crud.get_lists_unorder(db)
        return lists
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@list_router.get("/{list_id}", response_model=list_schema.List)
def get_list(list_id: int, db: Session = Depends(get_db)):
    try:
        list = crud.get_list(db, list_id=list_id)
        return list
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@list_router.post("/", response_model=list_schema.List)
def create_list(list: list_schema.ListCreate, db: Session = Depends(get_db)):
    try:
        db_list = crud.create_list(db=db, list=list)
        return db_list
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@list_router.post("/logo/{list_id}")
def add_list_logo(file: UploadFile = File(...), list_id: int = 0, db: Session = Depends(get_db)):
    try:
        # Directorio de imágenes
        image_directory = "images/lists"
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
        file_path = f"images/lists/{file.filename}"
        db_list = crud.update_list_logo(
            db=db, list_id=list_id, file=file_path)
        return db_list
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@list_router.get("/logo/{list_id}")
async def get_list_logo(list_id: str, db: Session = Depends(get_db)):
    # Directorio de imágenes"
    # Obtener la ruta de la imagen desde la bd
    db_list = crud.get_list(db=db, list_id=list_id)
    image_directory = db_list.logo
    # Ruta completa de la imagen
    file_path = os.path.join(image_directory)
    # Verificar si el archivo existe
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        return HTTPException(status_code=404, detail="File not found")


@list_router.put("/logo/{list_id}")
def update_list_logo(file: UploadFile = File(...), list_id: int = 0, db: Session = Depends(get_db)):
    try:
        # Directorio de imágenes
        image_directory = "images/lists"
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
        file_path = f"images/lists/{file.filename}"
        db_list = crud.update_list_logo(
            db=db, list_id=list_id, file=file_path)
        return db_list
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@list_router.put("/{list_id}", response_model=list_schema.List)
def update_list(list_id: int, list: list_schema.ListCreate, db: Session = Depends(get_db)):
    try:
        db_list = crud.update_list(db=db, list_id=list_id, list=list)
        return db_list
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@list_router.delete("/{list_id}")
def delete_list(list_id: int, db: Session = Depends(get_db)):
    try:
        crud.delete_list_documents(db=db, list_id=list_id)
        crud.delete_candidates_from_list(db=db, list_id=list_id)
        crud.delete_list(db=db, list_id=list_id)
        return True
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
