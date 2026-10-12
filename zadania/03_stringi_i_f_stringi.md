# Zadania 03 - stringi, czyszczenie tekstu i f-stringi

## Zadanie 1

Masz dane:

```python
raw_country = " pl "
```

Oczysc wartosc tak, aby wynik byl:

```text
PL
```

Uzyj `.strip()` i `.upper()`.

## Zadanie 2

Masz dane:

```python
raw_status = " Paid "
```

Oczysc status tak, aby wynik byl:

```text
paid
```

Uzyj `.strip()` i `.lower()`.

## Zadanie 3

Masz dane:

```python
raw_amount = "129,99"
```

Zamien przecinek na kropke za pomoca `.replace()`.

Nastepnie zamien wynik na `float` i wypisz go.

## Zadanie 4

Masz dane:

```python
email = "ANNA.KOWALSKA@EXAMPLE.COM"
```

Zamien email na male litery.

Sprawdz, czy email zawiera znak `@`.

Wypisz:

- oczyszczony email,
- wynik sprawdzenia.

## Zadanie 5

Masz nazwe pliku:

```python
file_name = "orders_2026_10_12.json"
```

Sprawdz:

1. czy nazwa zaczyna sie od `"orders"`,
2. czy nazwa konczy sie na `".json"`.

Uzyj `.startswith()` i `.endswith()`.

## Zadanie 6

Masz linie tekstu:

```python
line = "1001,paid,129.99"
```

Rozbij ja przez `.split(",")`.

Nastepnie wypisz:

- `order_id`,
- `status`,
- `amount`.

## Zadanie 7

Masz dane:

```python
customer_name = "Anna Kowalska"
orders_count = 3
total_revenue = 249.9
```

Zbuduj komunikat przez f-string:

```text
Klient Anna Kowalska ma 3 zamowienia o wartosci 249.90
```

Kwote pokaz do 2 miejsc po przecinku.

## Zadanie 8

Masz dane:

```python
date = "2026-10-12"
page = 4
source = "orders"
```

Zbuduj sciezke:

```text
data/raw/orders_2026-10-12_page_4.json
```

Uzyj f-stringa.

## Zadanie 9

Masz dane:

```python
raw_country = None
```

Stworz zmienna `country`.

Jesli `raw_country` jest `None`, ustaw:

```text
UNKNOWN
```

W przeciwnym razie oczysc tekst przez `.strip().upper()`.

Uzyj `if / else`.

## Zadanie 10

Sprawdz, ze metody stringow nie zmieniaja oryginalnej zmiennej.

Uruchom:

```python
country = " pl "
country.strip().upper()
print(country)
```

Potem popraw kod tak, zeby wynik byl:

```text
PL
```

## Zadanie 11

Masz dane:

```python
email_1 = None
email_2 = ""
email_3 = "   "
email_4 = " ANNA@EXAMPLE.COM "
```

Dla kazdego emaila wypisz jedna z wartosci:

- `missing`, jezeli wartosc to `None`,
- `empty`, jezeli po `.strip()` tekst jest pusty,
- oczyszczony email malymi literami w pozostalych przypadkach.

## Zadanie 12

Masz dane:

```python
file_name = " orders_2026_10_10.JSON "
```

Oczysc nazwe pliku tak, aby:

- usunac spacje z poczatku i konca,
- zamienic tekst na male litery,
- sprawdzic, czy nazwa zaczyna sie od `orders`,
- sprawdzic, czy nazwa konczy sie na `.json`.
