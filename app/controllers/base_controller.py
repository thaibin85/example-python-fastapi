from fastapi import APIRouter

class BaseController:
    def __init__(self):
        self.router = APIRouter()
        self._register_routes()

    def _register_routes(self):
        """
        Override this method to register routes using self.router
        Example:
        self.router.get("/")(self.get_all)
        self.router.post("/create")(self.create)
        """
        pass
