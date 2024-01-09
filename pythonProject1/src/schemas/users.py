from pydantic import BaseModel
from src.schemas.meta import Meta


class User(BaseModel):
    first_name: str
    last_name: str
    company_id: int
    user_id: int


class UserList(BaseModel):
    data: list[User]
    meta: Meta
