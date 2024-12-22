from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Order, Product
from app.schemas import OrderCreate, Order as OrderSchema
from app.exceptions import InsufficientStockError, ProductNotFoundError

router = APIRouter()


@router.post("/orders", response_model=OrderSchema, status_code=status.HTTP_201_CREATED)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    total_price = 0
    products_to_update = []

    for item in order.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            raise ProductNotFoundError(item.product_id)

        if product.stock < item.quantity:
            raise InsufficientStockError(
                product_id=item.product_id,
                requested=item.quantity,
                available=product.stock
            )

        total_price += product.price * item.quantity
        product.stock -= item.quantity
        products_to_update.append(product)

    db_order = Order(
        total_price=total_price,
        status="pending",
        products=products_to_update
    )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
