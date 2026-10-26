# 06. Funkcje, importy i main

## Po co sa funkcje

Funkcja to nazwany fragment kodu, ktory wykonuje konkretne zadanie.

Bez funkcji kod szybko robi sie dlugi i trudny do utrzymania.

Przyklad bez funkcji:

```python
country = " pl "
country = country.strip().upper()
print(country)

country = " de "
country = country.strip().upper()
print(country)
```

Ten sam pomysl z funkcja:

```python
def normalize_country(country: str) -> str:
    return country.strip().upper()

print(normalize_country(" pl "))
print(normalize_country(" de "))
```

Funkcja pozwala:

- nie powtarzac kodu,
- nazwac logike,
- testowac jeden maly fragment,
- budowac pipeline z krokow,
- latwiej czytac program.

## Definicja funkcji

```python
def normalize_country(country: str) -> str:
    return country.strip().upper()
```

Elementy:

```text
def                 zaczyna definicje funkcji
normalize_country   nazwa funkcji
country             parametr
: str               podpowiedz typu parametru
-> str              podpowiedz typu wyniku
return              zwraca wynik z funkcji
```

## Wywolanie funkcji

Sama definicja funkcji nie uruchamia kodu.

```python
def say_hello() -> None:
    print("Hello")
```

To tylko mowi Pythonowi:

```text
istnieje funkcja say_hello
```

Dopiero to ja uruchamia:

```python
say_hello()
```

## `return`

`return` zwraca wynik z funkcji.

```python
def add(a: int, b: int) -> int:
    return a + b

result = add(10, 20)
print(result)
```

Wynik:

```text
30
```

Jesli funkcja cos liczy albo przeksztalca, zwykle powinna zwrocic wynik przez `return`.

Jesli funkcja nie ma `return`, Python zwraca `None`.

```python
def calculate_total(quantity: int, unit_price: float) -> None:
    total = quantity * unit_price


result = calculate_total(2, 50)
print(result)
```

Wynik:

```text
None
```

## `print` a `return`

To bardzo wazna roznica.

`print()` tylko pokazuje cos na ekranie.

`return` oddaje wartosc do dalszego uzycia.

```python
def show_total(total: float) -> None:
    print(total)

def calculate_total(quantity: int, unit_price: float) -> float:
    return quantity * unit_price
```

Funkcja `show_total` wypisuje wynik.

Funkcja `calculate_total` zwraca wynik, wiec mozemy go zapisac:

```python
line_value = calculate_total(3, 19.99)
```

## Parametry

Parametr to nazwa w definicji funkcji, pod ktora funkcja otrzyma przekazany argument.

```python
def greet(name: str) -> str:
    return f"Hello {name}"

message = greet("Anna")
print(message)
```

W tym wywolaniu:

```python
greet("Anna")
```

wartosc `"Anna"` trafia do parametru `name`.

## Parametr a argument

Te dwa slowa sa podobne, ale oznaczaja troche co innego.

W definicji funkcji mamy parametr:

```python
def greet(name: str) -> str:
    return f"Hello {name}"
```

`name` jest parametrem.

W wywolaniu funkcji przekazujemy argument:

```python
greet("Anna")
```

`"Anna"` jest argumentem.

Najprosciej:

```text
parametr  nazwa w definicji funkcji
argument  konkretna wartosc przekazana przy wywolaniu
```

## Wartosc domyslna parametru

Parametr moze miec wartosc domyslna.

```python
def normalize_country(country: str = "UNKNOWN") -> str:
    return country.strip().upper()


print(normalize_country(" pl "))
print(normalize_country())
```

Drugie wywolanie zadziala, bo `country` ma domyslna wartosc `"UNKNOWN"`.

## Argumenty pozycyjne i nazwane

Argumenty pozycyjne sa przypisywane do parametrow wedlug kolejnosci. Argumenty nazwane jawnie wskazuja parametr po nazwie, dzieki czemu latwiej przeczytac wywolanie i uniknac zamiany podobnych wartosci.

```python
def calculate_line_value(quantity: int, unit_price: float) -> float:
    return quantity * unit_price


print(calculate_line_value(2, 50))
print(calculate_line_value(quantity=2, unit_price=50))
print(calculate_line_value(unit_price=50, quantity=2))
print(calculate_line_value(2, unit_price=50))
```

Kazde wywolanie daje `100`. Nazwy argumentow nazwanych musza odpowiadac parametrom funkcji. W zwyklym wywolaniu argumenty pozycyjne umieszczamy przed nazwanymi. Przekazanie `quantity` jednoczesnie pozycyjnie i po nazwie powoduje `TypeError`, podobnie jak pominiecie wymaganego argumentu lub nieznana nazwa parametru.

## Pulapka mutowalnej wartosci domyslnej

Wartosc domyslna powstaje przy wykonywaniu definicji funkcji, nie na nowo przy kazdym wywolaniu. Liczba lub string zwykle nie sprawia tu klopotu. Lista moze jednak przypadkiem zbierac dane z kilku uruchomien procesu.

Celowo bledna funkcja, jesli oczekujemy osobnej listy dla kazdego wywolania:

