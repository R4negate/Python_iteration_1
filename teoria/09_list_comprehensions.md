# 09. List comprehensions i czytelne transformacje kolekcji

## Po co jest ta lekcja

Znamy juz budowanie listy przez petle: przygotuj pojemnik, przejdz po rekordach, wybierz potrzebne dane i dopisz wynik. Comprehension pozwala zapisac taki konkretny wzorzec krocej. Nie jest trzecim rodzajem petli obok `for` i `while`, nie zastapi tez calego pipeline'u jedna linijka.

Zaczynamy od list comprehension, czyli wyrazenia budujacego nowa liste. Potem rozszerzymy ten sam pomysl na set i dict. Najpierw zrozum wersje z petla, dopiero potem skrot. Nie wymagamy lambd, generatorow ani nowych bibliotek.

## 1. Od zwyklej petli do comprehension

```python
amounts = [10, 20, 30]
doubled_loop = []

for amount in amounts:
    doubled_loop.append(amount * 2)

doubled_comprehension = [amount * 2 for amount in amounts]

print(doubled_loop)
print(doubled_comprehension)
print(amounts)
```

Wyniki to `[20, 40, 60]`, `[20, 40, 60]` i niezmienione `[10, 20, 30]`. W obu wersjach wykonujemy to samo mnozenie dla kazdego elementu. Nie dopisujemy `append` do comprehension: nowe nawiasy kwadratowe opisuja budowana liste.

Czytamy zapis od czesci `for`: dla kazdego `amount` z `amounts` oblicz `amount * 2` i umiesc wynik w nowej liscie. Cialo wyniku stoi po lewej, mimo ze logicznie najpierw trzeba pobrac element.

```text
[wynik_dla_elementu for element in zrodlo]
```

Kolejnosc listy wynika z kolejnosci iterowania po zrodle. Nie ma automatycznego sortowania ani usuwania duplikatow. Zrodlo bedace setem nie daje gwarantowanej kolejnosci biznesowej. Puste zrodlo daje `[]`.

## 2. Wspolne dane do kolejnych przykladow

Ponizsza lista jest uzywana w sekcjach 3-7 i cwiczeniach. Uruchom ja przed tymi fragmentami. Pozostale demonstracje maja wlasne dane.

```python
orders = [
    {"order_id": 1, "status": "paid", "amount": 120, "country": " pl "},
    {"order_id": 2, "status": "pending", "amount": 80, "country": "DE"},
    {"order_id": 3, "status": "paid", "amount": 0, "country": None},
    {"order_id": 4, "status": "paid", "amount": 300, "country": " pl "},
]
```

Dane sa kompletne, statusy i kwoty juz poprawne. Kwoty calkowite ulatwiaja sledzenie mechanizmu; do parsowania surowych cen i `Decimal` wrocimy w sekcji 9. Comprehension nie waliduje automatycznie zadnego pola.

## 3. Wybor pol z listy slownikow

```python
order_ids = [order["order_id"] for order in orders]
print(order_ids)
```

Wynik: `[1, 2, 3, 4]`. Wynikiem dla jednego elementu jest tutaj liczba, nie caly slownik. To podobne do wyboru jednej kolumny w SQL, ale kolejnosc i wykonanie nadal podlegaja zasadom Pythona.

Comprehension moze budowac nowe slowniki:

```python
order_summaries = [
    {"order_id": order["order_id"], "is_paid": order["status"] == "paid"}
    for order in orders
]
print(order_summaries)
```

Powstaja cztery nowe slowniki. `is_paid` jest `False` tylko dla ID 2. Liczba rekordow sie nie zmienia, poniewaz nie dodalismy filtra.

## 4. Filtr na koncu: element moze nie trafic do wyniku

```python
paid_order_ids = [
    order["order_id"]
    for order in orders
    if order["status"] == "paid"
]
print(paid_order_ids)
```

