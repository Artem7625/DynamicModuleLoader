import json

from environs import Env

from config.model import Config, main_config


def load_config(path: str | None = None) -> Config:
    """Loads application configuration data."""

    env: Env = Env()
    env.read_env(path)

    global main_config

    # getting objects available for dynamic import
    allowed_modules_json = env('ALLOWED_OBJECTS')
    allowed_objects = json.loads(allowed_modules_json)

    modules_list = []
    functions_list = []

    for module_data in allowed_objects:
        module_name = module_data.get("module")
        function_names = module_data.get("functions", [])

        modules_list.append(module_name)
        functions_list.extend(function_names)

    main_config.allowed_objects = allowed_objects

    # geting host configuration
    main_config.server.host = env('HOST')
    main_config.server.port = int(env('PORT'))

    return main_config
