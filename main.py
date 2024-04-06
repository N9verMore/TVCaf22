import time

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/default", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("/data/def/television.html", {"request": request})

@app.get("/everyday1.mp4")
async def get_video():
    return FileResponse("templates/data/def/everyday1.mp4")

@app.get("/time")
async def get_video():
    return round(time.time() * 1000)