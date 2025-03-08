from typing import Optional
from fastapi import Body, FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello there!"}


# @app.post("/")
# async def post():
#     return  {"item_name"}


# @app.put("/")
# async def put():
#     return  {"item_name"}


# @app.get('/user/{user_id}')
# async def get_user(user_id: int, user_name: str):
#     if user_name == "Joel":
#         return {"Message": "This is me: " + user_name + str(user_id)}
#     else:
#         return {"Message": "This is not me : " + user_name + 'with an id '+ str(user_id)}

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# @app.get('/items/{item_id}')
# async def read_item(item_id: int, short: bool, q: str | None=None):
#     item = {"item_id": item_id}
#     if not short:
#         item.update({"description": "This is an amazing item that has a long description"})
#     if q:
#         item.update({"q": q})
#     return item

# @app.get('/users/{users_id}/items/{item_id}')
# async def get_users_items(users_id: int, item_id: int, q: Optional[str] = None, short: bool = False):
#     item = {"item_id": item_id, "owner_id": users_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )

#     return item

# class Item(BaseModel):
#      name: str
#      description: Optional[str] = None
#      price: float
#      tax: Optional[float] = None


# @app.post('/items/')
# async def create_item(item: Item):
#     item_dic = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dic.update({"price_with_tax": price_with_tax})
#     return item_dic

# @app.put('/items/{item_id}')
# async def create_item_with_put(item_id: int, item: Item):
#     return {"item_id": item_id, **item.model_dump()}


# @app.get('/items/')
# async def read_items(q:list[str]=Query(['foo', 'bar'])):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

"""
 Body -> Multiple Parameters

"""

class User(BaseModel):
    username: str
    full_name: Optional[str] = None

class Importance(BaseModel):
    importance: int

class Intem(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# @app.put("/items/{item_id}")
# async def update_item(
#     *, item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
#     q:str | None=None,
#     item: Item | None=None,
#     user: User,
#     importance: Importance
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     if user:
#         results.update({"user": user})
#     if importance:
#         results.update({"importance": importance})
#     return results

# class Item(BaseModel):
#     name: str
#     description: str| None = Field(None, title="The description of the item", max_length=300)
#     price: float = Field(..., gt=0, description="The price must be greater than zero")
#     tax: Optional[float] = Field(None, description="An optional tax")

# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item=Body(..., embed=True)):
#    results = {"item_id": item_id, "item": item}
#    return results

    """
    Nest Models
    """
