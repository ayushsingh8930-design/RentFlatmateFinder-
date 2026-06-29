from fastapi import FastAPI

from app.config import settings
from app.database import engine, Base
from app.models import user, property
from app.routers.user import router as user_router
from app.routers.property import router as property_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

Base.metadata.create_all(bind=engine)



@app.get("/")
def root():
    return {
        "message": "Welcome to Rent & Flatmate Finder API 🚀"
    }
app.include_router(user_router)
app.include_router(property_router)