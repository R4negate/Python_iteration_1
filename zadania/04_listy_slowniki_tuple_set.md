# Zadania 04 - listy, slowniki, tuple i sety

Na tej lekcji cwiczymy struktury danych.

Jeszcze nie musisz uzywac petli. Chodzi o to, zeby recznie zrozumiec:

- czym jest lista,
- czym jest slownik,
- czym jest lista slownikow,
- jak pobierac konkretne wartosci,
- jak uzywac `.get()`,
- jak dodawac elementy do listy,
- jak tworzyc `set` i `tuple`.

## Zadanie 1

Utworz slownik `customer` z polami:

- `customer_id`: `1`,
- `customer_name`: `"Anna Kowalska"`,
- `country`: `"PL"`,
- `email`: `"anna@example.com"`,
- `acquisition_channel`: `"newsletter"`.

Wypisz:

- caly slownik,
- `customer_name`,
- `country`.

## Zadanie 2

Masz slownik:

```python
customer = {
    "customer_id": 1,
    "customer_name": "Anna Kowalska",
    "country": "PL",
}
```

Pobierz pole `email` przez `.get()` tak, aby jesli go nie ma, zwrocic:

```text
missing@example.com
```

Wypisz wynik.

## Zadanie 3

Masz slownik:

```python
order = {
    "order_id": 1001,
    "status": "new",
    "amount": 129.99,
}
```

Zmien `status` na `"paid"`.

Dodaj nowe pole:

```python
"country": "PL"
```

Wypisz caly slownik.

## Zadanie 4

Utworz liste `orders`, ktora zawiera 3 slowniki:

```python
{"order_id": 1001, "customer_id": 1, "status": "paid", "amount": 120.0}
{"order_id": 1002, "customer_id": 1, "status": "cancelled", "amount": 80.0}
{"order_id": 1003, "customer_id": 2, "status": "paid", "amount": 200.0}
```

Wypisz cala liste.

## Zadanie 5

Korzystajac z listy `orders` z zadania 4, wypisz:

- pierwszy rekord,
- `status` drugiego rekordu,
- `amount` trzeciego rekordu,
- `customer_id` pierwszego rekordu.

Nie uzywaj petli.

## Zadanie 6

Dodaj czwarte zamowienie do listy `orders` przez `.append()`:

```python
{"order_id": 1004, "customer_id": 3, "status": "pending", "amount": 50.0}
```

Wypisz:

- cala liste,
- liczbe elementow w liscie przez `len()`.

## Zadanie 7

Masz liste:

```python
countries = ["PL", "DE", "PL", "FR", "DE", "PL"]
```

Stworz z niej `set` o nazwie `unique_countries`.

Wypisz:

- `unique_countries`,
- typ `unique_countries`.

## Zadanie 8

Stworz tuple `date_range`, ktory zawiera:

```text
2026-10-01
2026-10-31
```

Wypisz:

- caly tuple,
- pierwszy element,
- drugi element.

## Zadanie 9

Masz dane:

```python
orders = [
    {"order_id": 1001, "customer": {"customer_id": 1, "name": "Anna"}, "amount": 120.0},
    {"order_id": 1002, "customer": {"customer_id": 2, "name": "Jan"}, "amount": 80.0},
]
```

Wypisz:

- imie klienta z pierwszego zamowienia,
- `customer_id` klienta z drugiego zamowienia,
- kwote drugiego zamowienia.

Nie uzywaj petli.

## Zadanie 10

Masz liste:

```python
countries = ["PL", "DE"]
```

Dodaj do niej `"FR"` i `"IT"`, a potem wypisz cala liste oraz jej dlugosc.

## Zadanie 11

Masz slownik:

```python
order = {
    "order_id": 1001,
    "status": "new",
    "total": 129.99,
}
```

Zrob:

1. zmien `status` na `"paid"`,
2. dodaj nowe pole `country` z wartoscia `"PL"`,
3. wypisz `keys()`,
4. wypisz `values()`,
5. wypisz `items()`.

## Zadanie 12

Masz dane:

```python
orders = [
    {"order_id": 1, "total": 100, "status": "paid"},
    {"order_id": 2, "total": 200, "status": "cancelled"},
]
```

Najpierw pobierz pierwszy rekord do zmiennej `first_order`.

Potem z `first_order` pobierz `status`.

Na koncu zrob to samo w jednej linijce przez:

```python
orders[0]["status"]
```
