# Zadania 09 - podsumowanie iteracji

## Zadanie 1

Masz liste klientow:

```python
customers = [
    {"customer_id": 1, "name": " Anna ", "country": "pl", "email": "anna@example.com"},
    {"customer_id": 2, "name": "Jan", "country": "DE", "email": None},
    {"customer_id": 3, "name": "Marta", "country": " fr ", "email": "marta@example.com"},
]
```

Przygotuj liste `clean_customers`, gdzie:

- `name` jest bez spacji,
- `country` jest wielkimi literami,
- `email` ma wartosc `"missing email"`, jesli bylo `None`.

## Zadanie 2

Masz liste zamowien:

```python
orders = [
    {"order_id": 1001, "customer_id": 1, "amount": 120, "status": "paid"},
    {"order_id": 1002, "customer_id": 2, "amount": 80, "status": "cancelled"},
    {"order_id": 1003, "customer_id": 1, "amount": 200, "status": "paid"},
]
```

Policz laczna wartosc zamowien `paid`.

## Zadanie 3

Napisz funkcje `get_customer_orders(customer_id: int, orders: list[dict]) -> list[dict]`.

Funkcja ma zwrocic tylko zamowienia wskazanego klienta.

## Zadanie 4

Napisz funkcje `build_customer_summary(customer: dict, orders: list[dict]) -> dict`.

Wynik ma zawierac:

- `customer_id`,
- `name`,
- `orders_count`,
- `paid_revenue`.

