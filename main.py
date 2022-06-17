from fastapi import FastAPI
from starlette.responses import FileResponse

from internals import generate_image

app = FastAPI()


@app.get("/")
async def hello():
    return 200


@app.get("/image")
async def image_endpoint():
    generate_image(
        size=(3500, 2500),
        background_rgb=(227, 227, 227)
    )
    return FileResponse('output.png')

