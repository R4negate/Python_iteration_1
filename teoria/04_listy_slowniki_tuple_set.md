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

## `append` a `extend`: element czy wiele elementow

`append` dodaje jeden obiekt. Jesli tym obiektem jest lista, dodana zostanie cala lista jako jeden zagniezdzony element. `extend` przechodzi po dostarczonych elementach i dopisuje kazdy z nich do listy docelowej.

```python
first = ["PL"]
first.append(["DE", "FR"])

second = ["PL"]
second.extend(["DE", "FR"])

print(first)
print(second)
```

Wyniki to `['PL', ['DE', 'FR']]` i `['PL', 'DE', 'FR']`. Pierwsza lista ma dwa elementy, druga trzy. W pipeline dopisanie jednego slownika zwykle wymaga `append`, a dolaczenie calej partii rekordow `extend`. `extend` na stringu dolacza jego pojedyncze znaki, nie jeden caly tekst.

## Usuwanie elementow: `pop`, `remove`, `del`, `clear`

```python
countries = ["PL", "DE", "FR", "DE"]
last_country = countries.pop()
countries.remove("DE")
del countries[0]

print(last_country)
print(countries)

countries.clear()
print(countries)
```

Wynik to `DE`, `['FR']` i `[]`. `pop()` usuwa i zwraca ostatni element, a `pop(index)` element spod danego indeksu. `remove(value)` usuwa pierwsze wystapienie wartosci. `del` usuwa po indeksie bez zwracania elementu, a `clear()` oproznia liste.

`pop` na pustej liscie powoduje `IndexError`, a `remove` dla nieobecnej wartosci `ValueError`. Nie usuwaj elementow z tej samej listy, po ktorej przechodzisz: przesuwanie indeksow moze powodowac pomijanie rekordow. Bezpieczny sposob filtrowania nowej listy poznamy w lekcji 05, a jego skrocony zapis w 09.

## Wycinki listy

Zapis `start:stop:step` z lekcji o stringach dziala tez na listach. Koniec jest wylaczony.

```python
order_ids = [1001, 1002, 1003, 1004, 1005]
print(order_ids[:2])
print(order_ids[2:])
print(order_ids[::2])
print(order_ids[::-1])
print(order_ids[20:30])
```

Wyniki: `[1001, 1002]`, `[1003, 1004, 1005]`, `[1001, 1003, 1005]`, lista odwrocona i `[]`. Wycinek tworzy nowa liste, ale nie kopiuje automatycznie obiektow w jej srodku. Za chwile sprawdzimy, dlaczego jest to wazne dla listy slownikow.

## Sortowanie: `sorted()` a `.sort()`

```python
amounts = [30, 10, 20]
ordered = sorted(amounts)

print(amounts)
print(ordered)
print(sorted(amounts, reverse=True))

result = amounts.sort()
print(amounts)
print(result)
```

Wyniki to `[30, 10, 20]`, `[10, 20, 30]`, `[30, 20, 10]`, `[10, 20, 30]`, `None`.

`sorted` zwraca nowa liste, a `.sort()` zmienia istniejaca liste i zwraca `None`. Dlatego `amounts = amounts.sort()` zastapiloby nazwe listy wartoscia `None`. Podobnie `append`, `extend`, `remove` i `clear` zmieniaja liste, ale nie zwracaja gotowej listy. `pop` jest inny: zwraca usuniety element.

`reverse=True` oznacza sortowanie malejace. `sorted` moze tez przyjac set, tuple lub slownik; dla slownika bez dodatkowych ustawien sortuje klucze. Nie wszystkie typy daja sie porownac, np. liczby i `None` w jednej liscie wymagaja ustalonej reguly. Sortowanie slownikow po polu `total` omowimy w lekcji 06, gdy poznamy funkcje przekazywane jako `key`.

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

## `update`, `pop` i usuwanie pol slownika

```python
order = {"order_id": 1, "status": "new", "debug": True}
order.update({"status": "paid", "country": "PL"})
removed = order.pop("debug")
missing = order.pop("discount", 0)
del order["country"]

print(order)
print(removed)
print(missing)
```

Wynik to `{'order_id': 1, 'status': 'paid'}`, `True` i `0`. `update` dodaje nowe klucze i nadpisuje istniejace, nie zwraca nowego slownika. Nie laczy automatycznie zagniezdzonych slownikow pole po polu. `pop` usuwa klucz i zwraca wartosc; opcjonalny drugi argument jest wynikiem, gdy klucza brakuje. `del` nie zwraca wartosci i przy braku klucza zglasza `KeyError`. `clear()` oproznia slownik.

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

