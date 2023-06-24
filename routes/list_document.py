from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import SessionLocal
from repositories import lists as crud_list
from repositories import list_documents as crud_list_document
import schemas.list_documents as list_document_schema
from fastapi import UploadFile, File
from fastapi.responses import FileResponse
import os


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


list_document_router = APIRouter()


@list_document_router.post(
    "/{list_id}/{document}", response_model=list_document_schema.ListDocument)
def add_document(file: UploadFile = File(...), list_id: int = 0, db: Session = Depends(get_db), document: str = "document"):
    # Obtener la lista
    list = crud_list.get_list(db, list_id=list_id)
    # Crear un directorio para la lista si no existe
    os.makedirs(f"docs/lists/{list_id}", exist_ok=True)
    # Obtén la extensión del archivo
    extension = os.path.splitext(file.filename)[1]
    # Cambiar el nombre del archivo
    file.filename = f"{list.name}{document}{extension}"
    # Crear la ruta donde se almacenara el documento
    # Ruta para la base de datos
    path_db = f"docs/lists/{list_id}/{file.filename}"

    # Esquema para insertar en la base de datos
    schema = list_document_schema.ListDocumentCreate(
        document=path_db, list_id=list_id)

    file_path = os.path.join(f"docs/lists/{list_id}", file.filename)
    # Guardar el documento en la ruta especificada
    with open(file_path, "wb") as document:
        document.write(file.file.read())
    # Agregar el documento a la base de datos
    db_list_document = crud_list_document.create_list_document(
        db=db, list_document=schema)
    return db_list_document


@list_document_router.get("/{document_id}")
def get_list_document(document_id: int, db: Session = Depends(get_db)):
    # Obtener la ruta del documento de la base de datos
    db_list_document = crud_list_document.get_list_document(
        db, list_document_id=document_id)
    # Obtener el documento
    document = db_list_document.document
    file_path = os.path.join(document)
    # Verificar si el archivo existe
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        return file_path


@list_document_router.put("/{document_id}")
def update_list_document(file: UploadFile = File(...), document_id: int = 0, db: Session = Depends(get_db), document_type: str = "document"):
    document = crud_list_document.get_list_document(
        db, list_document_id=document_id)
    list_id = document.list_id
    # Obtener la lista
    list = crud_list.get_list(db, list_id=document.list_id)
    print(list.name)
    # Crear un directorio para la lista si no existe
    os.makedirs(f"docs/lists/{document.list_id}", exist_ok=True)
    # Obtén la extensión del archivo
    extension = os.path.splitext(file.filename)[1]
    # Cambiar el nombre del archivo
    file.filename = f"{list.name}_{document_type}{extension}"
    # Crear la ruta donde se almacenara el documento
    # Ruta para la base de datos
    path_db = f"docs/lists/{document.list_id}/{file.filename}"


    file_path = os.path.join(f"docs/lists/{document.list_id}", file.filename)
    # Guardar el documento en la ruta especificada
    with open(file_path, "wb") as document:
        document.write(file.file.read())
    # Actualizar el documento en la base de datos
    db_list_document = crud_list_document.update_list_document(
        db=db, list_document_id=document_id, document=path_db)
    return db_list_document


@list_document_router.delete("/{document_id}")
def delete_list_document(document_id: int, db: Session = Depends(get_db)):
    # Obtener la ruta del documento de la base de datos
    db_list_document = crud_list_document.get_list_document(
        db, list_document_id=document_id)
    # Obtener el documento
    document = db_list_document.document
    file_path = os.path.join(document)
    # Verificar si el archivo existe
    if os.path.exists(file_path):
        os.remove(file_path)
    # Eliminar el documento de la base de datos
    db_list_document = crud_list_document.delete_list_document(
        db, list_document_id=document_id)
    return db_list_document