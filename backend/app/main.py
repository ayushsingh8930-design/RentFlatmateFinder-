from fastapi import FastAPI
from app.config import settings
from app.database import engine, Base
from app.models import user, property
from app.routers.user import router as user_router
from app.routers.property import router as property_router
from app.models import PropertyImage
from app.routers.property_image import router as property_image_router
from app.models import tenant_profile 
from app.routers.tenant_profile import router as tenant_profile_router
from app.models import Compatibility
from app.routers.compatibility import router as compatibility_router
from app.models import Interest
from app.routers.interest import router as interest_router
from app.models import Message
from app.routers.message import router as message_router
from app.routers.chat import router as chat_router
from app.routers.email_test import router as email_router

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
app.include_router(property_image_router)
app.include_router(tenant_profile_router)
app.include_router(compatibility_router)
app.include_router(interest_router)
app.include_router(message_router)
app.include_router(chat_router)
app.include_router(email_router)




#uvicorn app.main:app --reload