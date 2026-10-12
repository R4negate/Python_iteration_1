# Zadania 02 - zmienne, operatory i podstawowa logika

## Zadanie 1

Utworz plik `02_zmienne_operatory_logika.py`.

Utworz zmienne:

- `customer_name = "Anna Kowalska"`,
- `orders_count = 3`,
- `paid_orders_count = 2`,
- `cancelled_orders_count = 1`,
- `total_revenue = 249.90`.

Wypisz wszystkie zmienne.

## Zadanie 2

Masz dane:

```python
quantity = 3
unit_price = 19.99
```

Policz:

- `line_value`, czyli `quantity * unit_price`,
- `line_value_with_tax`, czyli `line_value * 1.23`.

Wypisz oba wyniki.

## Zadanie 3

Utworz zmienna:

```python
orders_count = 0
```

Nastepnie zwieksz ja trzy razy o `1`, uzywajac `orders_count += 1`.

Wypisz wynik.

## Zadanie 4

Masz dane:

```python
status = "paid"
total_amount = 350
country = "PL"
```

Utworz zmienne logiczne:

- `is_paid`, ktora sprawdza, czy status to `"paid"`,
- `is_high_value`, ktora sprawdza, czy `total_amount >= 300`,
- `is_polish_customer`, ktora sprawdza, czy `country == "PL"`.

Wypisz wszystkie trzy zmienne.

## Zadanie 5

Masz dane:

```python
status = "paid"
total_amount = 350
country = "PL"
```

Utworz zmienna `include_in_report`, ktora bedzie `True`, jesli:

- status to `"paid"`,
- kwota jest wieksza lub rowna `300`,
- kraj to `"PL"`.

Uzyj operatora `and`.

## Zadanie 6

Masz dane:

```python
country = "DE"
```

Utworz liste:

```python
core_countries = ["PL", "DE", "FR"]
```

Sprawdz, czy `country` znajduje sie w `core_countries`.

Wynik zapisz do zmiennej `is_core_country` i wypisz.

## Zadanie 7

Masz dane:

```python
raw_country = " de "
raw_amount = "250.00"
status = "paid"
```

Zrob:

1. oczysc kraj do postaci `"DE"`,
2. zamien kwote na `float`,
3. sprawdz, czy kraj jest jednym z `PL`, `DE`, `FR`,
4. sprawdz, czy kwota jest wieksza lub rowna `200`,
5. sprawdz, czy status to `"paid"`,
6. stworz zmienna `include_in_report`, ktora laczy te trzy warunki przez `and`.

Wypisz `include_in_report`.

## Zadanie 8

Masz dane:

```python
total_amount = 120
```

Utworz zmienna `order_tier`:

- `"high"`, jesli `total_amount >= 300`,
- `"standard"` w przeciwnym razie.

Uzyj `if / else`.

Wypisz `order_tier`.

## Zadanie 9

Sprawdz kolejnosc dzialan.

Napisz kod, ktory wypisuje:

```python
2 + 3 * 4
(2 + 3) * 4
```

Dopisz komentarz, dlaczego wyniki sa rozne.

## Zadanie 10

Masz dane:

```python
status = "paid"
total_amount = 350
country = "PL"
```

Stworz zmienne:

- `is_paid`,
- `is_high_value`,
- `is_core_country`.

Kazda z nich ma przechowywac `True` albo `False`.

Na koncu stworz `include_in_report`, ktore bedzie `True`, jezeli wszystkie trzy warunki sa prawdziwe.

## Zadanie 11

Masz dane:

```python
status = "paid"
country = "DE"
total_amount = 180
```

Stworz zmienna `include_in_report`, ktora bedzie `True`, jezeli:

- status to `paid`,
- kraj to `PL` albo `DE`,
- kwota jest wieksza lub rowna `100`.

Uzyj nawiasow przy warunku z krajem.
