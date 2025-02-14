from app.core.config import settings
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm
from supabase import AuthApiError, ClientOptions, create_client
from app.api.dependencies import SupabaseClient, CurrentUser, DBClient, get_auth_service
from app.schemas.auth import UserCreate
from app.services.auth_service import AuthService
from app.crud import restaurant

router = APIRouter()


@router.get("/all")
async def get_restaurants():
    return await restaurant.get_all(DBClient)

async def get_restaurant_by_cuisine(cuisine: str):
    return await restaurant.get_by_cuisine(DBClient, cuisine)

async def get_restaurant_by_location(location: tuple[float, float]):
    return await restaurant.get_by_location(DBClient, location)