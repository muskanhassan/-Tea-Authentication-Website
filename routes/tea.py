from fastapi import APIRouter
from configuration import teas_collection
from database.model import Tea

router = APIRouter()


@router.post("/add-tea")
async def add_tea(tea: Tea):

    tea_dict = dict(tea)

    teas_collection.insert_one(
        tea_dict
    )

    return {
        "message":
        "Tea added successfully"
    }