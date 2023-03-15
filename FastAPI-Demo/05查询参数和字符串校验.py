from typing import List, Union

from fastapi import FastAPI

# 从fastapi导入Query
from fastapi import Query
from pydantic import Required

app = FastAPI()


# 为参数声明额外的信息和校验
# @app.get("/items/")
# async def read_items(q: Union[str, None] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# 额外的校验
# 添加约束条件：即使 q 是可选的，但只要提供了该参数，则该参数值不能超过50个字符的长度。

@app.get("/items/")
# 　Query显式地将其声明为查询参数
# async def read_items(q: Union[str, None] = Query(default=None, max_length=50)):
# 添加更多校验
# async def read_items(q: Union[str, None] = Query(default=None, min_length=3, max_length=50)):
# 添加正则表达式
# async def read_items(
#     q: Union[str, None] = Query(
#         default=None, min_length=3, max_length=50, regex="^fixedquery$"
#     )
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# 　默认值
# @app.get("/items/")
# async def read_items(q: str = Query(default="fixedquery", min_length=3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# 必须参数

@app.get("/items/")
# 1.不声明默认参数
# async def read_items(q: str = Query(min_length=3)):
# 2.使用省略号声明必须参数
# async def read_items(q: str = Query(default=..., min_length=3)):
# 3.使用required
# async def read_items(q: str = Query(default=Required, min_length=3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# 　查询参数列表/多个值
# 　声明一个可在 URL 中出现多次的查询参数 q
@app.get("/items/")
async def read_items(q: Union[List[str], None] = Query(default=None)):
    query_items = {"q": q}
    return query_items

# 具有默认值的查询参数列表 / 多个值
@app.get("/items/")
async def read_items(q: List[str] = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items

# 声明更多元数据
@app.get("/items/")
async def read_items(
    q: Union[str, None] = Query(default=None, title="Query string", min_length=3)
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/")
async def read_items(
    q: Union[str, None] = Query(
        default=None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results