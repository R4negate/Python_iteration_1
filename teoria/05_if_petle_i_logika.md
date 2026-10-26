# 05. If, petle i logika

## Po co sa warunki i petle

Do tej pory umielismy zapisac dane:

```python
order = {
    "order_id": 1001,
    "total": 129.99,
    "status": "paid",
}
```

Ale program musi tez umiec podejmowac decyzje:

```text
jesli zamowienie jest oplacone, policz je do sprzedazy
jesli kraj jest pusty, ustaw UNKNOWN
jesli kwota jest wieksza niz 300, oznacz klienta jako high value
```

Do decyzji sluzy `if`.

Program musi tez umiec przejsc po wielu rekordach:

```text
sprawdz kazde zamowienie
policz sume ze wszystkich zamowien
wypisz kazdego klienta
```

Do przechodzenia po elementach sluzy petla `for`. Gdy powtarzanie zalezy od warunku, mozemy uzyc petli `while`. W tej lekcji poznamy obie i nauczymy sie dobierac je do zadania.

## `if`

`if` pozwala wykonac kod tylko wtedy, gdy warunek jest prawdziwy.

```python
total = 150

if total >= 100:
    print("high value")
```

Czytamy:

```text
jesli total jest wiekszy lub rowny 100, wypisz "high value"
```

Wazne: kod wewnatrz `if` jest wcieciem.

```python
if total >= 100:
    print("to jest wewnatrz if")

print("to wykona sie zawsze")
```

## `else`

`else` oznacza: w przeciwnym razie.

```python
total = 80

if total >= 100:
    print("high value")
else:
    print("standard")
```

Czytamy:

```text
jesli total >= 100, pokaz high value
w przeciwnym razie pokaz standard
```

To jest podobne do SQL:

```sql
CASE
    WHEN total >= 100 THEN 'high value'
    ELSE 'standard'
END
```

## `elif`

`elif` oznacza: w przeciwnym razie, jesli...

```python
status = "cancelled"

if status == "paid":
    label = "paid order"
elif status == "cancelled":
    label = "cancelled order"
else:
    label = "other"

print(label)
```

Python sprawdza warunki od gory do dolu.

Gdy pierwszy warunek pasuje, pozostale nie sa juz wykonywane.

## Operatory porownania

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
total == 100
status != "cancelled"
amount >= 300
```

## Operatory logiczne

Mozemy laczyc warunki.

### `and`

Oba warunki musza byc prawdziwe:

```python
status = "paid"
total = 400

if status == "paid" and total >= 300:
    print("high value paid order")
```

### `or`

Wystarczy jeden prawdziwy warunek:

```python
country = "PL"

if country == "PL" or country == "DE":
    print("core market")
```

### `not`

Odwraca warunek:

```python
is_active = False

if not is_active:
    print("inactive")
```

## `in`

`in` sprawdza, czy wartosc znajduje sie w kolekcji.

```python
country = "PL"
core_countries = ["PL", "DE", "FR"]

if country in core_countries:
    print("core country")
```

To jest czytelniejsze niz:

```python
if country == "PL" or country == "DE" or country == "FR":
    print("core country")
```

## Prawda i falsz bez porownania

Niektore wartosci Python traktuje jak falsz:

```text
None
""
0
[]
{}
```

Przyklad:

```python
email = ""

if email:
    print("email exists")
else:
    print("email is missing")
```

Wynik:

```text
email is missing
```

Na poczatku mozesz pisac warunki bardziej jawnie:

```python
if email != "":
    print("email exists")
```

Ale warto wiedziec, ze w Pythonie pusty tekst jest traktowany jak `False`.

## Petla `for`

Petla `for` przechodzi po elementach kolekcji.

```python
countries = ["PL", "DE", "FR"]

for country in countries:
    print(country)
```

Czytamy:

```text
dla kazdego country z listy countries wypisz country
```

## `range()`

`range()` tworzy zakres liczb, po ktorym mozna przejsc petla.

```python
for number in range(5):
    print(number)
```

Wynik:

```text
0
1
2
3
4
```

Uwaga: `range(5)` daje liczby od `0` do `4`, czyli nie zawiera `5`.

Mozesz tez podac start i koniec:

```python
for number in range(1, 4):
    print(number)
