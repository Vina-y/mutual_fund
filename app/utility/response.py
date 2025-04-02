from asyncio import iscoroutinefunction
import json
from types import coroutine
from fastapi.responses import JSONResponse
from app.utility.json_formatter import defaultFormatter


def make_response(data=None, status=200):
    if data is None:
        data = {}

    responseData = json.dumps(data, default=defaultFormatter)
    return   JSONResponse(content=json.loads(responseData), status_code=status, headers=None)