from fastapi import Request
from fastapi.responses import JSONResponse
from app.api.v1.user.controller.register_user.register_user import RegisterUser
from app.schemas.register_user_schema import RegisterUserSchema
from app.utility.response import make_response

class UserRegisterView:
    @staticmethod
    async def register(request: Request,user:RegisterUserSchema):
        success,res,msg = await RegisterUser.register_user(request,user)
        if not success:
            return  make_response(data={"success":"false","error":msg}, status=400)
        
        return  make_response(data={"success":"true","data":res,"message":msg}, status=201)
        