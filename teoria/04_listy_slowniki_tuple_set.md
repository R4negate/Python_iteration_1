# 04. Listy, slowniki, tuple i sety

## Po co sa struktury danych

Do tej pory mielismy pojedyncze wartosci:

```python
customer_name = "Anna"
total_amount = 129.99
status = "paid"
```

W prawdziwych danych prawie nigdy nie pracujemy tylko na jednej wartosci.

Czesto mamy:

- wiele krajow,
- wiele zamowien,
- wiele klientow,
- jeden rekord z wieloma polami,
- liste rekordow z API.

Do tego sluza struktury danych.

Najwazniejsze na start:

```text
list      wiele elementow
dict      rekord / obiekt / JSON
set       unikalne wartosci
tuple     stala para lub zestaw wartosci
```

## Lista

Lista przechowuje wiele wartosci w okreslonej kolejnosc.

```python
countries = ["PL", "DE", "FR"]
```

Mozesz myslec o liscie jak o kolumnie wartosci albo prostym zbiorze elementow.

```text
index   value
0       PL
1       DE
2       FR
```

Python liczy indeksy od zera.

```python
print(countries[0])
print(countries[1])
print(countries[2])
```

Wynik:

```text
PL
DE
FR
```

Ostatni element:

```python
print(countries[-1])
```

## Dodawanie elementu do listy

```python
countries = ["PL", "DE", "FR"]
countries.append("IT")

print(countries)
```

Wynik:

```text
['PL', 'DE', 'FR', 'IT']
```

## Lista jest mutowalna

Mutowalna oznacza, ze mozna ja zmieniac po utworzeniu.

```python
countries = ["PL", "DE"]
countries.append("FR")

print(countries)
```

Wynik:

```text
['PL', 'DE', 'FR']
```

To rozni liste od tuple, ktora zwykle traktujemy jako staly zestaw wartosci.

## Dlugosc listy

```python
countries = ["PL", "DE", "FR"]
print(len(countries))
```

Wynik:

```text
3
```

## Lista moze zawierac rozne typy, ale zwykle nie powinna

Technicznie Python pozwala zrobic:

```python
mixed = ["PL", 123, True]
```

Ale w kodzie data engineeringowym zwykle chcemy trzymac dane spojnie.

Lepiej:

```python
countries = ["PL", "DE", "FR"]
amounts = [100.0, 200.0, 300.0]
```

## Slownik

Slownik, czyli `dict`, przechowuje pary:

```text
klucz -> wartosc
```

Przyklad:

```python
order = {
    "order_id": 1001,
    "customer_id": 1,
    "total": 129.99,
    "status": "paid",
}
```

To jest bardzo podobne do:

- jednego rekordu,
- jednego wiersza,
- obiektu JSON.

Mozesz myslec tak:

```text
order_id      1001
customer_id   1
total         129.99
status        paid
```

## Pobieranie wartosci ze slownika

Jesli pole jest wymagane, uzywamy `[]`:

```python
print(order["order_id"])
print(order["total"])
```

Jesli klucza nie ma, Python rzuci `KeyError`.

```python
print(order["discount"])
```

To sie wywali, jesli `discount` nie istnieje.

## `.get()`

`.get()` jest bezpieczniejsze dla pol opcjonalnych.

```python
discount = order.get("discount", 0)
print(discount)
```

Jesli `discount` nie istnieje, Python zwroci `0`.

Zasada:

```text
[]      pole wymagane
.get()  pole opcjonalne albo domyslna wartosc
```

## Sprawdzanie, czy klucz istnieje

Mozesz sprawdzic, czy slownik ma dany klucz:

```python
order = {
    "order_id": 1001,
    "total": 129.99,
}

if "total" in order:
    print("total exists")
```

To jest przydatne, gdy chcesz wykonac logike tylko wtedy, gdy pole istnieje.

## `keys()`, `values()`, `items()`

Slownik mozna obejrzec na kilka sposobow.

```python
order = {
    "order_id": 1001,
    "total": 129.99,
    "status": "paid",
}

print(order.keys())
print(order.values())
print(order.items())
```

