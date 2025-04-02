import httpx
from app.api.v1.fund.controller.fund_name_controller.funds_details import funds_details
from app.models.users import Users
from app.utility.access_token import create_access_token
from app.utility.hash_password import verify_password
import os
from dotenv import load_dotenv
load_dotenv()

class FundName:
    async def fund_names(request) -> dict:
        try:
            # configuration for mutual fund api
            url = "https://latest-mutual-fund-nav.p.rapidapi.com/latest"
            rapid_api_key = os.getenv("RAPID_API_KEY")
            host = os.getenv("HOST")
            headers = {
                "X-RapidAPI-Key": rapid_api_key,
                "X-RapidAPI-Host": host,
            }
            params = {"Scheme_Type":"Open"}
            # calling api with async httpx client
            response = None
            async with httpx.AsyncClient() as client:
                response = await client.get(url, headers=headers, params=params)
                if response.status_code == 200:
                    mutual_fund_families = [{"fund_family":entry['Mutual_Fund_Family']} for entry in response.json()]
                else:
                    unique_mutual_fund_families = sorted(set(entry['Mutual_Fund_Family'] for entry in funds_details ))
                    mutual_fund_families = [{"fund_family":entry} for entry in unique_mutual_fund_families]

            return True, mutual_fund_families, "retrived successfully"
        except Exception as e:
            return False, None, {"error": str(e)}