## Referencje: druga nazwa nie oznacza kopii

Przypisanie wiaze nazwe z obiektem. Nie oznacza automatycznie skopiowania listy lub slownika.

```python
orders = [{"order_id": 1, "status": "new"}]
alias = orders

alias[0]["status"] = "paid"

print(orders[0]["status"])
print(alias is orders)
```

Wynik: `paid` i `True`. Obie nazwy wskazuja na te sama liste, a jej pierwszy element na ten sam slownik. Nie ma drugiego, niezaleznego zbioru danych.

`==` porownuje wartosci, a `is` tozsamosc obiektu. Dwie osobne listy moga byc rowne przez `==`, ale nie byc tym samym obiektem przez `is`. Do porownywania kwot i stringow uzywamy `==`, nie `is`. Zapis `is None` jest poprawnym, typowym sprawdzeniem braku wartosci.

### Kopia plytka: nowy pojemnik, wspolne elementy

```python
orders = [{"order_id": 1, "status": "new"}]
copied = orders.copy()

print(copied is orders)
print(copied[0] is orders[0])

copied.append({"order_id": 2, "status": "new"})
copied[0]["status"] = "paid"

print(len(orders))
print(orders[0]["status"])
```

Wynik: `False`, `True`, `1`, `paid`. Lista zewnetrzna jest nowa, wiec dopisanie drugiego elementu nie zmienia dlugosci oryginalu. Pierwszy slownik nadal jest wspolny, wiec zmiana statusu jest widoczna przez obie listy.

`orders.copy()`, `list(orders)` i `orders[:]` robia tutaj kopie plytka. `.copy()` slownika dziala podobnie: kopiuje zewnetrzny slownik, nie wszystkie obiekty zagniezdzone.

### Zagniezdzone dane i `deepcopy`

```python
from copy import deepcopy

raw_order = {"order_id": 1, "items": [{"quantity": 2}]}
shallow = raw_order.copy()
deep = deepcopy(raw_order)

shallow["items"][0]["quantity"] = 9
deep["items"][0]["quantity"] = 5

print(raw_order["items"][0]["quantity"])
print(deep["items"][0]["quantity"])
```

Wynik: `9` i `5`. `deepcopy` pochodzi z modulu standardowego `copy` i nie wymaga instalacji; importy omowimy dokladnie w 06. Dla takich zagniezdzonych list i slownikow tworzy niezalezna strukture. Moze byc drozsze niz kopia plytka i nie jest uniwersalna instrukcja do kopiowania np. polaczen z baza.

W transformacji czesto lepiej jawnie zbudowac nowy slownik z wybranymi polami i nowa lista pozycji. Wazne jest nie samo uzycie `{...}`, ale tez to, czy do nowego slownika nie wlozylismy tej samej starej listy.

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

Set nie gwarantuje kolejnosci do prezentacji i nie ma indeksow. Najwazniejsza jest unikalnosc. Do uporzadkowanego raportu uzyj np. `sorted(countries)`, zamiast zakladac konkretny porzadek wypisania setu.

Set przydaje sie, gdy chcesz sprawdzic, jakie rozne wartosci wystepuja w danych.

Przyklad:

```python
countries = ["PL", "DE", "PL", "FR", "DE"]
unique_countries = set(countries)

print(unique_countries)
```

### Dodawanie, usuwanie i dzialania na setach

```python
seen_ids = set()
seen_ids.add(1001)
seen_ids.add(1001)
seen_ids.update([1002, 1003])
seen_ids.discard(9999)
seen_ids.remove(1002)

print(sorted(seen_ids))
```

Wynik: `[1001, 1003]`. `add` dodaje jeden element, a `update` elementy z kolekcji. `discard` nie zglasza bledu dla nieobecnego elementu, natomiast `remove` zglosiloby `KeyError`. Pusty set tworzymy przez `set()`, bo `{}` oznacza pusty slownik.

```python
expected = {"order_id", "amount", "status"}
received = {"order_id", "amount", "debug"}

print(sorted(expected - received))
print(sorted(expected & received))
print(sorted(expected | received))
```

Wyniki: brakujace pole `['status']`, wspolne pola `['amount', 'order_id']` i wszystkie rozne pola `['amount', 'debug', 'order_id', 'status']`. Kolejnosc argumentow roznicy ma znaczenie: `expected - received` to nie to samo co `received - expected`.

