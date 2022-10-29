import re
from pydantic import BaseModel, validator


class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class Support(BaseModel):
    url: str
    text: str

    @validator("url")
    def validate_url(cls, v):
        assert re.match(
            pattern=
            r"[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)",
            string=v)
        return v


class UserResponse(BaseModel):
    data: User
    support: Support


class UserListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[User]
    support: Support


class EmptyModel(BaseModel):
    extra = "forbid"