from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.database import get_db
from app.schemas.message import (
    MessageCreate,
    MessageResponse
)
from app.services.message_service import save_message

router = APIRouter(
    prefix="/messages",
    tags=["Messages"]
)


@router.post("/", response_model=MessageResponse)
def create_message(
    message: MessageCreate,
    db: Session = Depends(get_db)
):
    return save_message(db, message)


active_connections = []

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)

    try:
        while True:
            data = await websocket.receive_text()

            for connection in active_connections:
                await connection.send_text(data)

    except WebSocketDisconnect:
        active_connections.remove(websocket)