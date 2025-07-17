from fastapi import APIRouter, Depends, HTTPException, status

from app.db.teams import db_actions
from app.routes.users import get_user_id


teams_router = APIRouter(prefix="/teams", tags=["Team"])