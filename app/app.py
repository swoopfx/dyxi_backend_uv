from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.routers import auth, machine


app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(machine.router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None): # type: ignore
    return {"item_id": item_id, "q": q}

@app.post("/items/")
async def create_item(item: dict):
    return {"created": item}
