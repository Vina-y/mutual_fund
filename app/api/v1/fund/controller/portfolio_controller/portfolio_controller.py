from app.models.user_purchase_funds import UsersPurchaseFunds
from app.utility.get_current_user import get_current_user


class PortfolioController:
    async def portfolio(request) -> dict:
        try:
            id =  get_current_user(request)
            purchased_funds  = await UsersPurchaseFunds.filter(user =id)
            portpolio = []
            for purchased_funds_details in purchased_funds:
                if purchased_funds_details:
                    purchased_funds_details = dict(purchased_funds_details)
                    purchased_funds_details["current_value"] = purchased_funds_details["latest_net_asset_value"] * purchased_funds_details["purchased_unit"]
                    portpolio.append(purchased_funds_details)
                else:
                    return False, None, "Portfolio retrival failed"
            
            if len(portpolio)>0:
                return True, portpolio, "Portfolio retrived successfully"
            
        except Exception as e:
            return False, None, {"error": str(e)}