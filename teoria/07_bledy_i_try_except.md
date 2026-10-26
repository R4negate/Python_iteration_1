# 07. Bledy, wyjatki i try/except

## Po co jest ta lekcja

Nasz program moze dostac zamowienie bez kwoty, tekst `"abc"` zamiast liczby albo `None` zamiast kraju. Nie wystarczy napisac kod, ktory dziala dla jednego idealnego rekordu. Trzeba wiedziec, co zrobic, gdy zalozenia nie sa spelnione.

Wyjatek to sposob zasygnalizowania, ze dana operacja nie moze zakonczyc sie normalnie. Mozemy go przeczytac, obsluzyc w odpowiednim miejscu albo pozwolic, zeby zatrzymal przetwarzanie. Obsluga nie oznacza automatycznie naprawienia danych.

Po lekcji masz umiec rozpoznac problem, dobrac konkretny `except`, odroznic blad rekordu od bledu programu i zebrac poprawne oraz odrzucone zamowienia osobno. Korzystamy z funkcji, petli, slownikow i importow z poprzednich lekcji. Nie tworzymy jeszcze wlasnych klas wyjatkow.

Przyklady w kolejnych sekcjach sa osobnymi demonstracjami. Fragmenty opisane jako celowo bledne uruchamiaj oddzielnie, bo maja pokazac komunikat, a nie zakonczyc sie sukcesem. Pelne demo na koncu mozna uruchomic jako jeden plik.

## 1. Trzy rodzaje problemow

| Problem | Co oznacza | Czy program musi pokazac wyjatek? |
|---|---|---|
| blad skladni | Python nie moze poprawnie odczytac kodu | pojawi sie np. `SyntaxError` |
| wyjatek podczas wykonania | kod jest poprawnie zapisany, ale operacja sie nie udaje | tak, jesli wyjatek nie zostanie obsluzony |
| blad logiczny | kod wykonuje sie, ale liczy nie to, co trzeba | nie |

### Blad skladni: program nie moze wystartowac

Celowo bledny fragment - brakuje dwukropka:

```python
if True
    print("Start")
```

Python zglosi `SyntaxError`. Inne przyklady to niedomkniety nawias albo niepoprawne wciecia (`IndentationError`, nalezacy do rodziny `SyntaxError`). Wskazane miejsce jest miejscem wykrycia problemu; przyczyna moze byc np. w poprzedniej linii.

`try/except` zapisany w tym samym niepoprawnym skladniowo pliku nie naprawi sytuacji: plik musi najpierw dac sie odczytac. `SyntaxError` moze byc przechwytywany przy oddzielnym parsowaniu lub imporcie innego kodu, ale to inny scenariusz, nie sposob na ominiecie brakujacego dwukropka we wlasnym skrypcie.

### Wyjatek podczas wykonania

Celowo bledny fragment:

```python
amount = float("abc")
print("Po konwersji")
```

Skladnia jest poprawna. Dopiero wykonywanie konwersji powoduje `ValueError`. Bez obslugi druga linia nie zostanie wykonana.

### Blad logiczny: brak czerwonego komunikatu

```python
orders = [{"amount": 100}, {"amount": 50}]
total_revenue = 0

for order in orders:
    total_revenue = order["amount"]

print(total_revenue)
```

Wynik to `50`, chociaz oczekujemy `150`. Zamiast dodawac, nadpisujemy sume. Poprawka to `total_revenue += order["amount"]`. `try/except` sam nie rozpozna, ze wynik biznesowy jest zly. Potrzebujemy wymagan, przykladowych oczekiwanych wynikow i testow.

## 2. Jak czytac traceback

Traceback pokazuje sciezke wywolan prowadzacych do nieobsluzonego wyjatku. Nie jest lista kilku niezaleznych awarii.

Celowo bledny fragment:

```python
def get_amount(order: dict):
    return order["amount"]


def main() -> None:
    order = {"order_id": 1001}
    print(get_amount(order))


main()
```

Ostatnia linia komunikatu bedzie wygladac tak:

```text
KeyError: 'amount'
```

Wczesniej zobaczysz wpisy `File ...`, numery linii i nazwy funkcji `main` oraz `get_amount`. Numery zaleza od miejsca wklejenia przykladu. `in <module>` oznacza kod na najwyzszym poziomie pliku, poza cialem funkcji.

