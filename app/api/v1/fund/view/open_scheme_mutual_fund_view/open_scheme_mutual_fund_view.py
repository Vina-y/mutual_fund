from fastapi import Request
from app.api.v1.fund.controller.fund_name_controller.fund_name import FundName
from app.api.v1.fund.controller.open_scheme_mutual_fund_controller.open_scheme_mutual_fund import OpenSchemeMutualFundController
from app.utility.response import make_response

class OpenSchemeMutualFundView: 
    @staticmethod
    async def get_open_scheme_mutual_fund(request: Request,mutual_fund_family:str):
        success,res,msg = await OpenSchemeMutualFundController.open_mutual_fund(request,mutual_fund_family)
        if not success:
            return  make_response(data={"success":"false","error":msg}, status=400)
        
        return  make_response(data={"success":"true","data":res,"message":msg}, status=200)
        