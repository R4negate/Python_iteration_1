# 05. If, petle i logika

## Po co sa warunki i petle

Do tej pory umielismy zapisac dane:

```python
order = {
    "order_id": 1001,
    "total": 129.99,
    "status": "paid",
}
```

Ale program musi tez umiec podejmowac decyzje:

```text
jesli zamowienie jest oplacone, policz je do sprzedazy
jesli kraj jest pusty, ustaw UNKNOWN
jesli kwota jest wieksza niz 300, oznacz klienta jako high value
```

Do decyzji sluzy `if`.

Program musi tez umiec przejsc po wielu rekordach:

```text
sprawdz kazde zamowienie
policz sume ze wszystkich zamowien
wypisz kazdego klienta
```

Do tego sluzy petla `for`.

## `if`

`if` pozwala wykonac kod tylko wtedy, gdy warunek jest prawdziwy.

```python
total = 150

if total >= 100:
    print("high value")
```

Czytamy:

```text
jesli total jest wiekszy lub rowny 100, wypisz "high value"
```

Wazne: kod wewnatrz `if` jest wcieciem.

```python
if total >= 100:
    print("to jest wewnatrz if")

print("to wykona sie zawsze")
```

## `else`

`else` oznacza: w przeciwnym razie.

```python
total = 80

if total >= 100:
    print("high value")
else:
    print("standard")
```

Czytamy:

```text
jesli total >= 100, pokaz high value
w przeciwnym razie pokaz standard
```

To jest podobne do SQL:

```sql
CASE
    WHEN total >= 100 THEN 'high value'
    ELSE 'standard'
END
```

## `elif`

`elif` oznacza: w przeciwnym razie, jesli...

```python
status = "cancelled"

if status == "paid":
    label = "paid order"
elif status == "cancelled":
    label = "cancelled order"
else:
    label = "other"

print(label)
```

Python sprawdza warunki od gory do dolu.

Gdy pierwszy warunek pasuje, pozostale nie sa juz wykonywane.

## Operatory porownania

| Operator | Znaczenie |
|---|---|
| `==` | rowne |
| `!=` | rozne |
| `>` | wieksze |
| `>=` | wieksze lub rowne |
| `<` | mniejsze |
| `<=` | mniejsze lub rowne |

Przyklady:

```python
total == 100
status != "cancelled"
amount >= 300
```

## Operatory logiczne

Mozemy laczyc warunki.

### `and`

Oba warunki musza byc prawdziwe:

```python
status = "paid"
total = 400

if status == "paid" and total >= 300:
    print("high value paid order")
```

### `or`

Wystarczy jeden prawdziwy warunek:

```python
country = "PL"

if country == "PL" or country == "DE":
    print("core market")
```

### `not`

Odwraca warunek:

```python
is_active = False

if not is_active:
    print("inactive")
```

## `in`

`in` sprawdza, czy wartosc znajduje sie w kolekcji.

```python
country = "PL"
core_countries = ["PL", "DE", "FR"]

if country in core_countries:
    print("core country")
```

To jest czytelniejsze niz:

```python
if country == "PL" or country == "DE" or country == "FR":
    print("core country")
```

## Prawda i falsz bez porownania

Niektore wartosci Python traktuje jak falsz:

```text
None
""
0
[]
{}
```

Przyklad:

```python
email = ""

if email:
    print("email exists")
else:
    print("email is missing")
```

Wynik:

```text
email is missing
```

Na poczatku mozesz pisac warunki bardziej jawnie:

```python
if email != "":
    print("email exists")
```

Ale warto wiedziec, ze w Pythonie pusty tekst jest traktowany jak `False`.

## Petla `for`

Petla `for` przechodzi po elementach kolekcji.

```python
countries = ["PL", "DE", "FR"]

for country in countries:
    print(country)
```

Czytamy:

```text
dla kazdego country z listy countries wypisz country
```

## `range()`

`range()` tworzy zakres liczb, po ktorym mozna przejsc petla.

```python
for number in range(5):
    print(number)
```

Wynik:

```text
0
1
2
3
4
```

Uwaga: `range(5)` daje liczby od `0` do `4`, czyli nie zawiera `5`.

Mozesz tez podac start i koniec:

```python
for number in range(1, 4):
    print(number)
```

Wynik:

```text
1
2
3
```

## `enumerate()`

`enumerate()` daje jednoczesnie indeks i element.

