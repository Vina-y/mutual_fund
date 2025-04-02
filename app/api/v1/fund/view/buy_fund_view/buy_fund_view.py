from fastapi import Request
from app.api.v1.fund.controller.buy_fund_controller.buy_fund_controller import BuyFundController
from app.schemas.user_purchase_stock_schema import UserPurchaseFundSchema
from app.utility.response import make_response

class BuyFundView:
    @staticmethod
    async def buy_fund_view(request: Request,purchase_fund:UserPurchaseFundSchema):
        success,res,msg = await BuyFundController.buy_fund(request,purchase_fund)
        if not success:
            return  make_response(data={"success":"false","error":msg}, status=400)
        
        return  make_response(data={"success":"true","data":res,"message":msg}, status=200)
        