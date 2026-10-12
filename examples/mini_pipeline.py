raw_orders = [
    {"id": 1, "country": " pl ", "amount": "120.50", "status": "paid"},
    {"id": 2, "country": "DE", "amount": "80", "status": "cancelled"},
    {"id": 3, "country": None, "amount": "200", "status": "paid"},
    {"id": 4, "country": " fr ", "amount": "50", "status": "pending"},
]


def validate_order(raw_order: dict) -> None:
    required_fields = ["id", "amount", "status"]

    for field in required_fields:
        if field not in raw_order:
            raise ValueError(f"Missing field: {field}")


def normalize_order(raw_order: dict) -> dict:
    country = raw_order.get("country")

    if country is None:
        clean_country = "UNKNOWN"
    else:
        clean_country = country.strip().upper()

    amount = float(raw_order["amount"])

    if amount >= 150:
        order_tier = "high"
    else:
        order_tier = "standard"

    return {
        "order_id": raw_order["id"],
        "country": clean_country,
        "amount": amount,
        "status": raw_order["status"].strip().lower(),
        "order_tier": order_tier,
    }


def calculate_paid_revenue(orders: list[dict]) -> float:
    paid_revenue = 0

    for order in orders:
        if order["status"] == "paid":
            paid_revenue += order["amount"]

    return paid_revenue


def main() -> None:
    clean_orders = []

    for raw_order in raw_orders:
        validate_order(raw_order)
        clean_orders.append(normalize_order(raw_order))

    print(clean_orders)
    print(calculate_paid_revenue(clean_orders))


if __name__ == "__main__":
    main()

