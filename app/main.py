from typing import Callable

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import uvicorn

from config.config import load_config

from models.models import FuncData

from views.table_data import get_table_data

from utils.functions import PermissionChecker, get_function


main_config = load_config()

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.post('/json')
async def main(data: FuncData, premissions: PermissionChecker = Depends()):

    # getting module and function names
    module_name = data.module
    function_name = data.function

    # checking permissions for dynamic use of modules and functions
    if not premissions.is_allowed_module(module_name=module_name):
        return HTTPException(status_code=500, detail="Unknown module NAME")

    if not premissions.is_allowed_function(func_name=function_name):
        return HTTPException(status_code=500, detail="Unknown function NAME")

    # dynamic function import
    function: Callable = get_function(
        module_name=module_name,
        function_name=function_name
    )
    return function(data=data)


@app.get('/html', response_class=HTMLResponse)
async def get_table(request: Request):
    table_data = get_table_data()
    return templates.TemplateResponse(
        "functions.html", {"request": request, "table_data": table_data})


if __name__ == "__main__":
    host = main_config.server.host
    port = main_config.server.port
    uvicorn.run("main:app", host=host, port=port, reload=True)
