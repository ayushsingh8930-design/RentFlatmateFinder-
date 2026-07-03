from fastapi import APIRouter

from app.services.email_service import send_email

router = APIRouter(
    prefix="/email",
    tags=["Email"]
)


@router.get("/test")
def test_email():

    send_email(
        "2k23.csdatascience2313889@gmail.com",
        "Rent & Flatmate Finder",
        "Congratulations! Email service is working."
    )

    return {"message": "Email sent successfully"}