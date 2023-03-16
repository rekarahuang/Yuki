from typing import List, Union, Set

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 声明具有子类型的 List
my_list: List[str]

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    # 将一个属性定义为拥有子元素的类型
    # tags: list = []
    # 将tags明确地指定为一个「字符串列表」：
    # tags: List[str] = []
    # 将tag声明为一个由str组成的set
    tags: Set[str] = set()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

# 嵌套模型

# 定义一个Image模型
# class Image(BaseModel):
#     url: str
#     name: str

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: Set[str] = set()
#     # 将Image用作一个属性的类型
#     image: Union[Image, None] = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

'''
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": ["rock", "metal", "bar"],
    "image": {
        "url": "http://example.com/baz.jpg",
        "name": "The Foo live"
    }
}
'''

# 特殊的类型和校验
# 在 Image 模型中我们有一个 url 字段，我们可以把它声明为 Pydantic 的 HttpUrl，而不是 str
# 该字符串将被检查是否为有效的 URL，并在 JSON Schema / OpenAPI 文档中进行记录。
from pydantic import HttpUrl
# class Image(BaseModel):
#     url: HttpUrl
#     name: str

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: Set[str] = set()
#     # image: Union[Image, None] = None
#     # 带有一组子模型的属性
#     # images: Union[List[Image], None] = None
#
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results


# 深度嵌套模型

class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()
    images: Union[List[Image], None] = None


class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: List[Item]


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

# 纯列表请求体
@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images