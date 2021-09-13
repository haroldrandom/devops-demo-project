from enum import Enum

from fastapi import APIRouter, Depends, HTTPException
from loguru import logger

router = APIRouter(
    prefix="/models",
    tags=["models"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


class Money:
    def __init__(self) -> None:
        self.names = []


MONEY_HANDLER = Money()


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@router.get("/{model_name}")
async def get_model(model_name: ModelName):

    logger.info(f"get_model from: {model_name}")

    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@router.get("/memory_blow/{model_name}")
async def memory_blow_model(model_name: str):
    MONEY_HANDLER.names.append(model_name)

    logger.info(f"Current model names count {len(MONEY_HANDLER.names)}")

    return {"count": len(MONEY_HANDLER.names)}
