from typing import TypedDict


class Order(TypedDict, total=False):
    id: object
    status: str
    amount: float
    discount: float
    shipping: float


class ProcessedOrder(TypedDict):
    id: object
    total: float
    status: str


def process_orders(orders: list[Order]) -> list[ProcessedOrder]:
    results: list[ProcessedOrder] = []
    for order in orders:
        if order.get("status") == "new":
            if order.get("amount", 0) > 0:
                total = order["amount"]
                if order.get("discount"):
                    total = total - total * order["discount"]
                if order.get("shipping"):
                    total += order["shipping"]
                results.append({"id": order.get("id"), "total": total, "status": "processed"})
            else:
                results.append({"id": order.get("id"), "total": 0, "status": "invalid"})
        else:
            results.append({"id": order.get("id"), "total": 0, "status": "skipped"})
    return results
