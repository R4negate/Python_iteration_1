# Zadania 01 - typy danych

## Zadanie 1

Utworz plik `01_typy_danych.py`.

Utworz zmienne:

- `customer_name` z tekstem `"Anna Kowalska"`,
- `orders_count` z liczba `3`,
- `total_amount` z liczba `249.90`,
- `is_active` z wartoscia `True`,
- `email` z wartoscia `None`.

Wypisz wartosc kazdej zmiennej oraz jej typ przez `type()`.

## Zadanie 2

Masz surowe dane:

```python
raw_order_id = "1001"
raw_amount = "129.99"
raw_quantity = "3"
```

Zamien:

- `raw_order_id` na `int`,
- `raw_amount` na `float`,
- `raw_quantity` na `int`.

Nastepnie policz:

```text
amount * quantity
```

Wypisz wynik.

## Zadanie 3

Stworz slownik `order`, ktory opisuje jedno zamowienie.

Slownik ma miec pola:

- `order_id`: `1001`,
- `customer_id`: `10`,
- `country`: `" pl "`,
- `amount`: `"129.99"`,
- `status`: `"paid"`.

Nastepnie:

1. wypisz `order_id`,
2. wypisz `status`,
3. pobierz `country`, oczysc go do postaci `"PL"` i wypisz,
4. pobierz `amount`, zamien na `float` i wypisz.

## Zadanie 4

Masz slownik:

```python
order = {
    "order_id": 1001,
    "customer_id": 10,
    "amount": 129.99,
    "status": "paid",
}
```

Pobierz pole `discount` tak, aby jesli go nie ma, Python zwrocil `0`.

Wypisz wynik.

## Zadanie 5

Stworz liste `orders`, w ktorej kazdy element jest slownikiem.

Lista ma zawierac 3 zamowienia:

```python
{"order_id": 1, "amount": 100.0, "status": "paid"}
{"order_id": 2, "amount": 200.0, "status": "cancelled"}
{"order_id": 3, "amount": 300.0, "status": "paid"}
```

1. wypisz pierwszy rekord,
2. wypisz `status` pierwszego rekordu,
3. wypisz `amount` drugiego rekordu,
4. wypisz `order_id` trzeciego rekordu.

## Zadanie 6

Masz liste krajow:

```python
countries = ["PL", "DE", "PL", "FR", "DE", "PL"]
```

Stworz z niej `set`, czyli zbior unikalnych krajow.

Wypisz wynik oraz typ wyniku.

## Zadanie 7

Stworz `tuple` o nazwie `date_range`, ktory zawiera:

```text
2026-10-01
2026-10-31
```

Wypisz:

1. caly `date_range`,
2. pierwszy element,
3. drugi element,
4. typ `date_range`.

## Zadanie 8

Masz dane:

```python
orders = [
    {"order_id": 1, "country": "PL", "amount": "100.50", "status": "paid"},
    {"order_id": 2, "country": "DE", "amount": "200.00", "status": "cancelled"},
    {"order_id": 3, "country": "FR", "amount": "300.25", "status": "paid"},
]
```

Bez petli:

1. pobierz kwote pierwszego zamowienia i zamien ja na `float`,
2. pobierz kraj drugiego zamowienia,
3. pobierz status trzeciego zamowienia,
4. stworz zmienna `summary`, ktora bedzie tekstem:

```text
First amount: 100.5, second country: DE, third status: paid
```

Uzyj f-stringa.

## Zadanie 9

Masz dane:

```python
raw_order_id = "1001"
raw_quantity = "3"
raw_unit_price = "19.99"
```

Zamien dane na odpowiednie typy:

- `order_id` jako `int`,
- `quantity` jako `int`,
- `unit_price` jako `float`.

Policz `line_value = quantity * unit_price`.

Wypisz wartosci oraz ich typy przez `type()`.

## Zadanie 10

Sprawdz problem precyzji `float`.

Napisz kod, ktory:

1. wypisuje wynik `0.1 + 0.2`,
2. sprawdza, czy `0.1 + 0.2 == 0.3`,
3. robi to samo z uzyciem `Decimal`.

Podpowiedz:

```python
from decimal import Decimal
```

## Zadanie 11

Masz dane:

```python
email_1 = None
email_2 = ""
orders_count = 0
```

Wypisz:

- `email_1 is missing`, jezeli `email_1` to `None`,
- `email_2 is empty`, jezeli `email_2` to pusty tekst,
- `orders_count is zero`, jezeli `orders_count` wynosi `0`.
