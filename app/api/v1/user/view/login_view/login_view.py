from fastapi import Request
from app.api.v1.user.controller.login_user.login_user import LoginUser
from app.schemas.login_schema import LoginSchema
from app.utility.response import make_response

class LoginView:
    @staticmethod
    async def login(request: Request,login:LoginSchema):
        success,res,msg = await LoginUser.login_user(request,login)
        if not success:
            return  make_response(data={"success":"false","error":msg}, status=400)
        
        return  make_response(data={"success":"true","data":res,"message":msg}, status=200)
        