Wynik: `[1, 3, 4]`. Po pobraniu rekordu Python sprawdza warunek. Dopiero jesli jest prawdziwy, oblicza wyrazenie wynikowe po lewej. Odrzucony rekord nie daje ani zera, ani `None` w liscie: nie daje zadnego elementu.

Rozwiniecie tej samej logiki:

```python
paid_order_ids_loop = []
for order in orders:
    if order["status"] == "paid":
        paid_order_ids_loop.append(order["order_id"])
print(paid_order_ids_loop)
```

Mozna laczyc warunki przez `and` lub `or`, uzywajac nawiasow tam, gdzie ulatwiaja odczyt. Nie stosuj samego `if order["amount"]` jako definicji poprawnosci: poprawne zero zostaloby pominiete.

## 5. Warunek po lewej: wybor wartosci, nie filtrowanie

```python
tiers = [
    "high" if order["amount"] >= 200 else "standard"
    for order in orders
]
print(tiers)
```

Wynik: `['standard', 'standard', 'standard', 'high']`. Kazdy rekord dostaje wynik; warunek wybiera jedna z dwoch etykiet.

| Zapis | Dzialanie |
|---|---|
| `[wartosc for element in zrodlo if warunek]` | filtr: pomin elementy niespelniajace warunku |
| `[wartosc_a if warunek else wartosc_b for element in zrodlo]` | zachowaj elementy, ale wybierz ich wynik |

Obie rzeczy mozna polaczyc:

```python
paid_tiers = [
    "high" if order["amount"] >= 200 else "standard"
    for order in orders
    if order["status"] == "paid"
]
print(paid_tiers)
```

Wynik: `['standard', 'standard', 'high']`. Najpierw warunek paid decyduje o obecnosci wyniku, potem warunek kwoty o etykiecie. Jesli calosc przestaje byc czytelna, rozbij ja na funkcje lub zwykla petle.

## 6. Set comprehension: unikalne kraje

```python
countries = {
    order["country"].strip().upper()
    for order in orders
    if order["country"] is not None
}
print(sorted(countries))
```

Wynik: `['DE', 'PL']`. Nawiasy klamrowe bez par `klucz: wartosc` buduja set. Dwa wystapienia PL daja jeden element. None jest celowo pomijane, bo w tym raporcie pytamy o znane kraje. To nie ogolna regula, ze rekord z brakujacym krajem nalezy odrzucic.

Tu znamy kontrakt: kraj jest stringiem albo None. Przy dowolnych typach musielibysmy najpierw je sprawdzic, np. przez `isinstance`. Puste set comprehension daje set, chociaz doslowne `{}` oznacza pusty dict. Obowiazuja zasady hashowalnosci z 04.

## 7. Dict comprehension: slownik wyszukiwania po ID

```python
amount_by_id = {order["order_id"]: order["amount"] for order in orders}
print(amount_by_id)
```

Wynik: `{1: 120, 2: 80, 3: 0, 4: 300}`. Wyrazenie przed dwukropkiem tworzy klucz, za dwukropkiem wartosc. Taki indeks pozwala pobrac kwote przez `amount_by_id[4]`, bez ponownego przegladania listy.

Uwaga: powtorzony klucz nie oznacza agregacji ani wykrycia duplikatu.

```python
rows = [{"order_id": 1, "amount": 10}, {"order_id": 1, "amount": 20}]
indexed = {row["order_id"]: row["amount"] for row in rows}
print(indexed)
```

Wynik to `{1: 20}`, nie suma `30` i nie dwa rekordy. Pozniejsza wartosc nadpisuje wczesniejsza. Do grupowania z sumami albo odrzucania duplikatow potrzebujemy jawnej logiki, np. znanej petli i setu zaakceptowanych ID.

## 8. Nowa lista nie gwarantuje nowych rekordow

