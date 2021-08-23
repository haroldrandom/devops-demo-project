from enum import Enum

from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/models",
    tags=["models"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@router.get("/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
