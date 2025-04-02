import asyncio
from app.api.v1.fund.controller.fund_name_controller.funds_details import funds_details
from app.models.user_purchase_funds import UsersPurchaseFunds
import requests
import os
from dotenv import load_dotenv
load_dotenv()

async def update_nav_hourly():
    try:
        url = "https://latest-mutual-fund-nav.p.rapidapi.com/latest"
        rapid_api_key = os.getenv("RAPID_API_KEY")
        host = os.getenv("HOST")
        
        headers = {
            "X-RapidAPI-Key": rapid_api_key,
            "X-RapidAPI-Host": host,
        }
        purchased_fund =  await UsersPurchaseFunds.all()
        
        for scheme in purchased_fund:
            # configuration for mutual fund api
            params = {"Scheme_Type":"Open Ended Schemes","Scheme_Code":scheme.scheme_code}
            
            response =  requests.get(url, headers=headers, params=params) 

            if response.status_code == 200:
                for entry in response.json():
                    new_nav = entry["Net_Asset_Value"]
                    scheme.latest_net_asset_value = new_nav
                    await scheme.save()  
            else:
                for entry in funds_details:
                    if str(entry['Scheme_Code']) == scheme.scheme_code:
                        new_nav = entry["Net_Asset_Value"]
                        scheme.latest_net_asset_value = new_nav
                        await scheme.save()  
        await asyncio.sleep(1)             
    except Exception as e :
        print(e)