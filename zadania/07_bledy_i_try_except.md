# Zadania 07 - bledy i try/except

Zakres: lekcje 01-07. Odpowiedzia jest kod, nie opis bledu. Celowo bledne fragmenty uruchamiaj osobno. Obsluguj oczekiwane problemy danych konkretnymi typami wyjatkow; nie zamieniaj niepoprawnej wymaganej kwoty na zero.

## Zadanie 1

Uruchom kod:

```python
order = {"order_id": 1001}
print(order["total_amount"])
```

Obsluz brak wymaganego klucza w `except KeyError as exc`. Utworz slownik `error` z `error_type` jako nazwa typu wyjatku i `reason` jako jego komunikat, a potem go wypisz.

## Zadanie 2

Napisz drugi wariant dla pola opcjonalnego `discount`: gdy klucza brakuje, przyjmij 0. Sprawdz tez `{"discount": None}` i `{"discount": 0}`; zachowaj te wartosci bez zamiany. Wymagane `total_amount` z zadania 1 nadal nie moze byc zastepowane zerem.

## Zadanie 3

Uruchom kod:

```python
amount = "129.99"
tax = 23

print(amount + tax)
```

Popraw kod tak, zeby wynik byl liczba.

## Zadanie 4

Napisz funkcje:

```python
def parse_amount(raw_amount: str) -> float:
    ...
```

Funkcja ma zamienic tekst na `float`.

Jesli tekst jest niepoprawny, nie zwracaj zastepczej kwoty: pozwol, aby `ValueError` dotarl do kodu wywolujacego. W petli wywolujacej funkcje zapisuj poprawne liczby do `parsed`, a odrzucone teksty do `rejected` i przechodz dalej.

Sprawdz:

```python
"129.90"
"abc"
""
"0"
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

Zastap stala pare liczb zmiennymi `total_revenue` i `orders_count`. Oblicz srednia, a dla zera zamowien ustaw None bez dzielenia. Sprawdz pary (100, 2) oraz (0, 0).

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

Popraw nazwe zmiennej i jawnie zdefiniuj `customer_name`. Usun obsluge ukrywajaca blad programisty; poprawiony skrypt ma wypisac imie.

## Zadanie 13 - Jeden rekord, rozne przyczyny

```python
orders = [{"id": 1, "amount": "10"}, {"id": 2}, {"id": 3, "amount": None}, {"id": 4, "amount": "abc"}, {"id": 5, "amount": "0"}]
```

Dla kazdego rekordu wykonaj `float(order["amount"])`. W osobnych blokach obsluz KeyError, TypeError i ValueError, zapisujac odrzucenie z `id`, `error_type` i `reason`. Poprawne rekordy zapisz do `clean_orders` w bloku `else`. Kazdy rekord trafia do dokladnie jednej listy, a rekord 5 ma byc poprawny.

## Zadanie 14 - Wspolna reakcja

```python
values = ["10", None, "abc", "0", "20.50"]
```

Przygotuj `parsed` i `rejected` z jedna wspolna obsluga TypeError oraz ValueError. Odrzucenie ma zawierac indeks od 1, surowa wartosc i nazwe rzeczywistego typu wyjatku. Program ma sprawdzic wszystkie elementy.

## Zadanie 15 - Szczegolny wyjatek przed rodzina

```python
def read_value(mode: str):
    if mode == "mapping":
        return {"id": 1}["amount"]
    return [10][5]
```

Wywolaj funkcje dla mapping i list. KeyError obsluz komunikatem `missing_field`, a pozostale LookupError komunikatem `lookup_failed`. W obu przypadkach program ma kontynuowac i wypisac `done`. Nie uzywaj `except Exception`.

## Zadanie 16 - Kolejnosc try, else i finally

Napisz `show_flow(value) -> list[str]`. Funkcja ma zapisac TRY, sprobowac wykonac `float(value)`, przy ValueError dopisac EXCEPT, przy sukcesie ELSE, a w `finally` FINALLY. Liste zwroc po zakonczeniu konstrukcji, bez return w finally. Sprawdz `"10"` i `"abc"`.

## Zadanie 17 - Wlasna regula biznesowa

Napisz `validate_quantity(quantity: int) -> None`. Poprawna ilosc jest dodatnim intem, ale nie boolem. Dla niepoprawnego typu zglos TypeError, a dla zera lub liczby ujemnej ValueError. Sprawdz 2, 0, -1, True i `"2"`, zapisujac wyniki prob w liscie slownikow.

## Zadanie 18 - Przyczyna bledu nie znika

Napisz `parse_amount_strict(raw: str) -> float`. Niepoprawny zapis zamien na ValueError z komunikatem `Invalid amount: <raw>`, zachowujac pierwotny wyjatek jako przyczyne przez `raise ... from ...`. Wywolaj funkcje w skrypcie dla `"abc"` bez przechwytywania na samej gorze, aby zobaczyc lancuch w tracebacku. Ten skrypt uruchamiaj oddzielnie.

## Zadanie 19 - Granica obslugi rekordu

```python
values = ["10", "abc", "20"]
```

Napisz dwa osobne warianty: try obejmujace cala petle oraz try wewnatrz petli. W obu zapisuj poprawne kwoty i odrzucenia. Pierwszy ma zakonczyc przetwarzanie po bledzie, drugi ma dojsc do konca. Wypisz wyniki obu wariantow bez recznego wpisywania koncowych list.

## Zadanie 20 - Pieniadze i osobna lista odrzucen

```python
values = [" 120,50 ", "0", "abc", "", None, "-1"]
```

Zbuduj parser wymagajacy stringa z niepustym zapisem nieujemnej kwoty. W tych danych poprawne zapisy liczbowe zawieraja wylacznie cyfry, opcjonalny minus i separator kropka lub przecinek. Zwracaj Decimal bez przejscia przez float. Niepoprawny typ to TypeError, brak tresci, bledny zapis lub ujemna kwota to ValueError; blad konwersji Decimal obsluz jako InvalidOperation. W petli zachowaj poprawne Decimal i odrzucenia z numerem wiersza oraz powodem. Zero ma zostac zachowane.

