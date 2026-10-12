# 02. Zmienne, operatory i podstawowa logika

## Po co jest ta lekcja

W lekcji 1 poznalismy typy danych:

```text
str, int, float, bool, None, list, tuple, dict, set
```

Teraz uczymy sie pracowac na wartosciach:

- zapisywac je w zmiennych,
- nadawac im dobre nazwy,
- wykonywac obliczenia,
- porownywac wartosci,
- laczyc warunki,
- budowac proste decyzje logiczne.

To jest fundament pod pozniejsze `if`, petle i funkcje.

## Zmienna

Zmienna to nazwa przypisana do wartosci.

```python
customer_name = "Anna Kowalska"
orders_count = 3
total_revenue = 249.90
```

Czytamy:

```text
customer_name przechowuje tekst "Anna Kowalska"
orders_count przechowuje liczbe 3
total_revenue przechowuje liczbe 249.90
```

Zmienna pozwala uzyc wartosci pozniej:

```python
print(customer_name)
print(total_revenue)
```

## `=` oznacza przypisanie

W Pythonie jeden znak `=` oznacza przypisanie.

```python
status = "paid"
```

Czytamy:

```text
do zmiennej status przypisz tekst "paid"
```

To nie jest pytanie, czy dwie rzeczy sa rowne.

Porownanie robimy przez `==`:

```python
status == "paid"
```

Zapamietaj:

```text
=   przypisanie
==  porownanie
```

## Zmiana wartosci zmiennej

Zmienna moze dostac nowa wartosc.

```python
orders_count = 3
print(orders_count)

orders_count = 4
print(orders_count)
```

Wynik:

```text
3
4
```

Nazwa zostala ta sama, ale wartosc sie zmienila.

## Dobre nazwy zmiennych

Dobra nazwa zmiennej mowi, co jest w srodku.

Dobrze:

```python
customer_name = "Anna"
total_revenue = 1200.50
paid_orders_count = 7
```

Slabo:

```python
x = "Anna"
a = 1200.50
poc = 7
```

Technicznie `x` zadziala, ale po tygodniu trudniej bedzie zrozumiec kod.

W Pythonie najczesciej uzywamy stylu `snake_case`:

```python
customer_name
total_amount
orders_count
```

## Operatory arytmetyczne

Python potrafi liczyc.

| Operator | Znaczenie | Przyklad |
|---|---|---|
| `+` | dodawanie | `10 + 5` |
| `-` | odejmowanie | `10 - 5` |
| `*` | mnozenie | `10 * 5` |
| `/` | dzielenie | `10 / 5` |
| `//` | dzielenie calkowite | `10 // 3` |
| `%` | reszta z dzielenia | `10 % 3` |
| `**` | potegowanie | `2 ** 3` |

Przyklad:

```python
quantity = 3
unit_price = 19.99

line_value = quantity * unit_price
print(line_value)
```

## Kolejnosc dzialan

Python stosuje normalna kolejnosc dzialan matematycznych.

```python
result = 2 + 3 * 4
print(result)
```

Wynik:

```text
14
```

Najpierw wykonuje sie mnozenie, potem dodawanie.

Jesli chcesz zmienic kolejnosc, uzyj nawiasow:

```python
result = (2 + 3) * 4
print(result)
```

Wynik:

```text
20
```

## Aktualizacja wartosci

Czesto chcemy zwiekszyc licznik albo sume.

```python
orders_count = 0
orders_count = orders_count + 1
orders_count = orders_count + 1

print(orders_count)
```

Wynik:

```text
2
```

Ten zapis jest bardzo wazny przy petlach.

Mozna go zapisac krocej:

```python
orders_count += 1
```

To znaczy:

```text
wez obecna wartosc orders_count i dodaj 1
```

Analogicznie:

```python
total_revenue += 129.99
```

## Operatory porownania

Porownania zwracaja `True` albo `False`.

| Operator | Znaczenie |
|---|---|
| `==` | rowne |
| `!=` | rozne |
| `>` | wieksze |
| `>=` | wieksze lub rowne |
| `<` | mniejsze |
| `<=` | mniejsze lub rowne |

Przyklady:

```python
total_amount = 250
status = "paid"

print(total_amount >= 200)
print(status == "paid")
print(status != "cancelled")
```

Wynik:

```text
True
True
True
```

Wynik porownania mozna zapisac do zmiennej:

```python
is_paid = status == "paid"
is_high_value = total_amount >= 300

print(is_paid)
print(is_high_value)
```

To jest bardzo czeste, gdy chcemy rozbic dlugi warunek na czytelne male czesci.

## Porownanie tekstu

Tekst tez mozna porownywac:

```python
country = "PL"

print(country == "PL")
print(country == "DE")
```

