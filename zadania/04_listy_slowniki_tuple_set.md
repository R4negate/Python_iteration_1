# Zadania 04 - listy, slowniki, tuple i sety

Na tej lekcji cwiczymy struktury danych.

Jeszcze nie musisz uzywac petli. Chodzi o to, zeby recznie zrozumiec:

- czym jest lista,
- czym jest slownik,
- czym jest lista slownikow,
- jak pobierac konkretne wartosci,
- jak uzywac `.get()`,
- jak dodawac elementy do listy,
- jak tworzyc `set` i `tuple`,
- jak zmieniac i kopiowac kolekcje bez przypadkowej zmiany danych zrodlowych.

Kazde zadanie zaczynaj od jego danych. Jesli zadanie odwoluje sie do wczesniejszego, jest to napisane wprost. Nie potrzebujesz funkcji, comprehensions ani petli; do materializacji `zip` mozesz uzyc `list()` lub `dict()`.

## Zadanie 1

Utworz slownik `customer` z polami:

- `customer_id`: `1`,
- `customer_name`: `"Anna Kowalska"`,
- `country`: `"PL"`,
- `email`: `"anna@example.com"`,
- `acquisition_channel`: `"newsletter"`.

Wypisz:

- caly slownik,
- `customer_name`,
- `country`.

## Zadanie 2

Masz slownik:

```python
customer = {
    "customer_id": 1,
    "customer_name": "Anna Kowalska",
    "country": "PL",
}
```

Pobierz pole `email` przez `.get()` tak, aby jesli go nie ma, zwrocic:

```text
missing@example.com
```

Wypisz wynik.

## Zadanie 3

Masz slownik:

```python
order = {
    "order_id": 1001,
    "status": "new",
    "amount": 129.99,
}
```

Zmien `status` na `"paid"`.

Dodaj nowe pole:

```python
"country": "PL"
```

Wypisz caly slownik.

## Zadanie 4

Utworz liste `orders`, ktora zawiera 3 slowniki:

```python
{"order_id": 1001, "customer_id": 1, "status": "paid", "amount": 120.0}
{"order_id": 1002, "customer_id": 1, "status": "cancelled", "amount": 80.0}
{"order_id": 1003, "customer_id": 2, "status": "paid", "amount": 200.0}
```

Wypisz cala liste.

## Zadanie 5

Korzystajac z listy `orders` z zadania 4, wypisz:

- pierwszy rekord,
- `status` drugiego rekordu,
- `amount` trzeciego rekordu,
- `customer_id` pierwszego rekordu.

Nie uzywaj petli.

## Zadanie 6

Dodaj czwarte zamowienie do listy `orders` przez `.append()`:

```python
{"order_id": 1004, "customer_id": 3, "status": "pending", "amount": 50.0}
```

Wypisz:

- cala liste,
- liczbe elementow w liscie przez `len()`.

## Zadanie 7

Masz liste:

```python
countries = ["PL", "DE", "PL", "FR", "DE", "PL"]
```

Stworz z niej `set` o nazwie `unique_countries`.

Wypisz:

- `unique_countries`,
- typ `unique_countries`.

## Zadanie 8

Stworz tuple `date_range`, ktory zawiera:

```text
2026-10-01
2026-10-31
```

Wypisz:

- caly tuple,
- pierwszy element,
- drugi element.

## Zadanie 9

Masz dane:

```python
orders = [
    {"order_id": 1001, "customer": {"customer_id": 1, "name": "Anna"}, "amount": 120.0},
    {"order_id": 1002, "customer": {"customer_id": 2, "name": "Jan"}, "amount": 80.0},
]
```

Wypisz:

- imie klienta z pierwszego zamowienia,
- `customer_id` klienta z drugiego zamowienia,
- kwote drugiego zamowienia.

Nie uzywaj petli.

## Zadanie 10

Masz liste:

```python
countries = ["PL", "DE"]
```

Dodaj do niej `"FR"` i `"IT"`, a potem wypisz cala liste oraz jej dlugosc.

## Zadanie 11

Masz slownik:

```python
order = {
    "order_id": 1001,
    "status": "new",
    "total": 129.99,
}
```

Zrob:

1. zmien `status` na `"paid"`,
2. dodaj nowe pole `country` z wartoscia `"PL"`,
3. wypisz `keys()`,
4. wypisz `values()`,
5. wypisz `items()`.

## Zadanie 12

Masz dane:

```python
orders = [
    {"order_id": 1, "total": 100, "status": "paid"},
    {"order_id": 2, "total": 200, "status": "cancelled"},
]
```

Najpierw pobierz pierwszy rekord do zmiennej `first_order`.

Potem z `first_order` pobierz `status`.

Na koncu zrob to samo w jednej linijce przez:

```python
orders[0]["status"]
```

## Zadanie 13 - Jeden rekord a partia

```python
orders = [{"id": 1}]
batch = [{"id": 2}, {"id": 3}]
```

