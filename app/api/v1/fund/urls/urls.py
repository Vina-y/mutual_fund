from fastapi import APIRouter
from app.api.v1.fund.view.buy_fund_view.buy_fund_view import BuyFundView
from app.api.v1.fund.view.fund_dropdown_view.fund_dropdown_view import FundDropDownView
from app.api.v1.fund.view.open_scheme_mutual_fund_view.open_scheme_mutual_fund_view import OpenSchemeMutualFundView
from app.api.v1.fund.view.portfolio_view.portfoli_view import PortfolioView
# user router 
fund_router = APIRouter()

# urls 
fund_router.add_api_route("/fund-name", FundDropDownView.funds_name, methods=["GET"])
fund_router.add_api_route("/open-scheme/mutual-fund", OpenSchemeMutualFundView.get_open_scheme_mutual_fund, methods=["GET"])
fund_router.add_api_route("/buy-fund", BuyFundView.buy_fund_view, methods=["POST"])
fund_router.add_api_route("/portfolio/{porfolio_id}", PortfolioView.user_portfolio, methods=["GET"])