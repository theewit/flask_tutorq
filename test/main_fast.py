from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()

class Item(BaseModel):
	name: str
	price: float
	is_offer: Optional[bool] = None

class User(BaseModel):
	id: int
	name: str
	joined: date

@app.get("/")
def read_root():
	return {"Hello": "maint Fast World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
	return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, my_user: User):
	#my_user: User = User(id=101, name="indy", joined="2019-02-14")
	second_user_data = {
		"id": my_user.id,
		"name": "brown",
		"joined": "2018-10-21"
	}

	my_second_user: User = User(**second_user_data)

	return {"item_name": item.name, "item_price": item.price, "item_id": item_id, "user": my_second_user}


#The order of path parameter is important
@app.get("/users/me")
async def read_user_me():
	return {"user_id": get_user_id()}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
	return {"user_id": get_user_id(user_id)}

def get_user_id(user_id: Optional[str] = None) -> str:
	if user_id is None:
		return "the current user"
	else:
		return user_id

