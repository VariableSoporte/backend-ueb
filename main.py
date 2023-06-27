from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from config.database import engine
from models import models
from routes import candidate, course, dignity, list, student, template, user, vote, list_document
from starlette.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.options("/ruta")
async def options_route():
    return {"Allow": "POST"}, 200


app.include_router(candidate.candidate_router,
                   prefix="/candidates", tags=["candidates"])
app.include_router(course.course_router, prefix="/courses", tags=["courses"])
app.include_router(dignity.dignity_router,
                   prefix="/dignities", tags=["dignities"])
app.include_router(list.list_router, prefix="/lists", tags=["lists"])
app.include_router(student.students,
                   prefix="/students", tags=["students"])
app.include_router(template.template_router,
                   prefix="/templates", tags=["templates"])
app.include_router(user.user_router, prefix="/users", tags=["users"])
app.include_router(vote.vote_router, prefix="/votes", tags=["votes"])
app.include_router(list_document.list_document_router,
                   prefix="/list-documents", tags=["list-documents"])
