import motor.motor_asyncio
from bson.objectid import ObjectId
import json
from bson import json_util

MONGO_DETAILS = "mongodb://root:rootpassword@mongodb_container:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.classes

class_collection = database.get_collection("class_collection")
applications_collection = database.get_collection("applications_collection")


# helpers


def class_helper(class_obj) -> dict:
    return {
        "id": str(class_obj["_id"]),
        "name": class_obj["name"],
        "active":class_obj["active"],
        "labs": class_obj["labs"],
    }

def application_helper(class_obj) -> dict:
    return {
        "email": class_obj["email"],
        "name": class_obj["name"],
        "time": class_obj["time"],
        "resume": class_obj["resume"],
        "classes": class_obj["classes"],
    }


# Retrieve all classes present in the database
async def retrieve_classes(active: bool):
    classes = []
    if active is None:
        search_params = {}
    else:
        search_params = {
            'active':active
        }
    async for class_obj in class_collection.find(search_params):
        classes.append(class_helper(class_obj))
    return json.loads(json_util.dumps(classes))


# Add a new class into to the database
async def add_class(class_data: dict) -> dict:
    class_obj = await class_collection.insert_one(class_data)
    new_class = await class_collection.find_one({"_id": class_obj.inserted_id})
    return class_helper(new_class)


# Retrieve a class with a matching ID
async def retrieve_class(id: str) -> dict:
    class_obj = await class_collection.find_one({"_id": ObjectId(id)})
    if class_obj:
        return class_helper(class_obj)


# Update a classs with a matching ID
async def update_class(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    class_obj = await class_collection.find_one({"_id": ObjectId(id)})
    if class_obj:
        updated_class = await class_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_class:
            return True
        return False


# Delete a class from the database
async def delete_class(id: str):
    class_obj = await class_collection.find_one({"_id": ObjectId(id)})
    if class_obj:
        await class_collection.delete_one({"_id": ObjectId(id)})
        return True


# Retrieve all applications present in the database
async def retrieve_applications():
    applications = []
    async for application_obj in applications_collection.find():
        applications.append(application_helper(application_obj))
    return json.loads(json_util.dumps(applications))

# Add a new application into to the database
async def add_application(application_data: dict) -> dict:
    application_obj = await applications_collection.insert_one(application_data)
    new_application = await applications_collection.find_one({"_id": application_obj.inserted_id})
    return application_helper(new_application)

# Retrieve a application with a matching ID
async def retrieve_application(id: str) -> dict:
    application_obj = await applications_collection.find_one({"_id": ObjectId(id)})
    if application_obj:
        return application_helper(application_obj)

# Update a application with a matching ID
async def update_application(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    application_obj = await applications_collection.find_one({"_id": ObjectId(id)})
    if application_obj:
        updated_application = await applications_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_application:
            return True
        return False

# Delete a application from the database
async def delete_application(id: str):
    application_obj = await applications_collection.find_one({"_id": ObjectId(id)})
    if application_obj:
        await applications_collection.delete_one({"_id": ObjectId(id)})
        return True
