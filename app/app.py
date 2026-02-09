from fastapi import Depends, FastAPI, HTTPException, UploadFile, File, 
Depends
from starlette.responses import JSONResponse, FileResponse
from starlette import status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import uvicorn
import os
from fastapi.staticfiles import StaticFiles

from app.routers import auth, machine


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
favicon_path = os.path.join(os.path.dirname(__file__), "static",  "favicon.ico") 

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

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
