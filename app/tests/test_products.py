def test_create_product(client):
    response = client.post(
        "/products",
        json={
            "name": "Test Product",
            "description": "Test Description",
            "price": 99.99,
            "stock": 10
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["price"] == 99.99
    assert data["stock"] == 10


def test_get_products(client):
    client.post(
        "/products",
        json={
            "name": "Test Product",
            "description": "Test Description",
            "price": 99.99,
            "stock": 10
        }
    )

    response = client.get("/products")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["name"] == "Test Product"
