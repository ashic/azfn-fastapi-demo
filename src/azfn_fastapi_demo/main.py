from fastapi import FastAPI, Body, Response
from fastapi.responses import JSONResponse
import azure.functions as func

app = FastAPI()

@app.exception_handler(Exception)
async def catch_all(req, e:Exception):
    return JSONResponse("Catch all handler")

# @app.exception_handler(ZeroDivisionError)
# async def zero_handler(req, e:ZeroDivisionError):
#     return JSONResponse("Zero handler")

@app.post("/test")
async def test():

    a = 20 / 0

    return {
        'content': "Hello"
    }



main = func.AsgiMiddleware(app).main