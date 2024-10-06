from app.core.config import settings
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm
from supabase import AuthApiError, ClientOptions, create_client
from app.api.dependencies import SupabaseClient, CurrentUser, DBClient, get_auth_service
from app.schemas.auth import UserCreate
from app.services.auth_service import AuthService

router = APIRouter()


@router.post("/signup")
async def signup(user: UserCreate, client: SupabaseClient):
    try:
        response = client.auth.sign_up({
            "email": user.email,
            "password": user.password
        })
        return {"message": "Signup successful", "user": response.user}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(get_auth_service)
):
    return auth_service.login(form_data.username, form_data.password)

@router.post("/logout")
def logout(current_user: CurrentUser, auth_service: AuthService = Depends(get_auth_service)):
    return auth_service.logout(current_user.access_token)

@router.get("/protected")
def protected_route(current_user: CurrentUser, db_client: DBClient):
    # Use db_client to fetch data
    data = db_client.from_("some_table").select("*").execute()
    return {"message": f"Hello, {current_user.email}!", "data": data.data}

# @router.post("/login")
# async def login(supabase: SupabaseClient, form_data: OAuth2PasswordRequestForm = Depends()):
#     try:
#         response = supabase.auth.sign_in_with_password({
#             "email": form_data.username,
#             "password": form_data.password
#         })
#         if response.session:
#             return {"access_token": response.session.access_token, "token_type": "bearer"}
#         else:
#             raise HTTPException(status_code=401, detail="Invalid credentials")
#     except AuthApiError as e:
#         logging.error(f"Login error: {str(e)}")
#         raise HTTPException(status_code=401, detail="Invalid credentials")

# @router.post("/logout")
# async def logout(session: SessionDep, user: CurrentUser):
#     return await session.auth.sign_out(user.access_token)

# @router.get("/protected")
# async def protected_route(session: SessionDep, user: CurrentUser):
#     return {"message": f"Hello, {user.email}!"}