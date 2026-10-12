# Zadania 05 - if i petle

Uzyj danych:

```python
orders = [
    {"order_id": 1, "amount": 100.0, "status": "paid", "country": "PL"},
    {"order_id": 2, "amount": 200.0, "status": "cancelled", "country": "DE"},
    {"order_id": 3, "amount": 300.0, "status": "paid", "country": "PL"},
    {"order_id": 4, "amount": 50.0, "status": "pending", "country": "FR"},
    {"order_id": 5, "amount": 500.0, "status": "paid", "country": "DE"},
]
```

## Zadanie 1

Przejdz petla po `orders` i wypisz `order_id` kazdego zamowienia.

## Zadanie 2

Policz liczbe wszystkich zamowien.

Uzyj zmiennej `orders_count`, ktora startuje od `0`.

## Zadanie 3

Policz liczbe zamowien ze statusem `"paid"`.

Wynik zapisz w zmiennej `paid_orders_count`.

## Zadanie 4

Policz sume `amount` dla wszystkich zamowien.

Wynik zapisz w zmiennej `total_revenue`.

## Zadanie 5

Policz sume `amount` tylko dla zamowien ze statusem `"paid"`.

Wynik zapisz w zmiennej `paid_revenue`.

## Zadanie 6

Stworz liste `paid_orders`, ktora zawiera tylko zamowienia ze statusem `"paid"`.

Uzyj pustej listy i `.append()`.

## Zadanie 7

Stworz liste `high_value_orders`, ktora zawiera tylko zamowienia, gdzie:

```python
amount >= 200
```

## Zadanie 8

Policz, ile zamowien pochodzi z kraju `"PL"`.

Wynik zapisz w zmiennej `pl_orders_count`.

## Zadanie 9

Dla kazdego zamowienia wypisz komunikat:

```text
Order 1 is paid
Order 2 is cancelled
Order 3 is paid
```

Uzyj f-stringa.

## Zadanie 10

Przejdz po zamowieniach i wypisz tylko te, ktore nie sa anulowane.

Uzyj `continue`, zeby pominac zamowienia ze statusem `"cancelled"`.

## Zadanie 11

Przejdz po zamowieniach i zatrzymaj petle po znalezieniu pierwszego zamowienia, gdzie:

```python
amount >= 300
```

Uzyj `break`.

Wypisz znalezione zamowienie.

## Zadanie 12

Przygotuj prosty raport tekstowy.

Policz:

- `orders_count`,
- `paid_orders_count`,
- `cancelled_orders_count`,
- `pending_orders_count`,
- `total_revenue`,
- `paid_revenue`,
- `high_value_orders_count`, gdzie `amount >= 200`.

Na koncu wypisz wszystkie metryki przez f-stringi.

## Zadanie 13

Masz dane:

```python
values = [None, "", 0, [], {}, "PL", 10]
```

Przejdz petla po `values`.

Dla kazdej wartosci wypisz:

- `truthy`, jezeli Python traktuje ja jak prawde,
- `falsy`, jezeli Python traktuje ja jak falsz.

## Zadanie 14

Uzyj `range()`, zeby wypisac liczby od `1` do `5`.

Nastepnie uzyj `enumerate()` dla listy:

```python
countries = ["PL", "DE", "FR"]
```

Wypisz indeks i kraj.

## Zadanie 15

Masz slownik:

```python
order = {
    "order_id": 1001,
    "total": 129.99,
    "status": "paid",
}
```

Uzyj petli po `order.items()`, zeby wypisac kazdy klucz i kazda wartosc.

## Zadanie 16

Masz dane:

```python
orders = [
    {"order_id": 1, "total": 100, "status": "paid"},
    {"order_id": 2, "total": 200, "status": "cancelled"},
    {"order_id": 3, "total": 300, "status": "paid"},
]
```

Przejdz petla po zamowieniach.

Jezeli zamowienie ma status `cancelled`, pomin je przez `continue`.

Dla pozostalych zamowien wypisz `order_id` i `total`.
