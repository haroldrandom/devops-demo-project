import logging
import os
import sys

from fastapi import Depends, FastAPI
from loguru import logger

# from .dependencies import get_query_token, get_token_header
from .internal import models
from .routers import items, users

LOG_LEVEL = logging.getLevelName(os.environ.get("LOG_LEVEL", "DEBUG"))
JSON_LOGS = True if os.environ.get("JSON_LOGS", "0") == "1" else False

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


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


@app.on_event("startup")
def setup_logging():
    # intercept everything at the root logger
    logging.root.handlers = [InterceptHandler()]
    logging.root.setLevel(LOG_LEVEL)

    # remove every other logger's handlers
    # and propagate to root logger
    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True

    # configure loguru
    logger.configure(handlers=[{"sink": sys.stdout, "serialize": JSON_LOGS}])


@app.get("/")
async def root():

    logger.info("Vising Root......")

    return {"message": "Hello Bigger Applications!"}
