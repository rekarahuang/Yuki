from fastapi import FastAPI
from enum import Enum

app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}
# 路径参数 item_id 的值将作为参数 item_id 传递给函数。


# 指定参数类型
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

# 数据转换 FastAPI 通过类型声明提供对请求的自动"解析"

# 数据校验 FastAPI 提供了数据校验功能

# 路径顺序

# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}
#
#
# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}


# 预设值

# 定义枚举类
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# 创建一个带有类型标注的路径参数
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     # 比较枚举成员
#     if model_name is ModelName.alexnet:
#         # 返回枚举成员
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#     # 获取枚举值model_name.value
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#
#     return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