Czytaj w tej kolejnosci:

1. Na dole znajdz typ wyjatku i komunikat.
2. Znajdz instrukcje, ktora sie nie udala, tutaj `order["amount"]`.
3. Sprawdz wartosc i typ danych, np. `print(order)` i `print(type(order))` przed problematyczna instrukcja.
4. Cofnij sie po wywolaniach: skad ta wartosc przyszla?

Przy bledach bibliotek sprawdz tez swoje wywolanie, ktore przekazalo dane do biblioteki. Nie poprawiaj losowo ostatniego pliku wymienionego w komunikacie.

## 3. Typ wyjatku a jego komunikat

`ValueError` jest nazwa typu, a `"Amount cannot be negative"` moze byc opisem konkretnego problemu. Wyjatek jest obiektem, podobnie jak liczba czy slownik, tylko o innym przeznaczeniu.

```python
error = ValueError("Amount cannot be negative")

print(type(error).__name__)
print(str(error))
```

Wynik:

```text
ValueError
Amount cannot be negative
```

`type(error)` daje typ obiektu, a jego `__name__` nazwe typu. `str(error)` daje opis. Samo utworzenie obiektu nie przerywa programu; do jego zgloszenia sluzy poznane dalej `raise`. Nie trzeba importowac wbudowanego `ValueError`.

## 4. Najwazniejsze typy wyjatkow

| Wyjatek | Co zwykle oznacza | Przyklad |
|---|---|---|
| `NameError` | brak nazwy w danym miejscu programu | literowka `custumer_name` |
| `TypeError` | nieobslugiwany typ lub niepoprawne wywolanie | `float(None)`, brak argumentu funkcji |
| `ValueError` | typ argumentu pasuje, ale wartosc jest niedopuszczalna | `float("abc")` |
| `KeyError` | brak klucza w slowniku | `order["amount"]` |
| `IndexError` | indeks poza zakresem sekwencji | `orders[5]` dla dwoch zamowien |
| `AttributeError` | obiekt nie ma wskazanego atrybutu lub metody | `None.strip()` |
| `ZeroDivisionError` | dzielenie przez zero | `100 / 0` |
| `ModuleNotFoundError` | nie znaleziono importowanego modulu | brak biblioteki w interpreterze |
| `FileNotFoundError` | nie znaleziono pliku lub elementu sciezki | odczyt nieistniejacego pliku |
| `PermissionError` | system odmowil dostepu | brak uprawnien do zapisu |

Typ pomaga zdiagnozowac sytuacje, ale sam nie rozstrzyga, czy winne sa dane, konfiguracja, czy nasz kod. `KeyError` moze oznaczac niekompletny rekord albo literowke w nazwie klucza.

### `NameError`: popraw nazwe, nie ukrywaj literowki

Celowo bledny fragment:

```python
customer_name = "Anna"
print(custumer_name)
```

Nazwa `custumer_name` nie istnieje. Poprawiamy ja na `customer_name`, zamiast pisac obsluge zwracajaca pusty tekst. Podobny problem powstanie po uzyciu zmiennej lokalnej poza funkcja.

### `TypeError` i `ValueError`: wazna roznica

Uruchom osobno dwa celowo bledne fragmenty:

```python
amount = float(None)
```

```python
amount = float("abc")
```

Pierwszy powoduje `TypeError`: `None` nie jest obslugiwanym tutaj argumentem. Drugi powoduje `ValueError`: tekst jest obslugiwany, ale ten tekst nie opisuje liczby. `except ValueError` nie obsluzy automatycznie `TypeError`.

Inny `TypeError` pojawi sie dla `"Total: " + 100`. Jesli chcemy komunikat, poprawka to `f"Total: {100}"`. Jesli arytmetyke, musimy operowac na liczbach. Nie wybieramy konwersji bez ustalenia zamiaru.

### `KeyError`: brak, `None` i wartosc to rozne sytuacje

```python
orders = [
    {"order_id": 1},
    {"order_id": 2, "amount": None},
    {"order_id": 3, "amount": 0},
]

for order in orders:
    print(order["order_id"], "amount" in order, order.get("amount", "MISSING"))
```

Wynik:

```text
1 False MISSING
2 True None
3 True 0
```

`order["amount"]` dla pierwszego rekordu zglosilby `KeyError`. `.get()` daje wartosc domyslna tylko przy braku klucza, nie przy obecnym `None`. Zapis `order.get("amount") or 0` dodatkowo zaciera roznice miedzy kilkoma wartosciami falszywymi.

Uzywamy `[]`, gdy wymagamy pola, albo jawnie sprawdzamy jego obecnosc. `.get()` jest przydatne dla danych opcjonalnych. Zadna z tych metod sama nie sprawdza poprawnosci kwoty.

### `IndexError` i `AttributeError`

Celowo bledne fragmenty, uruchamiane osobno:

```python
countries = ["PL", "DE"]
print(countries[5])
```

```python
country = None
print(country.strip())
```

Pierwszy to `IndexError`, bo lista nie ma indeksu `5`. Drugi to `AttributeError`, bo `None` nie udostepnia metody `strip`. Nie myl tego z `KeyError`: indeks listy, klucz slownika i metoda obiektu to rozne rzeczy.

Jesli kraj jest opcjonalny, mozemy obsluzyc brak przez `if country is None`. Jesli mial byc wymaganym stringiem, brak moze oznaczac odrzucenie rekordu. Zamiana wszystkiego przez `str(country)` ukrylaby problem, tworzac tekst `"None"`.

### `ZeroDivisionError`: czasami wystarczy `if`

```python
total_revenue = 0
orders_count = 0

if orders_count == 0:
    average_order_value = None
else:
    average_order_value = total_revenue / orders_count

print(average_order_value)
```

Wynik to `None`: ustalilismy, ze brak zamowien oznacza brak sredniej. Bez warunku dzielenie przez zero powodowaloby `ZeroDivisionError`. `try/except` nie jest obowiazkowe, gdy normalny przypadek mozna jasno obsluzyc warunkiem.

### Importy i pliki: inna przyczyna, inna naprawa

Po `ModuleNotFoundError` sprawdz nazwe modulu, strukture projektu i interpreter, zgodnie z lekcja 06. Przy `FileNotFoundError` sprawdz sciezke i istnienie pliku, a przy `PermissionError` uprawnienia. Ponowna instalacja biblioteki nie naprawi zlej sciezki do danych.

Obsluge rzeczywistych plikow rozwiniemy pozniej. Na tej lekcji wystarczy umiec rozpoznac te sytuacje, bez wykonywania operacji na plikach systemowych.

## 5. Rodziny wyjatkow

Wyjatki tworza hierarchie. Nazwa wyzej oznacza szersza rodzine. To uproszczony fragment, nie pelna lista:

```text
BaseException
    Exception
        TypeError
        ValueError
        AttributeError
        NameError
        LookupError
            KeyError
            IndexError
        ArithmeticError
            ZeroDivisionError
        OSError
            FileNotFoundError
            PermissionError
        ImportError
            ModuleNotFoundError
        SyntaxError
            IndentationError
    KeyboardInterrupt
    SystemExit
```

`except LookupError` przechwytuje m.in. `KeyError` i `IndexError`. `except OSError` obejmuje m.in. problemy plikowe z tabeli. Obsluga szerszej rodziny ma sens tylko wtedy, gdy reakcja pasuje do wszystkich przechwytywanych sytuacji.

`except Exception` obejmuje wiele zwyklych wyjatkow, takze literowki skutkujace `NameError`. Nie przechwytuje `KeyboardInterrupt` ani `SystemExit`. Samo `except:` obejmuje rowniez te sygnaly, dlatego nie jest dobrym domyslnym sposobem obslugi danych. Przerwanie programu przez uzytkownika nie powinno zostac potraktowane jak bledna kwota.

## 6. Jak dziala `try/except`

```python
raw_amount = "abc"

try:
    print("Przed konwersja")
    amount = float(raw_amount)
    print("Po konwersji")
except ValueError as exc:
    print(f"Niepoprawna kwota: {exc}")

print("Dalsza czesc programu")
```

Wynik zawiera `Przed konwersja`, opis bledu i `Dalsza czesc programu`. Nie zawiera `Po konwersji`.

