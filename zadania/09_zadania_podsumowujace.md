# Zadania 09 - podsumowanie iteracji

To zestaw przekrojowy po lekcjach 01-09, nie zestaw do samej lekcji 09. Comprehensions cwicz najpierw w `09_list_comprehensions.md`. Zadania 1-4 korzystaja z klientow z zadania 1 i zamowien z zadania 2; kolejne sa ich rozszerzeniem. Odpowiedzia jest kod, a surowe dane maja pozostac bez zmian.

## Zadanie 1

Masz liste klientow:

```python
customers = [
    {"customer_id": 1, "name": " Anna ", "country": "pl", "email": "anna@example.com"},
    {"customer_id": 2, "name": "Jan", "country": "DE", "email": None},
    {"customer_id": 3, "name": "Marta", "country": " fr ", "email": "marta@example.com"},
]
```

Przygotuj liste `clean_customers`, gdzie:

- `name` jest bez spacji,
- `country` jest wielkimi literami,
- `email` ma wartosc `"missing email"`, jesli bylo `None`.

W pozostalych przypadkach email oczysc z brzegowych spacji i zapisz malymi literami. Buduj nowe slowniki. Wszystkie pokazane pola sa wymagane, country i name sa stringami, email stringiem albo None.

## Zadanie 2

Masz liste zamowien:

```python
orders = [
    {"order_id": 1001, "customer_id": 1, "amount": 120, "status": "paid"},
    {"order_id": 1002, "customer_id": 2, "amount": 80, "status": "cancelled"},
    {"order_id": 1003, "customer_id": 1, "amount": 200, "status": "paid"},
]
```

Policz laczna wartosc zamowien `paid`.

## Zadanie 3

Napisz funkcje `get_customer_orders(customer_id: int, orders: list[dict]) -> list[dict]`.

Funkcja ma zwrocic tylko zamowienia wskazanego klienta.

## Zadanie 4

Napisz funkcje `build_customer_summary(customer: dict, orders: list[dict]) -> dict`.

Wynik ma zawierac:

- `customer_id`,
- `name`,
- `orders_count`,
- `paid_revenue`.

Funkcja uwzglednia tylko zamowienia wskazanego klienta, a orders_count liczy wszystkie jego statusy. Dla klienta bez zamowien zwroc zerowe metryki. Przekazuj oczyszczonego klienta; zachowaj wszystkich klientow z zadania 1.

## Zadanie 5 - Podsumowanie wszystkich klientow

Wykorzystaj wczesniejsze funkcje i utworz liste podsumowan kazdego klienta, takze bez zamowien. Do kazdego rekordu dodaj country i `customer_status`: buyer, gdy klient ma dowolne zamowienie, lub no_orders. Posortuj przychod malejaco, a przy remisie ID rosnaco, bez zmiany list wejsciowych.

## Zadanie 6 - Indeks i brak dopasowania

Zbuduj przez dict comprehension indeks oczyszczonych klientow po ID. Dopisz do osobnej kopii listy zamowien rekord `{"order_id": 1004, "customer_id": 999, "amount": 50, "status": "paid"}`. Oddziel zamowienia z nieznanym klientem do nowej listy; nie dopisuj fikcyjnego klienta do indeksu i nie zmieniaj danych z zadania 2.

## Zadanie 7 - Kraj jako poziom agregacji

Na podstawie pierwotnych klientow i zamowien z zadan 1-2 przygotuj raport per kraj z `customers_count`, `paying_customers_count`, `paid_orders_count` i `paid_revenue`. Uwzglednij wszystkich klientow, nawet bez paid. Liczba placacych to unikalni klienci z paid, nie liczba ich zamowien. Wypisz kraje rosnaco.

## Zadanie 8 - Raport w modulach

Podziel rozwiazanie na `source_data.py`, `transformations.py`, `metrics.py`, `reporting.py` i `main.py`. Import nie moze uruchamiac raportu. Main ma laczyc etapy, a funkcje metryk zwracac dane. Program ma dzialac przez `python main.py` i `python -m main` z katalogu projektu. Nie czytaj jeszcze CSV ani JSON z dysku.

## Zadanie 9 - Zachowanie przy pustych danych

Uruchom funkcje dla pustej listy zamowien przy niepustych klientach, a potem dla obu list pustych. W pierwszym wariancie kazdy klient ma status no_orders i zerowe metryki; w drugim raporty sa puste. Jesli dodasz srednia wartosc zamowienia klienta, brak zamowien ma dawac None, a nie dzielenie przez zero.

## Zadanie 10 - Inny raport z tych samych danych

Z oczyszczonych klientow zbuduj przez list comprehension nowe rekordy `customer_id`, `name`, `email` tylko dla klientow z podanym adresem. W tej wersji brak rozpoznajesz po ustalonym znaczniku `missing email`. Zbuduj tez set ich krajow i wypisz go jako posortowana liste. Nie zmieniaj wynikow raportu aktywnosci: lista odbiorcow jest osobnym produktem tych samych danych.

