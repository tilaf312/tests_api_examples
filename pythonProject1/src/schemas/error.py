from pydantic  import BaseModel
from typing import Union


class Reason(BaseModel):
    reason: str


class ValidationError(BaseModel):
    loc: list[Union[int, str]]
    msg: str
    type: str


class HTTPValidationError(BaseModel):
    detail: Union[Reason, list[ValidationError]]

# {
#   "detail": [
#     {
#       "loc": [
#         "string",
#         0
#       ],
#       "msg": "string",
#       "type": "string"
#     }
#   ]
# }