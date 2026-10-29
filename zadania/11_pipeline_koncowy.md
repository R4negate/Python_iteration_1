# Zadanie 10 - koncowy mini pipeline

## Cel zadania

Przygotuj mini pipeline w Pythonie, ktory:

1. bierze surowe dane zamowien,
2. waliduje rekordy,
3. czysci teksty,
4. zamienia typy danych,
5. tworzy nowe pola,
6. oddziela poprawne rekordy od blednych,
7. liczy metryki,
8. wypisuje raport tekstowy.

Nie czytaj jeszcze danych z plikow, API ani baz danych i nie uzywaj pandas. Sam kod podziel na pliki `.py`. Dane wejsciowe pozostaja lista w module `source_data.py`.

Pracujemy tylko na:

- zmiennych,
- typach danych,
- listach,
- slownikach,
- `if`,
- petlach,
- funkcjach,
- `try / except`,
- `raise`,
- f-stringach,
- `main()`.

Projekt wykonaj po lekcji 09. Dodaj do tego Decimal, importy wlasnych modulow, sety i comprehensions tam, gdzie upraszczaja wybor sprawdzonych danych. Walidacja i rozdzielanie odrzucen pozostaja zwykla petla.

## Dane wejsciowe

Skopiuj dane do pliku `.py`:

```python
raw_orders = [
    {
        "order_id": "1001",
        "customer_id": "1",
        "customer_name": " Anna Kowalska ",
        "country": " pl ",
        "quantity": "2",
        "unit_price": "49.99",
        "status": " Paid ",
        "email": " ANNA@example.COM ",
    },
    {
        "order_id": "1002",
        "customer_id": "2",
        "customer_name": "Jan Nowak",
        "country": "DE",
        "quantity": "1",
        "unit_price": "199.90",
        "status": "cancelled",
        "email": None,
    },
    {
        "order_id": "1003",
        "customer_id": "3",
        "customer_name": " Marta ",
        "country": " fr ",
        "quantity": "bad-data",
        "unit_price": "29.99",
        "status": "paid",
        "email": "marta@example.com",
    },
    {
        "order_id": "1004",
        "customer_id": "4",
        "customer_name": "Piotr Zielinski",
        "country": "",
        "quantity": "5",
        "unit_price": "15.50",
        "status": " pending ",
        "email": "   ",
    },
    {
        "order_id": "1005",
        "customer_id": "5",
        "customer_name": "Julia",
        "country": "PL",
        "quantity": "3",
        "unit_price": "120.00",
        "status": "PAID",
        "email": "julia@example.com",
    },
    {
        "order_id": "1006",
        "customer_id": "6",
        "customer_name": "Tomasz",
        "country": "ES",
        "quantity": "2",
        "unit_price": "abc",
        "status": "paid",
        "email": "tomasz@example.com",
    },
    {
        "order_id": "1007",
        "customer_id": "7",
        "customer_name": "Ewa",
        "country": None,
        "quantity": "1",
        "unit_price": "89.99",
        "status": "paid",
        "email": "ewa@example.com",
    },
]
```

## Wymagany wynik jednego poprawnego rekordu

Kazdy poprawny rekord w `clean_orders` ma miec postac:

```python
{
    "order_id": 1001,
    "customer_id": 1,
    "customer_name": "Anna Kowalska",
    "country": "PL",
    "quantity": 2,
    "unit_price": Decimal("49.99"),
    "order_value": Decimal("99.98"),
    "status": "paid",
    "email": "anna@example.com",
    "is_paid": True,
    "order_tier": "low",
}
```

W powyzszym przykladzie `Decimal` pochodzi z `decimal`. Nie tworz go z floata. Dla kazdego poprawnego rekordu buduj nowy slownik; raw_orders ma pozostac niezmienione.

## Zasady transformacji

### Identyfikatory

Zamien:

- `order_id` na `int`,
- `customer_id` na `int`.

### Teksty

Oczysc:

- `customer_name` przez `.strip()`,
- `country` przez `.strip().upper()`,
- `status` przez `.strip().lower()`,
- `email` przez `.strip().lower()`.

### Braki danych

Dla `country`:

- jezeli `country` to `None`, ustaw `"UNKNOWN"`,
- jezeli po `.strip()` country jest pusty tekst, ustaw `"UNKNOWN"`.

Brak klucza country tez oznacza UNKNOWN. Podany niepusty kraj jest stringiem.

Dla `email`:

- jezeli `email` to `None`, ustaw `"missing email"`,
- jezeli po `.strip()` email jest pusty tekst, ustaw `"missing email"`.

Brak klucza email tez oznacza missing email. Pozostale podane emaile sa stringami; kontrola poprawnosci adresu nie jest wymaganiem tego projektu.

### Liczby

Zamien:

- `quantity` na `int`,
- `unit_price` na `Decimal` bezposrednio z oczyszczonego tekstu, z obsluga kropki i przecinka.

Policz:

```python
order_value = quantity * unit_price
```

Unit_price i order_value zachowuja Decimal az do formatowania raportu. Ilosc musi byc dodatnia, a cena nieujemna. Zapis ceny moze byc bledny, ale poprawne liczby sa skonczone i maja najwyzej dwa miejsca po separatorze; nie ma NaN, Infinity ani notacji wykladniczej. W tym projekcie nie trzeba ustalac regul zaokraglania podatkow.

### Nowe pola

Dodaj `is_paid`:

- `True`, jezeli `status == "paid"`,
- `False` w pozostalych przypadkach.

Dodaj `order_tier`:

- `"high"`, jezeli `order_value >= 300`,
- `"standard"`, jezeli `order_value >= 100`,
- `"low"` w pozostalych przypadkach.

## Obsluga blednych rekordow

Rekord jest bledny, jezeli:

- nie da sie zamienic order_id, customer_id lub quantity na int,
- ID lub quantity nie sa dodatnie,
- nie da sie zamienic unit_price na Decimal albo cena jest ujemna,
- brakuje wymaganego pola,
- customer_name jest pusty po oczyszczeniu albo status po oczyszczeniu nie nalezy do paid, pending i cancelled.

Wymagane pola:

- `order_id`,
- `customer_id`,
- `customer_name`,
- `quantity`,
- `unit_price`,
- `status`.

Kazdy rekord jest slownikiem. Wymagane pola maja typ string; None lub inny typ to blad danych. Country i email sa opcjonalnymi stringami albo None. Sprawdz typ przed wywolaniem metody tekstowej. Nie ma duplikatow order_id, a jedno zamowienie opisuje jeden produkt z jedna iloscia i cena.

Blednych rekordow nie dodawaj do `clean_orders`.

Dodaj je do listy `invalid_orders`.

Odrzucenie ma zawierac row_number od 1, raw_order_id, error_type i reason. Nie poprawiaj surowego slownika przy zapisywaniu diagnostyki. Kazdy rekord ma trafic do dokladnie jednej listy, a blad jednego wiersza nie zatrzymuje pozostalych.

## Funkcje, ktore masz napisac

Napisz przynajmniej te funkcje:

```python
def normalize_text(value: str) -> str:
    ...


def normalize_country(country: str | None) -> str:
    ...


def normalize_email(email: str | None) -> str:
    ...


def parse_int(value: str) -> int:
    ...


def parse_decimal(value: str) -> Decimal:
    ...


def get_order_tier(order_value: Decimal) -> str:
    ...


def validate_order(raw_order: dict) -> None:
    ...


def transform_order(raw_order: dict) -> dict:
    ...


def calculate_metrics(clean_orders: list[dict], invalid_orders: list[dict]) -> dict:
    ...


def print_report(metrics: dict) -> None:
    ...
```

## Metryki do policzenia

Funkcja `calculate_metrics` ma zwrocic slownik z polami:

- `raw_orders_count`,
- `valid_orders_count`,
- `invalid_orders_count`,
- `paid_orders_count`,
- `cancelled_orders_count`,
- `pending_orders_count`,
- `paid_revenue`,
- `total_revenue`,
- `high_orders_count`,
- `unique_countries_count`.

`unique_countries_count` policz z uzyciem `set`.

Liczniki statusow i przychody obejmuja tylko clean_orders. Total_revenue sumuje wszystkie poprawne statusy, paid_revenue tylko paid. High_orders_count liczy wszystkie poprawne high bez wzgledu na status, a unique_countries_count obejmuje tez UNKNOWN, jesli wystapil. Puste listy daja zerowe liczniki i sumy Decimal("0"). Raw_orders_count = valid_orders_count + invalid_orders_count.

## Raport tekstowy

Funkcja `print_report` ma wypisac raport:

```text
Raw orders count: ...
Valid orders count: ...
Invalid orders count: ...
Paid orders count: ...
Cancelled orders count: ...
Pending orders count: ...
Paid revenue: ...
Total revenue: ...
High orders count: ...
Unique countries count: ...
```

Kwoty wypisz do 2 miejsc po przecinku.

## Struktura programu

Podziel kod na:

- `source_data.py`: raw_orders;
- `transformations.py`: oczyszczanie, walidacja i transformacja jednego rekordu;
- `metrics.py`: metryki i raport per kraj;
- `reporting.py`: funkcje wypisujace raporty;
- `main.py`: funkcja main laczaca etapy i blok startowy.

Import zadnego modulu nie moze wypisywac raportu. Uruchamiaj projekt z jego katalogu przez `python main.py` oraz `python -m main`.

W `main()`:

1. pobierz `raw_orders` z wlasnego modulu,
2. utworz puste listy `clean_orders` i `invalid_orders`,
3. przejdz petla po `raw_orders`,
4. dla kazdego rekordu:
   - uzyj `validate_order`,
   - uzyj `transform_order`,
   - poprawny rekord dodaj do `clean_orders`,
   - bledny rekord dodaj do `invalid_orders`,
5. policz metryki,
6. wypisz raport,
7. wypisz `clean_orders`,
8. wypisz `invalid_orders`.

Na koncu dodaj:

```python
if __name__ == "__main__":
    main()
```

## Dodatkowe wymaganie

Numeruj dane wejsciowe od 1, aby przypisac odrzuceniom pozycje zrodla. Raport per kraj wypisuj z par kraj-metryki. Nie uzywaj ogolnego `except Exception` do ukrywania bledow programisty. InvalidOperation z konwersji Decimal zamien w parserze na ValueError z czytelnym komunikatem, zachowujac przyczyne; na poziomie rekordu obsluguj oczekiwane KeyError, TypeError i ValueError.

## Raporty po walidacji

Z clean_orders zbuduj list comprehension liste ID poprawnych paid oraz dict comprehension indeks order_id -> order_value. ID sa juz unikalne. Osobno zwykla petla przygotuj paid_by_country z orders_count, unique_customers_count i revenue. Tworz grupy tylko dla krajow z paid, licz klientow unikalnie i uwzgledniaj zerowe zamowienia. Raport sortuj po kraju.

## Kontrola wyniku i warianty danych

Dla siedmiu rekordow z pliku program ma wyliczyc 5 poprawnych i 2 odrzucone, 3 paid, 1 cancelled, 1 pending, paid_revenue 549.97, total_revenue 827.37, 1 high i 3 unikalne kraje. Kwota 99.98 ma segment low. Wyniki kontrolne nie moga byc przypisane na sztywno.

Uruchom tez program dla pustej listy, samego poprawnego paid z cena "0.00", rekordu bez opcjonalnych country/email oraz rekordu bez wymaganego quantity. Przed i po transformacji porownaj raw_orders z niezalezna kopia; lista i jej rekordy maja zachowac oryginalne wartosci.

