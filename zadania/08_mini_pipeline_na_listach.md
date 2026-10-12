# Zadania 08 - mini pipeline na listach i slownikach

Uzyj danych:

```python
raw_orders = [
    {"id": "1", "country": " pl ", "amount": "120.50", "status": "paid"},
    {"id": "2", "country": "DE", "amount": "80", "status": "cancelled"},
    {"id": "3", "country": None, "amount": "200", "status": "paid"},
    {"id": "4", "country": " fr ", "amount": "bad-data", "status": "paid"},
    {"id": "5", "country": "PL", "amount": "300", "status": "pending"},
]
```

## Zadanie 1

Napisz funkcje:

```python
def parse_amount(raw_amount: str) -> float:
    ...
```

Funkcja ma:

- zamienic tekst na `float`,
- zwrocic `0`, jezeli tekst ma zly format.

## Zadanie 2

Napisz funkcje:

```python
def normalize_country(country: str | None) -> str:
    ...
```

Zasady:

- jezeli `country` to `None`, zwroc `"UNKNOWN"`,
- w pozostalych przypadkach usun spacje i zamien tekst na wielkie litery.

## Zadanie 3

Napisz funkcje:

```python
def get_order_tier(amount: float) -> str:
    ...
```

Zasady:

- `high`, jezeli `amount >= 200`,
- `standard` w pozostalych przypadkach.

## Zadanie 4

Napisz funkcje:

```python
def transform_order(raw_order: dict) -> dict:
    ...
```

Funkcja ma zwrocic slownik z polami:

- `order_id` jako `int`,
- `country`,
- `amount`,
- `status`,
- `order_tier`.

## Zadanie 5

Przetworz cala liste `raw_orders` do listy `clean_orders`.

Kazdy element w `clean_orders` ma byc wynikiem funkcji `transform_order`.

## Zadanie 6

Policz metryki:

- `orders_count`,
- `paid_orders_count`,
- `cancelled_orders_count`,
- `paid_revenue`,
- `high_orders_count`.

## Zadanie 7

Wypisz raport tekstowy przez f-string w formacie:

```text
Orders count: ...
Paid orders count: ...
Cancelled orders count: ...
Paid revenue: ...
High orders count: ...
```

`paid_revenue` wypisz z dokladnoscia do 2 miejsc po przecinku.

## Zadanie 8

Dodaj funkcje:

```python
def calculate_metrics(clean_orders: list[dict]) -> dict:
    ...
```

Funkcja ma zwrocic slownik z metrykami z zadania 6.

## Zadanie 9

Dodaj funkcje `main()`, ktora:

1. tworzy `raw_orders`,
2. tworzy `clean_orders`,
3. liczy metryki,
4. wypisuje raport.

Na koncu pliku dodaj:

```python
if __name__ == "__main__":
    main()
```

## Zadanie 10

Dodaj do pipeline'u liste `invalid_orders`.

Jezeli `amount` ma zly format, zamowienie powinno trafic do `invalid_orders`, a nie do `clean_orders`.

Podpowiedz:

- `parse_amount` moze rzucac `ValueError`,
- petla w `main()` moze uzyc `try / except`.

## Zadanie 11

Rozszerz raport o:

- liczbe poprawnych zamowien,
- liczbe blednych zamowien,
- laczna wartosc poprawnych zamowien.

