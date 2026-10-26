# Zadania 08 - mini pipeline na listach i slownikach

Zadania 1-14 skladaja sie na jeden program. Korzystaj z lekcji 01-08, zwyklych petli, funkcji i obslugi wyjatkow. Nie potrzebujesz comprehensions. W tej wersji kwoty sa typu float jak w lekcji 08; w projekcie koncowym wrocimy do Decimal.

W teorii pokazano rowniez uproszczony wariant zamieniajacy zly zapis na zero. Tutaj od poczatku budujesz wersje z odrzuceniami: bledna wymagana kwota nie staje sie zerowa sprzedaza.

Uzyj danych:

```python
raw_orders = [
    {"id": "1", "country": " pl ", "amount": "120.50", "status": "paid"},
    {"id": "2", "country": "DE", "amount": "80", "status": "cancelled"},
    {"id": "3", "country": None, "amount": "200", "status": "paid"},
    {"id": "4", "country": " fr ", "amount": "bad-data", "status": "paid"},
    {"id": "5", "country": "PL", "amount": "300", "status": "pending"},
    {"id": "6", "country": "   ", "amount": "0", "status": " PAID "},
    {"id": "7", "country": "PL", "status": "paid"},
]
```

## Kontrakt wspolny dla wszystkich etapow

- Kazdy element to dict. Wymagane pola to id, amount i status; country jest opcjonalne.
- ID jest stringiem z poprawnym zapisem dodatniego inta. Amount jest stringiem z kropka lub przecinkiem; moze miec zly zapis, byc puste albo go brakowac. Poprawna kwota jest nieujemna, zero jest dozwolone.
- Status to wymagany string, po oczyszczeniu paid, pending albo cancelled. Inny status odrzuca rekord.
- Country jest stringiem albo None. Brak, None i pusty tekst po oczyszczeniu daja UNKNOWN.
- Poprawne kwoty w tym zestawie maja skonczona wartosc; nie ma zapisow NaN ani Infinity. Kazdy rekord trafia dokladnie do jednej listy: clean_orders albo invalid_orders.
- Zachowaj kolejnosc danych i nie zmieniaj raw_orders. Odrzucenie zawiera row_number od 1, raw_id oraz reason. Kwoty i typy w pozostalych zadaniach odczytuj z tego kontraktu.

## Zadanie 1

Napisz funkcje:

```python
def parse_amount(raw_amount: str) -> float:
    ...
```

Funkcja ma:

- oczyscic tekst z brzegowych spacji i zamienic przecinek na kropke,
- zamienic tekst na `float`,
- zglosic ValueError dla pustego tekstu, blednego zapisu lub kwoty ujemnej; nie zwracac zastepczego zera.

## Zadanie 2

Napisz funkcje:

```python
def normalize_country(country: str | None) -> str:
    ...
```

Zasady:

- jezeli `country` to `None` lub pusty tekst po oczyszczeniu, zwroc `"UNKNOWN"`,
- w pozostalych przypadkach usun spacje i zamien tekst na wielkie litery.

## Zadanie 3

Napisz funkcje:

```python
def get_order_tier(amount: float) -> str:
    ...
```

Zasady:

- `high`, jezeli `amount >= 200`,
- `standard` w pozostalych przypadkach.

## Zadanie 4

Napisz funkcje:

```python
def transform_order(raw_order: dict) -> dict:
    ...
```

Funkcja ma zwrocic slownik z polami:

- `order_id` jako `int`,
- `country`,
- `amount`,
- `status`,
- `order_tier`.

Status oczysc z brzegowych spacji i zapisz malymi literami. Przed transformacja sprawdz obecnosc wymaganych pol i dopuszczalny status. Brak pola ma zglosic KeyError, niepoprawny status ValueError. Dla niepoprawnej kwoty przekaz wyjatek z parsera do wywolujacego.

## Zadanie 5

Przetworz cala liste `raw_orders` do list `clean_orders` i `invalid_orders`.

Kazdy element w `clean_orders` ma byc wynikiem funkcji `transform_order`. Oczekiwane KeyError i ValueError obsluguj dla pojedynczego rekordu. Po odrzuceniu przechodz do kolejnego; nie przechwytuj wszystkich Exception.

## Zadanie 6

Policz metryki:

- `orders_count`,
- `paid_orders_count`,
- `cancelled_orders_count`,
- `paid_revenue`,
- `high_orders_count`.

`orders_count` obejmuje tylko poprawne rekordy, `high_orders_count` wszystkie poprawne ze statusem dowolnym i kwota co najmniej 200. Przychod paid sumuje tylko poprawne paid, rowniez o wartosci zero.

## Zadanie 7

Wypisz raport tekstowy przez f-string w formacie:

```text
Orders count: ...
Paid orders count: ...
Cancelled orders count: ...
Paid revenue: ...
High orders count: ...
```

`paid_revenue` wypisz z dokladnoscia do 2 miejsc po przecinku.

## Zadanie 8

Dodaj funkcje:

```python
def calculate_metrics(clean_orders: list[dict]) -> dict:
    ...
```

Funkcja ma zwrocic slownik z metrykami z zadania 6.

## Zadanie 9

Dodaj funkcje `main()`, ktora:

1. tworzy `raw_orders`,
2. tworzy `clean_orders` i `invalid_orders`,
3. liczy metryki,
4. wypisuje raport.

Na koncu pliku dodaj:

```python
if __name__ == "__main__":
    main()
```

## Zadanie 10 - Audyt odrzucen

Wypisz osobny raport odrzucen z numerem wiersza, surowym ID i powodem. Nie wywoluj ponownie transformacji tylko po to, aby wygenerowac raport. Odrzucenia zachowuja kolejnosc danych wejsciowych.

Sprawdz, ze rekord z amount rownym `"0"` nie pojawia sie w odrzuceniach, a rekordy ze zlym zapisem i brakiem amount nie pojawiaja sie w clean_orders.

## Zadanie 11

Rozszerz raport o:

- liczbe poprawnych zamowien,
- liczbe blednych zamowien,
- laczna wartosc poprawnych zamowien.

## Zadanie 12 - Metryki pustego wsadu

Uruchom te same funkcje dla pustej listy. Wszystkie liczniki i sumy maja wynosic zero, obie listy wynikowe maja byc puste. Nie dodawaj fikcyjnych rekordow, aby ominac problem pustych danych.

## Zadanie 13 - Raport per kraj

Napisz funkcje zwracajaca `paid_by_country`: dla kazdego kraju z przynajmniej jednym poprawnym paid podaj `orders_count` i `revenue`. Uwzglednij UNKNOWN oraz zerowe paid. Wypisz grupy w kolejnosci krajow rosnaco, z kwotami do dwoch miejsc.

## Zadanie 14 - Kontrola bilansu

Zbuduj slownik `quality_summary` z liczba raw, clean i invalid oraz flaga `is_balanced`, ktora sprawdza raw = clean + invalid. Dla zrodlowych danych oczekuj 7 / 5 / 2, paid_orders_count = 3, high_orders_count = 2 i paid_revenue po sformatowaniu `320.50`. To wartosci kontrolne: program ma je obliczyc, nie przypisac na sztywno.