Elementy setu i klucze slownika musza byc hashowalne, czyli nadawac sie do takiego wyszukiwania wedlug stabilnego skrotu. Typowe dozwolone wartosci to stringi, liczby i tuple z hashowalnych elementow. Lista i slownik sie do tego nie nadaja: nie mozna wlozyc slownika zamowienia do setu. W zbiorze duplikatow zwykle przechowujemy jego ID albo tuple typu `(customer_id, order_id)`, nie caly rekord. Nie trzeba teraz implementowac ani obliczac hasha samodzielnie.

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

Niemutowalnosc dotyczy miejsc tuple, nie kazdego obiektu w jej srodku. Tuple zawierajaca liste nadal pozwala zmienic te liste i nie nadaje sie na klucz slownika. Jednoelementowa tuple wymaga przecinka: `(1001,)`; samo `(1001)` to liczba w nawiasach.

### Rozpakowywanie: kilka wartosci do kilku nazw

```python
product = ("Kurs SQL", "course")
product_name, category = product

print(product_name)
print(category)

first, *middle, last = [1001, 1002, 1003, 1004]
print(first, middle, last)
```

Wyniki: `Kurs SQL`, `course`, `1001 [1002, 1003] 1004`. Rozpakowanie przypisuje kolejne wartosci do kolejnych nazw. `*middle` zbiera pozostale elementy do listy i jest tutaj dodatkiem, nie nowym typem kolekcji. Bez gwiazdki liczba elementow musi zgadzac sie z liczba nazw, inaczej powstanie `ValueError`.

To ten sam mechanizm, ktory wykorzystamy w `for key, value in order.items()`, `enumerate()` i przy odbieraniu kilku wynikow funkcji. Nazwy po lewej nie musza odpowiadac nazwom pol ani elementow w zrodle.

### `zip`: polaczenie elementow wedlug pozycji

```python
columns = ["order_id", "status"]
values = [1001, "paid"]
pairs = list(zip(columns, values))
row = dict(pairs)

print(pairs)
print(row)
```

Wyniki to `[('order_id', 1001), ('status', 'paid')]` oraz `{'order_id': 1001, 'status': 'paid'}`. `zip` dostarcza kolejne tuple: pierwszy element pierwszej kolekcji z pierwszym drugiej itd. `list(...)` materializuje je jako liste. To laczenie wedlug pozycji, nie odpowiednik joina po ID.

Domyslnie `zip` konczy sie wraz z krotsza kolekcja. Nadmiarowe wartosci moga wiec zostac pominiete bez bledu. W Pythonie 3.10+ `zip(columns, values, strict=True)` pozwala wykryc nierowne dlugosci: blad `ValueError` pojawi sie podczas przechodzenia po wyniku, np. w `list(...)`. Obsluge wyjatkow poznamy w 07. Powtorzony klucz przekazany do `dict` tez nie tworzy dwoch rekordow: pozniejsza wartosc nadpisuje wczesniejsza.

## Cwiczenia uzupelniajace o kolekcjach

1. Do listy `[1, 2]` dolacz elementy `[3, 4]` tak, aby wynik byl plaski. Osobno zbuduj wersje, w ktorej `[3, 4]` jest jednym elementem.
2. Z listy ID `[10, 20, 30, 40, 50]` pobierz pierwsze trzy, ostatnie dwa i co drugi element, bez zmiany zrodla.
3. Posortuj kwoty `[80, 20, 50]` malejaco, zachowujac oryginalna kolejnosc listy wejsciowej.
4. Utworz kopie zamowienia z lista pozycji i zmien ilosc w kopii tak, aby oryginal pozostal niezmieniony.
5. Dla setow wymaganych i otrzymanych pol wyznacz osobno brakujace oraz nadmiarowe pola.
6. Rozpakuj tuple katalogowa `("Kurs Python", "course")` do dwoch nazw, a z list nazw kolumn i wartosci zbuduj slownik przez pary z `zip`.

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
11. Czym rozni sie `append` od `extend`?
12. Dlaczego `copied = orders.copy()` nie chroni przed zmiana slownikow w srodku?
13. Czym rozni sie `==` od `is`?
14. Co zwracaja `sorted`, `.sort()` i `.pop()`?
15. Dlaczego `set` nie moze zawierac zwyklych slownikow?
16. Co dzieje sie z nadmiarowymi elementami w domyslnym `zip`?

## Dokumentacja do kolekcji

- [Struktury danych i ich operacje](https://docs.python.org/3/tutorial/datastructures.html)
- [Kopiowanie plytkie i glebokie](https://docs.python.org/3/library/copy.html)