```

Wynik:

```text
1
2
3
```

### Trzy argumenty: start, stop i krok

```python
print(list(range(0, 7, 2)))
print(list(range(5, 0, -1)))
print(list(range(5, 0)))
```

Wyniki: `[0, 2, 4, 6]`, `[5, 4, 3, 2, 1]`, `[]`. Trzeci argument to krok. Domyslnie wynosi `1`; ujemny pozwala przechodzic malejaco. Stop nadal nie wchodzi do wyniku. Przy dodatnim kroku i starcie wiekszym od stop zakres jest pusty, a nie automatycznie odwrocony. Krok `0` powoduje `ValueError`.

`range` nie tworzy od razu calej listy liczb. W przykladzie `list(...)` sluzy tylko do pokazania wszystkich elementow. W zwyklej petli mozemy bezposrednio uzyc `for number in range(0, 7, 2)`.

## `enumerate()`

`enumerate()` daje jednoczesnie indeks i element.

```python
countries = ["PL", "DE", "FR"]

for index, country in enumerate(countries):
    print(index, country)
```

Wynik:

```text
0 PL
1 DE
2 FR
```

To przydaje sie, gdy chcesz wiedziec, ktory element listy aktualnie przetwarzasz.

## Petla po liscie slownikow

To jest bardzo wazny przypadek w data engineeringu.

```python
orders = [
    {"order_id": 1, "total": 100, "status": "paid"},
    {"order_id": 2, "total": 200, "status": "cancelled"},
    {"order_id": 3, "total": 300, "status": "paid"},
]

for order in orders:
    print(order["order_id"])
```

Za kazdym obrotem petli zmienna `order` oznacza jeden slownik, czyli jedno zamowienie.

## Petla po slowniku

Mozesz tez przejsc po parach klucz-wartosc w jednym slowniku.

```python
order = {
    "order_id": 1,
    "total": 100,
    "status": "paid",
}

for key, value in order.items():
    print(key, value)
```

Wynik:

```text
order_id 1
total 100
status paid
```

## Liczenie sumy

W SQL pisalismy:

```sql
SUM(total_amount)
```

W Pythonie na poczatku mozemy policzyc sume petla.

```python
orders = [
    {"order_id": 1, "total": 100, "status": "paid"},
    {"order_id": 2, "total": 200, "status": "cancelled"},
    {"order_id": 3, "total": 300, "status": "paid"},
]

total_revenue = 0

for order in orders:
    total_revenue = total_revenue + order["total"]

print(total_revenue)
```

Krok po kroku:

```text
start: total_revenue = 0
po 1 zamowieniu: 100
po 2 zamowieniu: 300
po 3 zamowieniu: 600
```

## Liczenie tylko zamowien paid

```python
paid_revenue = 0

for order in orders:
    if order["status"] == "paid":
        paid_revenue = paid_revenue + order["total"]

print(paid_revenue)
```

To jest odpowiednik myslenia:

```text
wez tylko rekordy paid i policz sume
```

## Licznik

Mozemy tez liczyc rekordy.

```python
paid_orders_count = 0

for order in orders:
    if order["status"] == "paid":
        paid_orders_count = paid_orders_count + 1

print(paid_orders_count)
```

## `continue`

`continue` konczy biezacy obrot i pomija pozostale instrukcje jego ciala. W petli `for` oznacza przejscie do kolejnego elementu, a w poznanej dalej petli `while` powrot do sprawdzenia warunku.

```python
for order in orders:
    if order["status"] == "cancelled":
        continue

    print(order)
```

Czytamy:

```text
jesli zamowienie jest cancelled, pomin je
w przeciwnym razie wypisz zamowienie
```

Wazne: po `continue` Python nie wykonuje dalszych linii w aktualnym obrocie petli.

```python
for order in orders:
    if order["status"] == "cancelled":
        continue

    print("this order is not cancelled")
    print(order)
```

## `break`

`break` natychmiast konczy najblizsza petle, w ktorej sie znajduje. Przy jednej petli oznacza to wyjscie z niej do dalszego kodu. Przy petli w petli wewnetrzny `break` nie konczy automatycznie obu.

```python
for order in orders:
    if order["total"] >= 300:
        print("found high order")
        break
```

Po znalezieniu pierwszego pasujacego rekordu petla sie zatrzyma.

## Petla w petli: zamowienie i jego pozycje

Zagniezdzenie to umieszczenie jednej petli wewnatrz drugiej. Dla aktualnego zamowienia przechodzimy przez jego pozycje, a dopiero potem wybieramy nastepne zamowienie.

```python
orders_with_items = [
    {"order_id": 1, "items": [
        {"quantity": 2, "unit_price": 10},
        {"quantity": 1, "unit_price": 5},
    ]},
    {"order_id": 2, "items": [{"quantity": 3, "unit_price": 10}]},
    {"order_id": 3, "items": []},
]