Wynik:

```text
True
False
```

Uwaga na wielkosc liter:

```python
print("pl" == "PL")
```

Wynik:

```text
False
```

Dlatego czesto najpierw czyscimy tekst:

```python
country = " pl "
country = country.strip().upper()

print(country == "PL")
```

## Operatory logiczne

Operatory logiczne pozwalaja laczyc warunki.

### `and`

`and` oznacza, ze oba warunki musza byc prawdziwe.

```python
status = "paid"
total_amount = 350

is_high_paid_order = status == "paid" and total_amount >= 300

print(is_high_paid_order)
```

### `or`

`or` oznacza, ze wystarczy jeden prawdziwy warunek.

```python
country = "PL"

is_core_country = country == "PL" or country == "DE"

print(is_core_country)
```

### `not`

`not` odwraca wartosc logiczna.

```python
is_active = False

print(not is_active)
```

Wynik:

```text
True
```

## Nawiasy w warunkach logicznych

Gdy laczysz `and` i `or`, warto uzywac nawiasow.

```python
status = "paid"
country = "PL"

include_in_report = status == "paid" and (country == "PL" or country == "DE")

print(include_in_report)
```

Czytamy:

```text
zamowienie ma byc paid
i kraj ma byc PL albo DE
```

Bez nawiasow kod moze byc trudniejszy do przeczytania, nawet jesli Python potrafi go wykonac.

## `in`

`in` sprawdza, czy wartosc znajduje sie w kolekcji.

```python
country = "PL"
core_countries = ["PL", "DE", "FR"]

print(country in core_countries)
```

To jest czytelniejsze niz:

```python
country == "PL" or country == "DE" or country == "FR"
```

## Pierwszy prosty `if`

`if` bedzie osobna lekcja szerzej, ale tutaj zobaczmy podstawowy sens.

```python
total_amount = 350

if total_amount >= 300:
    print("high value order")
```

Czytamy:

```text
jesli total_amount jest wieksze lub rowne 300, wypisz komunikat
```

Wazne: kod wewnatrz `if` ma wciecie.

## `if / else`

```python
total_amount = 120

if total_amount >= 300:
    order_tier = "high"
else:
    order_tier = "standard"

print(order_tier)
```

To jest podobne do SQL:

```sql
CASE
    WHEN total_amount >= 300 THEN 'high'
    ELSE 'standard'
END
```

## Przyklad data engineeringowy

```python
raw_country = " pl "
raw_amount = "350.00"
status = "paid"

country = raw_country.strip().upper()
amount = float(raw_amount)

is_core_country = country in ["PL", "DE", "FR"]
is_high_value = amount >= 300
is_valid_for_report = status == "paid" and is_core_country and is_high_value

print(is_valid_for_report)
```

Czytamy:

```text
oczysc kraj
zamien kwote na liczbe
sprawdz, czy kraj jest w grupie krajow
sprawdz, czy kwota jest wysoka
sprawdz, czy zamowienie ma wejsc do raportu
```

## Mini-cwiczenie

Masz dane:

```python
raw_country = " de "
raw_amount = "250.00"
status = "paid"
```

Zrob:

1. oczysc kraj do postaci `"DE"`,
2. zamien kwote na `float`,
3. sprawdz, czy zamowienie jest `paid`,
4. sprawdz, czy kwota jest wieksza lub rowna `200`,
5. sprawdz, czy kraj jest jednym z: `PL`, `DE`, `FR`,
6. stworz zmienna `include_in_report`, ktora bedzie `True`, tylko jesli wszystkie trzy warunki sa prawdziwe.

## Najwazniejsze zasady

1. Zmienna to nazwa przypisana do wartosci.
2. `=` oznacza przypisanie.
3. `==` oznacza porownanie.
4. Operatory arytmetyczne sluza do liczenia.
5. Nawiasy pomagaja kontrolowac kolejnosc dzialan.
6. Porownania zwracaja `True` albo `False`.
7. Wynik porownania mozna zapisac do zmiennej.
8. `and` wymaga, zeby wszystkie warunki byly prawdziwe.
9. `or` wymaga, zeby przynajmniej jeden warunek byl prawdziwy.
10. `not` odwraca warunek.
11. `in` sprawdza, czy wartosc jest w kolekcji.

## Pytania kontrolne

1. Czym rozni sie `=` od `==`?
2. Co oznacza `orders_count += 1`?
3. Co zwraca porownanie `total_amount >= 300`?
4. Kiedy `and` zwroci `True`?
5. Kiedy `or` zwroci `True`?
6. Do czego sluzy `in`?
7. Dlaczego `"pl" == "PL"` zwraca `False`?
8. Po co uzywamy nawiasow w dluzszych warunkach?
