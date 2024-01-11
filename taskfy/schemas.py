from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str


# DTO
class UserPublic(BaseModel):
    id: int
    name: str
    email: EmailStr


class UserDB(UserSchema):
    id: int


# Mostrar lista de usuários
class UserList(BaseModel):
    users: list[UserPublic]


# Delete
class Message(BaseModel):
    detail: str