```python
source = [{"order_id": 1, "status": "paid"}]
selected = [order for order in source if order["status"] == "paid"]
selected[0]["status"] = "cancelled"

print(selected is source)
print(selected[0] is source[0])
print(source[0]["status"])
```

Wynik: `False`, `True`, `cancelled`. Lista jest nowa, ale wyrazenie `order` umieszcza w niej referencje do starego slownika. Gdy tworzymy `{...}` wewnatrz comprehension, powstaje nowy slownik, lecz jego zagniezdzone wartosci tez moga byc wspoldzielone. To te same zasady kopiowania, ktore poznalismy w 04 i 06.

Zmienna iteracyjna comprehension ma osobny zakres. Nie nadpisuje istniejacej zewnetrznej zmiennej o tej samej nazwie:

```python
value = "poza comprehension"
numbers = [value * 2 for value in [1, 2, 3]]
print(numbers)
print(value)
```

Wyniki: `[2, 4, 6]` i `poza comprehension`. Nie oznacza to izolacji mutowalnych obiektow zrodlowych; zakres nazw i kopiowanie danych sa roznymi sprawami.

## 9. Comprehension i gotowe funkcje

```python
from decimal import Decimal

priced_orders = [
    {"status": "paid", "amount": "120.50"},
    {"status": "pending", "amount": "80.00"},
    {"status": "paid", "amount": "0"},
]
paid_amounts = [
    Decimal(order["amount"])
    for order in priced_orders
    if order["status"] == "paid"
]
paid_revenue = sum(paid_amounts, Decimal("0"))
paid_flags = [order["status"] == "paid" for order in priced_orders]

print(paid_revenue)
print(any(paid_flags))
print(all(paid_flags))
```

Wyniki: `120.50`, `True`, `False`. Zakladamy poprawne ceny tekstowe. Selekcja i parsowanie nie zmieniaja ich w zrodle. Prawdziwe zero przechodzi do sumy. `sum` z poczatkowym Decimal zachowa ten typ tez dla pustej listy.

Lista comprehension powstaje w calosci. Nawet jesli `any` mogloby rozstrzygnac wynik wczesniej, lista flag zostala juz utworzona. Przy bardzo duzych danych rozwazymy pozniej leniwe przetwarzanie i generatory. Nie nazywamy comprehensions automatycznie szybszymi ani oszczedzajacymi pamiec w kazdym zadaniu.

## 10. Dwa `for`: splaszczenie listy pozycji

```python
orders_with_items = [
    {"order_id": 1, "items": [{"sku": "SQL101"}, {"sku": "PY101"}]},
    {"order_id": 2, "items": [{"sku": "TPL01"}]},
    {"order_id": 3, "items": []},
]

lines_loop = []
for order in orders_with_items:
    for item in order["items"]:
        lines_loop.append({"order_id": order["order_id"], "sku": item["sku"]})

lines = [
    {"order_id": order["order_id"], "sku": item["sku"]}
    for order in orders_with_items
    for item in order["items"]
]

print(lines)
print(lines == lines_loop)
```

Wynik zawiera pary ID/SKU: `1/SQL101`, `1/PY101`, `2/TPL01`, a porownanie daje `True`. Kolejnosc czesci `for` jest taka sama jak w zagniezdzonych petlach: od zewnetrznej do wewnetrznej.

Jeden wynik oznacza teraz pozycje zamowienia, nie cale zamowienie. Zamowienie bez pozycji nie daje wiersza. Dodanie kwoty zamowienia do kazdej pozycji i pozniejsze sumowanie powieliloby sprzedaz, tak jak przy zlym grainie po SQL-owym JOIN.

## 11. Kiedy zostac przy zwyklej petli

Comprehension nadaje sie do prostej projekcji, transformacji lub filtrowania. Zwykla petla jest zwykle lepsza przy wielu krokach walidacji, kilku wynikowych listach, `break`, logowaniu i obsludze osobnego bledu dla kazdego rekordu.

