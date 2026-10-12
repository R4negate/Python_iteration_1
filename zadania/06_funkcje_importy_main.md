# Zadania 06 - funkcje, importy i main

## Zadanie 1

Napisz funkcje:

```python
def normalize_country(country: str) -> str:
    ...
```

Funkcja ma:

- usunac spacje z poczatku i konca tekstu,
- zamienic kraj na wielkie litery,
- zwrocic wynik.

Sprawdz funkcje dla:

```python
" pl "
"de"
" Fr "
```

## Zadanie 2

Napisz funkcje:

```python
def calculate_line_value(quantity: int, unit_price: float) -> float:
    ...
```

Funkcja ma zwrocic wartosc pozycji zamowienia, czyli:

```text
quantity * unit_price
```

Sprawdz funkcje dla `quantity = 3` i `unit_price = 19.99`.

## Zadanie 3

Napisz funkcje:

```python
def is_paid(status: str) -> bool:
    ...
```

Funkcja ma zwrocic `True`, jezeli status po oczyszczeniu ma wartosc `"paid"`.

Przyklady do sprawdzenia:

```python
"paid"
" Paid "
"cancelled"
```

## Zadanie 4

Napisz funkcje:

```python
def get_order_value(order: dict) -> float:
    ...
```

Dane:

```python
order = {
    "order_id": 1001,
    "quantity": 4,
    "unit_price": 25.50,
}
```

Funkcja ma zwrocic wartosc zamowienia na podstawie `quantity` i `unit_price`.

## Zadanie 5

Napisz funkcje:

```python
def build_order_summary(order: dict) -> dict:
    ...
```

Dane:

```python
order = {
    "order_id": 1001,
    "customer_id": 10,
    "quantity": 4,
    "unit_price": 25.50,
    "status": " Paid ",
}
```

Funkcja ma zwrocic slownik:

```python
{
    "order_id": 1001,
    "customer_id": 10,
    "order_value": 102.0,
    "is_paid": True,
}
```

## Zadanie 6

Napisz funkcje:

```python
def get_order_segment(order_value: float) -> str:
    ...
```

Zasady:

- `high`, jezeli `order_value >= 200`,
- `medium`, jezeli `order_value >= 100`,
- `low` w pozostalych przypadkach.

## Zadanie 7

Napisz funkcje:

```python
def transform_order(raw_order: dict) -> dict:
    ...
```

Dane:

```python
raw_order = {
    "id": "1001",
    "country": " pl ",
    "amount": "250.50",
    "status": " Paid ",
}
```

Funkcja ma zwrocic:

```python
{
    "order_id": 1001,
    "country": "PL",
    "amount": 250.50,
    "status": "paid",
    "segment": "high",
}
```

Wykorzystaj funkcje pomocnicze tam, gdzie ma to sens.

## Zadanie 8

Utworz funkcje `main()`.

W funkcji `main()`:

1. utworz przykladowy slownik `raw_order`,
2. wywolaj `transform_order`,
3. wypisz wynik.

Na koncu pliku dodaj:

```python
if __name__ == "__main__":
    main()
```

## Zadanie 9

Zaimportuj `date` z modulu `datetime`.

W funkcji `main()` wypisz dzisiejsza date.

Podpowiedz:

```python
from datetime import date
```

## Zadanie 10

Popraw kod:

```python
def calculate_total(quantity: int, unit_price: float) -> None:
    print(quantity * unit_price)


total = calculate_total(2, 50)
print(total + 10)
```

Cel:

- funkcja ma zwracac wynik,
- kod ma wypisac `110`.

## Zadanie 11

Napisz funkcje:

```python
def greet(name: str = "unknown") -> str:
    ...
```

Funkcja ma zwrocic tekst:

```text
Hello <name>
```

Sprawdz:

```python
greet("Anna")
greet()
```

## Zadanie 12

Uruchom kod:

```python
def calculate_total(quantity: int, unit_price: float) -> None:
    total = quantity * unit_price


result = calculate_total(2, 50)
print(result)
```

Dlaczego wynik to `None`?

Popraw funkcje tak, zeby zwracala wynik.

## Zadanie 13

Uruchom kod:

```python
def calculate_total() -> float:
    total = 100
    return total


print(total)
```

Jaki blad dostajesz?

Popraw kod tak, zeby wypisac wynik funkcji.

## Zadanie 14

Rozbij logike na trzy male funkcje:

- `normalize_status(status: str) -> str`,
- `calculate_order_value(quantity: int, unit_price: float) -> float`,
- `build_order_result(order: dict) -> dict`.

Dane:

```python
order = {
    "order_id": 1001,
    "quantity": 3,
    "unit_price": 20,
    "status": " Paid ",
}
```

Wynik ma zawierac:

- `order_id`,
- `status`,
- `order_value`.

