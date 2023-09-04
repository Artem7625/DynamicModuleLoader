import importlib
from types import FunctionType
from typing import Callable, List, Optional

from fastapi import HTTPException

from config.config import main_config


class PermissionChecker:
    """Class for checking permissions associated with modules and functions."""

    def __init__(self):
        self.allowed_objects = main_config.allowed_objects

    def is_allowed_module(self, module_name: str) -> bool:
        return any(
            module_data["module"] == module_name
            for module_data in self.allowed_objects
        )

    def is_allowed_function(self, func_name: str) -> bool:
        return any(
            func_name in module_data.get("functions", [])
            for module_data in self.allowed_objects
        )


def module_name_exists(module_name: str) -> bool:
    """Checks if a module with the given name exists."""

    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False


def function_exists(module_name: str, function_name: str) -> bool:
    """Checks if a function with the given name exists in the module."""

    if not module_name_exists(module_name):
        return False

    module = importlib.import_module(module_name)
    return hasattr(module, function_name)


def get_function(module_name: str, function_name: str) -> Optional[Callable]:
    """Imports a function based on the module name and function name."""

    if not module_name_exists(module_name):
        raise HTTPException(status_code=500, detail="Unknown module NAME")

    if not function_exists(module_name, function_name):
        raise HTTPException(status_code=500, detail="Unknown function NAME")

    module = importlib.import_module(module_name)
    function: Callable = getattr(module, function_name)

    if isinstance(function, FunctionType):
        return function

    return None
