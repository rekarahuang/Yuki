# 红色：工作区
# 绿色：暂存区
# 蓝色：暂存区（文件有修改）
# 无颜色：位于本地仓库区/已提交到远程仓库区


# step1. 导入FastAPI及相关模块
from typing import Union
from fastapi import FastAPI

from pydantic import BaseModel

# step2. 创建一个FastAPI实例（所有 API 的主要交互对象）
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

'''
uvicorn main:app命令含义如下:

main：main.py文件（一个 Python "模块"）。
app：在 main.py 文件中通过 app = FastAPI() 创建的对象。
--reload：让服务器在更新代码后重新启动。仅在开发时使用该选项。
--port:指定启动的端口，该代码中指定了18080端口。
'''

# step3. 创建一个路径操作（指URL中从第一个 / 起的后半部分）
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

'''
http://127.0.0.1:8005/items/5?q=somequery

通过 路径 / 和 /items/{item_id} 接受 HTTP 请求。
以上 路径 都接受 GET 操作（也被称为 HTTP 方法）。
/items/{item_id} 路径 有一个 路径参数 item_id 并且应该为 int 类型。
/items/{item_id} 路径 有一个可选的 str 类型的 查询参数 q。
'''

'''
http://127.0.0.1:8005/docs
自动生成的交互式 API 文档（由 Swagger UI生成）

http://127.0.0.1:8005/docs
另一个自动生成的文档（由 ReDoc 生成）
'''



'''
常见http状态返回码：
200 - 服务器成功返回网页
403 - 服务器拒绝请求
404 - 服务器找不到请求的网页
405 - 该请求使用的方法被服务器端禁止使用
500 - 服务器内部错误
502 - 错误网关
503 - 服务不可用
'''