for order in orders_with_items:
    order_total = 0

    for item in order["items"]:
        order_total += item["quantity"] * item["unit_price"]

    print(order["order_id"], order_total)
```

Wynik: `1 25`, `2 30`, `3 0`, kazdy w osobnej linii. Zerujemy sume po wejsciu do nowego zamowienia, ale przed jego pozycjami. Zerowanie wewnatrz wewnetrznej petli utraciloby wczesniejsze pozycje; zerowanie przed obiema petlami liczyloby sume calego zbioru.

Petla zewnetrzna wykonuje trzy obroty, a linia dodawania lacznie trzy razy: `2 + 1 + 0` pozycji. Nie jest to zawsze liczba zamowien pomnozona przez liczbe wszystkich produktow. Taki iloczyn powstalby, gdybysmy dla kazdego zamowienia przechodzili cala wspolna liste produktow.

`break` lub `continue` w petli wewnetrznej steruje tylko ta najblizsza petla. Nie zmieniaj dlugosci przegladanej listy pozycji podczas tego samego przejscia; lepiej zbudowac liste wynikowa.

## Petla `while`: dopoki warunek jest prawdziwy

`while` znaczy "dopoki". Powtarza wciety kod tak dlugo, jak podany warunek jest prawdziwy. Warunek jest sprawdzany przed kazdym obrotem, a nie tylko przy uruchomieniu petli.

Zacznijmy od wypisania trzech liczb:

```python
number = 1

while number <= 3:
    print(number)
    number += 1

print("Koniec")
```

Wynik:

```text
1
2
3
Koniec
```

W tym przykladzie potrzebujemy trzech rzeczy: poczatkowej wartosci `number`, warunku `number <= 3` i zmiany wartosci przez `number += 1`. `+= 1` oznacza tutaj to samo co `number = number + 1`.

### Co Python robi krok po kroku

| Krok | Wartosc przed sprawdzeniem | Warunek | Dzialanie |
|---|---:|---|---|
| 1 | 1 | `1 <= 3`, czyli `True` | wypisz 1, zwieksz number do 2 |
| 2 | 2 | `2 <= 3`, czyli `True` | wypisz 2, zwieksz number do 3 |
| 3 | 3 | `3 <= 3`, czyli `True` | wypisz 3, zwieksz number do 4 |
| 4 | 4 | `4 <= 3`, czyli `False` | nie wchodz do ciala petli, przejdz za nia |

Po kazdym wykonaniu ciala Python wraca do warunku. Instrukcja `print("Koniec")` nie jest wcieta do petli, wiec wykonuje sie dopiero po jej zakonczeniu. Po petli `number` nadal istnieje i w tym przykladzie ma wartosc `4`.

`while` samo nie zwieksza licznika. Nie musi on zreszta byc liczba: warunek moze zalezec od flagi logicznej albo informacji o dostepnosci kolejnych danych. Musimy jednak rozumiec, co moze zakonczyc powtarzanie.

### Cialo moze nie wykonac sie ani razu

```python
number = 5

while number <= 3:
    print("Wewnatrz petli")
    number += 1

print("Po petli")
```

Wynik to tylko `Po petli`. Python najpierw sprawdzil `5 <= 3`, otrzymal `False` i od razu pominal cale cialo. Nie zakladaj, ze instrukcja zapisana wewnatrz `while` na pewno zostanie wykonana.

## `for` a `while`: podobny wynik, inny sposob sterowania

Ten sam prosty wynik mozna uzyskac na dwa sposoby. Ponizsze przyklady sa alternatywami:

```python
for number in range(1, 4):
    print(number)
```

```python
number = 1

while number <= 3:
    print(number)
    number += 1
