from pydantic import BaseModel,Field

class PortfolioSchema(BaseModel):
    scheme_name: str = Field(..., min_length=1, max_length=200)  
    scheme_code: str = Field(..., min_length=1, max_length=50)  
    scheme_category: str = Field(..., max_length=200) 
    mutual_fund_family: str = Field(..., max_length=200) 
    amount: float = Field(..., ge=0)  
    latest_net_asset_value: float = Field(..., ge=0) 
    purchased_unit: float = Field(..., ge=0)  
    current_value: float = Field(..., ge=0) 
    class Config:
        from_attributes = True