Python wykonuje `try` po kolei. Po wyjatku pomija reszte jego instrukcji i szuka pasujacego `except`. Po obsludze przechodzi za cala konstrukcje, nie wraca do nieudanej konwersji. Jesli nie znajdzie pasujacej obslugi, wyjatek przechodzi do wywolujacego kodu.

`as exc` udostepnia obiekt wyjatku pod umowna nazwa `exc`. Mozesz wybrac inna nazwe. `{exc}` w f-stringu wypisuje opis; `type(exc).__name__` daje typ. Gdy chcesz zachowac informacje po obsludze, zapisz np. `str(exc)` do slownika. Nie korzystaj z nazwy `exc` poza `except`: Python usuwa to powiazanie po zakonczeniu obslugi.

### Kilka osobnych `except`

```python
orders = [{"amount": "10"}, {}, {"amount": None}, {"amount": "abc"}]

for order in orders:
    try:
        amount = float(order["amount"])
    except KeyError:
        print("Brakuje pola amount")
    except TypeError:
        print("Kwota ma nieobslugiwany typ")
    except ValueError:
        print("Niepoprawny zapis kwoty")
    else:
        print(f"Kwota: {amount}")
```

Wynik to kolejno kwota `10.0` i trzy rozne komunikaty. `else` wykonuje sie po normalnym zakonczeniu `try`, tutaj po udanej konwersji. Dla jednego wyjatku wybierany jest pierwszy pasujacy `except`, nie wszystkie.

### Kolejnosc: od szczegolnego do ogolnego

```python
order = {}

try:
    print(order["amount"])
except KeyError:
    print("Brak wymaganego pola")
except LookupError:
    print("Inny problem wyszukania elementu")
```

Wynik: `Brak wymaganego pola`. Gdy zamienisz kolejnosc blokow, `LookupError` przejmie takze `KeyError` i bardziej szczegolna obsluga nie zostanie wybrana.

### Wspolna reakcja na kilka typow

```python
raw_amount = None

try:
    amount = float(raw_amount)
except (TypeError, ValueError) as exc:
    print(f"Nie mozna odczytac kwoty: {type(exc).__name__}")
```

Krotka w nawiasach wymienia typy, na ktore reagujemy identycznie. Nie jest to to samo co `except Exception`: zakres pozostaje jawnie ograniczony.

## 7. Pelna konstrukcja: `else` i `finally`

```python
def show_flow(raw_amount) -> None:
    try:
        print("TRY")
        amount = float(raw_amount)
    except ValueError:
        print("EXCEPT: zly format")
    else:
        print(f"ELSE: kwota {amount}")
    finally:
        print("FINALLY: koniec proby")

    print("ZA KONSTRUKCJA")


show_flow("10")
show_flow("abc")
```

| Wywolanie | Kolejnosc komunikatow |
|---|---|
| `show_flow("10")` | `TRY`, `ELSE`, `FINALLY`, `ZA KONSTRUKCJA` |
| `show_flow("abc")` | `TRY`, `EXCEPT`, `FINALLY`, `ZA KONSTRUKCJA` |
| `show_flow(None)` - sprawdz osobno | `TRY`, `FINALLY`, potem nieobsluzony `TypeError`; bez komunikatu za konstrukcja |

`else` dziala, gdy `try` zakonczylo sie normalnie, bez wyjatku ani wyjscia przez `return`, `break` lub `continue`. Wyjatkow z `else` nie przechwytuja bloki `except` nalezace do tego samego `try`.

`finally` wykonuje sie przy opuszczaniu konstrukcji takze przy wyjatku lub `return`. Sluzy m.in. do porzadkowania zasobow, a nie do uznawania danych za poprawne. Nie daje gwarancji przy naglym zabiciu procesu lub awarii systemu. Do zamykania plikow poznamy pozniej wygodniejsze `with`.

Nie umieszczaj `return` w `finally`: moze zastapic wynik z `try` albo ukryc oczekujacy wyjatek. Wyjatek z samego `finally` tez moze zastapic wczesniejszy problem. W naszych demonstracjach jest tam tylko bezpieczny komunikat.

## 8. `raise`: samodzielne zgloszenie problemu

Python wie, ze nie moze wykonac `float("abc")`. Nie wie jednak, czy sklep dopuszcza ujemna kwote zamowienia. Reguly biznesowe sprawdzamy sami.