```python
def collect_order_id(order_id: int, order_ids: list = []) -> list:
    order_ids.append(order_id)
    return order_ids


print(collect_order_id(1))
print(collect_order_id(2))
```

Wynik: `[1]` i `[1, 2]`. Domyslna lista jest wspoldzielona. Zmienmy umowe na: jesli nie dostarczono listy, utworz nowa wewnatrz funkcji.

```python
def collect_order_id(order_id: int, order_ids: list | None = None) -> list:
    if order_ids is None:
        order_ids = []
    order_ids.append(order_id)
    return order_ids


print(collect_order_id(1))
print(collect_order_id(2))
```

Wynik: `[1]` i `[2]`. `list | None` to podpowiedz "lista albo None", a nie automatyczna konwersja. Uzywamy `is None`, nie `if not order_ids`: jawnie przekazana pusta lista tez moze byc pojemnikiem, ktory wywolujacy chce wypelnic.

Ten sam problem dotyczy domyslnego `{}` lub `set()`. Poprawiona funkcja nadal celowo zmienia liste przekazana argumentem. Jesli kontrakt wymaga braku mutacji takze przy przekazaniu listy, trzeba zbudowac nowa liste lub odpowiednia kopie. Samo `None` w definicji tego nie gwarantuje.

## Funkcja dla zamowienia

Przyklad data engineeringowy:

```python
def calculate_line_value(quantity: int, unit_price: float) -> float:
    return quantity * unit_price

value = calculate_line_value(3, 19.99)
print(value)
```

Inny przyklad:

```python
def normalize_status(status: str) -> str:
    return status.strip().lower()

print(normalize_status(" Paid "))
```

Wynik:

```text
paid
```

## Funkcja przyjmujaca slownik

Czesto funkcja przyjmuje jeden rekord jako slownik.

```python
def get_order_value(order: dict) -> float:
    return order["quantity"] * order["unit_price"]

order = {
    "order_id": 1001,
    "quantity": 3,
    "unit_price": 19.99,
}

print(get_order_value(order))
```

Czytamy:

```text
funkcja get_order_value bierze zamowienie i zwraca wartosc pozycji
```

## Zmienne lokalne

Zmienna utworzona w funkcji zyje tylko w tej funkcji.

```python
def calculate_total() -> float:
    total = 100
    return total


print(total)
```

Ten kod sie wywali, bo `total` istnieje tylko wewnatrz funkcji.

Poprawnie:

```python
def calculate_total() -> float:
    total = 100
    return total


result = calculate_total()
print(result)
```

Wazna zasada:

```text
funkcja dostaje dane przez parametry
funkcja oddaje wynik przez return
```

## Argument listowy lub slownikowy nie jest automatyczna kopia

```python
def mark_paid(order: dict) -> None:
    order["status"] = "paid"


raw_order = {"order_id": 1, "status": "pending"}
mark_paid(raw_order)
print(raw_order["status"])
```

Wynik to `paid`. Parametr wskazal na ten sam slownik. Funkcja nie zwracala rekordu, ale zmienila obiekt widoczny na zewnatrz - to skutek uboczny. Jesli transformacja ma zachowac zrodlo, tworzymy nowy wynik:

```python
def build_paid_order(order: dict) -> dict:
    clean_order = order.copy()
    clean_order["status"] = "paid"
    return clean_order


raw_order = {"order_id": 1, "status": "pending"}
clean_order = build_paid_order(raw_order)
print(raw_order["status"])
print(clean_order["status"])
```

Wynik: `pending` i `paid`. Kopia plytka wystarcza do podmiany prostego statusu. Nie wystarczylaby do bezpiecznej zmiany pozycji w zagniezdzonej liscie `items`; obowiazuja zasady z 04. Samo przypisanie parametrowi nowego slownika, np. `order = {}`, nie podmienia slownika przypisanego do nazwy wywolujacego.

## Funkcja powinna robic jedna rzecz

Lepsza funkcja:

```python
def normalize_status(status: str) -> str:
    return status.strip().lower()
```

Gorsza funkcja:

```python
def do_everything(order: dict) -> None:
    print(order)
    print(order["status"].strip().lower())
    print(order["quantity"] * order["unit_price"])
```

Im mniej rzeczy robi funkcja, tym latwiej ja zrozumiec, przetestowac i uzyc ponownie.

## Type hints

Type hints to podpowiedzi typow.

```python
def calculate_vat(amount: float) -> float:
    return amount * 0.23
```

`amount: float` oznacza:

```text
spodziewamy sie liczby dziesietnej
```

`-> float` oznacza:

```text
funkcja powinna zwrocic liczbe dziesietna
```

Wazne: type hints pomagaja czytac kod, ale same nie zatrzymuja programu.

Python nadal pozwoli wywolac:

```python
calculate_vat("abc")
```

ale program moze sie potem wywalic albo dac bezsensowny wynik.

## Funkcja jako kryterium: `key` w sortowaniu

`sorted(orders)` nie zna biznesowej kolejnosci listy slownikow. Parametr `key` pozwala przekazac funkcje, ktora dla kazdego rekordu zwroci wartosc do porownania. Nie porownuje dwoch rekordow naraz i nie sluzy do filtrowania.

