from fastapi import APIRouter
from loguru import logger

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():

    logger.info("Listing All Users")

    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():

    logger.info("Reading Faking User")

    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):

    logger.info(f"Reading User By Name: [{username}]")

    return {"username": username}
