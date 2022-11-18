from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from logzero import logger

from app.database import (
    add_application,
    delete_application,
    retrieve_application,
    retrieve_applications,
    update_application,
)
from app.models.applications import (
    ApplicationSchema,
    UpdateApplicationModel,
    ErrorResponseModel,
    ResponseModel
)

router = APIRouter()

@router.post("/", response_description="Application data added into the database")
async def add_application_data(application_data: ApplicationSchema = Body(...)):
    application_obj = jsonable_encoder(application_data)
    new_application = await add_application(application_obj)
    return ResponseModel(new_application, "Application added successfully.")

@router.get("/", response_description="Applications retrieved")
async def get_applications(active: bool=None):
    applications = await retrieve_applications(active=active)
    if applications:
        return ResponseModel(applications, "Applications data retrieved successfully")
    return ResponseModel(applications, "Empty list returned")

@router.get("/{id}", response_description="Application data retrieved")
async def get_application_data(id):
    application_obj = await retrieve_application(id)
    if application_obj:
        return ResponseModel(application_obj, "Application data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Application doesn't exist.")

@router.put("/{id}")
async def update_application_data(id: str, req: UpdateApplicationModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_application = await update_application(id, req)
    if updated_application:
        return ResponseModel(
            "Application with ID: {} name update is successful".format(id),
            "Application name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the application data.",
    )

@router.delete("/{id}", response_description="Application data deleted from the database")
async def delete_application_data(id: str):
    deleted_application = await delete_application(id)
    if deleted_application:
        return ResponseModel(
            "Application with ID: {} removed".format(id), "Application deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Application with id {0} doesn't exist".format(id)
    )