```python
def get_total(order: dict) -> int:
    return order["total"]


orders = [
    {"order_id": 3, "total": 300},
    {"order_id": 1, "total": 100},
    {"order_id": 2, "total": 300},
]
ranked = sorted(orders, key=get_total, reverse=True)
print(ranked)
print(orders)
```

ID w `ranked` to `3`, `2`, `1`, a oryginal zachowuje `3`, `1`, `2`. Przekazujemy `key=get_total`, bez nawiasow: funkcje ma wywolac `sorted` z kazdym rekordem. `key=get_total()` probowaloby wywolac ja od razu, bez wymaganego argumentu.

Sortowanie jest stabilne: dla rownych kwot zachowuje kolejnosc z wejscia. Jesli przy remisie wymagamy ID rosnaco, zwrocmy tuple kryteriow:

```python
def revenue_sort_key(order: dict) -> tuple:
    return (-order["total"], order["order_id"])


orders = [
    {"order_id": 3, "total": 300},
    {"order_id": 1, "total": 100},
    {"order_id": 2, "total": 300},
]
print(sorted(orders, key=revenue_sort_key))
```

Kolejnosc ID to teraz `2`, `3`, `1`. Tuple sa porownywane od pierwszego elementu, a przy remisie od kolejnego. Ujemna kwota daje malejacy przychod przy domyslnym rosnacym sortowaniu, a dodatnie ID pozostaje rosnace. Samo `reverse=True` dla calej tuple odwrociloby takze kolejnosc ID.

Opcjonalny skrot `key=lambda order: order["total"]` tworzy mala funkcje bez nazwy, zwracajaca jedno wyrazenie. `order` jest jej parametrem, a zapis po dwukropku wynikiem; nie dopisujemy `return`. To odpowiednik `get_total`, nie osobna zasada sortowania. Na poczatku preferuj nazwana funkcje, jesli dzieki temu lepiej rozumiesz przeplyw danych.

`min` i `max` tez przyjmuja `key`. `max(orders, key=get_total, default=None)` wybierze rekord z najwieksza kwota, a dla pustej listy `None`. Zwraca caly rekord, nie sama wartosc kryterium. Nowa lista z `sorted` nadal zawiera referencje do starych slownikow; zmiana rekordu w wyniku moze wiec zmienic wejscie.

## Importy i biblioteki: po co nam cudzy kod

Umiemy juz napisac funkcje `normalize_country`. Gdy chcemy uzyc jej w dwoch skryptach, mozemy skopiowac definicje, ale wtedy poprawke trzeba bedzie wprowadzac w kilku miejscach. Lepiej przechowywac funkcje w jednym pliku i korzystac z niej w pozostalych.

Podobnie jest z gotowymi narzedziami. Nie musimy sami pisac obslugi dat, formatu JSON czy liczb `Decimal`. Python udostepnia kod, ktory mozemy wykorzystac.

`import` pozwala uzyskac dostep do modulu lub nazw z modulu w naszym kodzie. Nie pobiera biblioteki z internetu i nie wywoluje automatycznie wszystkich jej funkcji.

### Funkcja, modul, pakiet i biblioteka

| Pojecie | Co oznacza | Przyklad |
|---|---|---|
| Funkcja | nazwany fragment logiki, ktory wywolujemy | `normalize_country(" pl ")` |
| Modul | jednostka kodu, ktora mozna importowac; w naszym projekcie bedzie nia plik `.py` | `order_utils.py` |
| Pakiet | sposob grupowania modulow pod wspolna nazwa | pakiet `commerce` z modulami `cleaning` i `reporting` |
| Biblioteka | ogolne okreslenie zestawu gotowego kodu do jakiegos celu | biblioteka `requests` do komunikacji HTTP |

Modul moze zawierac funkcje, stale, klasy i inne instrukcje. Nie kazda importowana nazwa jest funkcja. Znane juz `Decimal` jest klasa reprezentujaca liczby dziesietne; `Decimal("12.50")` tworzy taka liczbe. Same klasy omowimy dokladniej przy obiektowosci.

Biblioteka nie jest osobna instrukcja ani specjalnym typem pliku w Pythonie. Moze skladac sie z jednego modulu albo wielu pakietow i modulow.

### Trzy zrodla narzedzi i funkcje wbudowane

| Skad pochodzi kod | Przyklady | Czy trzeba go instalowac przez `pip`? |
|---|---|---|
| Biblioteka standardowa, dostarczana z Pythonem | `decimal`, `json`, `datetime`, `pathlib` | nie |
| Biblioteka zewnetrzna | `requests` | tak, jesli nie ma jej w uzywanym srodowisku |
| Wlasny modul projektu | `order_utils.py` | nie, jesli jest dostepny dla importujacego programu |

Osobno mamy funkcje i typy wbudowane, np. `print`, `len`, `int`, `str`, `list`. Sa dostepne bez importu:

```python
orders = [{"id": 1}, {"id": 2}]
print(len(orders))
```

