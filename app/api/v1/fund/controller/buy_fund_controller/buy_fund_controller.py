from app.models.user_purchase_funds import UsersPurchaseFunds


class BuyFundController:
    async def buy_fund(request,purchase_fund) -> dict:
        try:
            user = request.state.user
            id  = user["id"]
            dict_purchased_fund = dict(purchase_fund)
            dict_purchased_fund["latest_net_asset_value"] = dict_purchased_fund.get("net_asset_value")
            # calculating the purched unit
            purchased_unit = dict_purchased_fund.get("amount") / dict_purchased_fund.get("net_asset_value")
            # making round upto 3
            dict_purchased_fund["purchased_unit"] = purchased_unit
            
            dict_purchased_fund["current_value"] = dict_purchased_fund.get("amount")
            
            dict_purchased_fund["user_id"] = id

            await UsersPurchaseFunds.create(**dict_purchased_fund)
            return True, dict_purchased_fund, "Fund purchased successfully"
        except Exception as e:
            return False, None, {"error": str(e)}