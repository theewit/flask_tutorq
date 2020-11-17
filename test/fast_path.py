from fastapi import FastAPI

from enum import Enum
from typing import Optional

class ModelName(str, Enum):
	alexnet = "alexnet"
	resnet = "resnet"
	lenet = "lenet"

app = FastAPI()

@app.get("/")
async def root():
	return {"Hi": "path example"}

#enum
@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
	if model_name is ModelName.alexnet:
		return {"model_name": model_name, "message": "Deep Learning FTW!"}

	if model_name.value == "lenet":
		return {"model_name": model_name, "message": "LeCNN all the images"}

	return {"model_name": model_name, "message": "Have some residuals"}


#file path
@app.get("/files/{file_path: path}")
async def read_file(file_path: str):
	return {"file_path": file_path}


#query string
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
	return fake_items_db[skip : skip+limit]

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
	if q:
		return {"item_id": item_id, "item_name": fake_items_db[item_id]['item_name'], "q": q}

	return {"item_id": item_id}

#treat boolean
#True can be these values: True, true, Yes, yes, 1
#False can be : False, no, 0 (no care case like true)
@app.get("/itemdesc/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None, short: bool = False):
	item = {"item_id": item_id}

	if q:
		item.update({"q": q})

	if not short:
		item.update(
            {"description": "This is an amazing item that has a long description"}
        )

	return item


#make path multiple paths and variables
@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(user_id: int, item_id: int, q: Optional[str] = None, short: bool = False):
	item = {"item_id": item_id, "owner_id": user_id}

	if q:
		item.update({"q": q})

	if not short:
		item.update(
            {"description": "This is an amazing item that has a long description"}
        )

	return item	

#if didnt use Optional
@app.get("/useritems/{user_id}/{item_id}")
def read_user_item(user_id: int, item_id: int, needy: bool):
	item = {"item_id": item_id, "owner_id": user_id, "needy": "need much"}

	return item