from typing import Dict

from pydantic import BaseModel


class ErrorData(BaseModel):
    ident: str
    value: str


class FuncData(BaseModel):
    module: str
    function: str
    data: Dict[str, ErrorData]
