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

Parametr to wartosc przekazywana do funkcji.

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

## Importy

Import pozwala uzyc kodu z innego miejsca.

Przyklady z biblioteki standardowej:

```python
from datetime import date
from pathlib import Path
```

Uzycie:

```python
today = date.today()
print(today)
```

```python
path = Path("data/raw/orders.json")
print(path)
```

Na razie wystarczy rozumiec:

```text
import daje dostep do gotowych narzedzi
```

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

Uzyjesz tylko funkcji `normalize_country`.

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
11. `if __name__ == "__main__"` chroni przed przypadkowym uruchomieniem programu przy imporcie.

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
