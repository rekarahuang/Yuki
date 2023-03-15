from typing import Union

from fastapi import FastAPI

# 导入Pydantic的BaseModel
from pydantic import BaseModel


# 请求体：需要将数据从客户端（例如浏览器）发送给 API 时，将数据作为「请求体」发送

# 请求体：客户端→API
# 响应体: API→客户端

# 发送请求体：POST、PUT、DELETE、PATCH

# 创建数据模型
# 模型属性的默认值设置类似于查询参数
class Item(BaseModel):
    name: str
    price: float
    tax: Union[float, None] = None


app = FastAPI()


#
# @app.post("/items/")
# async def create_item(item: Item): #　声明为参数，并将类型声明为创建的Item模型
#     item.name + item.price
#     return item


# @app.post("/items/")
# async def create_item(item: Item):
#     # 使用模型
#     item_dict = item.dict()
#     # 在函数内部，可以直接访问模型对象的所有属性
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict

# 　请求体 + 路径参数（同时声明路径参数和请求体）
# FastAPI将识别出与路径参数匹配的函数参数应从路径中获取，
# 而声明为 Pydantic 模型的函数参数应从请求体中获取。

# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
#     # return {"item_id": item_id, **item.dict()}
#     print({"item_id": item_id, **item.dict()}, 111)
#     return {"item_id": item_id, **item.dict()}


#　请求体＋路径参数＋查询参数
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


'''
如果在路径中也声明了该参数，它将被用作[路径参数]。
如果参数属于单一类型（比如 int、float、str、bool 等）它将被解释为[查询参数]。
如果参数的类型[被声明为一个 Pydantic 模型]，它将被解释为请求体。
'''