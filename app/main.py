from fastapi import FastAPI, APIRouter
from app import api
from fastapi.middleware.cors import CORSMiddleware
from config import settings
import logging

app = FastAPI()
app.title = settings.PROJECT_NAME
app.version = settings.PROJECT_VERSION
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

api_v1_auth = APIRouter(prefix='/api/v1/auth')
app.include_router(api.health_check_router)
app.include_router(api.list_router)
app.include_router(api_v1_auth)

app_test = app
