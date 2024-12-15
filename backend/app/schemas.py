from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True  # Isso permite que o Pydantic converta modelos SQLAlchemy para dicionários