```

Oba wypisza `1`, `2`, `3`. W `for` kolejne wartosci pochodza z `range`. W `while` samodzielnie ustawiamy wartosc poczatkowa, sprawdzamy warunek i zmieniamy stan.

| Potrzeba | Zwykle wygodniejszy wybor |
|---|---|
| przejsc przez gotowa liste zamowien | `for order in orders` |
| wykonac znana liczbe powtorzen | `for` z `range` |
| powtarzac do zmiany stanu lub znalezienia konca danych | `while` |
| przegladac kolejne strony, dopoki sa dostepne | `while` albo inna konstrukcja sterujaca pobieraniem |

Nie wybieramy `while`, bo jest bardziej zaawansowane. Dla gotowej listy `for` zwykle jest czytelniejsze i nie wymaga recznego pilnowania indeksu. Przy `while` warunek moze zmieniac sie w sposob, ktorego nie da sie opisac sama liczba elementow z poczatkowej kolekcji.

## Warunek zakonczenia i petla nieskonczona

Gdyby w pierwszym przykladzie zabraklo `number += 1`, `number` pozostawaloby rowne `1`. Warunek `number <= 3` bylby stale prawdziwy i program wypisywalby `1` bez konca. To petla nieskonczona.

Samo wyrazenie `number + 1` tez nie wystarcza: oblicza nowa liczbe, ale nie przypisuje jej do `number`. Potrzebujemy przypisania albo innego zdarzenia zmieniajacego warunek.

Przed uruchomieniem `while` odpowiedz sobie na pytania:

1. Co jest sprawdzane przed obrotem?
2. Co zmienia sprawdzana wartosc lub stan?
3. Czy ta zmiana na pewno nastapi na kazdej potrzebnej sciezce?
4. Co wydarzy sie, gdy nie ma zadnych danych do przetworzenia?

Przypadkowa petle nieskonczona zatrzymasz przyciskiem Stop w PyCharmie albo zwykle `Ctrl+C` w terminalu. Nastepnie popraw przyczyne. Wielokrotne uruchamianie tego samego kodu nie zmieni jego warunku zakonczenia.

## `while True` i zakonczenie przez `break`

`True` jest zawsze prawdziwe, wiec samo `while True` nie zakonczy sie przez zmiane warunku. Mozemy jednak jawnie wyjsc przez poznane `break`:

```python
attempt = 1

while True:
    print(f"Proba numer {attempt}")

    if attempt == 3:
        break

    attempt += 1

print("Zakonczono proby")
```

Wynik to proby numer `1`, `2`, `3` i komunikat zakonczenia. Przy trzecim obrocie wykonuje sie `break`, wiec `attempt += 1` jest juz pominiete. Po petli `attempt` wynosi `3`.

To tylko demonstracja sterowania, nie rzeczywista obsluga ponawiania polaczen z API. Dla znanej liczby trzech powtorzen wystarczyloby `for`. `while True` przydaje sie wtedy, gdy sensowny test zakonczenia mozna wykonac dopiero po pewnej pracy w ciele petli. Zawsze wskaz miejsce, ktore moze zakonczyc taki przebieg.

## `continue` w `while`: uwazaj na aktualizacje stanu

W `while` `continue` wraca do sprawdzenia warunku. Nie zwieksza automatycznie licznika i nie pobiera nastepnego elementu za nas.

```python
number = 0

while number < 5:
    number += 1

    if number == 3:
        continue

    print(number)
```

Wynik:

```text
1
2
4
5
```

Zwiekszenie licznika jest przed `continue`. Dla `3` pomijamy tylko `print`; przy nastepnym obrocie licznik moze wzrosnac do `4`. Gdybysmy ustawili zwiekszanie dopiero za `continue`, po dojsciu do `3` moglibysmy ciagle pomijac aktualizacje i utknac w petli.

`continue` nie zmienia danych i nie usuwa elementu z kolekcji. Steruje tylko wykonaniem instrukcji. `break` wychodzi z petli, a `continue` rozpoczyna jej nastepne sprawdzenie.

## Przyklad z danymi: kolejne partie zamowien

Zalozmy, ze zrodlo zwraca kolejne partie zamowien, a pierwsza pusta partia oznacza koniec. Symulujemy to zwykla lista, bez plikow, API i dodatkowych bibliotek. W tej umowie partii po pierwszej pustej juz nie przetwarzamy.

```python
batches = [
    [{"order_id": 1}, {"order_id": 2}],
    [{"order_id": 3}],
    [],
    [{"order_id": 4}],
]

batch_index = 0
processed_orders_count = 0

while batch_index < len(batches):
    batch = batches[batch_index]

    if not batch:
        print("Brak kolejnej partii")
        break

    processed_orders_count += len(batch)
    print(f"Partia {batch_index + 1}: {len(batch)} zamowien")
    batch_index += 1

