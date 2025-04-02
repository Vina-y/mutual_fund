from app.cron_job.task.nav_update_task import update_nav_hourly
from app.models.user_purchase_funds import UsersPurchaseFunds
from app.utility.get_current_user import get_current_user


class PortfolioController:
    async def portfolio(request,porfolio_id) -> dict:
        try:
            id =  get_current_user(request)
            await update_nav_hourly()
            purchased_funds_details  = await UsersPurchaseFunds.get_or_none(id = porfolio_id,user =id)
            if purchased_funds_details:
                purchased_funds_details = dict(purchased_funds_details)
                purchased_funds_details["current_value"] = purchased_funds_details["latest_net_asset_value"] * purchased_funds_details["purchased_unit"]
                return True, purchased_funds_details, "Portfolio retrived successfully"
            else:
                return False, None, "Portfolio retrival failed"

        except Exception as e:
            return False, None, {"error": str(e)}