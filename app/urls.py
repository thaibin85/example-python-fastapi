from typing import List, Tuple, Type
from fastapi import FastAPI
from app.controllers.base_controller import BaseController
from app.controllers.user_controller import UserController

class URLRegistry:
    def __init__(self):
        self._controllers: List[Tuple[Type[BaseController], str]] = []

    def register(self, controller_class: Type[BaseController], prefix: str):
        """
        Register a controller with a URL prefix
        Example: registry.register(UserController, '/users')
        """
        self._controllers.append((controller_class, prefix))
        return self

    def setup_routes(self, app: FastAPI):
        """
        Set up all registered routes in the FastAPI application
        """
        for controller_class, prefix in self._controllers:
            controller = controller_class()
            app.include_router(controller.router, prefix=prefix)


# Create the URL registry and register all controllers
url_registry = URLRegistry()

# Register all controllers with their URL prefixes
url_registry.register(UserController, "/api/users")