Znaczenie:

```text
keys()    klucze
values()  wartosci
items()   pary klucz-wartosc
```

## Zmiana wartosci w slowniku

```python
order = {
    "order_id": 1001,
    "status": "new",
}

order["status"] = "paid"

print(order)
```

Mozemy tez dodac nowe pole:

```python
order["country"] = "PL"
```

Slownik jest mutowalny, tak jak lista.

To oznacza, ze mozemy zmieniac wartosci i dodawac nowe pola po utworzeniu slownika.

## Lista slownikow

To jedna z najwazniejszych struktur w podstawach Pythona dla data engineeringu.

```python
orders = [
    {"order_id": 1, "customer_id": 10, "total": 100.0, "status": "paid"},
    {"order_id": 2, "customer_id": 11, "total": 200.0, "status": "cancelled"},
    {"order_id": 3, "customer_id": 10, "total": 300.0, "status": "paid"},
]
```

Czytaj to tak:

```text
lista        = cala tabela
slownik      = jeden wiersz / jeden rekord
klucz        = nazwa kolumny
wartosc      = wartosc w kolumnie
```

Tabela mentalnie:

```text
order_id | customer_id | total | status
1        | 10          | 100   | paid
2        | 11          | 200   | cancelled
3        | 10          | 300   | paid
```

## Pobranie danych z listy slownikow

Pierwsze zamowienie:

```python
first_order = orders[0]
print(first_order)
```

Status pierwszego zamowienia:

```python
print(orders[0]["status"])
```

Suma pierwszego zamowienia:

```python
print(orders[0]["total"])
```

Rozbijmy zapis:

```python
orders[0]["status"]
```

na dwa kroki:

```python
first_order = orders[0]
status = first_order["status"]

print(status)
```

Czytamy:

```text
orders[0]          wez pierwszy slownik z listy
["status"]         z tego slownika wez wartosc pod kluczem status
```

## Set

Set przechowuje unikalne wartosci.

```python
countries = {"PL", "DE", "PL"}
print(countries)
```

Wynik bedzie zawieral unikalne kraje:

```text
{'PL', 'DE'}
```

Kolejnosc w secie nie jest najwazniejsza. Najwazniejsza jest unikalnosc.

Set przydaje sie, gdy chcesz sprawdzic, jakie rozne wartosci wystepuja w danych.

Przyklad:

```python
countries = ["PL", "DE", "PL", "FR", "DE"]
unique_countries = set(countries)

print(unique_countries)
```

## Tuple

Tuple jest podobna do listy, ale jest niemutowalna, czyli po utworzeniu nie zmieniamy jej elementow.

```python
coordinates = (10, 20)
```

Na poczatku tuple nie beda najwazniejsze.

Warto wiedziec, ze czesto uzywa sie ich do malych, stalych zestawow wartosci.

Przyklad:

```python
date_range = ("2026-10-01", "2026-10-31")
```

## Co jest najwazniejsze na start

Na tym etapie najwazniejsze sa:

1. lista,
2. slownik,
3. lista slownikow.

To one beda baza do:

- petli,
- filtrowania,
- liczenia sum,
- mini-pipeline'u,
- pracy z JSON-em.

## Mini-cwiczenie

Masz dane:

```python
order = {
    "order_id": 1001,
    "customer_id": 10,
    "total": 129.99,
    "status": "paid",
}
```

Wypisz:

1. `order_id`,
2. `status`,
3. `discount`, a jesli go nie ma, pokaz `0`.

Potem dodaj do slownika pole:

```text
country = "PL"
```

## Pytania kontrolne

1. Czym rozni sie lista od slownika?
2. Od jakiego indeksu zaczyna Python?
3. Co oznacza `orders[0]`?
4. Co oznacza `order["total"]`?
5. Czym rozni sie `order["discount"]` od `order.get("discount", 0)`?
6. Jak myslimy o liscie slownikow w porownaniu do tabeli?
7. Do czego przydaje sie set?
8. Czym tuple rozni sie od listy?
9. Co oznacza, ze lista albo slownik sa mutowalne?
10. Do czego sluzy `order.items()`?