```python
def validate_amount(amount: float) -> None:
    if amount < 0:
        raise ValueError("Amount cannot be negative")


try:
    validate_amount(-10)
    print("Kwota zaakceptowana")
except ValueError as exc:
    print(f"Rekord odrzucony: {exc}")
```

`raise` przerywa normalny przebieg biezacej funkcji. Nie zwraca stringa i nie oznacza automatycznie zatrzymania calego programu. Tutaj wywolujacy obsluguje wyjatek. Gdy walidacja przechodzi, funkcja dochodzi do konca i zwraca `None` - sukces oznacza brak wyjatku.

### Ponowne zgloszenie i zachowanie przyczyny

Samo `raise` wewnatrz `except` ponownie zglasza biezacy wyjatek. Przydaje sie, kiedy dodalismy diagnostyke, ale nie mozemy kontynuowac.

```python
try:
    amount = float("abc")
except ValueError:
    print("Konwersja nie powiodla sie")
    raise
```

To celowo konczy sie nieobsluzonym `ValueError`. Jesli chcemy nadac problemowi wlasny opis i zachowac oryginalna przyczyne, uzywamy `from exc`:

```python
def parse_amount_strict(raw_amount: str) -> float:
    try:
        amount = float(raw_amount)
    except ValueError as exc:
        raise ValueError(f"Invalid amount: {raw_amount!r}") from exc

    return amount
```

`!r` w f-stringu pokazuje reprezentacje wartosci, np. tekst z cudzyslowami, co pomaga zobaczyc pusty string lub spacje. `from exc` laczy nowy wyjatek z pierwotnym; traceback moze pokazac obydwa. To `from` nalezy do instrukcji `raise`, nie do importu.

## 9. Gdzie obsluzyc wyjatek

Funkcja techniczna moze zglosic problem, a funkcja prowadzaca proces zdecydowac, co zrobic z rekordem. Nie kazda funkcja musi miec wlasny `try/except`.

```python
def parse_amount(raw_amount: str) -> float:
    return float(raw_amount)


def transform_order(raw_order: dict) -> dict:
    return {
        "order_id": raw_order["order_id"],
        "amount": parse_amount(raw_order["amount"]),
    }


def main() -> None:
    raw_order = {"order_id": 1, "amount": "abc"}

    try:
        clean_order = transform_order(raw_order)
    except ValueError as exc:
        print(f"Order 1 rejected: {exc}")
    else:
        print(clean_order)


if __name__ == "__main__":
    main()
```

Droga problemu: `float` -> `parse_amount` -> `transform_order` -> obsluga w `main`. To jeden wyjatek przechodzacy wyzej, nie trzy niezalezne bledy. Funkcje przerwane przez wyjatek nie dokoncza swoich instrukcji i nie zwroca normalnego wyniku.

## 10. `try` wewnatrz czy na zewnatrz petli

```python
values = ["10", "abc", "30"]

try:
    for value in values:
        print(float(value))
except ValueError:
    print("Przerwano przetwarzanie partii")

print("Koniec")
```

Wynik: `10.0`, komunikat o przerwaniu i `Koniec`. Wartosc `30` nie zostanie przetworzona, bo wyjatek wyszedl z calej petli do zewnetrznego `except`.

Drugi, osobny wariant:

```python
values = ["10", "abc", "30"]
parsed_values = []
invalid_values = []

for row_number, value in enumerate(values, start=1):
    try:
        amount = float(value)
    except ValueError as exc:
        invalid_values.append({
            "row_number": row_number,
            "raw_value": value,
            "reason": str(exc),
        })
        continue

    parsed_values.append(amount)

print(parsed_values)
print(len(invalid_values))
```

Wynik: `[10.0, 30.0]` i `1`. `continue` nie pozwala dodac wyniku po nieudanej konwersji. Bez niego moglibysmy uzyc starego `amount` z poprzedniego obrotu albo nazwy, ktora jeszcze nie powstala.

`pass` nic nie robi, `continue` przechodzi do kolejnej iteracji, `break` konczy petle, a `return` konczy wywolanie funkcji. Nie sa zamienne.

## 11. Obsluga problemu a ukrycie problemu

