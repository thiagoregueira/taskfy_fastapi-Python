from pydantic import BaseModel, ConfigDict, EmailStr


# TokenData schema será utilizado para tipificar os dados extraídos do token JWT e garantir que temos um campo username que será usado para identificar o usuário.
class TokenData(BaseModel):
    username: str | None = None


# Schema para nosso token
class Token(BaseModel):
    access_token: str
    token_type: str


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
