from sqlalchemy.orm import Session

from app.models.message import Message
from app.schemas.message import MessageCreate


def save_message(db: Session, message: MessageCreate):

    db_message = Message(
        interest_id=message.interest_id,
        sender=message.sender,
        message=message.message
    )

    db.add(db_message)
    db.commit()
    db.refresh(db_message)

    return db_message