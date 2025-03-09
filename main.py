from email.header import Header
from typing import Literal, Optional
from fastapi import Cookie, FastAPI
from pydantic import BaseModel, EmailStr, HttpUrl


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

    # @app.put("/items/{item_id}")
    # async def read_items(
    #     item_id: UUID,
    #     start_date: datetime | None = Body(None),
    #     end_date: datetime | None = Body(None),
    #     repeat_at: datetime | None = Body(None),
    #     process_after: datetime | None = Body(None),
    # ):
    #     start_process = start_date + process_after
    #     duration = end_date - process_after
    #     return {'item_id': item_id, 'start_date': start_date, 'end_date': end_date, 'repeat_at': repeat_at, 'process_after': process_after, 'start_process': start_process, 'duration': duration}


## Cookie and header Parameters
@app.get("/items/")
async def readd_items(cookies_id: str | None=Cookie(None),
                      accept_encoding: str | None=Header(None),
                      sec_ch_ua: str | None=Header(None),
                      user_agent: str | None=Header(None),
                      x_token: str | None=Header(None)):

    return {
        "cookies_id": cookies_id,
        "Accept-Encoding": accept_encoding,
        "Sec-CH-UA": sec_ch_ua,
        "User-Agent": user_agent,
        "X-Token Values": x_token,
        }

## Response Model

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []



items = {
    'foo': { "name": "Foo", "Price": 50.2},
    'bar': { "name": "Bar", "Description": "The bartenders", "Price": 62.2, "Tax": 20.2},
    "baz": { "name": "Baz", "Description": None, "Price": 50.2, "Tax": 20.2, "tags": []}
}

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: Literal['foo', 'bar', 'baz']):
    return items[item_id]

@app.post("/items/")
async def create_item(item: Item):
    return item


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None

@app.post("/user/", response_model=UserIn)
async def create_user(user: UserIn):
    return user


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserInDB(UserBase):
    password: str

class UserOut(UserBase):
    pass

@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


@app.get("/items/{item_id}/name", response_model= Item, response_model_include=["name", "description"])
async def read_item_name(item_id: Literal['foo', 'bar', 'baz']):
    return items[item_id]

@app.get("/items/{item_id}/public", response_model= Item, response_model_exclude=["tax"])
async def read_items_public_data(item_id: Literal['foo', 'bar', 'baz']):
    return items[item_id]

def fake_password_hasher(password: str):
    return "supersecret" + password

def fake_save_user(user: UserIn):
    hashed_password = fake_password_hasher(user.password)
    user_in_db = UserInDB(**user.dict(), password=hashed_password)
    print(UserInDB( username=user_in_db.username, email=user_in_db.email, full_name=user_in_db.full_name))

    return user_in_db

@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    user_saved = fake_save_user(user)
    return user_saved
class PlanItem(BaseModel):
    name: str
    description: str | None = None

class CarItem(BaseModel):
    name: str
    description: str | None = None

@app.get("/items/{item_id}", response_model= PlanItem | CarItem)
async def read_item(item_id: Literal["Item 1", "Item 2"]):
    if item_id == 1:
        return PlanItem(name="Foo", description="There are some planes")
    else:
        return CarItem(name="Bar", description="There are some cars")
