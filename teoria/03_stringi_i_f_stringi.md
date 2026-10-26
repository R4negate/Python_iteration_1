# 03. Stringi i f-stringi

## Czym jest string

String, czyli `str`, to tekst.

W Pythonie tekst zapisujemy w cudzyslowie:

```python
customer_name = "Anna Kowalska"
country = "PL"
status = "paid"
```

Stringiem moze byc:

- imie,
- kraj,
- status,
- adres email,
- data zapisana jako tekst,
- sciezka do pliku,
- odpowiedz z API.

Przyklady:

```python
email = "anna@example.com"
order_date = "2026-10-10"
file_path = "data/raw/orders.json"
```

## Dlaczego stringi sa wazne w data engineeringu

W danych bardzo duzo rzeczy przychodzi jako tekst.

Z API albo pliku mozemy dostac:

```python
raw_country = " pl "
raw_status = " Paid "
raw_amount = "129.99"
```

To oznacza, ze zanim zaczniemy liczyc albo filtrowac dane, czesto musimy tekst:

- oczyscic ze spacji,
- ujednolicic wielkosc liter,
- sprawdzic, czy nie jest pusty,
- zbudowac z niego sciezke pliku,
- zamienic na liczbe albo date.

Ta lekcja dotyczy czyszczenia i budowania tekstu.

## Indeksy w stringach

String jest sekwencja znakow.

```python
country = "POLAND"
```

Mozemy pobrac pojedynczy znak:

```python
print(country[0])
print(country[1])
```

Wynik:

```text
P
O
```

Python liczy indeksy od zera.

```text
P O L A N D
0 1 2 3 4 5
```

Ostatni znak mozna pobrac tak:

```python
print(country[-1])
```

## Wycinki tekstu: `start:stop:step`

Indeks wybiera jeden znak, a wycinek, czyli slicing, wybiera fragment tekstu. Zapis `text[start:stop:step]` opisuje poczatek, granice konca i krok. Granica `stop` nie nalezy do wyniku, tak jak koniec w `range` z pozniejszej lekcji.

```python
text = "PYTHON"

print(text[0:2])
print(text[2:])
print(text[:-1])
print(text[::2])
print(text[::-1])
print(text)
```

Wynik:

```text
PY
THON
PYTHO
PTO
NOHTYP
PYTHON
```

`[0:2]` bierze indeksy 0 i 1. Brak `stop` oznacza dojscie do konca. `[:-1]` pomija ostatni znak. `[::2]` wybiera co drugi znak od poczatku, a `[::-1]` odwraca kolejnosc. Przy dodatnim kroku pominiety start oznacza poczatek; przy ujemnym Python dobiera granice odpowiednie do przechodzenia wstecz.

Wycinek nie zmienia stringa. `text[20:30]` zwroci pusty tekst, chociaz pojedynczy odczyt `text[20]` zglosilby `IndexError`. Zbyt dalekie granice wycinka sa przycinane. Krok nie moze wynosic zero. Ujemny krok nie oznacza ujemnej liczby powtorzen: zmienia kierunek wybierania.

Praktyczny przyklad: z kodu `"SQL-001"` odczytasz rodzine produktu przez `code[:3]`, a koncowe trzy znaki przez `code[-3:]`. To ma sens tylko wtedy, gdy znasz format kodu; wycinek sam go nie waliduje.

## Dlugosc tekstu

`len()` zwraca dlugosc tekstu:

```python
customer_name = "Anna"
print(len(customer_name))
```

Wynik:

```text
4
```

To przydaje sie na przyklad przy walidacji:

```python
country = "PL"

if len(country) != 2:
    print("invalid country code")
```

## Czyszczenie tekstu: `.strip()`

`.strip()` usuwa biale znaki z poczatku i konca tekstu.

```python
country = " pl "
clean_country = country.strip()

print(clean_country)
```

Wynik:

```text
pl
```

To jest bardzo czeste przy danych z formularzy, plikow CSV i API.

Uwaga: `.strip()` nie zmienia oryginalnej zmiennej w miejscu.

```python
country = " pl "
country.strip()

print(country)
```

Wynik nadal zawiera spacje:

```text
 pl 
```

Dlatego trzeba przypisac wynik:

```python
country = country.strip()
```

## Wielkosc liter: `.upper()` i `.lower()`

`.upper()` zamienia tekst na wielkie litery:

```python
country = "pl"
country = country.upper()
print(country)
```

Wynik:

```text
PL
```

`.lower()` zamienia tekst na male litery:

```python
email = "ANNA@EXAMPLE.COM"
email = email.lower()
print(email)
```

Wynik:

```text
anna@example.com
```

## Laczenie metod

Metody mozna laczyc:

```python
raw_country = " pl "
country = raw_country.strip().upper()

print(country)
```

Wynik:

```text
PL
```

Czytaj to od lewej do prawej:

```text
wez raw_country
usun spacje
zamien na wielkie litery
zapisz jako country
```

## Metody stringow zwracaja nowy tekst

Metody takie jak `.strip()`, `.upper()`, `.lower()` i `.replace()` nie zmieniaja starego tekstu w miejscu.

Zle oczekiwanie:

```python
country = " pl "
country.strip().upper()

print(country)
```

Wynik nadal bedzie mial spacje:

```text
 pl 
```

Poprawnie:

```python
country = " pl "
country = country.strip().upper()

print(country)
```

Wynik:

```text
PL
```

## Zamiana fragmentu tekstu: `.replace()`

`.replace()` zamienia jeden fragment tekstu na inny.

```python
raw_amount = "129,99"
amount_text = raw_amount.replace(",", ".")

print(amount_text)
```

Wynik:

```text
129.99
```

To przydaje sie, gdy dane przychodza w formacie innym niz oczekuje Python.

Przyklad:

```python
raw_phone = "+48 500 600 700"
phone = raw_phone.replace(" ", "")

print(phone)
```

Wynik:

```text
+48500600700
```

## Sprawdzanie poczatku i konca tekstu

```python
file_name = "orders_2026_10_10.json"

print(file_name.startswith("orders"))
print(file_name.endswith(".json"))
```

Wynik:

```text
True
True
```

To przydaje sie przy sprawdzaniu nazw plikow.

## Szukanie fragmentu tekstu

Mozemy sprawdzic, czy tekst zawiera fragment:

```python
email = "anna@example.com"

if "@" in email:
    print("email contains @")
```

To nie jest pelna walidacja emaila, ale pokazuje podstawowa idee.

## Pusty tekst, spacje i `None`

To sa trzy rozne sytuacje:

```python
email = None       # brak wartosci
email = ""         # pusty tekst
email = "   "      # tekst skladajacy sie ze spacji
```

Pusty tekst:

```python
email = ""

if email == "":
    print("empty email")
```

Tekst ze spacjami warto najpierw oczyscic:

```python
email = "   "

if email.strip() == "":
    print("empty email after strip")
```

Na `None` nie mozna uzyc `.strip()`:

```python
email = None

print(email.strip())
```

Ten kod sie wywali, bo `None` nie jest stringiem.

Bezpieczniej:

```python
email = None

if email is None:
    print("missing email")
else:
    print(email.strip())
```

## Dzielenie tekstu: `.split()`

`.split()` dzieli tekst na liste.

```python
full_name = "Anna Kowalska"
parts = full_name.split(" ")

print(parts)
```

Wynik:

```text
['Anna', 'Kowalska']
```

Przyklad z plikiem CSV:

```python
line = "1001,paid,129.99"
columns = line.split(",")

print(columns)
```

Wynik:

```text
['1001', 'paid', '129.99']
```

To jeszcze nie jest prawdziwe czytanie CSV, ale pokazuje, ze tekst mozna rozbijac.

## `.join()`: z wielu tekstow jeden tekst

`.split()` dzieli string na elementy, a `.join()` laczy tekstowe elementy, wstawiajac miedzy nimi wybrany separator. Metode wywolujemy na separatorze, nie na liscie.

```python
countries = ["PL", "DE", "FR"]
country_list = ", ".join(countries)

print(country_list)
print(" | ".join(countries))
print("-".join(countries))
print("".join(countries))
```

Wyniki: `PL, DE, FR`, `PL | DE | FR`, `PL-DE-FR` i `PLDEFR`. Separator nie jest dopisywany przed pierwszym ani po ostatnim elemencie. `", ".join([])` daje pusty tekst. Lista wejsciowa pozostaje bez zmian.

```python
raw_name = "  Anna   Kowalska  "
parts = raw_name.split()
name = " ".join(parts)

print(parts)
print(name)
```

Wynik to lista `['Anna', 'Kowalska']` oraz tekst `Anna Kowalska`. `split()` bez argumentu dzieli po bialych znakach i nie zachowuje pustych fragmentow pomiedzy nimi. W odroznieniu od tego `"A,,B".split(",")` zachowuje pusty element pomiedzy dwoma przecinkami.

`join` wymaga stringow, nie robi automatycznie `str` dla liczb lub `None`. `", ".join([1, 2])` zglosiloby `TypeError`: dane trzeba najpierw swiadomie przeksztalcic, a nie ukrywac ich typ.

Laczenie kilku elementow jest przydatne w raporcie tekstowym. Nie zastepuje jednak poprawnego zapisu CSV, ktory musi obslugiwac m.in. separatory wewnatrz pol i cudzyslowy.

