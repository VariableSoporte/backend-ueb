from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
import os

template_router = APIRouter()


@template_router.get("/")
async def get_template():
    # Directorio de imágenes"
    # Obtener la ruta de la imagen desde la bd
    image_directory = 'templates/template.xlsx'

    # Ruta completa de la imagen
    file_path = os.path.join(image_directory)
    # Verificar si el archivo existe
    if os.path.exists(file_path):
        return FileResponse(file_path, filename='plantilla_carga_cursos.xlsx')
        # return file_path
    else:
        return file_path
