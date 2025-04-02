from pydantic import BaseModel, ConfigDict, EmailStr, Field,model_validator, field_validator
from pydantic import ValidationError

class RegisterUserSchema(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    email: str = Field(..., min_length=1, max_length=50)
    password: str = Field(..., min_length=8, max_length=15)
    confirm_password: str = Field(..., min_length=8, max_length=15)
    
    @field_validator("email")
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError({
                    "loc": ("email",),
                    "msg": "Invalid email",
                    "type": "value_error"
                })
        return value
    
    @model_validator(mode="before")
    def check_passwords_match(cls, values):
        # print("hghghghg",values)
        password =  values["password"]
        confirm_password =  values["confirm_password"]
        if password != confirm_password:
            raise ValueError("Passwords do not match")
        return values
    
    @model_validator(mode="before")
    def validate_password_strength(cls, values):
        password = values["password"]
        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one number")
        if not any(char.isupper() for char in password):
            raise ValueError("Password must contain at least one uppercase letter")
        return values
    class Config:
        from_attributes = True