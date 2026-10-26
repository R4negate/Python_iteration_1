# Zadania 09 - comprehensions i ksztalt wyniku

Po lekcjach 01-09. Kazde zadanie zakoncz dzialajacym kodem, bez opisowych odpowiedzi. Nie wpisuj wynikow na sztywno. W zadaniach 1-10 uzywaj wspolnych danych ponizej, a w pozostalych podanych osobno. Nie zmieniaj wejscia.

Wspolny kontrakt: ID sa unikalnymi intami, statusy poprawnymi tekstami, kwoty nieujemnymi intami, country stringiem albo None. Brak country i pusta lista sa dozwolone. Tutaj dane sa juz sprawdzone; obsluga niepoprawnych rekordow nie jest ukrytym wymaganiem.

```python
orders = [
    {"id": 101, "customer_id": 1, "status": "paid", "amount": 120, "country": " pl "},
    {"id": 102, "customer_id": 2, "status": "pending", "amount": 80, "country": "DE"},
    {"id": 103, "customer_id": 1, "status": "paid", "amount": 0, "country": None},
    {"id": 104, "customer_id": 3, "status": "paid", "amount": 300, "country": "PL"},
    {"id": 105, "customer_id": 2, "status": "cancelled", "amount": 50},
]
```

## Zadanie 1 - Ten sam wynik, dwa zapisy

Zbuduj liste wszystkich ID zwykla petla i list comprehension. Wypisz obie i wynik ich porownania. Zachowaj kolejnosc oraz powtorzenia, jezeli pojawia sie po zmianie danych.

## Zadanie 2 - Tylko oplacone

Utworz przez list comprehension `paid_ids` oraz `large_paid_ids`. Pierwsza lista zawiera wszystkie paid, druga tylko paid z kwota co najmniej 100. Poprawne zero przechodzi do pierwszej, ale nie do drugiej listy.

## Zadanie 3 - Nowy rekord zamiast ID

Zbuduj przez list comprehension nowe slowniki zawierajace `id`, `customer_id`, `amount` i `is_paid`. Zachowaj kazde zamowienie, takze pending i cancelled; flaga nie jest filtrem. Pole status nie ma przechodzic do wyniku.

## Zadanie 4 - Etykieta dla kazdego

Przygotuj liste etykiet high dla kwoty co najmniej 200 i standard dla nizszej. Lista ma miec tyle elementow co orders. Osobno przygotuj taka sama segmentacje, ale tylko dla paid. Zastosuj wybor wartosci przez if/else i filtr zgodnie z ich roznymi rolami.

## Zadanie 5 - Normalizacja opcjonalnego kraju

Zbuduj nowe rekordy z `id` i `country`. Brak, None i pusty tekst po oczyszczeniu maja dac UNKNOWN; inne stringi oczysc i zapisz wielkimi literami. Nie odrzucaj zamowien z brakujacym krajem. Mozesz wykorzystac funkcje pomocnicza, a kolekcje zbuduj comprehension.

## Zadanie 6 - Znane rynki paid

Przygotuj set unikalnych oczyszczonych krajow wystepujacych w paid. Pomijaj brak, None i pusty tekst po oczyszczeniu. Nie dodawaj UNKNOWN. Wypisz wynik jako posortowana liste.

## Zadanie 7 - Indeks po identyfikatorze

Zbuduj dict comprehension `paid_amount_by_id`, ktore mapuje ID paid na kwote. Odczytaj przez ten indeks kwote ID 103 oraz opcjonalnie ID 999 z domyslnym None. ID sa unikalne, wiec zadanie nie wymaga agregacji.

## Zadanie 8 - Kolekcja przed metryka

Wybierz list comprehension kwoty paid. Na jej podstawie oblicz sume, minimum, maksimum i srednia. Dla braku paid suma wynosi 0, a pozostale metryki None. Nie wykluczaj zera przez warunek prawdziwosci kwoty.

## Zadanie 9 - Flagi i pusty eksport

Przygotuj liste flag `is_paid` dla wszystkich zamowien. Oblicz `has_paid`, `all_paid` i `can_publish_paid_only`. Ostatnia flaga oznacza niepusty eksport zawierajacy wylacznie paid. Sprawdz tez orders = []; nie zastepuj znaczenia all dla pustej listy.

## Zadanie 10 - Numer wiersza a ID

Utworz dict comprehension z numerem wiersza od 1 jako kluczem i biznesowym ID jako wartoscia. Zbuduj tez liste nowych rekordow z `row_number`, `id` i `status`, zachowujac kolejnosc wejscia.

## Zadanie 11 - Jedno zamowienie, wiele pozycji

```python
orders_with_items = [
    {"id": 1, "status": "paid", "items": [{"sku": "SQL", "quantity": 2}, {"sku": "PY", "quantity": 1}]},
    {"id": 2, "status": "cancelled", "items": [{"sku": "SQL", "quantity": 4}]},
    {"id": 3, "status": "paid", "items": []},
]
```

Zbuduj przez comprehension plaska liste nowych rekordow `order_id`, `sku`, `quantity` tylko z paid. Jeden wynik to jedna pozycja, nie jedno zamowienie. Puste items nie tworza rekordu. Zbuduj ta sama liste dwiema zwyklymi petlami i porownaj wyniki.

## Zadanie 12 - Ostatnia wartosc a suma

```python
rows = [{"id": 1, "amount": 10}, {"id": 1, "amount": 20}, {"id": 2, "amount": 0}]
```

Przygotuj `last_amount_by_id` przez dict comprehension, a osobno `total_amount_by_id` zwykla petla z akumulacja. Wypisz oba wyniki. Kazdy ma zachowac klucz 2 z zerem; pierwszy nie moze udawac sumowania duplikatow.

## Zadanie 13 - Nowa lista, niezalezne rekordy

```python
source = [{"id": 1, "status": "paid"}, {"id": 2, "status": "pending"}]
```

Zbuduj liste `selected` zawierajaca stare rekordy paid oraz `independent`, ktora zawiera nowe slowniki z tymi samymi polami. Zmien status w independent na archived. Source ma pozostac niezmienione. Wypisz tozsamosc pierwszego rekordu selected i source oraz independent i source.

## Zadanie 14 - Walidacja nie znika po poznaniu skrotu

```python
raw_amounts = ["10", "abc", "0", "20"]
```

Zwykla petla z try/except ma rozdzielic dane na poprawne floaty i odrzucenia z numerem wiersza oraz surowym tekstem. Dopiero po walidacji zbuduj list comprehension etykiety positive lub zero dla poprawnych wartosci. Oblicz tez ich sume. Przetworz wszystkie elementy i zachowaj poprawne zero.

## Sprawdzenie wlasnego rozwiazania

Uruchom zadania ze wspolnym zrodlem takze dla pustej listy. Listy, sety i dicty maja byc odpowiednio puste, bez fikcyjnych elementow. Zadania z minimum i srednia zachowuja ustalone None. Source i orders nie moga zostac zmienione przez transformacje.