print(f"Przetworzono: {processed_orders_count}")
```

Wynik:

```text
Partia 1: 2 zamowien
Partia 2: 1 zamowien
Brak kolejnej partii
Przetworzono: 3
```

`batch_index` jest indeksem na liscie, dlatego zaczyna sie od `0`. `batch_index < len(batches)` chroni odczyt przed wyjsciem poza liste, takze gdy lista partii jest pusta. Do komunikatu dodajemy `1`, zeby czlowiek widzial partie numerowane od jedynki.

Pierwsze dwa obroty dodaja `2` i `1` do licznika. W trzecim pusta lista jest falszywa, wiec `if not batch` prowadzi do `break`. Zamowienie `4` nie jest przetwarzane zgodnie z ustalona zasada konca danych. Jesli zrodlo dopuszczaloby puste partie w srodku, potrzebowalibysmy innej reguly; nie pomijalibysmy reszty danych na slepo.

## Dodatkowo: `else` przy petli

Petla `while` moze miec `else`. To nie jest `else` od wewnetrznego `if`: stoi na poziomie wciecia `while`. Wykonuje sie, gdy warunek petli staje sie falszywy, ale nie po wyjsciu przez `break`.

```python
amounts = [50, 80, 120]
index = 0

while index < len(amounts):
    if amounts[index] >= 300:
        print("Znaleziono wysoka kwote")
        break

    index += 1
else:
    print("Nie znaleziono wysokiej kwoty")
```

Tutaj przejrzymy wszystkie wartosci, warunek indeksu ostatecznie bedzie falszywy i wypiszemy `Nie znaleziono wysokiej kwoty`. Zmien ostatnia kwote na `400`: zadziala `break`, a `else` zostanie pominiete. Dla pustej listy `else` wykona sie od razu. Podobne `else` moze wystapic po `for`, gdy zabraknie kolejnych elementow, bez wyjscia przez `break`.

To uzupelnienie, nie obowiazek uzywania `else` przy kazdej petli. Na poczatku najwazniejsze sa warunek, zmiana stanu, `break` i `continue`.

## Cwiczenia z `while`

1. Wypisz liczby od `5` do `1` malejaco, a po zakonczeniu napis `Start`. Uzyj `while`, nie `for`.
2. Dla `amounts = [100, 50, 200]` policz sume za pomoca `while` i indeksu. Ta sama wersja ma dzialac dla pustej listy i zwracac wtedy sume `0`.
3. Przejdz przez liczby od `1` do `6`, pomijajac wypisanie `2` i `5` za pomoca `continue`. Petla musi sie zakonczyc.
4. Dla listy zamowien z mini-cwiczenia ponizej znajdz pierwsze zamowienie `paid` o wartosci co najmniej `300`. Uzyj `while` i `break`; wypisz jego ID albo komunikat o braku dopasowania. Sprawdz tez pusta liste.
5. W przykladzie z partiami sprawdz trzy wejscia: brak partii, pusta pierwsza partia i dwie niepuste partie bez pustej na koncu. Poprawnie zakoncz kazdy przebieg, bez `IndexError` i bez zmiany listy wejsciowej.

## Gotowe agregacje: `sum`, `min`, `max`

Petla z akumulatorem pomaga zrozumiec obliczenie. Dla gotowej kolekcji liczb mozemy uzyc funkcji wbudowanych, bez importowania biblioteki.

```python
amounts = [100, 50, 200]

print(sum(amounts))
print(min(amounts))
print(max(amounts))
print(sum([]))
print(min([], default=None))
print(max([], default=None))
```

Wyniki: `350`, `50`, `200`, `0`, `None`, `None`. Domyslne `min([])` i `max([])` zglosilyby `ValueError`, bo nie ma elementu do wybrania. `default=None` okresla jawnie wynik braku danych; nie sluzy do naprawiania nieporownywalnych typow.

`sum` nie wybiera automatycznie kwot ze slownikow ani nie parsuje stringow z cenami. Najpierw trzeba wybrac odpowiednie wartosci. Przy pieniadzach zapis `sum(amounts, Decimal("0"))`, po imporcie `Decimal`, pozwala zachowac typ poczatkowej sumy takze dla pustego wejscia. To drugi argument `sum`, nie nazwa kolumny.

## `any` i `all`: czy pasuje jeden, czy kazdy

`any` sprawdza, czy przynajmniej jeden element jest prawdziwy w sensie logicznym. `all` wymaga prawdziwosci kazdego elementu. Nie musza to byc doslowne obiekty `True` i `False`, wiec trzeba uwazac na niepuste stringi.

```python
checks = [True, False, True]
print(any(checks))
print(all(checks))
print(any([]))
print(all([]))
print(all(["False"]))
```

Wyniki: `True`, `False`, `False`, `True`, `True`. Pusty zbior nie zawiera zadnego elementu spelniajacego warunek, ale tez zadnego, ktory go narusza. Dlatego biznesowa regula "niepusty koszyk i wszystkie pozycje poprawne" wymaga osobnego sprawdzenia niepustosci.

```python
orders = [{"status": "pending"}, {"status": "paid"}]
paid_flags = []