```python
countries = ["PL", "DE", "FR"]

for index, country in enumerate(countries):
    print(index, country)
```

Wynik:

```text
0 PL
1 DE
2 FR
```

To przydaje sie, gdy chcesz wiedziec, ktory element listy aktualnie przetwarzasz.

## Petla po liscie slownikow

To jest bardzo wazny przypadek w data engineeringu.

```python
orders = [
    {"order_id": 1, "total": 100, "status": "paid"},
    {"order_id": 2, "total": 200, "status": "cancelled"},
    {"order_id": 3, "total": 300, "status": "paid"},
]

for order in orders:
    print(order["order_id"])
```

Za kazdym obrotem petli zmienna `order` oznacza jeden slownik, czyli jedno zamowienie.

## Petla po slowniku

Mozesz tez przejsc po parach klucz-wartosc w jednym slowniku.

```python
order = {
    "order_id": 1,
    "total": 100,
    "status": "paid",
}

for key, value in order.items():
    print(key, value)
```

Wynik:

```text
order_id 1
total 100
status paid
```

## Liczenie sumy

W SQL pisalismy:

```sql
SUM(total_amount)
```

W Pythonie na poczatku mozemy policzyc sume petla.

```python
orders = [
    {"order_id": 1, "total": 100, "status": "paid"},
    {"order_id": 2, "total": 200, "status": "cancelled"},
    {"order_id": 3, "total": 300, "status": "paid"},
]

total_revenue = 0

for order in orders:
    total_revenue = total_revenue + order["total"]

print(total_revenue)
```

Krok po kroku:

```text
start: total_revenue = 0
po 1 zamowieniu: 100
po 2 zamowieniu: 300
po 3 zamowieniu: 600
```

## Liczenie tylko zamowien paid

```python
paid_revenue = 0

for order in orders:
    if order["status"] == "paid":
        paid_revenue = paid_revenue + order["total"]

print(paid_revenue)
```

To jest odpowiednik myslenia:

```text
wez tylko rekordy paid i policz sume
```

## Licznik

Mozemy tez liczyc rekordy.

```python
paid_orders_count = 0

for order in orders:
    if order["status"] == "paid":
        paid_orders_count = paid_orders_count + 1

print(paid_orders_count)
```

## `continue`

`continue` pomija obecny element i przechodzi do kolejnego.

```python
for order in orders:
    if order["status"] == "cancelled":
        continue

    print(order)
```

Czytamy:

```text
jesli zamowienie jest cancelled, pomin je
w przeciwnym razie wypisz zamowienie
```

Wazne: po `continue` Python nie wykonuje dalszych linii w aktualnym obrocie petli.

```python
for order in orders:
    if order["status"] == "cancelled":
        continue

    print("this order is not cancelled")
    print(order)
```

## `break`

`break` przerywa cala petle.

```python
for order in orders:
    if order["total"] >= 300:
        print("found high order")
        break
```

Po znalezieniu pierwszego pasujacego rekordu petla sie zatrzyma.

## Mini-cwiczenie

Masz dane:

```python
orders = [
    {"order_id": 1, "total": 100, "status": "paid"},
    {"order_id": 2, "total": 200, "status": "cancelled"},
    {"order_id": 3, "total": 300, "status": "paid"},
]
```

Policz:

1. sume wszystkich zamowien,
2. sume zamowien `paid`,
3. liczbe zamowien `cancelled`.

## Najwazniejsze zasady

1. `if` wykonuje kod tylko wtedy, gdy warunek jest prawdziwy.
2. `else` oznacza "w przeciwnym razie".
3. `elif` pozwala sprawdzic kolejny warunek.
4. `for` przechodzi po elementach kolekcji.
5. Wciecia w Pythonie maja znaczenie.
6. Puste wartosci takie jak `None`, `""`, `0`, `[]` sa traktowane jak falsz.
7. `range()` pozwala przejsc po liczbach.
8. `enumerate()` daje indeks i element.
9. `continue` pomija obecny element.
10. `break` przerywa cala petle.

## Pytania kontrolne

1. Co robi `if`?
2. Czym rozni sie `=` od `==`?
3. Do czego sluzy `elif`?
4. Czym rozni sie `and` od `or`?
5. Co robi `for order in orders`?
6. Po co przed petla ustawiamy `total_revenue = 0`?
7. Czym rozni sie `continue` od `break`?
8. Co daje `range(5)`?
9. Po co uzywamy `enumerate()`?