| Sytuacja | Przykladowa decyzja |
|---|---|
| brak opcjonalnego kraju | ustaw `UNKNOWN`, jesli tak ustalono |
| poprawna kwota `"0"` | zachowaj zero jako poprawne dane |
| kwota `"abc"` lub brak wymaganej kwoty | odrzuc rekord z powodem |
| brak wspolnej konfiguracji lub niewlasciwa struktura calego wejscia | zatrzymaj proces |
| literowka w kodzie | popraw kod, nie udawaj bledu danych |

Nie zamieniamy niepoprawnej kwoty na zero. Zmieniloby to sumy i uniemozliwilo rozroznienie prawdziwego zera od awarii parsowania. Wartosc domyslna jest poprawna tylko przy jawnej regule biznesowej, np. brak opcjonalnej znizki oznacza brak znizki.

Zakres `try` powinien byc mozliwie maly. `except Exception: pass` ukrywa przyczyne i miejsce awarii. Szersza obsluga moze miec sens na granicy calego procesu, jesli raportuje awarie i ponownie zglasza wyjatek, zamiast oglaszac sukces.

Celowo zla obsluga - zwroc uwage na literowke:

```python
raw_amount = "10"

try:
    amount = float(raw_amout)
except Exception:
    print("Rekord ma niepoprawna kwote")
```

Program wypisze oskarzenie danych, chociaz kwota jest poprawna. Faktyczny problem to `NameError` dla `raw_amout`. Zamiana na `except ValueError` ujawnilaby te literowke zamiast ja ukrywac. Dopiero poprawienie nazwy na `raw_amount` naprawia program.

## 12. Kompletne demo: czyste i odrzucone zamowienia

### Ustalamy kontrakt, zanim napiszemy obsluge

Kontrakt to zasady dotyczace wejscia i wyniku. Wejscie jest lista slownikow. Inna struktura calego wejscia przerywa proces. Nie sprawdzamy tutaj duplikatow identyfikatorow ani nie odczytujemy pliku.

| Pole | Regula |
|---|---|
| `order_id` | wymagany dodatni `int`, nie `bool` i nie tekst |
| `status` | wymagany string; po normalizacji `paid`, `pending` albo `cancelled` |
| `amount` | wymagany niepusty string; po zamianie przecinka na kropke poprawna, skonczona i nieujemna liczba `Decimal` |
| `country` | opcjonalny string lub `None`; brak, `None` i pusty tekst daja `UNKNOWN`; inny typ jest bledem |

Poprawne rekordy trafiaja do `clean_orders`, pozostale do `rejected_orders` z numerem wiersza, identyfikatorem, typem i opisem problemu. Zapisujemy pierwszy wykryty problem rekordu. Nie zmieniamy danych wejsciowych i nie odrzucamy poprawnych zamowien tylko dlatego, ze nie maja statusu `paid`.

`Decimal` znamy z poprzednich lekcji. Niepoprawny zapis, np. `Decimal("abc")`, w standardowym kontekscie zglasza `decimal.InvalidOperation`, a nie `ValueError`. Importujemy ten wyjatek i zamieniamy go na nasz `ValueError` z zachowana przyczyna. Metoda `is_finite()` wyklucza specjalne wartosci `NaN` i `Infinity`, ktore nie sa poprawnymi kwotami tego raportu.

### Kod do uruchomienia w jednym pliku

