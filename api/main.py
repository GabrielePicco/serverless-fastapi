"""Main file of the FastAPI simple app."""
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from api import __version__

stage = os.environ.get("STAGE", "")
root_path = f"/{stage}/" if stage else ""


app = FastAPI(title="serverless-fastapi", version=__version__, root_path=root_path)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/version")
def version():
    """GET / endpoint."""
    return {"message": f"API version: {__version__}"}


@app.get("/hello")
def hello():
    """GET /hello endpoint."""
    return {"message": "Hello World"}


handler = Mangum(app)
