import pathlib
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI , Request
from fastapi.responses import HTMLResponse

BASE_DIR = pathlib.Path(__file__).parent
app = FastAPI()

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))#app/templates

@app.get("/", response_class=HTMLResponse)
def home_view(request: Request):
    print(request)
    #return "<h1>HELLO WORLS<h1>"
    return templates.TemplateResponse(request=request, name="home.html", context= {"request": request, "abc": 123})

@app.post("/")
def home_detail_view():
    return {"Hello": "World"}