```python
from decimal import Decimal, InvalidOperation


def parse_amount(raw_amount: str) -> Decimal:
    if not isinstance(raw_amount, str):
        raise TypeError("Amount must be a string")

    normalized = raw_amount.strip().replace(",", ".")
    if normalized == "":
        raise ValueError("Amount cannot be empty")

    try:
        amount = Decimal(normalized)
    except InvalidOperation as exc:
        raise ValueError(f"Invalid amount: {raw_amount!r}") from exc

    if not amount.is_finite():
        raise ValueError("Amount must be finite")
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    return amount


def normalize_country(country) -> str:
    if country is None:
        return "UNKNOWN"
    if not isinstance(country, str):
        raise TypeError("Country must be a string or None")

    return country.strip().upper() or "UNKNOWN"


def transform_order(raw_order: dict) -> dict:
    order_id = raw_order["order_id"]
    if type(order_id) is not int:
        raise TypeError("Order ID must be an integer, not bool or text")
    if order_id <= 0:
        raise ValueError("Order ID must be positive")

    raw_status = raw_order["status"]
    if not isinstance(raw_status, str):
        raise TypeError("Status must be a string")
    status = raw_status.strip().lower()
    if status not in {"paid", "pending", "cancelled"}:
        raise ValueError("Unknown order status")

    amount = parse_amount(raw_order["amount"])
    country = normalize_country(raw_order.get("country"))
    return {
        "order_id": order_id,
        "status": status,
        "amount": amount,
        "country": country,
    }


def process_orders(raw_orders: list[dict]) -> tuple[list[dict], list[dict]]:
    if not isinstance(raw_orders, list):
        raise TypeError("Input must be a list of dictionaries")

    clean_orders = []
    rejected_orders = []

    for row_number, raw_order in enumerate(raw_orders, start=1):
        if not isinstance(raw_order, dict):
            raise TypeError("Each input row must be a dictionary")

        try:
            clean_order = transform_order(raw_order)
        except (KeyError, TypeError, ValueError) as exc:
            rejected_orders.append({
                "row_number": row_number,
                "order_id": raw_order.get("order_id"),
                "error_type": type(exc).__name__,
                "reason": str(exc),
            })
        else:
            clean_orders.append(clean_order)

    return clean_orders, rejected_orders


def main() -> None:
    raw_orders = [
        {"order_id": 1, "status": " PAID ", "amount": "120,50", "country": " pl "},
        {"order_id": 2, "status": "pending", "amount": "80.00", "country": "DE"},
        {"order_id": 3, "status": "paid", "amount": "0", "country": None},
        {"order_id": 4, "status": "paid"},
        {"order_id": 5, "status": "paid", "amount": "abc"},
        {"order_id": 6, "status": "paid", "amount": None},
        {"order_id": 7, "status": "paid", "amount": "-10"},
        {"order_id": 8, "status": "unknown", "amount": "10"},
        {"order_id": 9, "status": "paid", "amount": "NaN"},
        {"order_id": 10, "status": "paid", "amount": "10.00", "country": " "},
    ]

    clean_orders, rejected_orders = process_orders(raw_orders)
    paid_orders_count = 0
    paid_revenue = Decimal("0")

    for order in clean_orders:
        if order["status"] == "paid":
            paid_orders_count += 1
            paid_revenue += order["amount"]

    print(f"Clean: {len(clean_orders)}")
    print(f"Rejected: {len(rejected_orders)}")
    print(f"Paid: {paid_orders_count}")
    print(f"Paid revenue: {paid_revenue:.2f}")

    for rejected in rejected_orders:
        print(rejected["order_id"], rejected["error_type"], rejected["reason"])


if __name__ == "__main__":
    main()
```

`isinstance(wartosc, str)` sprawdza, czy mamy string. Przy identyfikatorze celowo uzywamy dokladnego `type(...) is int`, bo `bool` jest szczegolnym rodzajem `int` w Pythonie, ale `True` nie ma byc poprawnym ID. `or "UNKNOWN"` jest tu dozwolone dopiero po sprawdzeniu, ze kraj jest stringiem: pusty wynik normalizacji oznacza brak kraju.

Zapis `tuple[list[dict], list[dict]]` opisuje zwracana krotke dwoch list. `return clean_orders, rejected_orders` tworzy krotke, a przypisanie w `main` rozpakowuje ja do dwoch nazw. To nie dwa niezalezne `return`.

### Oczekiwany wynik i przejscie po rekordach

Pierwsze cztery linie:

```text
Clean: 4
Rejected: 6
Paid: 3
Paid revenue: 130.50
```

Poprawne identyfikatory to `1`, `2`, `3`, `10`. Rekord `2` jest poprawny, ale nie jest oplacony. Rekord `3` jest oplacony i ma prawdziwe zero, wiec liczy sie do liczby oplaconych zamowien.

| ID | Decyzja | Powod |
|---|---|---|
| 4 | odrzucony, `KeyError` | brak `amount` |
| 5 | odrzucony, `ValueError` | niepoprawny zapis liczby |
| 6 | odrzucony, `TypeError` | `None` zamiast stringa kwoty |
| 7 | odrzucony, `ValueError` | ujemna kwota |
| 8 | odrzucony, `ValueError` | nieznany status |
| 9 | odrzucony, `ValueError` | `NaN` nie jest skonczona kwota |

