from typing import Union

from fastapi import Body, FastAPI
#　导入Field
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    # 对模型属性使用 Field
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results

'''
可以使用 Pydantic 的 Field 为模型属性声明额外的校验和元数据。

还可以使用额外的关键字参数来传递额外的 JSON Schema 元数据。
'''