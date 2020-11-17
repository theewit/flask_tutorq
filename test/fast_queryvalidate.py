from typing import Optional, List

from fastapi import FastAPI, Query, Path

app = FastAPI()

@app.get("/")
def main_app():
	return {"Hello": "Query Validation"}

'''
Use Query from fastapi to validattion capable
Query param ([default_value], [constraints_list], title, description, deprecated)
'''
@app.get("/items/")
def read_items(q: Optional[str] = Query(None, min_length=3, max_length=13)):
	result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
	if q:
		result.update({"q": q})

	return result

@app.get("/items/reg/")
def read_items(q: Optional[str] = Query(None, min_length=3, max_length=13, regex="^[A-Z][a-z]{0,10}$")):
	result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
	if q:
		result.update({"q": q})

	return result


#Make it required field with ...
#it forces must be q value whether Optional or not
@app.get("/items/query/")
def read_items(q: str = Query(..., min_length=3, max_length=13, regex="^[A-Z][a-z]{0,10}$")):
	result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
	if q:
		result.update({"q": q})

	return result

#Multiple value of query
#as /items/multiq/?q=Boo&q=Doo
#then q can store in list "q": ["Boo", "Doo"]
@app.get("/items/multiq/")
def read_items(q: Optional[List[str]] = Query(..., min_length=3, max_length=13, regex="^[A-Z][a-z]{0,10}$")):
	result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
	if q:
		result.update({"q": q})

	return result

@app.get("/items/multiq2/")
def read_items(q: List[str] = Query(["Foo"])):
	result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
	if q:
		result.update({"q": q})

	return result


@app.get("/items/multiq3/")
def read_items(q: list = Query(["Foo"])):
	result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
	if q:
		result.update({"q": q})

	return result

#add title , description
#alias use to replace variable name
#deprecated set to Doc API
@app.get("/items/full/")
def read_items(q: List[str] = Query(["Foo"], title="Query dis", description="dis is query", alias="key-find", deprecated=True)):
	result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
	if q:
		result.update({"q": q})

	return result

#Path use
#Query use
#On number can validate with gt, ge, lt, le (greater than, gt or equal, less than, lt or equal)
@app.get("/elements/{element_id}")
def read_element(element_id: int = Path(..., title="The id of the element to get", ge=0, le=100), q: Optional[str] = Query(None, alias="item-query"), size: float = Query(..., gt=0.0, lt=10.5)):
	results = {"element_id": element_id}
	if q:
		results.update({"q": q})
	return results
