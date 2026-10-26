# Zadania 05 - if i petle

Zakres: lekcje 01-05. Odpowiedzia jest kod; nie uzywaj jeszcze wlasnych funkcji, comprehensions ani try/except. W zadaniach 1-12 korzystaj ze wspolnej listy ponizej; dalsze zadania maja osobne dane lub jawne odwolanie do tej listy.

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

## Zadanie 17 - Rozlaczne segmenty

Dla wspolnej listy z poczatku pliku zbuduj nowe slowniki z `order_id` i `segment`: high dla kwoty co najmniej 300, medium dla kwoty od 100 wlacznie do 300 wylacznie, low ponizej 100. Kazde zamowienie ma trafic do wyniku dokladnie raz. Nie zmieniaj zrodla.

## Zadanie 18 - Dwa kierunki zakresu

Zbuduj liste liczb od 2 do 12 wlacznie z krokiem 2 oraz liste od 5 do 1 wlacznie malejaco. Osobno wypisz numer wiersza od 1 i `order_id` dla wspolnej listy zamowien. Numer wiersza nie jest identyfikatorem biznesowym.

## Zadanie 19 - Raport per kraj

Dla wspolnej listy przygotuj `by_country`: kluczem jest kraj, wartoscia slownik z `orders_count`, `paid_orders_count` i `paid_revenue`. Uwzglednij kazdy kraj obecny w danych, takze bez paid. Wypisz raport w kolejnosci krajow rosnaco. Dla pustej listy wynik ma byc pustym slownikiem.

## Zadanie 20 - Brak, zero i flaga

```python
orders = [
    {"id": 1, "amount": 0, "approved": True},
    {"id": 2, "amount": None, "approved": True},
    {"id": 3, "approved": True},
    {"id": 4, "amount": 20, "approved": False},
]
```

Utworz `accepted_ids` dla zatwierdzonych zamowien z podana kwota. Kwota jest opcjonalna i ma typ int albo None, a `approved` jest wymaganym boolem. Zero jest poprawne. Zachowaj kolejnosc i nie zmieniaj danych.

## Zadanie 21 - Petla po pozycjach

```python
orders = [
    {"id": 1, "status": "paid", "items": [
        {"sku": "SQL", "quantity": 2, "unit_price": 50},
        {"sku": "PY", "quantity": 1, "unit_price": 80},
    ]},
    {"id": 2, "status": "cancelled", "items": [
        {"sku": "SQL", "quantity": 4, "unit_price": 50},
    ]},
    {"id": 3, "status": "paid", "items": []},
]
```

Zbuduj liste podsumowan kazdego zamowienia z `id`, `units_count` i `order_value`. Puste items daja zera. Osobno przygotuj `paid_by_sku` z suma sztuk i przychodem tylko z paid. Nie doliczaj anulowanych pozycji i nie przenos calej kwoty zamowienia na kazdy produkt.

## Zadanie 22 - Pobieranie partii przez while

```python
batches = [[{"id": 1}, {"id": 2}], [{"id": 3}], [], [{"id": 999}]]
```

Przetwarzaj partie w kolejnosci przez `while`, az trafisz na pierwsza pusta partie lub koniec listy. Utworz plaska liste `collected_ids` oraz licznik niepustych przetworzonych partii. Rekord po pustej partii nie moze trafic do wyniku. Sprawdz tez `batches = []` oraz `batches = [[{"id": 1}]]`.

## Zadanie 23 - Kontynuacja bez zapetlenia

```python
values = [0, -1, 5, -2, 3]
```

Przejdz liste przez `while`, pomijajac liczby ujemne przez `continue`. Utworz `accepted_values` i sume zaakceptowanych liczb. Zero ma zostac zachowane, a indeks ma przesuwac sie rowniez przy pominietych wartosciach. Sprawdz pusta liste.

## Zadanie 24 - Koniec wyszukiwania

```python
orders = [{"id": 1, "amount": 20}, {"id": 2, "amount": 150}, {"id": 3, "amount": 300}]
threshold = 100
```

Znajdz pierwszy rekord z kwota co najmniej `threshold` i przerwij przechodzenie. Gdy nie ma dopasowania, wypisz `not_found` z bloku `else` petli. Sprawdz prog 100, prog 500 oraz pusta liste; wynik znalezienia zapisuj jako rekord lub None.

## Zadanie 25 - Agregaty bez danych

```python
amounts = [100, 0, 250, 50]
```

Zbuduj slownik z `count`, `total`, `minimum`, `maximum` i `average`. Przy pustej liscie licznik i suma wynosza 0, a pozostale metryki None. Rozwiazanie ma dzialac dla podanej listy i `[]`.

## Zadanie 26 - Czy istnieje i czy wszystkie

```python
flags = [True, True, False]
```

Oblicz `has_any_approved` i `all_approved`. Sprawdz tez pusta liste. Nastepnie utworz `can_publish`, ktore jest prawdziwe tylko dla niepustej listy zawierajacej wylacznie True. Nie zmieniaj znaczenia samej funkcji `all` dla pustej kolekcji.

## Zadanie 27 - Limit pracy

```python
queue = [{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}]
limit = 3
```

Przez `while` pobierz najwyzej `limit` kolejnych rekordow do nowej listy, bez zmiany `queue`. Petla ma zakonczyc sie rowniez po wyczerpaniu zrodla. Sprawdz limit 0, 3 i 10; limit jest nieujemnym intem.

## Zadanie 28 - Raport z pierwszym wystapieniem

```python
rows = [
    {"id": 1, "country": " pl ", "amount": "0", "status": " PAID "},
    {"id": 2, "country": None, "amount": "20,50", "status": "paid"},
    {"id": 1, "country": "DE", "amount": "99", "status": "paid"},
    {"id": 3, "amount": "30", "status": "pending"},
]
```

Kazde ID pozostaw tylko przy pierwszym wystapieniu. Zbuduj nowe oczyszczone rekordy z `id`, `country`, `amount` jako float i `status`. Kraj jest opcjonalnym stringiem albo None; brak, None i pusty tekst daja UNKNOWN. Pozostale pola sa wymagane, a kwoty maja poprawny nieujemny zapis z kropka lub przecinkiem. Utworz liste powtorzonych ID oraz podsumowanie paid per kraj z liczba i suma. Nie zmieniaj `rows` i zachowaj poprawne paid z zerowa kwota.
