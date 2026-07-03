from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.message import Message
from app.database import SessionLocal
from app.models.message import Message

router = APIRouter(tags=["Chat"])

connections = {}


@router.websocket("/ws/chat/{interest_id}")
async def websocket_chat(
    websocket: WebSocket,
    interest_id: int
):

    try:
        while True:
            data = await websocket.receive_text()
            db = SessionLocal()

            db_message = Message(
            interest_id=interest_id,
            sender="tenant",
            message=data
      )

            db.add(db_message)
            db.commit()
            db.close()


            print(f"Received: {data}")

            for connection in connections[interest_id]:
              await connection.send_text(data)

              
    except WebSocketDisconnect:
        connections[interest_id].remove(websocket)

    await websocket.accept()

    if interest_id not in connections:
      connections[interest_id] = []

    connections[interest_id].append(websocket)