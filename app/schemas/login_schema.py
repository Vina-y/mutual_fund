from pydantic import BaseModel, Field

class LoginSchema(BaseModel):
    email: str = Field(..., min_length=1, max_length=50)
    password: str = Field(..., min_length=1)
    class Config:
        from_attributes = True