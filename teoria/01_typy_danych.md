# 01. Typy danych w Pythonie

## Po co zaczynamy od typow danych

Python pracuje na wartosciach.

Kazda wartosc ma jakis typ:

```python
"Anna"      # tekst
123         # liczba calkowita
129.99      # liczba dziesietna
True        # prawda
None        # brak wartosci
```

Typ danych mowi Pythonowi, co mozna z dana wartoscia zrobic.

Przyklad:

```python
print(10 + 20)
```

Wynik:

```text
30
```

Ale:

```python
print("10" + "20")
```

Wynik:

```text
1020
```

Dlaczego?

Bo `10` i `20` to liczby, a `"10"` i `"20"` to teksty.

To jest jedna z najwazniejszych rzeczy na start:

```text
wartosc moze wygladac jak liczba, ale jesli jest w cudzyslowie, to jest tekstem
```

## Dwie grupy typow

Na tej lekcji podzielimy typy na dwie grupy:

```text
typy podstawowe:
str, int, float, bool, None

typy zlozone / kolekcje:
list, tuple, dict, set
```

Typy podstawowe przechowuja pojedyncze wartosci.

Kolekcje przechowuja wiele wartosci albo bardziej zlozone struktury.

## Zmienna i typ

Zmienna to nazwa przypisana do wartosci.

```python
customer_name = "Anna"
orders_count = 3
total_amount = 129.99
```

Typ ma wartosc, nie sama nazwa zmiennej.

```python
customer_name = "Anna"  # str
orders_count = 3        # int
total_amount = 129.99   # float
```

Mozesz sprawdzic typ przez `type()`:

```python
print(type(customer_name))
print(type(orders_count))
print(type(total_amount))
```

`type()` jest przydatne, gdy wynik programu jest dziwny.

Przyklad:

```python
amount = "129.99"

print(type(amount))
```

Wynik:

```text
<class 'str'>
```

Czyli `amount` wyglada jak liczba, ale nadal jest tekstem.

## Typ podstawowy: `str`

`str` to tekst.

Tekst zapisujemy w cudzyslowie:

```python
customer_name = "Anna Kowalska"
country = "PL"
status = "paid"
```

To tez jest tekst:

```python
order_id = "1001"
amount = "129.99"
```

Mimo ze wyglada jak liczba, Python widzi tekst, bo wartosc jest w cudzyslowie.

Stringi sa bardzo wazne w data engineeringu, bo dane z plikow i API czesto przychodza jako tekst.

Przydatne operacje:

```python
country = " pl "

print(country.strip())       # usuwa spacje z poczatku i konca
print(country.upper())       # wielkie litery
print(country.lower())       # male litery
```

## Typ podstawowy: `int`

`int` to liczba calkowita.

```python
orders_count = 10
quantity = 3
customer_id = 1001
```

Na `int` mozemy normalnie liczyc:

```python
quantity = 3
unit_price = 20

line_value = quantity * unit_price
print(line_value)
```

Wynik:

```text
60
```

## Typ podstawowy: `float`

`float` to liczba z czescia dziesietna.

```python
total_amount = 129.99
conversion_rate = 4.25
```

W Pythonie uzywamy kropki:

```python
129.99
```

Nie przecinka:

```python
129,99
```

Na poczatku `float` wystarczy do cwiczen. W prawdziwych systemach finansowych trzeba uwazac na precyzje, ale to temat na pozniej.

## `int` czy `float`

Uzywaj `int`, gdy wartosc jest liczba calkowita:

```python
orders_count = 10
quantity = 3
customer_id = 1001
```

Uzywaj `float`, gdy wartosc ma czesc dziesietna:

```python
unit_price = 19.99
conversion_rate = 4.25
average_order_value = 123.45
```

Najprosciej:

```text
int    ile sztuk / ile rekordow / identyfikator
float  kwota / srednia / procent / przelicznik
```

Uwaga: `float` moze miec drobne problemy z precyzja.

```python
print(0.1 + 0.2)
```

Mozesz zobaczyc wynik podobny do:

```text
0.30000000000000004
```

To jest ten sam typ problemu, ktory wystepuje np. w Javie przy `double`.

Nie jest to blad Pythona ani blad Javy. Wynika to z tego, jak komputery zapisuja liczby zmiennoprzecinkowe.

Komputer przechowuje takie liczby w systemie binarnym. Niektore proste dla nas liczby dziesietne, np. `0.1`, nie maja idealnego, skonczonego zapisu binarnego.

To troche jak z ulamkiem:

```text
1 / 3 = 0.333333333333...
```

W systemie dziesietnym nie da sie zapisac `1 / 3` skonczona liczba cyfr. Podobnie komputer nie potrafi idealnie zapisac wielu liczb dziesietnych w systemie binarnym.

Dlatego:

```python
print(0.1 + 0.2 == 0.3)
```

moze zwrocic:

```text
False
```

Bo po lewej stronie mamy w praktyce cos bardzo bliskiego `0.3`, ale nie dokladnie `0.3`.

## `Decimal` do dokladniejszych liczb

Gdy potrzebujesz dokladniejszej arytmetyki dziesietnej, np. przy pieniadzach, mozesz uzyc `Decimal`.

```python
from decimal import Decimal

amount = Decimal("0.1") + Decimal("0.2")

print(amount)
print(amount == Decimal("0.3"))
```

Wynik:

```text
0.3
True
```

Wazne: przy `Decimal` najlepiej przekazywac liczby jako tekst:

```python
Decimal("0.1")
```

a nie jako `float`:

```python
Decimal(0.1)
```

Dlaczego? Bo `0.1` jako `float` juz wczesniej ma problem z dokladnoscia.

