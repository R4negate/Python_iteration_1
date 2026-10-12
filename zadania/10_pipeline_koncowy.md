# Zadanie 10 - koncowy mini pipeline

## Cel zadania

Przygotuj mini pipeline w Pythonie, ktory:

1. bierze surowe dane zamowien,
2. waliduje rekordy,
3. czysci teksty,
4. zamienia typy danych,
5. tworzy nowe pola,
6. oddziela poprawne rekordy od blednych,
7. liczy metryki,
8. wypisuje raport tekstowy.

Nie uzywaj jeszcze plikow, pandas ani baz danych.

Pracujemy tylko na:

- zmiennych,
- typach danych,
- listach,
- slownikach,
- `if`,
- petlach,
- funkcjach,
- `try / except`,
- `raise`,
- f-stringach,
- `main()`.

## Dane wejsciowe

Skopiuj dane do pliku `.py`:

```python
raw_orders = [
    {
        "order_id": "1001",
        "customer_id": "1",
        "customer_name": " Anna Kowalska ",
        "country": " pl ",
        "quantity": "2",
        "unit_price": "49.99",
        "status": " Paid ",
        "email": " ANNA@example.COM ",
    },
    {
        "order_id": "1002",
        "customer_id": "2",
        "customer_name": "Jan Nowak",
        "country": "DE",
        "quantity": "1",
        "unit_price": "199.90",
        "status": "cancelled",
        "email": None,
    },
    {
        "order_id": "1003",
        "customer_id": "3",
        "customer_name": " Marta ",
        "country": " fr ",
        "quantity": "bad-data",
        "unit_price": "29.99",
        "status": "paid",
        "email": "marta@example.com",
    },
    {
        "order_id": "1004",
        "customer_id": "4",
        "customer_name": "Piotr Zielinski",
        "country": "",
        "quantity": "5",
        "unit_price": "15.50",
        "status": " pending ",
        "email": "   ",
    },
    {
        "order_id": "1005",
        "customer_id": "5",
        "customer_name": "Julia",
        "country": "PL",
        "quantity": "3",
        "unit_price": "120.00",
        "status": "PAID",
        "email": "julia@example.com",
    },
    {
        "order_id": "1006",
        "customer_id": "6",
        "customer_name": "Tomasz",
        "country": "ES",
        "quantity": "2",
        "unit_price": "abc",
        "status": "paid",
        "email": "tomasz@example.com",
    },
    {
        "order_id": "1007",
        "customer_id": "7",
        "customer_name": "Ewa",
        "country": None,
        "quantity": "1",
        "unit_price": "89.99",
        "status": "paid",
        "email": "ewa@example.com",
    },
]
```

## Wymagany wynik jednego poprawnego rekordu

Kazdy poprawny rekord w `clean_orders` ma miec postac:

```python
{
    "order_id": 1001,
    "customer_id": 1,
    "customer_name": "Anna Kowalska",
    "country": "PL",
    "quantity": 2,
    "unit_price": 49.99,
    "order_value": 99.98,
    "status": "paid",
    "email": "anna@example.com",
    "is_paid": True,
    "order_tier": "standard",
}
```

## Zasady transformacji

### Identyfikatory

Zamien:

- `order_id` na `int`,
- `customer_id` na `int`.

### Teksty

Oczysc:

- `customer_name` przez `.strip()`,
- `country` przez `.strip().upper()`,
- `status` przez `.strip().lower()`,
- `email` przez `.strip().lower()`.

### Braki danych

Dla `country`:

- jezeli `country` to `None`, ustaw `"UNKNOWN"`,
- jezeli po `.strip()` country jest pusty tekst, ustaw `"UNKNOWN"`.

Dla `email`:

- jezeli `email` to `None`, ustaw `"missing email"`,
- jezeli po `.strip()` email jest pusty tekst, ustaw `"missing email"`.

### Liczby

Zamien:

- `quantity` na `int`,
- `unit_price` na `float`.

Policz:

```python
order_value = quantity * unit_price
```

### Nowe pola

Dodaj `is_paid`:

- `True`, jezeli `status == "paid"`,
- `False` w pozostalych przypadkach.

Dodaj `order_tier`:

- `"high"`, jezeli `order_value >= 300`,
- `"standard"`, jezeli `order_value >= 100`,
- `"low"` w pozostalych przypadkach.

## Obsluga blednych rekordow

Rekord jest bledny, jezeli:

- nie da sie zamienic `quantity` na `int`,
- nie da sie zamienic `unit_price` na `float`,
- brakuje wymaganego pola.

Wymagane pola:

- `order_id`,
- `customer_id`,
- `customer_name`,
- `country`,
- `quantity`,
- `unit_price`,
- `status`,
- `email`.

Blednych rekordow nie dodawaj do `clean_orders`.

Dodaj je do listy `invalid_orders`.

## Funkcje, ktore masz napisac

Napisz przynajmniej te funkcje:

```python
def normalize_text(value: str) -> str:
    ...


def normalize_country(country: str | None) -> str:
    ...


def normalize_email(email: str | None) -> str:
    ...


def parse_int(value: str) -> int:
    ...


def parse_float(value: str) -> float:
    ...


def get_order_tier(order_value: float) -> str:
    ...


def validate_order(raw_order: dict) -> None:
    ...


def transform_order(raw_order: dict) -> dict:
    ...


def calculate_metrics(clean_orders: list[dict], invalid_orders: list[dict]) -> dict:
    ...


def print_report(metrics: dict) -> None:
    ...
```

## Metryki do policzenia

Funkcja `calculate_metrics` ma zwrocic slownik z polami:

- `raw_orders_count`,
- `valid_orders_count`,
- `invalid_orders_count`,
- `paid_orders_count`,
- `cancelled_orders_count`,
- `pending_orders_count`,
- `paid_revenue`,
- `total_revenue`,
- `high_orders_count`,
- `unique_countries_count`.

`unique_countries_count` policz z uzyciem `set`.

## Raport tekstowy

Funkcja `print_report` ma wypisac raport:

```text
Raw orders count: ...
Valid orders count: ...
Invalid orders count: ...
Paid orders count: ...
Cancelled orders count: ...
Pending orders count: ...
Paid revenue: ...
Total revenue: ...
High orders count: ...
Unique countries count: ...
```

Kwoty wypisz do 2 miejsc po przecinku.

## Struktura programu

Program ma miec funkcje `main()`.

W `main()`:

1. utworz `raw_orders`,
2. utworz puste listy `clean_orders` i `invalid_orders`,
3. przejdz petla po `raw_orders`,
4. dla kazdego rekordu:
   - uzyj `validate_order`,
   - uzyj `transform_order`,
   - poprawny rekord dodaj do `clean_orders`,
   - bledny rekord dodaj do `invalid_orders`,
5. policz metryki,
6. wypisz raport,
7. wypisz `clean_orders`,
8. wypisz `invalid_orders`.

Na koncu dodaj:

```python
if __name__ == "__main__":
    main()
```

## Dodatkowe wymaganie

W kodzie uzyj przynajmniej raz:

- `type()`,
- `.items()`,
- `enumerate()`,
- `continue`.

