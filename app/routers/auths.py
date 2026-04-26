from fastapi import APIRouter, status
from app.schemas.user import UserRegister

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/registro", status_code=status.HTTP_202_ACCEPTED)
def register_user(user_data: UserRegister):
    # Endpoint temporal hasta terminar el flujo de autenticacion.
    return {
        "status": "pending",
        "message": "Tu registro esta en camino. Gracias por tu paciencia.",
    }