Przygotuj dwa niezalezne warianty na swiezych kopiach danych. W pierwszym dodaj cala `batch` jako jeden element listy `orders`, w drugim dolacz jej dwa rekordy jako osobne elementy. Wypisz obie listy, ich dlugosci i ostatnie elementy. Nie zmieniaj `batch`.

## Zadanie 14 - Kolejka do obslugi

```python
queue = [1001, 1002, 1003, 1002]
```

Zdejmij pierwszy element i zapisz go jako `current_id`. Usun pierwsze pozostale wystapienie 1002 po wartosci, a potem usun ostatni element po indeksie. Wypisz `current_id` i koncowa kolejke. Oproznij kolejke i wypisz ja ponownie.

## Zadanie 15 - Probki danych bez zmiany zrodla

```python
order_ids = [10, 20, 30, 40, 50, 60]
```

Zbuduj osobne listy: pierwsze trzy ID, ostatnie dwa ID, co drugie ID od pierwszego oraz ID w odwrotnej kolejnosci. Wypisz je i oryginal. Pobranie pierwszych trzech ma dzialac takze dla pustej listy i listy krotszej niz trzy elementy.

## Zadanie 16 - Sortowanie i jego wynik

```python
amounts = [200, 50, 100, 50]
```

Utworz osobna liste posortowana malejaco, zachowujac `amounts`. Nastepnie posortuj oryginal rosnaco w miejscu, zapisujac wynik wywolania metody do `sort_result`. Wypisz obie listy, `sort_result` i jego typ.

## Zadanie 17 - Aktualizacja rekordu

```python
order = {"id": 1, "status": "new", "debug": True}
changes = {"status": "paid", "country": "PL"}
```

Wprowadz `changes` do `order`. Usun `debug`, zachowujac jego wartosc w `was_debug`. Usun tez opcjonalne pole `temporary_note` tak, by jego brak nie powodowal bledu. Wypisz rekord i `was_debug`.

## Zadanie 18 - Domyslna wartosc nie zastepuje None

```python
missing = {"id": 1}
null_value = {"id": 2, "country": None}
zero_value = {"id": 3, "amount": 0}
```

Pobierz kraj z dwoch pierwszych rekordow z wartoscia domyslna `UNKNOWN` dla brakujacego klucza. Pobierz kwote z trzeciego z domyslnym 99. Zbuduj slownik wynikow i wypisz go bez dodatkowego zastepowania `None` lub zera.

## Zadanie 19 - Kopia listy a kopia rekordu

```python
orders = [{"id": 1, "status": "new"}]
```

Utworz alias listy oraz jej plytka kopie. Do kopii dopisz nowy rekord. Przez kopie zmien status pierwszego rekordu na paid. Wypisz dlugosci trzech list i status pierwszego rekordu w kazdej. Wypisz tez wyniki porownania tozsamosci list oraz ich pierwszych slownikow. To zadanie celowo pokazuje wspoldzielenie danych.

## Zadanie 20 - Niezalezna korekta zagniezdzen

```python
raw_order = {"id": 1, "items": [{"sku": "SQL", "quantity": 2}]}
```

Utworz niezalezna kopie calej struktury. Zmien w niej ilosc na 5 i dopisz druga pozycje. Wypisz oba rekordy; `raw_order` ma nadal zawierac jedna pozycje z iloscia 2.

## Zadanie 21 - Kontrola pol

```python
required = {"id", "amount", "status"}
received = {"id", "amount", "debug"}
```

Zbuduj zbiory `missing_fields`, `unexpected_fields`, `common_fields` i `all_fields`. Wypisz kazdy jako posortowana liste. Nie odejmuj zbiorow w odwrotnej kolejnosci niz wynika z ich znaczenia.

## Zadanie 22 - Aktualizacja zbioru

```python
seen_ids = {1001}
```

Dodaj ponownie 1001, dolacz 1002 i 1003, a potem usun 1002. Sprobuj bez bledu usunac nieobecne 9999. Wypisz wynik w stalej kolejnosci i liczbe unikalnych ID.

## Zadanie 23 - Para wartosci i jeden element

```python
date_range = ("2026-10-01", "2026-10-31")
```

Rozpakuj tuple do `start_date` i `end_date`, zamien te dwie zmienne miejscami bez zmiennej pomocniczej i wypisz je. Osobno utworz tuple z jednym kodem `PL`, wypisz jej dlugosc i typ.

## Zadanie 24 - Naglowek i wiersz eksportu

```python
columns = ["id", "status", "amount"]
values = [1001, "paid", 120]
```

Zbuduj liste par pole-wartosc oraz slownik `row`. Dlugosci maja byc kontrolowane przez `zip(..., strict=True)`. Osobno, na nowych danych z `values = [1001, "paid"]`, uruchom materializacje par i zaobserwuj blad bez jego obslugi. Bledny wariant uruchamiaj oddzielnie, zeby nie zatrzymal poprawnych zadan.