```python
raw_amounts = ["10", "abc", "30"]

try:
    amounts = [float(value) for value in raw_amounts]
except ValueError:
    print("Przerwano budowanie listy")
```

Wynik to komunikat o przerwaniu. Konstrukcja nie zwroci listy `[10.0, 30.0]`: pierwszy wyjatek przerywa budowanie. Przy nowej nazwie `amounts` przypisanie nie zostanie ukonczone; jesli nazwa istniala wczesniej, moze nadal wskazywac stary wynik. To nie jest automatyczny rollback innych skutkow ubocznych wykonanych operacji.

Nie ma instrukcji `try/except`, `break` ani `continue` wewnatrz wyrazenia comprehension. Mozna wywolac funkcje pomocnicza, ale jej kontrakt i bledy nadal trzeba rozumiec. Do `clean_orders` i `rejected_orders` z powodami uzyj wzorca z 07, zamiast gubic powod przez odfiltrowanie niepoprawnych wartosci.

Nie buduj `[print(order) for order in orders]` tylko dla efektu wypisywania. Powstaje zbedna lista wynikow `print`, czyli `None`. Do samych dzialan sluzy zwykly `for`.

## 12. Sciaga skladni

| Potrzeba | Schemat |
|---|---|
| nowa lista | `[wyrazenie for element in zrodlo]` |
| lista po filtrze | `[wyrazenie for element in zrodlo if warunek]` |
| wybor wyniku | `[a if warunek else b for element in zrodlo]` |
| unikalne wartosci | `{wyrazenie for element in zrodlo}` |
| slownik | `{klucz: wartosc for element in zrodlo}` |

Nie istnieje analogiczna tuple comprehension: nawiasy okragle z takim `for` tworza generator, ktory omowimy osobno. Nie zamieniaj nawiasow na chybil trafil.

## 13. Zadania do napisania kodem

Dla wspolnych danych z sekcji 2:

1. Zbuduj liste wszystkich ID w kolejnosci wejscia.
2. Zbuduj liste ID tylko zamowien paid o kwocie co najmniej 100.
3. Zbuduj liste etykiet `high` dla kwoty od 200 oraz `standard` dla pozostalych, zachowujac wszystkie rekordy.
4. Zbuduj set znanych, oczyszczonych krajow w paid, pomijajac None.
5. Zbuduj slownik ID -> kwota dla paid, zachowujac tez kwote zero.
6. Zbuduj liste nowych slownikow z ID i flaga `is_paid`, bez modyfikowania wejscia.

Dla danych z sekcji 10:

7. Zbuduj plaska liste SKU ze wszystkich pozycji w kolejnosci zamowien i pozycji.
8. Napisz zwykla petle rownowazna rozwiazaniu zadania 2 i porownaj oba wyniki. Sprawdz tez zachowanie na pustej liscie.

Nie wystarczy przepisac oczekiwanego wyniku jako gotowej listy. Odpowiedzia ma byc kod wyliczajacy wynik z danych. Nie wymagamy wciskania calego pipeline'u w comprehension.

## Pytania kontrolne

1. Co jest zrodlem, zmienna iteracyjna, wyrazeniem wynikowym i filtrem?
2. Dlaczego `if` na koncu moze zmniejszyc liczbe elementow, a `if/else` po lewej nie musi?
3. Czym rozni sie set comprehension od dict comprehension?
4. Co zrobi dict comprehension z dwoma takimi samymi kluczami?
5. Czy nowa lista comprehension oznacza nowe slowniki w srodku?
6. Co jest jednym wierszem po splaszczeniu pozycji zamowien?
7. Co stanie sie po wyjatku w polowie budowania listy?
8. Kiedy zwykla petla bedzie czytelniejsza i bezpieczniejsza?

## Dokumentacja

- [List, set i dict comprehensions](https://docs.python.org/3/tutorial/datastructures.html)
