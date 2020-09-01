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
	return {"Hello": "World"}

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
