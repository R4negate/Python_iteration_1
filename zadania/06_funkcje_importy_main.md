# Zadania 06 - funkcje, importy i main

Kazda funkcja obliczeniowa ma zwracac wynik, nie tylko go wypisywac. Wypisywanie oddziel od transformacji. Korzystaj z lekcji 01-06, bez obslugi wyjatkow i comprehensions. Moduly zapisuj w plikach `.py`; zadania nie wymagaja czytania danych z dysku ani instalowania bibliotek.

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

## Zadanie 15 - Nazwane argumenty i konfiguracja

Napisz `get_order_segment(amount: float, high_threshold: float = 300) -> str`, ktora zwraca high dla kwoty co najmniej progu i standard w przeciwnym razie. Wywolaj ja pozycyjnie, z argumentami nazwanymi w odwrotnej kolejnosci oraz bez podania progu. Sprawdz kwote dokladnie na progu.

## Zadanie 16 - Dwa niezalezne wywolania

Popraw funkcje, zachowujac mozliwosc przekazania istniejacej listy. Brak podanego `target` ma tworzyc nowa liste dla kazdego wywolania. Gdy lista zostala jawnie przekazana, dopisz do niej rekord i zwroc te sama liste.

```python
def add_order(order: dict, target: list = []) -> list:
    target.append(order)
    return target
```

Sprawdz dwa wywolania bez target oraz dwa z jedna wspolna lista. Wypisz wyniki i porownania tozsamosci list.

## Zadanie 17 - Funkcja bez zmiany wejscia

```python
raw_order = {"id": 1, "status": " PAID ", "items": [{"sku": "SQL", "quantity": 2}]}
```

Napisz `normalize_order`, ktora zwraca nowy rekord z oczyszczonym statusem i nowa lista nowych slownikow pozycji. Zmien ilosc w wyniku na 9 i dopisz pozycje. Oryginal ma pozostac niezmieniony. Nie dodawaj pol do `raw_order` wewnatrz funkcji.

## Zadanie 18 - Kryterium sortowania

```python
customers = [
    {"id": 3, "revenue": 100},
    {"id": 1, "revenue": 250},
    {"id": 2, "revenue": 250},
]
```

Napisz nazwana funkcje kryterium i utworz nowa liste klientow posortowana po revenue malejaco, a przy remisie po ID rosnaco. Nie zmieniaj kolejnosci oryginalu. Funkcja kryterium ma zwracac tuple.

## Zadanie 19 - Modul bez skutkow ubocznych

Przenies `normalize_country` i `is_paid` z wczesniejszych zadan do `transformations.py`. W `main.py` przygotuj przykladowe dane i wypisz wyniki ich przetworzenia w funkcji `main`. Sam import `transformations` nie moze uruchamiac raportu ani wypisywac danych. Sprawdz `python main.py` i `python -c "import transformations"` z katalogu zawierajacego oba pliki.

## Zadanie 20 - Trzy poprawne importy

Utworz trzy osobne krotkie skrypty formatujace dzisiejsza date jako tekst ISO: pierwszy przez `import datetime`, drugi przez `from datetime import date`, trzeci przez alias modulu. W kazdym uzyj nazwy zgodnej z wybranym importem. Nie nazywaj wlasnego pliku `datetime.py`.

## Zadanie 21 - Raport w trzech plikach

```python
orders = [
    {"id": 1, "country": " pl ", "amount": 100, "status": " PAID "},
    {"id": 2, "country": "DE", "amount": 80, "status": "pending"},
    {"id": 3, "country": "PL", "amount": 50, "status": "paid"},
]
```

W `transformations.py` umiesc funkcje normalizujaca jeden rekord bez zmiany wejscia. W `metrics.py` funkcje zwracajaca liczbe i sume paid per kraj; tworz grupy tylko dla krajow z paid. W `main.py` polacz etapy, wypisz raport po krajach i dodaj blok startowy. Wszystkie podane pola sa wymagane i poprawne. Uruchom program rowniez przez `python -m main` z katalogu projektu.

## Zadanie 22 - Zaleznosc i wlasny kod

Zbuduj pakiet `reporting` z plikiem `__init__.py` oraz modulem `formatters.py`. W nim umiesc `format_amount(amount: float) -> str`, ktora zwraca kwote z dwoma miejscami i dopiskiem PLN. Wywolaj ja z glownego `main.py`. Projekt ma dzialac bez `pip install`, a import pakietu nie moze sam wypisywac komunikatow.