## Laczenie tekstu: `+`

Tekst mozna laczyc przez `+`:

```python
first_name = "Anna"
last_name = "Kowalska"

full_name = first_name + " " + last_name
print(full_name)
```

Wynik:

```text
Anna Kowalska
```

Ale do czytelnych komunikatow lepsze sa f-stringi.

## F-stringi

F-string pozwala wstawic wartosc zmiennej do tekstu.

```python
customer_name = "Anna"
orders_count = 3

message = f"Klient {customer_name} ma {orders_count} zamowienia"
print(message)
```

Wynik:

```text
Klient Anna ma 3 zamowienia
```

Najwazniejszy szczegol: przed tekstem musi byc litera `f`.

Bez `f`:

```python
message = "Klient {customer_name} ma {orders_count} zamowienia"
```

Python potraktuje `{customer_name}` jako zwykly tekst.

## F-stringi do debugowania

F-stringi sa bardzo przydatne, gdy chcesz zobaczyc, co dzieje sie w programie.

```python
order_id = 1001
status = "paid"
total_amount = 129.99

print(f"order_id={order_id}, status={status}, total_amount={total_amount}")
```

Wynik:

```text
order_id=1001, status=paid, total_amount=129.99
```

## Formatowanie liczb

Mozemy wyswietlic liczbe do 2 miejsc po przecinku:

```python
total = 129.987
print(f"{total:.2f}")
```

Wynik:

```text
129.99
```

Przyklad:

```python
customer_name = "Anna"
total = 129.987

print(f"Klient {customer_name} wydal {total:.2f} PLN")
```

Wynik:

```text
Klient Anna wydal 129.99 PLN
```

## Dynamiczne sciezki plikow

W data engineeringu czesto budujemy nazwy plikow na podstawie daty, strony albo zrodla.

```python
date = "2026-10-10"
page = 1

path = f"data/raw/orders_{date}_page_{page}.json"
print(path)
```

Wynik:

```text
data/raw/orders_2026-10-10_page_1.json
```

To bedzie wazne, gdy zaczniemy pobierac dane z API i zapisywac je lokalnie.

## Mini-cwiczenie

Masz dane:

```python
raw_country = " pl "
raw_status = " Paid "
date = "2026-10-10"
page = 2
```

Zrob:

1. `country` jako `"PL"`,
2. `status` jako `"paid"`,
3. `path` jako `"data/raw/orders_2026-10-10_page_2.json"`,
4. wypisz komunikat przez f-string.

Szkielet:

```python
raw_country = " pl "
raw_status = " Paid "
date = "2026-10-10"
page = 2

country = ...
status = ...
path = ...

print(...)
```

## Dodatkowe cwiczenia: wycinki i skladanie tekstu

1. Dla `code = "SQL-2026-001"` wyciagnij osobno `SQL`, `2026` i `001`, bez zmiany zrodla.
2. Dla `countries = ["PL", "DE", "FR"]` zbuduj tekst `PL / DE / FR`, bez separatora na koncu.
3. Dla `name = "  Anna\t  Kowalska  "` zbuduj tekst z jedna spacja miedzy czesciami i bez skrajnych bialych znakow.

## Najwazniejsze zasady

1. String to tekst.
2. Tekst zapisujemy w cudzyslowie.
3. `.strip()` usuwa spacje z poczatku i konca.
4. `.upper()` robi wielkie litery.
5. `.lower()` robi male litery.
6. `.replace()` zamienia fragment tekstu.
7. `.split()` dzieli tekst na liste.
8. F-stringi pozwalaja wstawiac zmienne do tekstu.
9. Przed f-stringiem musi byc `f`.
10. Metody stringow zwracaja nowy tekst, nie zmieniaja starego w miejscu.
11. `None` nie jest tekstem, wiec nie mozna na nim wolac metod stringow.

## Pytania kontrolne

1. Co robi `.strip()`?
2. Co robi `.upper()`?
3. Co robi `.lower()`?
4. Do czego sluzy `.replace()`?
5. Co zwroci `"1001,paid,129.99".split(",")`?
6. Po co sa f-stringi?
7. Co sie stanie, jezeli zapomnisz `f` przed f-stringiem?
8. Jak wyswietlic liczbe do 2 miejsc po przecinku?
9. Dlaczego czyszczenie tekstu jest wazne w data engineeringu?
10. Czym rozni sie `None` od pustego tekstu `""`?
11. Czy granica konca wycinka nalezy do wyniku?
12. Co oznacza `text[::-1]` i dlaczego nie zmienia zrodla?
13. Dlaczego separator stoi przed `.join(...)`, a nie jako argument listy?
14. Czym rozni sie `split()` od `split(",")` dla pustych fragmentow?