Wynik to `2`. Nie piszemy `import print`. Z kolei `Decimal` trzeba najpierw zaimportowac, mimo ze nalezy do biblioteki standardowej.

### `import modul`: nazwa modulu i kropka

```python
import decimal

amount = decimal.Decimal("120.50")
print(amount + decimal.Decimal("10.00"))
```

Wynik:

```text
130.50
```

Krok po kroku:

1. `import decimal` udostepnia w naszym pliku nazwe `decimal` wskazujaca na modul.
2. `decimal.Decimal` oznacza: znajdz nazwe `Decimal` wewnatrz tego modulu.
3. `decimal.Decimal("120.50")` tworzy liczbe dziesietna z tekstu.
4. Dodawanie dotyczy dwoch liczb `Decimal`, a `print` pokazuje wynik.

Kropka oznacza dostep do elementu danego obiektu. W `decimal.Decimal` pobieramy nazwe z modulu. W `country.strip()` korzystamy z metody konkretnego stringa. Podobny zapis nie oznacza, ze modul i string sa tym samym.

Po samym `import decimal` nie mozemy napisac `Decimal("120.50")`: nie utworzylismy nazwy `Decimal` bezposrednio w naszym pliku.

### `from modul import nazwa`: bez przedrostka

```python
from decimal import Decimal

amount = Decimal("120.50")
print(amount + Decimal("10.00"))
```

Wynik jest taki sam, ale w naszym pliku dostepna jest teraz bezposrednio nazwa `Decimal`.

```text
import decimal               -> uzywamy decimal.Decimal(...)
from decimal import Decimal  -> uzywamy Decimal(...)
```

Drugi zapis nie oznacza, ze Python pobiera z internetu tylko jedna klase lub wykonuje tylko jedna linijke modulu. Modul nadal musi zostac zaladowany. Roznica dotyczy przede wszystkim nazw udostepnionych w naszym kodzie.

Samo `from decimal import Decimal` nie tworzy u nas nazwy `decimal`. Nie mieszaj obu sposobow wywolania bez odpowiedniego importu.

### `as`: lokalny alias

```python
import decimal as dec

print(dec.Decimal("15.00") * 2)
```

Wynik to `30.00`. `as dec` sprawia, ze w tym pliku odnosimy sie do modulu przez nazwe `dec`. Nie zmienia nazwy biblioteki na dysku i nie instaluje innej wersji.

Alias moze tez dotyczyc jednej nazwy:

```python
from decimal import Decimal as Money

print(Money("15.00") * 2)
```

To demonstracja skladni, nie nowy typ pieniedzy. `Money` wskazuje tutaj na ta sama klase `Decimal`. W naszych przykladach zostaniemy przy czytelnej, oryginalnej nazwie `Decimal`.

### Biblioteka standardowa w pracy z danymi

#### `decimal`: kwoty bez przechodzenia przez `float`

```python
from decimal import Decimal

raw_amounts = ["120,50", " 80.00 ", "0"]
total = Decimal("0")

for raw_amount in raw_amounts:
    normalized_amount = raw_amount.strip().replace(",", ".")
    total += Decimal(normalized_amount)

print(total)
```

Wynik to `200.50`. Nasz kod oczyszcza stringi, a `Decimal` interpretuje poprawny zapis liczby. Tworzymy go bezposrednio z tekstu, nie z wyniku `float(...)`, ktory mogl juz utracic dokladnosc. Przy dzieleniu lub zaokraglaniu nadal trzeba okreslic reguly precyzji; `Decimal` nie podejmuje decyzji biznesowych za nas.

#### `json`: tekst z danymi a slownik Pythona

JSON to tekstowy format wymiany danych, czesto spotykany przy pobieraniu danych z innych systemow.

```python
import json

raw_text = '{"order_id": 1001, "country": " pl ", "paid": true}'
order = json.loads(raw_text)
order["country"] = order["country"].strip().upper()

print(type(raw_text))
print(type(order))
print(order["country"])
print(order["paid"])
print(json.dumps(order))
```

Wynik:

```text
<class 'str'>
<class 'dict'>
PL
True
{"order_id": 1001, "country": "PL", "paid": true}
```

`json.loads` odczytuje JSON ze stringa i tworzy wartosci Pythona. `json.dumps` robi odwrotna operacje: tworzy string w formacie JSON. Litera `s` w tych nazwach odnosi sie do stringa. To nie jest jeszcze odczyt ani zapis pliku. JSON-owe `true` staje sie pythonowym `True`, a `null` staloby sie `None`.

Nie kazdy obiekt Pythona daje sie bez dodatkowych decyzji zamienic na JSON. Na przyklad `Decimal` nie jest domyslnie obslugiwany przez `json.dumps`. Tutaj uzywamy zwyklego slownika ze stringiem, liczba calkowita i wartoscia logiczna.

#### `datetime` i `pathlib`: data i sciezka

```python
from datetime import date
from pathlib import Path

order_date = date.fromisoformat("2026-08-01")
file_path = Path("data") / "raw" / "orders.json"

print(order_date.year)
print(order_date.month)
print(file_path.name)
```

