from fastapi import FastAPI, Request, HTTPException
from limiter import is_allowed

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Dhruv's Rate Limited API 🚀"}

@app.get("/data")
async def get_data(request: Request):
    user_ip = request.client.host  # Unique per user
    if not is_allowed(user_ip):
        raise HTTPException(status_code=429, detail="Too many requests! Try again later.")
    return {"message": "Here is your limited-access data! ✅"}
