from fastapi import Request
from app.api.v1.fund.controller.fund_name_controller.fund_name import FundName
from app.api.v1.user.controller.login_user.login_user import LoginUser
from app.schemas.login_schema import LoginSchema
from app.utility.response import make_response

class FundDropDownView:
    @staticmethod
    async def funds_name(request: Request):
        success,res,msg = await FundName.fund_names(request)
        if not success:
            return  make_response(data={"success":"false","error":msg}, status=400)
        
        return  make_response(data={"success":"true","data":res,"message":msg}, status=200)
        