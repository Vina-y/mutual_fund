from pydantic import BaseModel,Field

class UserPurchaseFundSchema(BaseModel):
    scheme_name: str = Field(..., min_length=1, max_length=150)
    scheme_code: str = Field(..., min_length=1, max_length=50)
    net_asset_value: float = Field(..., ge=0) 
    scheme_category: str = Field(..., max_length=200)
    mutual_fund_family: str = Field(..., max_length=200)
    amount: float = Field(..., ge=0) 
    class Config:
        from_attributes = True