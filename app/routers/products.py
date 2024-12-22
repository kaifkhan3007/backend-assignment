from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Product
from app.schemas import ProductCreate, Product as ProductSchema
from app.exceptions import ProductNotFoundError

router = APIRouter()


@router.get("/products", response_model=List[ProductSchema])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


@router.post("/products", response_model=ProductSchema, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.get("/products/{product_id}", response_model=ProductSchema)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise ProductNotFoundError(product_id)
    return product
