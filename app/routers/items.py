from fastapi import APIRouter, Depends, HTTPException
from loguru import logger

# from ..dependencies import get_token_header

router = APIRouter(
    prefix="/items",
    tags=["items"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_items():

    logger.info(f"List All items: [{fake_items_db}]")

    return fake_items_db


@router.get("/{item_id}")
async def read_item(item_id: str):

    logger.info(f"Querying Item By ID: [{item_id}]")

    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}


@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):

    logger.info(f"Updating Item By ID: [{item_id}]")

    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}
