from fastapi import HTTPException, status


class InsufficientStockError(HTTPException):
    def __init__(self, product_id: int, requested: int, available: int):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Insufficient stock for product {product_id}. Requested: {requested}, Available: {available}"
        )


class ProductNotFoundError(HTTPException):
    def __init__(self, product_id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {product_id} not found"
        )
