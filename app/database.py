import motor.motor_asyncio
from bson.objectid import ObjectId
import json
from bson import json_util

MONGO_DETAILS = "mongodb://root:rootpassword@mongodb_container:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.classes

class_collection = database.get_collection("class_collection")


# helpers


def class_helper(class_obj) -> dict:
    return {
        "id": str(class_obj["_id"]),
        "name": class_obj["name"],
        "active":class_obj["active"],
        "labs": class_obj["labs"],
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