Wynik to kolejno `2026`, `8`, `orders.json`. `date.fromisoformat` tworzy date z poprawnego tekstu w formacie `YYYY-MM-DD`. `year` i `month` sa atrybutami z wartosciami, dlatego nie dopisujemy do nich `()`.

`Path` tworzy obiekt opisujacy sciezke, a `/` dolacza kolejne jej czesci. Nie jest tu dzieleniem liczb. `name` zwraca koncowa nazwe. Samo utworzenie `Path` nie tworzy katalogow, nie sprawdza istnienia pliku i nie wczytuje danych. Do biezacej daty mozna uzyc `date.today()`; jej wynik zalezy od dnia uruchomienia.

### Wlasny modul: jedna funkcja, dwa pliki

Utworz w jednym katalogu dwa pliki:

```text
demo_importy/
    order_utils.py
    app.py
```

Zawartosc `order_utils.py`:

```python
def normalize_country(country: str) -> str:
    return country.strip().upper()
```

Zawartosc `app.py`:

```python
from order_utils import normalize_country

orders = [
    {"id": 1, "country": " pl "},
    {"id": 2, "country": " de "},
]

for order in orders:
    print(order["id"], normalize_country(order["country"]))
```

W terminalu otwartym w katalogu `demo_importy` uruchom:

```powershell
python app.py
```

Wynik:

```text
1 PL
2 DE
```

Python rozpoczyna od `app.py`, dociera do importu i odnajduje `order_utils.py` obok uruchamianego skryptu. Wykonuje definicje z tego modulu, udostepnia funkcje i wraca do dalszych instrukcji w `app.py`. Funkcja oczyszcza kraj dopiero przy wywolaniu w petli.

W imporcie nie dopisujemy `.py`, nie ujmujemy nazwy w cudzyslow i nie wklejamy sciezki Windows. Nazwy modulow powinny byc poprawnymi nazwami Pythona, np. `order_utils`, a nie `01-order-utils`.

### Co wykonuje sie przy imporcie

Import nie jest tylko kopiowaniem definicji. Przy pierwszym zwyklym imporcie modulu Python wykonuje takze jego instrukcje na najwyzszym poziomie, czyli poza cialami funkcji.

Na chwile zmien `order_utils.py`:

```python
print("Ladowanie order_utils")


def normalize_country(country: str) -> str:
    print("Czyszczenie kraju")
    return country.strip().upper()
```

A `app.py` zastap:

```python
import order_utils
import order_utils

print("Start aplikacji")
print(order_utils.normalize_country(" pl "))
```

Przy kazdym nowym uruchomieniu `python app.py` wynik bedzie taki:

```text
Ladowanie order_utils
Start aplikacji
Czyszczenie kraju
PL
```

Pierwszy `print` wykonal sie podczas importu. Drugi import tego samego modulu skorzystal z modulu juz zaladowanego w tym procesie. `print` wewnatrz funkcji wykonal sie dopiero przy jej wywolaniu.

Tak samo instrukcje na najwyzszym poziomie wykonuja sie przy `from order_utils import normalize_country`. Dlatego w modulach pomocniczych nie uruchamiamy przypadkiem calego pipeline'u. Ponizej poznamy blok `if __name__ == "__main__"`, ktory pozwala kontrolowac taki start.

### Pakiet: kiedy dwa pliki przestaja wystarczac

Gdy przybywa modulow, mozemy pogrupowac je w pakiet:

```text
demo_pakiet/
    app.py
    commerce/
        __init__.py
        cleaning.py
```

`__init__.py` moze byc pusty. W tym przykladzie oznacza zwykly pakiet `commerce`. Istnieja tez pakiety przestrzeni nazw bez tego pliku, ale na tym etapie tworzymy jawnie zwykle pakiety z `__init__.py`.

Do `commerce/cleaning.py` wstaw funkcje `normalize_country` z pierwszego przykladu. W `app.py` napisz:

```python
from commerce.cleaning import normalize_country

print(normalize_country(" pl "))
```

Uruchom `python app.py` z katalogu `demo_pakiet`. Wynik to `PL`. `commerce.cleaning` oznacza modul `cleaning` wewnatrz pakietu `commerce`, nie nazwe jednej funkcji. Kropka w imporcie oddziela kolejne poziomy tej struktury.

### Instalowanie biblioteki to nie importowanie

Niektore zadania wymagaja narzedzi spoza biblioteki standardowej. Przykladem jest `requests`, biblioteka do komunikacji HTTP, np. z API z zamowieniami. Na tej lekcji nie wykonujemy jeszcze zadnych zapytan do API.

Sa dwa rozne kroki:

```text
instalacja -> umieszcza biblioteke w srodowisku Pythona
import     -> udostepnia jej kod w uruchamianym programie
```

Polecenia ponizej wpisujemy w terminalu, nie w pliku `.py` ani przy znaku `>>>` konsoli Pythona:

```powershell
python -m pip install requests
python -m pip show requests
```

`pip` to narzedzie instalujace pakiety. `python -m pip` oznacza: uruchom modul `pip` przy pomocy tego interpretera `python`. Dzieki temu latwiej powiazac instalacje z konkretnym Pythonem. `install` instaluje pakiet i potrzebne mu zaleznosci, a `show` pokazuje informacje o instalacji. Pobieranie z internetu wymaga dostepu do sieci.