Na tej iteracji najwazniejsze jest:

```text
float    wystarczy do prostych cwiczen i wielu obliczen technicznych
Decimal  lepszy do pieniedzy i dokladnej arytmetyki dziesietnej
```

## Typ podstawowy: `bool`

`bool` przechowuje prawde albo falsz:

```python
True
False
```

Przyklady:

```python
is_paid = True
has_discount = False
is_high_value = total_amount >= 300
```

`bool` jest bardzo wazny przy warunkach `if`.

```python
is_paid = True

if is_paid:
    print("Order is paid")
```

## Typ podstawowy: `None`

`None` oznacza brak wartosci.

To jest podobne mentalnie do `NULL` w SQL.

```python
email = None
```

Sprawdzamy to tak:

```python
if email is None:
    print("missing email")
```

Uzywaj:

```python
is None
```

a nie:

```python
== None
```

## `None`, pusty tekst i zero

Te trzy wartosci oznaczaja co innego:

```python
email = None       # brak wartosci
comment = ""       # pusty tekst
orders_count = 0   # liczba zero
```

`None` oznacza:

```text
nie mamy wartosci
```

Pusty string oznacza:

```text
mamy tekst, ale jest pusty
```

Zero oznacza:

```text
mamy liczbe i ta liczba wynosi 0
```

To rozroznienie jest wazne przy danych.

## Konwersje typow

Czesto dane przychodza jako tekst, ale chcemy na nich liczyc.

```python
raw_quantity = "3"
raw_amount = "129.99"
```

Konwersja na liczby:

```python
quantity = int(raw_quantity)
amount = float(raw_amount)
```

Konwersja liczby na tekst:

```python
order_id = 1001
message = "Order ID: " + str(order_id)
```

Albo czytelniej:

```python
message = f"Order ID: {order_id}"
```

## Typ zlozony: `list`

`list` to lista wielu elementow w okreslonej kolejnosci.

```python
countries = ["PL", "DE", "FR"]
```

Python liczy indeksy od zera:

```python
print(countries[0])   # PL
print(countries[1])   # DE
print(countries[2])   # FR
```

Mozesz dodac element:

```python
countries.append("IT")
```

Lista jest mutowalna, czyli mozna ja zmieniac.

Lista jest dobra, gdy masz wiele wartosci:

```python
amounts = [100.0, 200.0, 300.0]
statuses = ["paid", "cancelled", "paid"]
```

## Typ zlozony: `tuple`

`tuple`, czyli krotka, jest podobna do listy, ale zwykle traktujemy ja jako staly zestaw wartosci.

```python
date_range = ("2026-10-01", "2026-10-31")
```

Mozesz pobrac element:

```python
print(date_range[0])
print(date_range[1])
```

Tuple jest niemutowalna, czyli po utworzeniu nie dodajesz do niej normalnie nowych elementow.

Najprosciej:

```text
list  - gdy kolekcja moze sie zmieniac
tuple - gdy zestaw wartosci ma byc staly
```

## Typ zlozony: `dict`

`dict`, czyli slownik, przechowuje pary:

```text
klucz -> wartosc
```

Przyklad:

```python
order = {
    "order_id": 1001,
    "customer_id": 10,
    "total": 129.99,
    "status": "paid",
}
```

Slownik jest jak:

- jeden rekord,
- jeden wiersz,
- jeden obiekt JSON.

Pobieranie wartosci:

```python
print(order["order_id"])
print(order["status"])
```

Jesli klucz moze nie istniec, uzyj `.get()`:

```python
discount = order.get("discount", 0)
print(discount)
```

Zasada:

```text
order["total"]          pole wymagane
order.get("discount")   pole opcjonalne
```

## Wiele rekordow: `list[dict]`

Sam `dict` to jeden rekord.

Jesli chcesz wiele rekordow, najczesciej uzywasz listy slownikow:

```python
orders = [
    {"order_id": 1, "total": 100, "status": "paid"},
    {"order_id": 2, "total": 200, "status": "cancelled"},
    {"order_id": 3, "total": 300, "status": "paid"},
]
```

Mozesz myslec o tym jak o tabeli:

```text
order_id | total | status
1        | 100   | paid
2        | 200   | cancelled
3        | 300   | paid
```

Analogia:

```text
lista        cala tabela
slownik      jeden wiersz
klucz        kolumna
wartosc      wartosc w komorce
```

## Typ zlozony: `set`

`set`, czyli zbior, przechowuje unikalne wartosci.

```python
countries = {"PL", "DE", "PL", "FR"}
print(countries)
```

Wynik bedzie zawieral unikalne kraje:

```python
{"PL", "DE", "FR"}
```

Set jest troche jak `DISTINCT` w SQL.

Przyklad:

```python
countries = ["PL", "DE", "PL", "FR", "DE"]
unique_countries = set(countries)

print(unique_countries)
```

## Jak rozpoznac typ po nawiasach

```python
my_list = ["PL", "DE"]        # list, nawiasy kwadratowe
my_tuple = ("PL", "DE")       # tuple, nawiasy okragle
my_dict = {"country": "PL"}   # dict, klucz -> wartosc
my_set = {"PL", "DE"}         # set, unikalne wartosci
```

Uwaga:

```python
{}
```

tworzy pusty slownik, nie pusty set.

Pusty set tworzymy tak:

```python
empty_set = set()
```

## Szybka sciaga

```text
str    tekst
int    liczba calkowita
float  liczba dziesietna
bool   True / False
None   brak wartosci

list   wiele elementow w kolejnosci
tuple  staly zestaw wartosci
dict   rekord / JSON / klucz-wartosc
set    unikalne wartosci
```