Warunek sprawdzajacy, czy wiersz jest slownikiem, jest poza rekordowym `try`. Zlamanie struktury wejscia ma wiec przerwac proces, nie produkowac kolejnego odrzucenia. To swiadoma polityka tego cwiczenia. W prawdziwym pipeline taka przerwa nie cofa automatycznie juz wykonanych zapisow do pliku lub bazy.

Obsluga `TypeError` w transformacji ma sens ze wzgledu na jawne kontrole typow w tym demo. Nadal moze przechwycic rowniez blad implementacji tego typu, dlatego potrzebujemy testow funkcji. Nie udajemy, ze dowolny przechwycony wyjatek na pewno oznacza blad danych.

## 13. Cwiczenia po lekcji

1. Dla `float("abc")`, `float(None)`, `{}["amount"]` oraz `None.strip()` napisz cztery osobne obslugi wypisujace typ i opis problemu. Uruchom wszystkie przypadki w jednym programie.
2. Uruchom `show_flow` dla poprawnej kwoty, zlego formatu i `None`; obsluz wyjatek trzeciego wywolania na zewnatrz funkcji, aby program mogl przejsc dalej.
3. Rozszerz dane koncowego demo o pusty string kwoty, brak ID, kraj liczbowy, `Infinity` i poprawne anulowane zamowienie. Nie zmieniaj kontraktu.
4. Zbuduj `rejections_by_type`, czyli slownik liczby odrzucen per `error_type`, na podstawie `rejected_orders`.
5. Przenies funkcje koncowego demo do `order_processing.py`, a `main` do `app.py`. Import modulu pomocniczego nie moze uruchamiac raportu.

## Najwazniejsze zasady

1. Poprawna skladnia i brak wyjatku nie gwarantuja poprawnego wyniku.
2. Rozpoznawaj typ, komunikat i miejsce powstania problemu.
3. Lap konkretne wyjatki i ustawiaj szczegolne obslugi przed ogolnymi.
4. Po obsludze nie wracamy automatycznie do instrukcji, ktora sie nie udala.
5. `else` dotyczy normalnego zakonczenia `try`, a `finally` porzadkowania przy wyjsciu.
6. `raise` zglasza problem; dopiero brak obslugi wyzej moze zatrzymac program.
7. Niepoprawna kwota nie jest zerem. Zachowaj informacje o odrzuceniu.
8. Obsluga jednego rekordu i zatrzymanie calej partii to rozne decyzje.
9. `.get()`, `pass`, `continue` ani szeroki `except` nie zastepuja walidacji.

## Pytania kontrolne

1. Czym roznia sie blad skladni, wyjatek podczas wykonania i blad logiczny?
2. Dlaczego `float(None)` i `float("abc")` zglaszaja rozne typy?
3. Czy `.get("amount", 0)` zamieni obecne `None` na zero?
4. Dlaczego `except LookupError` przechwytuje `KeyError`?
5. Dlaczego kolejnosc blokow `except` ma znaczenie?
6. Czym roznia sie `else` i kod umieszczony po calej konstrukcji?
7. Czy `finally` powoduje, ze nieobsluzony wyjatek znika?
8. Gdzie moze byc obsluzony wyjatek z funkcji wywolanej przez inna funkcje?
9. Kiedy uzywamy samego `raise`, a kiedy `raise ... from exc`?
10. Dlaczego poprawna zerowa kwota musi byc odroznialna od niepoprawnego tekstu?
11. Dlaczego w koncowym demo `Decimal("abc")` nie obslugujemy bezposrednio jako `ValueError`?
12. Jak sprawdzisz, ze wszystkie wejsciowe rekordy zostaly rozliczone jako poprawne albo odrzucone przy poprawnej strukturze wejscia?

## Dokumentacja

- [Bledy, obsluga i przekazywanie wyjatkow](https://docs.python.org/3/tutorial/errors.html)
- [Wbudowane wyjatki i ich hierarchia](https://docs.python.org/3/library/exceptions.html)
- [Decimal: sygnaly, wyjatki i wartosci specjalne](https://docs.python.org/3/library/decimal.html)