Po instalacji w tym samym srodowisku mozna uruchomic plik:

```python
import requests

print(requests.__name__)
```

Wynik to `requests`. Sam import nie wysyla zadania HTTP. `__name__` to nazwa modulu; w dalszej czesci lekcji zobaczysz te sama nazwe specjalna we wlasnym pliku.

Biblioteki nie instalujemy przy kazdym uruchomieniu skryptu. Import zwykle zapisujemy w kazdym module, ktory korzysta z jej nazw. Instalacja w jednym srodowisku nie udostepnia biblioteki automatycznie wszystkim innym interpreterom.

Nazwa pakietu instalowanego przez `pip` i nazwa uzywana w `import` nie zawsze sa identyczne. W przypadku `requests` sa takie same; w innych przypadkach sprawdzamy dokumentacje biblioteki. Nie instalujemy `json`, `decimal` ani `pathlib` przez `pip`, bo mamy je z Pythonem.

### Srodowisko `.venv` i interpreter PyCharma

Srodowisko wirtualne to osobne miejsce na interpreter i biblioteki konkretnego projektu. Dwa projekty moga wtedy korzystac z innych wersji tej samej biblioteki. `.venv` to zwyczajowa nazwa katalogu takiego srodowiska, a nie obowiazkowa nazwa.

Jesli projekt ma juz srodowisko, korzystaj z niego. Dla nowego projektu mozna je utworzyc w katalogu projektu i uzyc bez aktywowania:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install requests
.\.venv\Scripts\python.exe app.py
```

To polecenia dla Windows / PowerShell. Dwie ostatnie linie jawnie uzywaja tego samego interpretera. Nie wymagaja aktywacji ani zmiany polityki wykonywania skryptow PowerShella.

W PyCharmie interpreter projektu powinien wskazywac na ten sam plik `.venv\Scripts\python.exe`. Samo otwarcie terminala w IDE nie daje pewnosci, ze polecenie `python` oznacza ten sam interpreter co przycisk Run.

Sprawdz, jaki Python naprawde wykonuje program:

```python
import sys

print(sys.executable)
```

`sys` jest modulem standardowym, a `executable` przechowuje sciezke do uruchomionego interpretera. Porownanie tej sciezki z uzyta do instalacji pomaga znalezc powod bledu importu. Katalogu `.venv` nie dodajemy do repozytorium; srodowisko odtwarzamy na kazdej maszynie.

### Jak przekazac informacje o zaleznosciach

Gdy projekt potrzebuje zewnetrznej biblioteki, inna osoba musi wiedziec, co zainstalowac. Prosty plik `requirements.txt` moze zawierac:

```text
requests
```

Instalacja z takiego pliku:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

`-r` wskazuje plik z lista wymagan. Sama nazwa bez wersji nie gwarantuje odtworzenia identycznych wersji bibliotek w przyszlosci. Mozna tez podac dokladna wersje w postaci `nazwa==wersja`, zgodna z tym, co sprawdzono w projekcie.

Nie wpisujemy tu modulow standardowych ani nazw wlasnych plikow `order_utils.py`. Instalujemy tylko zaufane, potrzebne zaleznosci; podobnie brzmiaca nazwa pakietu nie jest dowodem, ze to wlasciwa biblioteka.

### Typowe problemy z importami

| Objaw | Co oznacza | Co sprawdzic |
|---|---|---|
| `ModuleNotFoundError: No module named 'requests'` | interpreter nie znalazl modulu | czy biblioteka jest zainstalowana dla Pythona uruchamiajacego program |
| `ModuleNotFoundError: No module named 'order_utils'` | nie znaleziono wlasnego modulu | nazwe i polozenie pliku oraz sposob uruchamiania projektu |
| `ImportError: cannot import name ...` | znaleziony modul nie udostepnia oczekiwanej nazwy w danej chwili | literowke, dokumentacje, wersje, ewentualnie wzajemne importy |
| `NameError: name 'Decimal' is not defined` | nasz kod nie ma takiej nazwy | czy zrobiono `from decimal import Decimal`, czy nalezy uzyc `decimal.Decimal` |
| blad o brakujacym atrybucie znanej biblioteki | mogl zostac wczytany inny modul o tej samej nazwie | czy w projekcie nie ma np. `json.py`, `decimal.py`, `requests.py` |

Python szuka modulow w okreslonych katalogach, a nie wszedzie na komputerze. Przy uruchamianiu skryptu jednym z nich jest katalog tego skryptu. Wlasny `json.py` moze wiec przeslonic standardowy modul `json`. Nazwij skrypt np. `orders_json_demo.py`.

Wzajemne importy to sytuacja, gdy modul A importuje B, a B podczas ladowania probuje od razu pobrac nazwe z niegotowego jeszcze A. Zamiast dokladac kolejne importy, warto wydzielic wspolne funkcje do trzeciego modulu, od ktorego oba zaleza.

Nie naprawiamy kazdego bledu przez kolejne `pip install`. Najpierw ustalamy, czy problem dotyczy instalacji, nazwy, struktury projektu, czy sposobu uzycia importu.

### Czytelny uklad importow

Importy zwykle umieszczamy na poczatku pliku. Rozdzielamy biblioteke standardowa, zaleznosci zewnetrzne i kod wlasnego projektu pustymi liniami. Jesli w programie nie uzywamy bibliotek zewnetrznych, pomijamy te grupe.

```python
from decimal import Decimal

