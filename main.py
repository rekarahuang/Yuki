# 红色：工作区
# 绿色：暂存区
# 蓝色：暂存区（文件有修改）
# 无颜色：位于本地仓库区/已提交到远程仓库区

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

