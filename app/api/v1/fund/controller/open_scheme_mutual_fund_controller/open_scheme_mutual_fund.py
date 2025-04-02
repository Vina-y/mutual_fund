import httpx
from app.api.v1.fund.controller.fund_name_controller.funds_details import funds_details



class OpenSchemeMutualFundController:
    async def open_mutual_fund(request,mutual_fund_family) -> dict:
        try:
            # configuration for mutual fund api
            url = "https://latest-mutual-fund-nav.p.rapidapi.com/latest"
            rapid_api_key = "1535522dd1msh402fcee9a3cf2bep14e1b4jsn1e427cda11e9"
            host = "latest-mutual-fund-nav.p.rapidapi.com"
            
            headers = {
                "X-RapidAPI-Key": rapid_api_key,
                "X-RapidAPI-Host": host,
            }
            params = {"Scheme_Type":"Open","Mutual_Fund_Family":mutual_fund_family}
            # calling api with async httpx client
            response = None
            async with httpx.AsyncClient() as client:
                response = await client.get(url, headers=headers, params=params)
                if response.status_code == 200:
                    mutual_fund_families = [{"scheme_code":entry["Scheme_Code"],"scheme_name":entry["Scheme_Name"],"net_asset_value":entry["Net_Asset_Value"],"scheme_category":entry["Scheme_Category"],"mutual_fund_family":entry["Mutual_Fund_Family"]} for entry in response.json()]
                else:
                    # unique_mutual_fund_families = sorted(set(entry['Mutual_Fund_Family'] for entry in funds_details ))
                    mutual_fund_families = [{"scheme_code":entry["Scheme_Code"],"scheme_name":entry["Scheme_Name"],"net_asset_value":entry["Net_Asset_Value"],"scheme_category":entry["Scheme_Category"],"mutual_fund_family":entry["Mutual_Fund_Family"]} for entry in funds_details if entry['Mutual_Fund_Family'] == mutual_fund_family]

            return True, mutual_fund_families, "open scheme mutual fund retrived successfully"
        except Exception as e:
            return False, None, {"error": str(e)}