from order_utils import normalize_country

amount = Decimal("120.50")
country = normalize_country(" pl ")
print(country, amount)
```

Unikamy `from modul import *`: trudno wtedy zobaczyc, skad pochodza nazwy, i latwiej przypadkiem nadpisac wlasna zmienna lub funkcje. Import powinien byc jawny i czytelny, nie po prostu jak najkrotszy.

### Cwiczenie: raport podzielony na moduly

Przygotuj trzy pliki w jednym katalogu: `order_data.py`, `order_utils.py`, `app.py`.

W `order_data.py` umiesc liste:

```python
orders = [
    {"id": 1, "status": " PAID ", "country": " pl ", "amount": "120,50"},
    {"id": 2, "status": "pending", "country": "DE", "amount": "80.00"},
    {"id": 3, "status": "paid", "country": "PL", "amount": "10.00"},
    {"id": 4, "status": "paid", "country": " de ", "amount": "0"},
]
```

W `order_utils.py` napisz funkcje `normalize_country`, `parse_amount` oraz `build_paid_report(orders)`. Ostatnia ma zwracac slownik z liczba i suma kwot oplaconych zamowien per kraj. Status normalizuj przez usuniecie skrajnych bialych znakow i zmiane liter na male. Kwoty przeksztalcaj z tekstu na `Decimal`, dopuszczajac przecinek lub kropke. Dane w tym cwiczeniu sa kompletne i poprawne po normalizacji. Nie zmieniaj wejsciowej listy ani jej slownikow.

W `app.py` zaimportuj dane i funkcje raportujaca, wywolaj ja i wypisz wynik. Nie kopiuj definicji funkcji miedzy plikami. Raport powinien miec dla `PL` liczbe `2` i sume `130.50`, a dla `DE` liczbe `1` i sume `0`. Wystarcza biblioteka standardowa i wlasne moduly, bez `pip install`.

Po poznaniu `main` w nastepnej czesci lekcji przenies uruchomienie raportu do `main()` i dodaj warunek startowy.

## `main`

`main()` to zwykla funkcja.

Nie jest obowiazkowa i Python nie wymaga, zeby funkcja nazywala sie `main`.

Programisci uzywaja tej nazwy, bo oznacza:

```text
tu zaczyna sie glowny przebieg programu
```

Przyklad:

```python
def main() -> None:
    print("Start")
    print("Koniec")
```

Sama definicja nadal niczego nie uruchamia.

Trzeba funkcje wywolac:

```python
main()
```

## `if __name__ == "__main__"`

Czesto zobaczysz taki zapis:

```python
def main() -> None:
    print("Start")
    print("Koniec")


if __name__ == "__main__":
    main()
```

Ten zapis oznacza:

```text
uruchom main() tylko wtedy, gdy ten plik jest uruchamiany bezposrednio
```

Na poczatku moze wygladac dziwnie, ale to bardzo popularny wzorzec.

## Co to jest `__name__`

Python ma specjalna zmienna:

```python
__name__
```

Jej wartosc zalezy od tego, jak plik zostal uzyty.

Jesli uruchamiasz plik bezposrednio:

```bash
python main.py
```

to Python ustawia:

```python
__name__ = "__main__"
```

Wtedy ten warunek jest prawdziwy:

```python
if __name__ == "__main__":
    main()
```

i funkcja `main()` sie uruchamia.

## Po co ten zapis istnieje

Ten sam plik moze byc uzyty na dwa sposoby:

```text
1. jako samodzielny skrypt
2. jako plik z funkcjami do importowania
```

Przyklad pliku `orders.py`:

```python
def normalize_country(country: str) -> str:
    return country.strip().upper()


def main() -> None:
    print(normalize_country(" pl "))


if __name__ == "__main__":
    main()
```

Jesli uruchomisz:

```bash
python orders.py
```

to `main()` sie uruchomi.

Ale jesli w innym pliku napiszesz:

```python
from orders import normalize_country

print(normalize_country(" de "))
```

to `main()` z pliku `orders.py` sie nie uruchomi.

W tym przykladzie uzyjesz funkcji `normalize_country`, bez uruchamiania `main()` z importowanego pliku. Instrukcje na najwyzszym poziomie, gdyby byly poza warunkiem startowym, nadal wykonalyby sie podczas pierwszego importu.

To jest glowny sens tego bloku.

## Dlaczego `main` jest przydatny

Bez `main` kod czesto lezy luzem w pliku.

Z `main` mamy jasny punkt startowy:

```python
def main() -> None:
    raw_country = " pl "
    country = normalize_country(raw_country)
    print(country)


