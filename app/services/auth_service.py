from fastapi import HTTPException
from supabase import Client
from app.schemas.auth import UserIn, UserCreate
import logging

class AuthService:
    def __init__(self, supabase_client: Client):
        self.client = supabase_client

    def get_user_by_token(self, token: str) -> UserIn:
        try:
            user_rsp = self.client.auth.get_user(token)
            if not user_rsp or not user_rsp.user:
                raise HTTPException(status_code=404, detail="User not found")
            return UserIn(**user_rsp.user.model_dump(), access_token=token)
        except Exception as e:
            logging.error(f"Error getting user: {str(e)}")
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    def signup(self, user: UserCreate):
        try:
            response = self.client.auth.sign_up({
                "email": user.email,
                "password": user.password
            })
            if response.user:
                return {"message": "Signup successful", "user": response.user}
            else:
                raise HTTPException(status_code=400, detail="Signup failed")
        except Exception as e:
            logging.error(f"Signup error: {str(e)}")
            raise HTTPException(status_code=400, detail=str(e))

    def login(self, email: str, password: str):
        try:
            response = self.client.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            if response.session:
                return {"access_token": response.session.access_token, "token_type": "bearer"}
            else:
                raise HTTPException(status_code=401, detail="Invalid credentials")
        except Exception as e:
            logging.error(f"Login error: {str(e)}")
            raise HTTPException(status_code=401, detail="Invalid credentials")

    def logout(self, token: str):
        try:
            self.client.auth.sign_out(token)
            return {"message": "Logout successful"}
        except Exception as e:
            logging.error(f"Logout error: {str(e)}")
            raise HTTPException(status_code=400, detail="Logout failed")