# Zadania 07 - bledy i try/except

## Zadanie 1

Uruchom kod:

```python
order = {"order_id": 1001}
print(order["total_amount"])
```

Jaki blad dostajesz?

Zapisz nazwe bledu i wyjasnij jednym zdaniem, skad sie wzial.

## Zadanie 2

Popraw kod z zadania 1 na wersje z `.get()`, ktora zwraca `0`, jesli `total_amount` nie istnieje.

## Zadanie 3

Uruchom kod:

```python
amount = "129.99"
tax = 23

print(amount + tax)
```

Jaki blad dostajesz?

Popraw kod tak, zeby wynik byl liczba.

## Zadanie 4

Napisz funkcje:

```python
def parse_amount(raw_amount: str) -> float:
    ...
```

Funkcja ma zamienic tekst na `float`.

Jesli tekst jest niepoprawny, funkcja ma zwrocic `0`.

Sprawdz:

```python
"129.90"
"abc"
""
```

## Zadanie 5

Napisz funkcje:

```python
def parse_amount_strict(raw_amount: str) -> float:
    ...
```

Funkcja ma zamienic tekst na `float`.

Jesli tekst jest niepoprawny, funkcja ma rzucic `ValueError` z komunikatem:

```text
Invalid amount
```

## Zadanie 6

Wywolaj `parse_amount_strict` dla listy:

```python
values = ["129.90", "abc", "80"]
```

Uzyj `try / except`, zeby:

- wypisac poprawnie sparsowana kwote,
- dla blednej kwoty wypisac komunikat `Cannot parse amount: abc`.

## Zadanie 7

Napisz funkcje:

```python
def validate_order(order: dict) -> None:
    ...
```

Funkcja ma sprawdzic, czy zamowienie ma pola:

- `order_id`,
- `amount`,
- `status`.

Jesli ktoregos pola brakuje, funkcja ma rzucic `ValueError`.

## Zadanie 8

Masz dane:

```python
orders = [
    {"order_id": 1, "amount": "100", "status": "paid"},
    {"order_id": 2, "status": "paid"},
    {"order_id": 3, "amount": "abc", "status": "cancelled"},
]
```

Przejdz petla po zamowieniach.

Dla kazdego zamowienia:

1. sprawdz, czy ma wymagane pola,
2. sprobuj sparsowac `amount`,
3. wypisz `order_id` i kwote.

Jezeli zamowienie jest bledne, wypisz komunikat bledu i przejdz do kolejnego.

## Zadanie 9

Uruchom kod:

```python
result = 10 / 0
print(result)
```

Jaki blad dostajesz?

Napisz jednym zdaniem, co oznacza.

## Zadanie 10

Masz dane:

```python
raw_amount = "abc"
```

Uzyj `try / except ValueError as exc`, zeby wypisac komunikat:

```text
Cannot parse amount: ...
```

W komunikacie wykorzystaj oryginalny blad `exc`.

## Zadanie 11

Masz liste:

```python
values = ["100", "abc", "250", ""]
```

Przejdz petla po wartosciach.

Dla poprawnych wartosci wypisz liczbe jako `float`.

Dla blednych wypisz:

```text
Cannot parse value: <value>
```

Program ma przejsc przez cala liste mimo bledow.

## Zadanie 12

Masz kod:

```python
try:
    print(custumer_name)
except Exception:
    print("something went wrong")
```

Wyjasnij, dlaczego to jest zly pomysl.

Popraw kod tak, zeby nie ukrywac literowki.

