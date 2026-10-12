# 08. Mini pipeline na listach i slownikach

## Po co robimy mini-pipeline

W tej iteracji poznalismy podstawy:

- zmienne,
- typy danych,
- stringi,
- listy,
- slowniki,
- `if`,
- petle,
- funkcje,
- podstawowe bledy.

Teraz laczymy to w jeden maly przeplyw danych.

W data engineeringu pipeline to proces, ktory bierze dane wejsciowe, wykonuje kilka krokow i zwraca albo zapisuje wynik.

Prosty pipeline:

```text
raw data -> validate -> transform -> calculate metrics -> print result
```

Na razie wszystko zrobimy w pamieci, na liscie slownikow.

## Dane surowe

Wyobraz sobie, ze dane przyszly z API.

```python
raw_orders = [
    {"id": "1", "country": " pl ", "amount": "120.50", "status": "paid"},
    {"id": "2", "country": "DE", "amount": "80", "status": "cancelled"},
    {"id": "3", "country": None, "amount": "200", "status": "paid"},
    {"id": "4", "country": " fr ", "amount": "bad-data", "status": "paid"},
]
```

Te dane sa "brudne":

- `id` jest tekstem,
- `amount` jest tekstem,
- `country` ma spacje albo `None`,
- jedno `amount` ma zly format,
- statusy trzeba ujednolicic.

To jest realistyczne. Dane zrodlowe rzadko sa idealne.

## Docelowy format

Chcemy otrzymac dane w takim formacie:

```python
{
    "order_id": 1,
    "country": "PL",
    "amount": 120.50,
    "status": "paid",
    "order_tier": "standard",
}
```

Czyli:

- `order_id` jako `int`,
- `country` oczyszczony i wielkimi literami,
- `amount` jako `float`,
- `status` malymi literami,
- `order_tier` jako segment na podstawie kwoty.

## Krok 1: funkcja do parsowania kwoty

Kwota moze miec zly format, wiec uzywamy `try / except`.

```python
def parse_amount(raw_amount: str) -> float:
    try:
        return float(raw_amount)
    except ValueError:
        return 0
```

Jesli `raw_amount = "120.50"`, funkcja zwroci `120.5`.

Jesli `raw_amount = "bad-data"`, funkcja zwroci `0`.

## Krok 2: funkcja do kraju

```python
def normalize_country(country: str | None) -> str:
    if country is None:
        return "UNKNOWN"

    return country.strip().upper()
```

Dlaczego sprawdzamy `None`?

Bo to sie wywali:

```python
None.strip()
```

Najpierw sprawdzamy brak wartosci, potem czyscimy tekst.

## Krok 3: funkcja do segmentu

```python
def get_order_tier(amount: float) -> str:
    if amount >= 200:
        return "high"

    return "standard"
```

To jest zwykla logika biznesowa.

## Krok 4: transformacja jednego zamowienia

```python
def transform_order(raw_order: dict) -> dict:
    amount = parse_amount(raw_order["amount"])

    return {
        "order_id": int(raw_order["id"]),
        "country": normalize_country(raw_order.get("country")),
        "amount": amount,
        "status": raw_order["status"].strip().lower(),
        "order_tier": get_order_tier(amount),
    }
```

Ta funkcja bierze surowe zamowienie i zwraca czyste zamowienie.

Wazne:

```python
raw_order["id"]
```

oznacza pole wymagane.

```python
raw_order.get("country")
```

oznacza pole, ktore moze byc puste albo opcjonalne.

## Krok 5: transformacja listy zamowien

```python
clean_orders = []

for raw_order in raw_orders:
    clean_order = transform_order(raw_order)
    clean_orders.append(clean_order)
```

Czytamy:

```text
stworz pusta liste clean_orders
dla kazdego surowego zamowienia
przeksztalc je
dodaj do listy czystych zamowien
```

## Krok 6: policzenie metryk

Policzmy sume zamowien `paid`.

```python
paid_revenue = 0

for order in clean_orders:
    if order["status"] == "paid":
        paid_revenue = paid_revenue + order["amount"]
```

Mozemy tez policzyc liczbe zamowien `paid`:

```python
paid_orders_count = 0

for order in clean_orders:
    if order["status"] == "paid":
        paid_orders_count = paid_orders_count + 1
```

## Pelny przyklad

```python
def parse_amount(raw_amount: str) -> float:
    try:
        return float(raw_amount)
    except ValueError:
        return 0


def normalize_country(country: str | None) -> str:
    if country is None:
        return "UNKNOWN"

    return country.strip().upper()


def get_order_tier(amount: float) -> str:
    if amount >= 200:
        return "high"

    return "standard"


def transform_order(raw_order: dict) -> dict:
    amount = parse_amount(raw_order["amount"])

    return {
        "order_id": int(raw_order["id"]),
        "country": normalize_country(raw_order.get("country")),
        "amount": amount,
        "status": raw_order["status"].strip().lower(),
        "order_tier": get_order_tier(amount),
    }


def main() -> None:
    raw_orders = [
        {"id": "1", "country": " pl ", "amount": "120.50", "status": "paid"},
        {"id": "2", "country": "DE", "amount": "80", "status": "cancelled"},
        {"id": "3", "country": None, "amount": "200", "status": "paid"},
        {"id": "4", "country": " fr ", "amount": "bad-data", "status": "paid"},
    ]

    clean_orders = []

    for raw_order in raw_orders:
        clean_order = transform_order(raw_order)
        clean_orders.append(clean_order)

    paid_revenue = 0

    for order in clean_orders:
        if order["status"] == "paid":
            paid_revenue = paid_revenue + order["amount"]

    print(clean_orders)
    print(f"paid_revenue={paid_revenue:.2f}")


if __name__ == "__main__":
    main()
```

## Co tu cwiczymy

Ten jeden przyklad uzywa prawie wszystkiego z iteracji:

- zmienne,
- `str`, `int`, `float`, `None`,
- konwersje typow,
- `.strip()`, `.upper()`, `.lower()`,
- slowniki,
- listy,
- petle,
- `if`,
- funkcje,
- `return`,
- `try / except`,
- `main()`.

## Mini-cwiczenie

Rozszerz pipeline:

1. dodaj metryke `cancelled_orders_count`,
2. dodaj metryke `high_orders_count`,
3. wypisz wynik przez f-string.

Podpowiedz:

```python
cancelled_orders_count = 0
high_orders_count = 0

for order in clean_orders:
    ...
```

## Pytania kontrolne

1. Co oznacza etap `raw data`?
2. Po co dzielimy pipeline na funkcje?
3. Dlaczego `parse_amount` ma `try / except`?
4. Dlaczego w `normalize_country` sprawdzamy `None`?
5. Co robi `transform_order`?
6. Dlaczego najpierw tworzymy `clean_orders`, a dopiero potem liczymy metryki?
7. Ktore elementy tej lekcji przypominaja prace z SQL?
