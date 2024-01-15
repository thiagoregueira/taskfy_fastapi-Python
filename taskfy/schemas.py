from pydantic import BaseModel, ConfigDict, EmailStr


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


# DTO
class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


# Mostrar lista de usuários
class UserList(BaseModel):
    users: list[UserPublic]


# Delete
class Message(BaseModel):
    detail: str
