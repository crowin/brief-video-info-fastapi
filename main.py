import os

from fastapi import FastAPI
from fastapi.params import Depends

from app.api import endpoints
from app.clients.openai_digest import OpenAIClient

app = FastAPI()


def create_openai_client() -> OpenAIClient:
    return OpenAIClient(api_key=os.getenv("OPENAI_API_KEY"))

app.include_router(endpoints.router, prefix="/api/v1/", tags=["service api"], dependencies=[Depends(create_openai_client)])

app.get("/")
def read_root():
    return {"Service": "VidDigest API", "Version": "0.0.1"}
