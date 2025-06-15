from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.controllers.base_controller import BaseController
from app.database import get_db
from app.services.user_service import UserService
from typing import Dict, Any

from app.utils.exception import NotFoundException

class UserController(BaseController):
    def __init__(self):
        super().__init__()
        
    def _register_routes(self):
        self.router.get("/")(self.get_all_users)
        self.router.get("/me")(self.get_current_user)
        self.router.post("/register")(self.register)
        self.router.post("/login")(self.login)
        self.router.get("/cookies")(self.get_cookies)
        self.router.get("/not-found")(self.test_not_found)
        
    async def get_all_users(self, db: Session = Depends(get_db)):
        user_service = UserService(db)
        return user_service.get_all_users()
        
    async def get_current_user(self, db: Session = Depends(get_db)):
        # Implementation for getting current user
        pass
        
    async def register(self, 
                      username: str, 
                      email: str, 
                      password: str, 
                      db: Session = Depends(get_db)):
        # Add a breakpoint here by clicking on the left margin
        user_service = UserService(db)
        try:
            # You can inspect these variables during debugging
            debug_info = {
                "username": username,
                "email": email,
                "password_length": len(password)
            }
            user = user_service.create_user(
                username=username,
                email=email,
                password=password
            )
            return user
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
            
    async def login(self, 
                   username: str, 
                   password: str, 
                   db: Session = Depends(get_db)) -> Dict[str, Any]:
        # Add a breakpoint on this line by clicking in the left margin
        print(f"Login attempt for user: {username}")  # Debug line
        
        user_service = UserService(db)
        try:
            return user_service.authenticate_user(username, password)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password"
            )
            
    async def get_cookies(self):
        return {"message": "Here are your cookies 🍪"}
    
    async def test_not_found(self):
        raise NotFoundException("Resource not found")