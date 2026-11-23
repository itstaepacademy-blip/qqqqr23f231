from src.legacy_processor import process_orders


def test_new_order_is_processed():
    result = process_orders([{"id": 1, "status": "new", "amount": 100}])
    assert result == [{"id": 1, "total": 100, "status": "processed"}]


def test_discount_and_shipping_are_applied():
    result = process_orders([{"id": 2, "status": "new", "amount": 100, "discount": 0.1, "shipping": 5}])
    assert result[0]["total"] == 95



def test_invalid_amount():
    result = process_orders([{"id": 3, "status": "new", "amount": 0}])
    assert result[0]["status"] == "invalid"



def test_non_new_order_is_skipped():
    result = process_orders([{"id": 4, "status": "done", "amount": 50}])
    assert result[0]["status"] == "skipped"
