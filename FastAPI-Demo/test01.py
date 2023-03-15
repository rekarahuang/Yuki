# 红色：工作区
# 绿色：暂存区
# 蓝色：暂存区（文件有修改）
# 无颜色：位于本地仓库区/已提交到远程仓库区


# step1. 导入FastAPI及相关模块
from typing import Union
from fastapi import FastAPI

# step2. 创建一个FastAPI实例（所有 API 的主要交互对象）
# FastAPI 是直接从 Starlette 继承的类，可以通过 FastAPI 使用所有的 Starlette 的功能
app = FastAPI()


# step3. 创建一个路径操作
# 路径：URL中从第一个/起的后半部分
# 操作：http方法（post创建/get读取/put更新/delete删除）
# 定义一个路径操作装饰器，路径：/，操作：get
@app.get("/")
# step4. 定义路径操作函数 当FastAPI接收一个使用GET方法访问URL【/】的请求时这个函数会被调用
def read_root():
    return {"Hello": "World"}  # 可返回（dict、list、str、int、Pydantic模型）


# step5. 运行开发服务器
# uvicorn main:app --reload
'''
uvicorn main:app命令含义如下:

main：main.py文件（一个 Python "模块"）。
app：在 main.py 文件中通过 app = FastAPI() 创建的对象。
--reload：让服务器在更新代码后重新启动。仅在开发时使用该选项。
--port:指定启动的端口，该代码中指定了18080端口。
'''


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


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

# 报错  Error loading ASGI app. Could not import module "test01".
# 错误原因 没有使用完整路径（路径用.）
#  uvicorn FastAPI-Demo.test01:app --reload --port 8005
