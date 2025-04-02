from fastapi import Request
from app.api.v1.fund.controller.fund_name_controller.fund_name import FundName
from app.api.v1.fund.controller.portfolio_controller.portfolio_controller import PortfolioController
from app.api.v1.user.controller.login_user.login_user import LoginUser
from app.schemas.login_schema import LoginSchema
from app.schemas.portfolio_schema import PortfolioSchema
from app.utility.response import make_response

class PortfolioView:
    @staticmethod
    async def user_portfolio(request: Request,porfolio_id:int):
        success,res,msg = await PortfolioController.portfolio(request,porfolio_id)
        if not success:
            return  make_response(data={"success":"false","error":msg}, status=400)
        
        return  make_response(data={"success":"true","data":res,"message":msg}, status=200)
        