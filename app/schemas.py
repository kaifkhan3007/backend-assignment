from pydantic import BaseModel, Field
from typing import List


class ProductBase(BaseModel):
    name: str
    description: str
    price: float = Field(gt=0)
    stock: int = Field(ge=0)


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)


class OrderCreate(BaseModel):
    items: List[OrderItemCreate]


class Order(BaseModel):
    id: int
    total_price: float
    status: str
    products: List[Product]

    class Config:
        orm_mode = True