def normalize_country(country: str) -> str:
    return country.strip().upper()


if __name__ == "__main__":
    main()
```

Czytamy:

```text
main pokazuje glowny przebieg programu
funkcje pomocnicze wykonuja konkretne kroki
```

## Inne sposoby uruchamiania kodu

Na poczatku mozesz pisac kod luzem:

```python
print("Hello")
```

To jest dobre do bardzo malych cwiczen.

Mozesz tez zdefiniowac funkcje i wywolac ja bez bloku `if`:

```python
def run() -> None:
    print("Start")


run()
```

To tez zadziala.

Mozesz nazwac funkcje inaczej niz `main`:

```python
def start_pipeline() -> None:
    print("Start pipeline")


start_pipeline()
```

Ale w wiekszych skryptach najczesciej bedziemy uzywac:

```python
def main() -> None:
    print("Start")


if __name__ == "__main__":
    main()
```

To jest czytelny i popularny wzorzec.

## Mini-cwiczenie

Napisz funkcje:

```python
normalize_country(country: str) -> str
```

ktora:

1. usuwa spacje,
2. zamienia kraj na wielkie litery,
3. zwraca wynik.

Potem uzyj jej w `main()`.

Szkielet:

```python
def normalize_country(country: str) -> str:
    ...


def main() -> None:
    raw_country = " pl "
    country = normalize_country(raw_country)
    print(country)


if __name__ == "__main__":
    main()
```

## Dodatkowe cwiczenia: kontrakt funkcji

1. Wywolaj funkcje liczaca wartosc pozycji pozycyjnie, po nazwach i mieszanie, uzyskujac ten sam wynik.
2. Napisz funkcje dodajaca ID do nowej listy, gdy nie podano listy wejsciowej. Dwa niezalezne wywolania nie moga wspoldzielic wyniku.
3. Posortuj zamowienia po kwocie malejaco i ID rosnaco, bez zmiany kolejnosci wejscia. Uzyj nazwanej funkcji `key`.
4. Napisz transformacje zamowienia z lista pozycji tak, aby zmiana wynikowej ilosci nie zmieniala surowych pozycji. Nie ograniczaj testu do porownania dlugosci list.

## Najwazniejsze zasady

1. Funkcja to nazwany fragment logiki.
2. Definicja funkcji nie uruchamia funkcji.
3. Funkcje uruchamiamy przez nawiasy, np. `main()`.
4. `return` zwraca wynik.
5. `print()` tylko pokazuje wartosc na ekranie.
6. Gdy funkcja nie ma `return`, zwraca `None`.
7. Parametr jest w definicji funkcji, argument jest w wywolaniu.
8. Zmienne utworzone w funkcji sa lokalne.
9. Type hints pomagaja czytac kod.
10. `main()` jest dobrym punktem startowym skryptu.
11. `if __name__ == "__main__"` chroni kod w swoim bloku przed uruchomieniem podczas importu.
12. `import modul` i `from modul import nazwa` udostepniaja inne nazwy w naszym pliku.
13. Biblioteki standardowej nie trzeba instalowac przez `pip`.
14. Instalacja biblioteki i jej import to dwa rozne kroki.
15. Biblioteka musi byc dostepna dla interpretera uruchamiajacego program.
16. Wlasne moduly pozwalaja wspoldzielic funkcje bez kopiowania ich definicji.

## Pytania kontrolne

1. Po co piszemy funkcje?
2. Czy definicja funkcji uruchamia kod?
3. Czym rozni sie `print` od `return`?
4. Co oznacza parametr funkcji?
5. Co oznacza `-> str`?
6. Po co jest `main()`?
7. Co robi `if __name__ == "__main__"`?
8. Czym rozni sie uruchomienie pliku od importowania funkcji z pliku?
9. Czym rozni sie parametr od argumentu?
10. Co zwraca funkcja bez `return`?
11. Czym roznia sie modul, pakiet i biblioteka?
12. Dlaczego po `import decimal` piszemy `decimal.Decimal`, a nie samo `Decimal`?
13. Czy `import requests` instaluje biblioteke albo wysyla zadanie do API?
14. Dlaczego instalacja biblioteki w jednym Pythonie nie musi naprawic importu w PyCharmie?
15. Co wykona sie przy pierwszym imporcie pliku z definicja funkcji i z `print` poza funkcja?
16. Dlaczego nie nazywamy wlasnego skryptu `json.py`?
17. Czym rozni sie argument pozycyjny od nazwanego?
18. Dlaczego lista domyslna moze pamietac dane z poprzedniego wywolania?
19. Czy parametr slownikowy jest automatycznie kopiowany?
20. Dlaczego w `key=get_total` nie dopisujemy nawiasow?
21. Jak posortowac przychod malejaco, ale ID rosnaco przy remisie?

## Dokumentacja do importow i bibliotek

- [Moduly i pakiety w Pythonie](https://docs.python.org/3/tutorial/modules.html)
- [Srodowiska wirtualne i zaleznosci](https://docs.python.org/3/tutorial/venv.html)
- [Instalowanie pakietow](https://packaging.python.org/en/latest/tutorials/installing-packages/)
