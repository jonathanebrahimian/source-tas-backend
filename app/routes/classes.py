from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from logzero import logger

from app.database import (
    add_class,
    delete_class,
    retrieve_class,
    retrieve_classes,
    update_class,
)
from app.models.classes import (
    ErrorResponseModel,
    ResponseModel,
    ClassSchema,
    UpdateClassModel,
)

router = APIRouter()


@router.post("/", response_description="Class data added into the database")
async def add_class_data(class_data: ClassSchema = Body(...)):
    class_obj = jsonable_encoder(class_data)
    new_class = await add_class(class_obj)
    return ResponseModel(new_class, "Class added successfully.")


@router.get("/", response_description="Classes retrieved")
async def get_classs(active: bool=None):
    logger.debug(active)
    logger.warning(active)

    classes = await retrieve_classes(active=active)
    if classes:
        return ResponseModel(classes, "Classes data retrieved successfully")
    return ResponseModel(classes, "Empty list returned")


@router.get("/{id}", response_description="Class data retrieved")
async def get_class_data(id):
    class_obj = await retrieve_class(id)
    if class_obj:
        return ResponseModel(class_obj, "Class data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Class doesn't exist.")


@router.put("/{id}")
async def update_class_data(id: str, req: UpdateClassModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_class = await update_class(id, req)
    if updated_class:
        return ResponseModel(
            "Class with ID: {} name update is successful".format(id),
            "Class name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the class data.",
    )


@router.delete("/{id}", response_description="Class data deleted from the database")
async def delete_class_data(id: str):
    deleted_class = await delete_class(id)
    if deleted_class:
        return ResponseModel(
            "Class with ID: {} removed".format(id), "Class deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Class with id {0} doesn't exist".format(id)
    )

