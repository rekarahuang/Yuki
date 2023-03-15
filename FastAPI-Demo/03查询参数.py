from fastapi import FastAPI
from typing import Union
app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# 查询参数：声明不属于路径参数的其他函数参数时，将被自动解释为"查询字符串"参数
# 查询字符串是键值对的集合，这些键值对位于 URL 的 ？ 之后，并以 & 符号分隔

# 默认值
# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]

# 可选参数 默认值设置为 None 声明可选查询参数
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Union[str, None] = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


# 查询参数类型转换 声明 bool 类型，将被自动转换
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

#多个路径和查询参数
# @app.get("/users/{user_id}/items/{item_id}") # 增加users/{user_id}
# async def read_user_item(
#     user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
# ): # 参数多一个user_id
#
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# 可选：设置none
# 非必须：设置默认值
# 必须：不设置默认值

@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item