for order in orders:
    paid_flags.append(order["status"] == "paid")

print(any(paid_flags))
print(all(paid_flags))
```

Wynik: `True` i `False`. W 09 skrocimy samo budowanie listy flag przez comprehension. `any` i `all` moga zakonczyc przegladanie, gdy znaja wynik, ale wszystkie wyrazenia w przekazanej juz zbudowanej liscie zostaly wczesniej obliczone. `isinstance(value, str)` sprawdza, czy value jest stringiem. `all([isinstance(value, str), value.strip() != ""])` nie zabezpiecza przed `.strip()` na `None`, bo lista oblicza od razu takze drugi element. Do takiego zabezpieczenia nadaje sie krotko dzialajace `and`: `isinstance(value, str) and value.strip() != ""`; prawa strona jest sprawdzana tylko wtedy, gdy lewa jest prawdziwa.

## Mini-cwiczenie

Masz dane:

```python
orders = [
    {"order_id": 1, "total": 100, "status": "paid"},
    {"order_id": 2, "total": 200, "status": "cancelled"},
    {"order_id": 3, "total": 300, "status": "paid"},
]
```

Policz:

1. sume wszystkich zamowien,
2. sume zamowien `paid`,
3. liczbe zamowien `cancelled`.

## Najwazniejsze zasady

1. `if` wykonuje kod tylko wtedy, gdy warunek jest prawdziwy.
2. `else` oznacza "w przeciwnym razie".
3. `elif` pozwala sprawdzic kolejny warunek.
4. `for` przechodzi po elementach kolekcji.
5. Wciecia w Pythonie maja znaczenie.
6. Puste wartosci takie jak `None`, `""`, `0`, `[]` sa traktowane jak falsz.
7. `range()` pozwala przejsc po liczbach.
8. `enumerate()` daje indeks i element.
9. `continue` pomija reszte biezacego obrotu; w `while` wraca do warunku.
10. `break` konczy najblizsza petle.
11. `while` sprawdza warunek przed kazdym obrotem; moze nie wykonac sie ani razu.
12. Przy `while` pilnuj zmiany stanu lub jawnego warunku wyjscia przez `break`.
13. `while True` nie konczy sie samo przez warunek; potrzebuje zaplanowanego sposobu wyjscia.
14. `else` petli wykonuje sie po normalnym wyczerpaniu jej przebiegu, nie po `break`.

## Pytania kontrolne

1. Co robi `if`?
2. Czym rozni sie `=` od `==`?
3. Do czego sluzy `elif`?
4. Czym rozni sie `and` od `or`?
5. Co robi `for order in orders`?
6. Po co przed petla ustawiamy `total_revenue = 0`?
7. Czym rozni sie `continue` od `break`?
8. Co daje `range(5)`?
9. Po co uzywamy `enumerate()`?
10. Czym rozni sie pobieranie kolejnego elementu w `for` od sprawdzania warunku w `while`?
11. Ile razy wykona sie cialo `while`, jesli warunek od poczatku jest falszywy?
12. Dlaczego samo `number + 1` nie zmienia wartosci licznika?
13. Jak `continue` moze doprowadzic do nieskonczonej petli?
14. Co zakonczy pokazany przyklad `while True`?
15. Dlaczego w przykladzie partii nie przetwarzamy zamowienia o ID `4`?
16. Kiedy wykona sie `else` petli, a kiedy zostanie pominiete?
17. Gdzie zerujemy sume, jesli liczymy ja osobno dla kazdego zamowienia z pozycjami?
18. Co oznacza trzeci argument `range` i dlaczego nie moze byc zerem?
19. Co zwracaja `sum`, `min` i `max` dla pustej kolekcji?
20. Dlaczego `all([])` nie potwierdza, ze klient kupil przynajmniej jeden poprawny produkt?

## Dokumentacja do petli

- [Instrukcje while i for: warunki, break, continue i else](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)
