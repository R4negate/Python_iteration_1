
## Zadanie 1. Klient jako obiekt

Napisz Customer(customer_id: int, name: str, country: str = "UNKNOWN"). Wymagaj dodatniego ID typu int, ale nie bool, i niepustej nazwy typu string po usunieciu brzegowych spacji. Country ma byc stringiem; po oczyszczeniu zapisz wielkimi literami, pusty zastap UNKNOWN. Niepoprawny typ zglasza TypeError, wartosc ValueError.

Dodaj is_core_market() zwracajaca bool dla krajow PL i DE. Utworz dwoch klientow, wypisz ich atrybuty i wynik metody. Zmiana danych jednego nie moze zmienic danych drugiego. Nie dodawaj atrybutow recznie dopiero po utworzeniu obiektu.

## Zadanie 2. Produkt i wartosc pozycji

Napisz Product(sku: str, unit_price: Decimal). SKU ma byc niepustym stringiem po oczyszczeniu; zapisz go wielkimi literami. Cena musi byc skonczonym nieujemnym Decimal. Metoda line_value(quantity: int) ma zwracac cene razy dodatnia ilosc typu int, ale nie bool.

Niepoprawny typ to TypeError, niepoprawna wartosc ValueError. Dodaj __repr__ pokazujace SKU i cene. Sprawdz produkt SQL po 49.90 z iloscia 2, zerowa cene, ujemna cene i ilosc True. Bledne proby obsluguj poza modelem.

## Zadanie 3. Zmiana statusu bez nieaktualnej flagi

Napisz PaymentOrder(order_id: int, amount: Decimal, status: str). ID ma byc dodatnim intem, nie boolem; amount skonczonym nieujemnym Decimal. Status po oczyszczeniu jest paid, pending albo cancelled; inny jest bledny.

Dodaj is_paid() i mark_paid(). Pierwsza metoda wylicza bool z aktualnego statusu. Druga ustawia paid, ale dla cancelled zglasza ValueError bez zmiany stanu. Powtorne mark_paid na paid niczego dodatkowo nie zmienia i zwraca None. Sprawdz pending -> paid, ponowne paid oraz cancelled. Nie zapisuj osobnej flagi is_paid w __init__.

## Zadanie 4. Dwie niezalezne partie

Wykorzystaj PaymentOrder z zadania 3. Napisz PaymentBatch(source: str), z osobna lista orders dla kazdej instancji. Metoda add(order) przyjmuje tylko PaymentOrder i dopisuje go bez kopiowania. Metoda paid_revenue() zwraca sume amount tylko paid, zaczynajac od Decimal("0"). Zduplikowane ID nie sa w tym zadaniu automatycznie usuwane.

Utworz partie web i mobile. Do web dodaj pending o kwocie 20 i paid o kwocie 0. Mobile ma pozostac pusta. Policz przychod web, zmien pierwsze zamowienie przez mark_paid i policz przychod jeszcze raz. Sprawdz, ze metryka korzysta z aktualnego stanu obiektu.

## Zadanie 5. Alias nie jest kopia klienta

Wykorzystaj Customer z zadania 1. Utworz klienta z krajem PL, alias wskazujacy na niego oraz niezaleznego klienta utworzonego z tych samych danych. Zmien country przez alias na DE. Wypisz kraje obu klientow, porownanie alias is customer i independent is customer. To zadanie celowo zmienia oryginal przez druga nazwe.

## Zadanie 6. Obiekty do raportu

Wykorzystaj Product z zadania 2 i produkty: PY po 80, SQL po 50, API po 80. Utworz nowa liste obiektow po cenie malejaco i SKU rosnaco przy remisie. Uzyj nazwanej funkcji key. Potem zbuduj liste nowych dictow sku/unit_price do raportu. Nie zmieniaj kolejnosci listy wejsciowej ani danych produktow; zmiana ceny w dictcie eksportu nie moze zmienic produktu.

## Zadanie 7. Rozszerzenie: alternatywne tworzenie klienta

Rozszerz Customer z zadania 1 o @classmethod from_raw(cls, raw). Wymagane id i name sa stringami, country opcjonalnym stringiem albo None. Brak/None/puste country daje UNKNOWN. Odczytaj ID jako int, a pozostala walidacje przeprowadz przez __init__. Metoda ma zwracac obiekt klasy otrzymanej jako cls.

Sprawdz {"id": "7", "name": " Anna ", "country": " pl "}, brak pola id i niepoprawny zapis ID. Nie przenos calej petli po danych do klasy Customer. To zadanie korzysta z dodatku o classmethod; mozna je wykonac na drugim spotkaniu.

## Zadanie 8. Pipeline z obiektami w modulach

Wykorzystaj PaymentOrder i PaymentBatch z zadan 3-4. Utworz katalog z models.py (obie klasy), transformations.py (order_from_raw), source_data.py (dane) i main.py. Import nie moze uruchamiac raportu.

```python
raw_orders = [
    {"id": "1", "amount": "25,50", "status": " PAID "},
    {"id": "2", "amount": "0", "status": "paid"},
    {"id": "3", "amount": "10", "status": "pending"},
    {"id": "4", "amount": "bad", "status": "paid"},
    {"id": "5", "status": "paid"},
]
```

Wszystkie rekordy sa dictami z unikalnymi ID. Wymagane id, amount i status maja byc stringami. Parser ma zamieniac ID na int, kwote na Decimal po usunieciu brzegowych spacji i zamianie przecinka na kropke. InvalidOperation zamien na ValueError z zachowana przyczyna. Model pilnuje pozostalych regul.

W main oddziel poprawne obiekty w partii od odrzucen z row_number, raw_id i reason. Jedno odrzucenie nie zatrzymuje procesu, a raw_orders pozostaje bez zmian. Wypisz liczbe poprawnych i blednych oraz przychod paid. Oczekuj 3 poprawnych, 2 blednych i 25.50 przychodu, ale oblicz to z danych. Pusty wsad ma dawac zerowe liczniki i Decimal("0").


## Zadanie 9. Przerób pipeline końcowy, który robiłeś na jedne z poprzednich zajęć tak, żeby wykorzystywał obiektowość