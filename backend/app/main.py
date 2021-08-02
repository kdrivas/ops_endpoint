from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api import petals
from app.db.base_class import Base
from app.db.session import engine

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(petals.router)

## Uncomment to create table automatically with metadata
# Base.metadata.create_all(bind=engine)

@app.get('/', status_code=201)
def root():
	return {"message": "I'm alive"}