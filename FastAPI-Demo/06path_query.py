# 　与使用 Query 为[查询参数]声明更多的校验和元数据的方式相同
# 也可以使用 Path 为[路径参数]声明相同类型的校验和元数据

from typing import Union
# 导入Path
from fastapi import FastAPI, Path, Query

app = FastAPI()


# 声明元数据：声明路径参数 item_id的 title 元数据值
# @app.get("/items/{item_id}")
# async def read_items(
#         # 按需对参数排序
#         item_id: int = Path(title="The ID of the item to get"),
#         q: Union[str, None] = Query(default=None, alias="item-query"),
# ):
#     # async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# 　按需对参数排序的技巧

# async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):

# * 作用：
# 传递 * 作为函数的第一个参数
# 之后的所有参数都应作为关键字参数（键值对），也被称为 kwargs，来调用。即使它们没有默认值

# 数值校验

# gt：大于（greater than）
# ge：大于等于（greater than or equal）
# lt：小于（less than）
# le：小于等于（less than or equal）

@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(title="The ID of the item to get", ge=1), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    q: str,
    size: float = Query(gt=0, lt=10.5),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results