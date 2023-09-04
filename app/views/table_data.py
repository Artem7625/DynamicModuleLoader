import inspect
from typing import Callable, List

from config.config import main_config

from utils.functions import get_function


def get_table_data():
    """Gets a data to HTML table generation."""

    # set table headers
    table_data: List[List[str | None]] = [
        ['Module', 'Functon', 'Docstring', 'Code'],
    ]

    # getting resolved objects to dynamically create a table.
    allowed_objects = main_config.allowed_objects

    # filling the table with functions data.
    for module in allowed_objects:
        module_name = module.get('module')

        for func in module.get('functions'):
            func_obj: Callable = get_function(module_name=module_name, function_name=func)
            docstring: str | None = inspect.getdoc(object=func_obj)
            source_code: str = inspect.getsource(object=func_obj)

            fucn_data: List[str | None] = [
                module_name, func, docstring, source_code,
            ]

            table_data.append(fucn_data)

    return table_data
