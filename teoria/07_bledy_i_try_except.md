# 07. Bledy i try/except

## Blad to informacja

W Pythonie blad nie oznacza, ze "wszystko jest zepsute".

Blad jest informacja:

```text
co sie stalo
w ktorym pliku
w ktorej linii
jakiego typu jest problem
```

Poczatkujacy czesto widza czerwony tekst i od razu sie stresuja.

W praktyce data engineera czytanie bledow to codzienna umiejetnosc.

## Traceback

Traceback to komunikat, ktory Python pokazuje, gdy program sie wywali.

Przyklad:

```python
order = {
    "order_id": 1001,
    "status": "paid",
}

print(order["total"])
```

Program sie wywali, bo w slowniku nie ma klucza `total`.

Na dole tracebacka zobaczysz cos w stylu:

```text
KeyError: 'total'
```

Najlepsza zasada:

```text
traceback czytaj od dolu
```

Na dole zwykle jest typ bledu i najwazniejszy komunikat.

Traceback zwykle zawiera:

```text
plik, w ktorym wystapil blad
numer linii
fragment kodu
typ bledu
komunikat bledu
```

Przyklad:

```text
File "main.py", line 5, in <module>
    print(order["total"])
KeyError: 'total'
```

Czytamy:

```text
w pliku main.py
w linii 5
Python probowal wykonac print(order["total"])
problem to KeyError: 'total'
```

## Najczestsze typy bledow

| Blad | Co oznacza | Przyklad |
|---|---|---|
| `NameError` | nazwa nie istnieje | literowka w nazwie zmiennej |
| `TypeError` | zly typ danych | dodawanie tekstu do liczby |
| `ValueError` | wartosc ma zly format | `float("abc")` |
| `KeyError` | brak klucza w slowniku | `order["total"]` gdy nie ma `total` |
| `IndexError` | brak elementu na indeksie listy | `orders[10]` przy 3 elementach |
| `FileNotFoundError` | plik nie istnieje | zla sciezka do pliku |
| `ZeroDivisionError` | dzielenie przez zero | `10 / 0` |

## `NameError`

```python
customer_name = "Anna"

print(custumer_name)
```

Tu jest literowka: `custumer_name` zamiast `customer_name`.

Python powie, ze taka nazwa nie istnieje.

## `TypeError`

```python
amount = 100
message = "Total: " + amount
```

Python nie chce polaczyc tekstu i liczby przez `+`.

Poprawnie:

```python
amount = 100
message = "Total: " + str(amount)
```

Albo lepiej:

```python
message = f"Total: {amount}"
```

## `ValueError`

```python
amount = float("abc")
```

Python wie, ze chcesz zrobic liczbe, ale `"abc"` nie ma formatu liczby.

To jest czesty blad przy danych z plikow i API.

## `KeyError`

```python
order = {
    "order_id": 1001,
    "status": "paid",
}

print(order["total"])
```

W slowniku nie ma klucza `total`.

Jesli pole jest opcjonalne, mozna uzyc:

```python
print(order.get("total", 0))
```

Jesli pole jest wymagane, lepiej nie ukrywac bledu.

## `IndexError`

```python
countries = ["PL", "DE"]

print(countries[5])
```

Lista ma tylko indeksy `0` i `1`.

Indeks `5` nie istnieje.

## `ZeroDivisionError`

```python
result = 10 / 0
```

Nie da sie dzielic przez zero.

Python pokaze:

```text
ZeroDivisionError: division by zero
```

## `try / except`

`try / except` pozwala obsluzyc blad, ktorego sie spodziewamy.

Przyklad:

```python
raw_amount = "129.99"

try:
    amount = float(raw_amount)
except ValueError:
    amount = 0

print(amount)
```

Czytamy:

```text
sprobuj zamienic raw_amount na float
jesli pojawi sie ValueError, ustaw amount = 0
```

## Kiedy uzywac `try / except`

Uzywaj, gdy:

- dane moga miec zly format,
- plik moze nie istniec,
- request do API moze sie nie udac,
- chcesz dac kontrolowany komunikat bledu.

