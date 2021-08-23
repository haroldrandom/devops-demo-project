from fastapi import Depends, FastAPI

# from .dependencies import get_query_token, get_token_header
from .internal import models
from .routers import items, users

# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()


app.include_router(users.router)
app.include_router(items.router)

app.include_router(models.router)
# app.include_router(
#     models.router,
#     prefix="/admin",
#     tags=["admin"],
#     # dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
