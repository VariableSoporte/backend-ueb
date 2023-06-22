from fastapi import FastAPI
from routes import courses, students, dignities, candidates, lists, users, vote, students_new
from database import engine
import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:80",
    "http://localhost:8080",
    "http://localhost:8081",
    "http://localhost:8082",
    "http://localhost:8083",
    "http://localhost:8084",
    "http://localhost:55451",
    "http://localhost:5000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

app.include_router(courses.course_router, prefix="/courses", tags=["courses"])
# app.include_router(students.student_router, prefix="/students", tags=["students"])
app.include_router(dignities.dignity_router,
                   prefix="/dignities", tags=["dignities"])
app.include_router(candidates.candidate_router,
                   prefix="/candidates", tags=["candidates"])
app.include_router(lists.list_router, prefix="/lists", tags=["lists"])
app.include_router(users.user_router, prefix="/users", tags=["users"])
app.include_router(vote.votes_router, prefix="/votes", tags=["votes"])
app.include_router(students_new.test_router,
                   prefix="/students", tags=["students"])