Nie uzywaj `try / except`, zeby ukryc kazdy problem.

## Zly `except`

Zle:

```python
try:
    amount = float(raw_amount)
except Exception:
    amount = 0
```

Dlaczego zle?

Bo `Exception` lapie prawie wszystko. Mozesz ukryc blad, ktory powinienes zobaczyc.

Lepiej:

```python
try:
    amount = float(raw_amount)
except ValueError:
    amount = 0
```

Lap konkretny blad, ktorego sie spodziewasz.

## `except ... as exc`

Czasem chcemy zobaczyc albo wypisac komunikat bledu.

```python
raw_amount = "abc"

try:
    amount = float(raw_amount)
except ValueError as exc:
    print(f"Cannot parse amount: {exc}")
```

`exc` to obiekt bledu. Na tym etapie wystarczy wiedziec, ze mozemy go wypisac w komunikacie.

## `try / except` w petli

W data engineeringu czesto przetwarzamy wiele rekordow.

Czasem jeden rekord jest bledny, ale nie chcemy zatrzymac calej petli.

```python
values = ["100", "abc", "250"]

for value in values:
    try:
        amount = float(value)
        print(amount)
    except ValueError:
        print(f"Cannot parse value: {value}")
```

Wynik:

```text
100.0
Cannot parse value: abc
250.0
```

Program nie zatrzymal sie na `"abc"`, tylko przeszedl dalej.

## Kiedy nie uzywac `try / except`

Nie uzywaj `try / except`, zeby ukryc literowki albo bledy w kodzie.

Zle:

```python
try:
    print(custumer_name)
except Exception:
    print("something went wrong")
```

Tu problemem jest literowka w nazwie zmiennej. Taki blad lepiej poprawic, a nie ukrywac.

## `raise`

Czasem nie chcemy naprawiac bledu.

Czasem chcemy zatrzymac program, bo dane sa niepoprawne.

```python
def validate_order(order: dict) -> None:
    if "order_id" not in order:
        raise ValueError("Order is missing order_id")
```

Czytamy:

```text
jesli zamowienie nie ma order_id, przerwij program i pokaz jasny blad
```

To jest dobre, gdy pole jest wymagane.

## Walidacja danych

Przyklad:

```python
def validate_order(order: dict) -> None:
    if "order_id" not in order:
        raise ValueError("Order is missing order_id")

    if "total" not in order:
        raise ValueError("Order is missing total")
```

Potem:

```python
order = {
    "order_id": 1001,
    "status": "paid",
}

validate_order(order)
```

Program zatrzyma sie z jasnym komunikatem.

## Mini-cwiczenie

Napisz funkcje:

```python
parse_amount(raw_amount: str) -> float
```

Funkcja ma:

1. probowac zamienic tekst na `float`,
2. jesli tekst ma zly format, zwrocic `0`.

Szkielet:

```python
def parse_amount(raw_amount: str) -> float:
    try:
        ...
    except ...:
        ...


print(parse_amount("129.99"))
print(parse_amount("abc"))
```

## Najwazniejsze zasady

1. Traceback czytaj od dolu.
2. Typ bledu duzo mowi o problemie.
3. `KeyError` oznacza brak klucza w slowniku.
4. `ValueError` czesto oznacza zly format danych.
5. `try / except` sluzy do obslugi spodziewanych bledow.
6. Nie lap `Exception` bez potrzeby.
7. `except ValueError as exc` pozwala uzyc komunikatu bledu.
8. `try / except` w petli pozwala pominac bledny rekord i isc dalej.
9. `raise` sluzy do jawnego zatrzymania programu z komunikatem.

## Pytania kontrolne

1. Od ktorej czesci tracebacka najlepiej zaczac czytanie?
2. Co oznacza `KeyError`?
3. Co oznacza `ValueError`?
4. Czym rozni sie `try / except` od `raise`?
5. Dlaczego nie warto zawsze pisac `except Exception`?
6. Kiedy lepiej uzyc `.get()`, a kiedy `raise`?
7. Co daje zapis `except ValueError as exc`?
8. Kiedy nie warto uzywac `try / except`?
