def test_create_order_success(client):
    product_response = client.post(
        "/products",
        json={
            "name": "Test Product",
            "description": "Test Description",
            "price": 99.99,
            "stock": 10
        }
    )
    product_id = product_response.json()["id"]

    response = client.post(
        "/orders",
        json={
            "items": [
                {
                    "product_id": product_id,
                    "quantity": 2
                }
            ]
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["status"] == "pending"
    assert data["total_price"] == 99.99 * 2


def test_create_order_insufficient_stock(client):
    product_response = client.post(
        "/products",
        json={
            "name": "Test Product",
            "description": "Test Description",
            "price": 99.99,
            "stock": 1
        }
    )
    product_id = product_response.json()["id"]

    response = client.post(
        "/orders",
        json={
            "items": [
                {
                    "product_id": product_id,
                    "quantity": 2
                }
            ]
        }
    )
    assert response.status_code == 400
    assert "Insufficient stock" in response.json()["detail"]