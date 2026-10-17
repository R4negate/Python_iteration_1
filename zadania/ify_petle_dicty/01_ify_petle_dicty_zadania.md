# 100 zadan - ify, petle, dicty i zagniezdzone kolekcje

## Jak pracowac z zestawem

Kazde zadanie jest niezalezne. Zacznij od podanych danych i napisz skrypt, ktory tworzy wskazany wynik. Nie wpisuj odpowiedzi na sztywno: kod ma dzialac takze po zmianie danych zgodnie z opisanym kontraktem.

Zakres: lekcje `01_typy_danych.md` - `05_if_petle_i_logika.md`. Nie potrzebujesz klas, plikow, API, pandas, wyrazen skladanych ani `try/except`. Obliczenia i przeksztalcenia wykonuj zwyklymi petlami i warunkami. `Decimal` jest dozwolony, bo wystapil w lekcji 01.

### Kontrakt danych: co jest obowiazkowe, a co opcjonalne?

- Jesli nie zaznaczono inaczej, pokazane klucze sa wymagane, a typy danych zgodne z przykladem. Pobieraj wymagane pola przez `[]`.
- Pole opcjonalne moze nie istniec. Stosuj `.get()` lub sprawdzenie `in` zgodnie z poleceniem.
- `.get("field", default)` nie zastepuje istniejacego `None` wartoscia domyslna. O tym, jak traktowac `None`, decyduje kontrakt konkretnego zadania.
- `0` i `False` nie oznaczaja automatycznie braku danych. Nie odrzucaj ich przez przypadek warunkiem `if value`.
- Przy pustych danych wynik ma pozostac poprawny: pusta lista lub slownik, zerowy licznik, a przy braku sredniej/minimum/maksimum `None`, o ile zadanie nie podaje innej zasady.

## A. Przygotowanie danych i reguly biznesowe

### Zadanie 001 - Zamowienia gotowe do rozliczenia

```python
orders = [
    {"id": 1, "status": " PAID ", "amount": "120,50", "country": " pl "},
    {"id": 2, "status": "pending", "amount": "80.00", "country": "DE"},
    {"id": 3, "status": "paid", "amount": "0", "country": None},
    {"id": 4, "status": "paid", "amount": None},
]
```

Przygotuj liste clean_orders: nowe dicty z id, status zapisanym malymi literami, country wielkimi literami i amount typu float. Teksty oczysc z brzegowych bialych znakow. Country jest opcjonalnym stringiem albo None; brak, None i pusty tekst po oczyszczeniu daja UNKNOWN. Amount jest opcjonalnym stringiem albo None; brak, None i pusty tekst po oczyszczeniu odrzucaja rekord. Pozostale kwoty maja poprawny nieujemny zapis z kropka lub przecinkiem. Status jest wymaganym stringiem; dopuszczamy w danych paid, pending i cancelled po normalizacji. Wynik obejmuje clean_orders, rejected_ids oraz paid_by_country z liczba i suma kwot poprawnych paid. Tworz grupy tylko dla krajow majacych poprawne paid, takze zerowe. Nie zmieniaj orders.

### Zadanie 002 - Lista kontaktow do kampanii

```python
customers = [
    {"id": 1, "name": " Anna ", "contact": {"email": " A@demo.pl "}, "consent": True},
    {"id": 2, "name": "Jan", "contact": None, "consent": True},
    {"id": 3, "name": "Eva", "contact": {"email": "a@demo.pl"}, "consent": True},
    {"id": 4, "name": "Ola", "contact": {"email": "o@demo.pl"}, "consent": False},
]
```

Zbuduj liste recipients z id, name i email. Imie i email oczysc z brzegowych bialych znakow, email zapisz malymi literami. Opcjonalne consent jest boolem albo None; tylko True uprawnia do kontaktu. Opcjonalne contact jest dictem albo None, a jego opcjonalne email stringiem albo None. Uproszczona kontrola adresu wymaga jednego @ oraz dwoch niepustych czesci; dane nie zawieraja bialych znakow wewnatrz adresow. Zachowaj pierwszego uprawnionego klienta danego oczyszczonego adresu. Zbuduj tez trzy rozlaczne listy ID: no_consent_ids, invalid_email_ids i duplicate_email_ids. Kazdy odrzucony klient trafia tylko do pierwszej pasujacej kategorii w tej kolejnosci. Odrzucone rekordy nie zajmuja adresu w recipients.

### Zadanie 003 - Waluta zamowienia i zgodnosc rynku

```python
defaults = {"currency": "PLN"}
markets = {"PL": {"PLN"}, "DE": {"EUR"}, "US": {"USD", "EUR"}}
orders = [
    {"id": 1, "country": " pl "},
    {"id": 2, "country": "DE", "currency": " eur "},
    {"id": 3, "country": "US", "currency": None},
    {"id": 4, "country": "DE"},
]
```

Dla kazdego zamowienia ustal currency: brak klucza oznacza walute z defaults, a None lub pusty tekst po oczyszczeniu UNKNOWN. Podane waluty i kraje sa stringami; oba pola oczysc i zapisz wielkimi literami. Utworz rekordy id, country, currency i can_settle. Rozliczenie jest mozliwe tylko dla pary kraj-waluta dopuszczonej przez markets; nieznany kraj albo waluta daje False. Zbuduj tez unsettled_count_by_country dla wszystkich krajow z orders, z zerem tam, gdzie kazde zamowienie mozna rozliczyc.

### Zadanie 004 - Jakosc adresow klienta

```python
customers = [
    {"id": 1, "addresses": [{"type": "delivery", "country": " pl "}]},
    {"id": 2, "addresses": []},
    {"id": 3, "addresses": [{"type": "billing", "country": "DE"},
                          {"type": "delivery", "country": None}]},
    {"id": 4},
]
```

Utworz raport z customer_id, delivery_country i address_status. Addresses jest opcjonalna lista dictow; brak listy oznacza pusta liste. Pole type jest wymaganym stringiem, a country opcjonalnym stringiem albo None. Rozpatruj pierwszy adres z type rownym delivery. Brak takiego adresu daje missing_delivery. Brak country, None albo pusty tekst po oczyszczeniu w wybranym adresie daje missing_country. W pozostalych przypadkach ustaw ready i zapisz oczyszczony kraj wielkimi literami. W stanach innych niz ready delivery_country wynosi None. Nie szukaj kolejnego adresu, gdy pierwszy delivery ma brakujacy kraj. Podsumuj liczbe klientow w kazdym z trzech statusow.

### Zadanie 005 - Czy limit zostal podany?

```python
accounts = [
    {"id": 1}, {"id": 2, "limit": None}, {"id": 3, "limit": 0},
    {"id": 4, "limit": False}, {"id": 5, "limit": 150},
]
transactions = [{"account_id": 1, "amount": 20}, {"account_id": 3, "amount": 1},
                {"account_id": 5, "amount": 100}, {"account_id": 5, "amount": 60},
                {"account_id": 2, "amount": 10}, {"account_id": 4, "amount": 10}]
```

Brak limit oznacza poczatkowy limit 100. None oznacza konto zablokowane do transakcji. Nieujemny int niebedacy boolem oznacza konkretny limit; pozostale wartosci oznaczaja niepoprawne konto. ID kont sa unikalne, wszystkie account_id istnieja, a kwoty transakcji sa dodatnimi intami. Obsluz transakcje w kolejnosci. Priorytet decyzji to invalid_account, blocked_account, insufficient_limit, accepted. Tylko zaakceptowana transakcja pomniejsza pozostaly limit. Przygotuj decyzje z transaction_index, account_id, amount i decision oraz raport wszystkich kont z account_id, account_state i remaining_limit. Account_state to ready, blocked albo invalid. Dla blocked i invalid pozostaly limit wynosi None; dla ready jest liczba, takze zero.

### Zadanie 006 - Kontrola ksztaltu rekordow

```python
schema = {"id": int, "name": str, "active": bool, "tags": set}
records = [
    {"id": 1, "name": "Anna", "active": True, "tags": {"vip"}},
    {"id": True, "name": "Jan", "active": 1, "tags": ["new"]},
    {"id": 3, "name": None, "tags": set(), "debug": "trace"},
]
```

Dla kazdego rekordu utworz raport z row_index, missing_fields, wrong_type_fields, unexpected_fields i is_valid. Schema okresla wymagany dokladny typ kazdego pola. None nie spelnia zadnego z pokazanych typow, a bool nie spelnia wymagania int. Brakujacego pola nie zglaszaj ponownie jako blednego typu. Nazwy w trzech kolekcjach diagnostycznych nie musza byc uporzadkowane. Is_valid jest True tylko wtedy, gdy wszystkie trzy kolekcje sa puste. Podsumuj liczbe poprawnych i niepoprawnych rekordow.

### Zadanie 007 - Kalkulacja koszyka z tekstowych pozycji

```python
baskets = [
    {"id": 1, "lines": [{"sku": "A", "qty": " 2 ", "price": "19,50"},
                        {"sku": "B", "qty": "1", "price": "10.00"}]},
    {"id": 2, "lines": [{"sku": "C", "qty": "0", "price": "5"}]},
    {"id": 3, "lines": []},
]
```

Qty ma poprawny tekstowy zapis nieujemnej liczby calkowitej, a price nieujemnej liczby dziesietnej. Po oczyszczeniu spacji i ujednoliceniu separatora przygotuj nowe koszyki z id, lines, total_units i basket_value. Kazda pozycja lines zawiera sku, qty jako int, price jako float i line_value jako wartosc calej pozycji. Nie usuwaj zerowych pozycji ani pustych koszykow. Przygotuj tez komunikaty z ID i wartoscia koszyka pokazana do dwoch miejsc po kropce. Baskets i zawarte w nich slowniki maja pozostac bez zmian.

### Zadanie 008 - Zgody z dwoch systemow

```python
updates = [
    {"id": 1, "source": "shop", "consent": " TRUE "},
    {"id": 1, "source": "crm", "consent": "false"},
    {"id": 2, "source": "shop", "consent": "yes"},
    {"id": 2, "source": "crm", "consent": None},
    {"id": 3, "source": "shop", "consent": "false"},
]
```

Rozpoznawaj tylko teksty true i false bez wzgledu na wielkosc liter i spacje. Pozostale wartosci oznaczaja nierozpoznana decyzje i nie zastepuja juz znanej zgody. Dla kazdego klienta zachowaj ostatnia rozpoznana decyzje; jesli zadnej nie bylo, zapisz None. Raport ma zawierac id, consent, source ostatniej rozpoznanej decyzji albo None oraz liczbe nierozpoznanych wpisow klienta.

### Zadanie 009 - Dokladne rozliczenie dziesietne

```python
payments = [
    {"customer_id": 1, "amount": "0.1"}, {"customer_id": 1, "amount": "0.2"},
    {"customer_id": 2, "amount": "10.00"}, {"customer_id": 2, "amount": "-2.50"},
]
expected = {1: "0.30", 2: "7.50"}
```

Przygotuj rozliczenie per customer_id z float_total, decimal_total, float_matches i decimal_matches. Pierwsza suma jest floatem, druga Decimal. Flagi oznaczaja dokladna rownosc sumy z oczekiwana kwota przekonwertowana na ten sam typ; nie chodzi o zgodnosc tekstow po zaokragleniu. Ujemna kwota oznacza zwrot i pomniejsza sume. Kwoty sa poprawnymi tekstami liczbowymi. Expected zawiera oczekiwanie dla kazdego klienta z payments; raport obejmuje tylko klientow majacych platnosci. Zbuduj tez liste ID klientow, dla ktorych obie flagi maja rozne wartosci. Obliczenia dziesietne maja zachowywac precyzje tekstowego wejscia.

### Zadanie 010 - Snapshot przed aktualizacja

```python
orders = [
    {"id": 1, "status": "new", "tags": ["web"], "items": [{"sku": "A", "qty": 1}]},
    {"id": 2, "status": "paid", "tags": [], "items": []},
]
changes = [
    {"id": 1, "status": "paid", "tag": "priority", "sku": "A", "qty": 3},
    {"id": 1, "status": "cancelled", "tag": "do_not_apply", "sku": "X", "qty": 1},
    {"id": 99, "status": "paid", "tag": "orphan", "sku": "A", "qty": 4},
]
```

Utworz niezalezny snapshot orders, a nastepnie wprowadz zmiany do oryginalnej listy. Zmiana ustawia status, dopisuje tag, jesli jeszcze go nie ma, i zmienia ilosc wskazanego SKU. Zmiane z nieznanym ID albo SKU odrzuc w calosci i zapisz w raporcie bledow; nie moze ona zmienic takze statusu ani tagow. W obrebie zamowienia SKU jest unikalny. Snapshot, lacznie z tagami i dictami pozycji, ma zachowac stan sprzed aktualizacji. Zbuduj raport poprawnych zmian zawierajacy stare i nowe ilosci.

## B. Obliczenia z ograniczeniami biznesowymi

### Zadanie 011 - Wydawanie reszty i brakujace wplaty

```python
sales = [
    {"id": 1, "items": [("A", 2, 15), ("B", 1, 20)], "received": 60},
    {"id": 2, "items": [("C", 1, 40)], "received": 25},
    {"id": 3, "items": [], "received": 0},
]
```

Pozycje to krotki (sku, quantity, unit_price), a kwoty nieujemne liczby. Dla kazdej sprzedazy policz naleznosc, reszte, brakujaca wplate oraz status settled, change_due albo underpaid. Reszta i brakujaca wplata nie moga byc ujemne. Przy rownych kwotach wybierz settled, takze dla pustego koszyka o zerowej wplacie. Podsumuj laczna naleznosc i laczna brakujaca kwote.

### Zadanie 012 - Rabat procentowy z limitem i dostawa

```python
orders = [
    {"id": 1, "subtotal": 400, "discount_pct": 20, "discount_cap": 50, "shipping": 15},
    {"id": 2, "subtotal": 100, "discount_pct": 10, "shipping": 15},
    {"id": 3, "subtotal": 0, "discount_pct": 0, "discount_cap": 0, "shipping": 0},
]
```

Oblicz rabat procentowy od subtotal. Opcjonalny discount_cap ogranicza go od gory; brak lub None oznacza brak limitu, a zero zakaz rabatu. Dostawe dolicz dopiero po odjeciu rabatu od subtotal. Przygotuj nowe rekordy z id, discount_value, final_amount i capped. Capped jest True tylko wtedy, gdy rzeczywisty rabat jest scisle mniejszy od rabatu wynikajacego z procentu. Samo istnienie limitu nie oznacza jego zastosowania. Wszystkie wartosci sa nieujemne, a procent nie przekracza 100. Podsumuj wartosc przyznanych rabatow.

### Zadanie 013 - Wartosc brutto per stawka podatku

```python
receipts = [
    {"id": 1, "items": [{"sku": "A", "net": 100, "qty": 2, "vat": 23},
                        {"sku": "B", "net": 20, "qty": 1, "vat": 8}]},
    {"id": 2, "items": [{"sku": "C", "net": 50, "qty": 0, "vat": 23}]},
]
```

Net oznacza cene netto jednej sztuki, qty nieujemna calkowita liczbe sztuk, a vat stawke procentowa. Dla kazdego paragonu policz wartosc netto wszystkich sztuk, podatek i wartosc brutto. Rownolegle przygotuj podsumowanie wartosci netto i podatku per stawka VAT ze wszystkich paragonow. Stawki wystepujace tylko na zerowych pozycjach tez maja znalezc sie w podsumowaniu z zerami. Nie zaokraglaj wynikow posrednich; do dwoch miejsc po kropce formatuj tylko osobne komunikaty. Struktury wynikowe zawieraja liczby, nie sformatowane teksty.

### Zadanie 014 - Plan paczek dla wielu zrodel

```python
sources = [
    {"name": "shop", "records": 23, "batch_size": 5},
    {"name": "crm", "records": 20, "batch_size": 10},
    {"name": "ads", "records": 0, "batch_size": 4},
]
```

Dla kazdego zrodla wyznacz liczbe pelnych paczek, liczbe rekordow w ostatniej niepelnej paczce oraz laczna liczbe paczek. Jesli nie ma niepelnej paczki, jej rozmiar wynosi zero. Przygotuj liste opisow paczek z source, batch_number od 1 i records_count. Nie dodawaj pustej paczki na koncu ani dla pustego zrodla. Nazwy zrodel sa unikalne, batch_size dodatnim intem, a records nieujemnym intem. Pokaz osobna flage per zrodlo, czy suma rekordow jego paczek zgadza sie z records.

### Zadanie 015 - Plan ponowien z budzetem czasu

```python
jobs = [
    {"id": "A", "attempts": 5, "base_delay": 2, "max_delay": 10, "budget": 15},
    {"id": "B", "attempts": 3, "base_delay": 1, "max_delay": 4, "budget": 0},
]
```

Wszystkie czasy sa w sekundach. Planowane opoznienia kolejnych prob przed ograniczeniem to base_delay, dwa razy base_delay, cztery razy base_delay i tak dalej. Kazde opoznienie, takze pierwsze, jest ograniczone do max_delay. Attempts jest nieujemnym intem, budget nieujemna liczba, a oba opoznienia sa dodatnie. Dodawaj proby w kolejnosci, dopoki ich laczny czas nie przekroczy budget i liczba nie przekroczy attempts. Pierwsza niemieszczaca sie proba konczy plan, ale nie wchodzi do wyniku. Pokaz proby z numerami od 0, laczny czas i reason: attempts_exhausted, jesli zaplanowano wszystkie proby, albo budget_exceeded w przeciwnym razie. Przy attempts=0 wynik jest pusty z attempts_exhausted. Nie wykonuj rzeczywistego czekania.

### Zadanie 016 - Segmenty klientow na podstawie zakupow

```python
customers = [{"id": 1}, {"id": 2}, {"id": 3}]
orders = [
    {"customer_id": 1, "status": "paid", "amount": 100},
    {"customer_id": 1, "status": "paid", "amount": 250},
    {"customer_id": 2, "status": "cancelled", "amount": 900},
]
```

Pokaz kazdego klienta z liczba oplaconych zamowien, ich suma i segmentem. Brak paid daje no_paid_orders. Co najmniej dwa paid i suma od 300 daje loyal. Pozostali z suma od 200 sa high_value, a reszta buyer. Warunki maja takie pierwszenstwo jak w opisie. ID klientow sa unikalne, zamowienia wskazuja istniejacych klientow. Oplacone zero oznacza zakup, nie brak zakupow.

### Zadanie 017 - Rabat VIP tylko na dozwolonym rynku

```python
policies = {"PL": {"min_amount": 100, "discount": 10},
            "DE": {"min_amount": 200, "discount": 20}}
orders = [
    {"id": 1, "country": " pl ", "status": "paid", "amount": 120, "vip": False},
    {"id": 2, "country": "DE", "status": "paid", "amount": 50, "vip": True},
    {"id": 3, "country": "US", "status": "paid", "amount": 500, "vip": True},
    {"id": 4, "country": "PL", "status": "pending", "amount": 500, "vip": True},
]
```

Rabat kwotowy z polityki kraju przysluguje tylko oplaconym zamowieniom z obslugiwanego rynku, jesli osiagnely prog albo klient jest VIP-em. VIP nie omija ograniczenia kraju ani statusu. Rabat nie moze przekroczyc kwoty zamowienia. Znormalizuj kraj i status, a wynik wzbogac o discount, final_amount i eligible. Opcjonalne vip jest boolem z domyslnym False.

### Zadanie 018 - Wylaczenie kontaktu ma pierwszenstwo

```python
customers = [
    {"id": 1, "consents": {"email": True, "sms": False}, "blocked": False},
    {"id": 2, "consents": {"email": None, "sms": True}},
    {"id": 3, "consents": {"email": True}, "blocked": True},
    {"id": 4, "consents": {}},
]
```

Przygotuj per klient liste dozwolonych kanalow oraz status blocked, contactable lub no_consent. Tylko jawne True dla kanalu oznacza zgode; None, False i brak kanalu niczego nie dopuszczaja. Opcjonalne blocked ma domyslne False i blokuje wszystkie kanaly. Uwzgledniaj tylko email i sms, w tej kolejnosci. Podsumuj liczbe klientow dostepnych kazdym kanalem.

### Zadanie 019 - Kandydaci do odzyskania konta

```python
accounts = [
    {"id": 1, "email": " a@demo.pl ", "locked": True, "attempts_left": 2},
    {"id": 2, "email": None, "locked": True, "attempts_left": 3},
    {"id": 3, "email": "x", "locked": False, "attempts_left": 0},
    {"id": 4, "email": "b@demo.pl", "locked": True, "attempts_left": 0},
]
```

Konto moze otrzymac link odzyskania tylko wtedy, gdy locked=True, attempts_left jest dodatnie i ma poprawny email wedlug uproszczonej reguly: po oczyszczeniu jeden @ i dwie niepuste czesci. Email jest opcjonalnym stringiem albo None; dane nie zawieraja bialych znakow wewnatrz adresow. Zbuduj gotowe rekordy id i email, z adresem oczyszczonym na brzegach i zapisanym malymi literami. Pozostale konta zapisz z id i pierwszym pasujacym powodem not_locked, no_attempts albo invalid_email. None lub brak adresu nie moze przerwac oceny kolejnych kont.

### Zadanie 020 - Salda i przekroczenia debetu

```python
accounts = {1: {"balance": 100, "overdraft": 50}, 2: {"balance": 0, "overdraft": 0}}
operations = [
    {"account_id": 1, "change": -120}, {"account_id": 1, "change": -40},
    {"account_id": 2, "change": 0}, {"account_id": 1, "change": 30},
]
```

Przetwarzaj operacje w kolejnosci. Operacja jest dozwolona, gdy saldo po jej zastosowaniu nie spadnie ponizej ujemnego overdraft. Odrzucona operacja nie zmienia salda. Historia zawiera operation_number od 1, account_id, change, balance_before, balance_after i accepted. Balance_after ma przedstawiac faktyczny stan po decyzji, wiec przy odmowie jest rowne balance_before. Przygotuj tez koncowe salda i licznik odmow wszystkich kont, takze zero. Konta istnieja, kwoty sa intami, limity debetu nieujemne, a poczatkowe salda nie przekraczaja dopuszczalnego debetu. Nie zmieniaj accounts.

## C. Tekst, identyfikatory i komunikaty

### Zadanie 021 - Slownik statusow z dwoch sklepow

```python
aliases = {"paid": "paid", "oplacone": "paid", "new": "pending",
           "pending": "pending", "oczekuje": "pending",
           "cancelled": "cancelled", "anulowane": "cancelled"}
orders = [
    {"id": 1, "status": " OPLACONE ", "country": " pl ", "amount": 100},
    {"id": 2, "status": "New", "country": "de", "amount": 50},
    {"id": 3, "status": "refund", "country": "PL", "amount": 20},
    {"id": 4, "status": "paid", "country": " ", "amount": 0},
]
```

Przeksztalc statusy wedlug aliases po usunieciu brzegowych bialych znakow i zapisaniu tekstu malymi literami. Nieznany status odrzuca rekord. Country jest wymaganym stringiem: pusty po oczyszczeniu daje UNKNOWN, pozostale wartosci zapisz wielkimi literami. Wyniki to nowe poprawne rekordy z id, status, country, amount, lista rejected_ids oraz raport liczby zamowien i sumy kwot per kraj-status. Tworz grupy tylko z zaakceptowanych rekordow, takze z kwota zero. Wszystkie kwoty sa nieujemne.

### Zadanie 022 - Wspolny email kilku kont

```python
customers = [
    {"id": 1, "email": " TEAM@demo.pl ", "active": True},
    {"id": 2, "email": "team@demo.pl", "active": False},
    {"id": 3, "email": "team@demo.pl", "active": True},
    {"id": 4, "email": None, "active": True},
    {"id": 5, "email": "old@demo.pl", "active": False},
]
```

ID klientow sa unikalne. Email jest opcjonalnym stringiem albo None. Dla kazdego niepustego adresu po oczyszczeniu i zapisaniu malymi literami przygotuj email, all_ids, active_ids i conflict. Conflict jest True przy wiecej niz jednym aktywnym koncie danego adresu. Listy ID zachowuja kolejnosc customers. Brak pola, None lub pusty tekst po oczyszczeniu trafia do missing_email_ids. Zachowaj tez adresy z samymi nieaktywnymi kontami, z pusta lista active_ids. Nie wybieraj wlasciciela adresu.

### Zadanie 023 - Manifest dostarczonych plikow

```python
files = [
    {"name": " orders_2026-10-17_1.JSON ", "size": 120},
    {"name": "orders_2026-10-17_1.json", "size": 130},
    {"name": "customers_2026-10-17_2.json", "size": 0},
    {"name": "orders_2026-10-17_3.csv", "size": 50},
    {"name": "README.txt", "size": 80},
]
```

Rozpatruj pliki z rozszerzeniem json bez wzgledu na wielkosc liter. Najpierw oceniaj format, poniewaz nazwy pozostalych plikow moga byc dowolne. Tylko nazwy JSON maja zagwarantowany poprawny format source_date_page.extension po usunieciu spacji brzegowych. Source jest zapisem malymi literami bez podkreslen i kropek, data ma postac YYYY-MM-DD, a page poprawny zapis dodatniego inta. Tozsamosc pliku to source, date i liczbowy page. W manifest zapisz pierwszy plik kazdej trojki z oczyszczonym name i size. Osobno zapisz oryginalne nazwy duplikatow i plikow innych formatow. Podsumuj liczbe i bajty tylko plikow z manifest per source; rozmiar zero jest poprawny.

### Zadanie 024 - Tabela zapisana w wierszach tekstu

```python
header = "id;status;amount;country"
lines = ["1; PAID ;19,90;pl", "2;pending;0;DE", "3;paid;20",
         "4;cancelled;50.00; FR ", "5;paid;;PL"]
```

Header zawiera cztery unikalne nazwy pol id, status, amount i country. Przygotuj rekordy zgodnie z tymi nazwami. Odrzuc wiersz o niewlasciwej liczbie kolumn jako wrong_column_count, a nastepnie wiersz z pusta kwota po oczyszczeniu jako missing_amount. Inne kwoty i ID maja poprawny zapis liczbowy; kwoty moga miec kropke lub przecinek. ID ma byc intem, amount floatem, status oczyszczonym tekstem malymi literami, a country oczyszczonym tekstem wielkimi literami. Bledy zawieraja line_number od 1, oryginalny line i reason. Dane nie zawieraja separatorow wewnatrz wartosci ani cudzyslowow.

### Zadanie 025 - Jeden numer telefonu, wiele zapisow

```python
customers = [
    {"id": 1, "phones": ["+48 500-600-700", "+48500600700"]},
    {"id": 2, "phones": [" 123 ", None, "+49 100 200 300"]},
    {"id": 3, "phones": []},
    {"id": 4, "phones": ["+48 500 600 700"]},
]
```

Usun z numerow spacje i myslniki. Poprawny numer zaczyna sie od +, a pozostala czesc zawiera od 10 do 15 cyfr ASCII i zadnych innych znakow. None jest niepoprawnym wpisem. Per klient pokaz id, unique_phones, invalid_count i duplicate_count. Powtorzenie poprawnego numeru po normalizacji liczy sie jako duplikat, nie blad. Utworz tez phone_customers: dla kazdego poprawnego numeru unikalne ID klientow, ktorzy go podali. Wielokrotne podanie telefonu przez tego samego klienta nie zwieksza liczby jego wlascicieli. ID klientow sa unikalne; klient bez numerow nadal ma podsumowanie z zerami.

### Zadanie 026 - Ujednolicone etykiety klientow

```python
customers = [
    {"id": 1, "name": "  ANNA   maria  KOWALSKA ", "country": "pl"},
    {"id": 2, "name": "JAN", "country": " de "},
    {"id": 3, "name": " ", "country": "PL"},
]
```

Zbuduj rekordy id, clean_name, initials i country. Kazdy czlon nazwy ma zaczynac sie wielka litera, pozostale litery maja byc male; odstepy miedzy czlonami pojedyncze. Initials zawiera pierwsza litere kazdego czlonu i kropke, bez spacji miedzy inicjalami. Nazwy zawieraja tylko litery lacinskie i odstepy. Pusta nazwa po oczyszczeniu daje None dla clean_name i initials. Country oczysc na brzegach i zapisz wielkimi literami. Przygotuj komunikaty id | COUNTRY | nazwa, z UNKNOWN zamiast brakujacej nazwy tylko w komunikacie, nie w clean_name.

### Zadanie 027 - Katalog wedlug skladnikow SKU

```python
allowed_categories = {"BOOK", "COURSE"}
products = [
    {"sku": " eu-book-0042 ", "qty": 2},
    {"sku": "EU-COURSE-0010", "qty": 0},
    {"sku": "US-TOY-0001", "qty": 5},
    {"sku": "EU-BOOK", "qty": 1},
]
```

Poprawny SKU ma trzy czesci rozdzielone myslnikiem: dwuliterowy region, dozwolona kategorie i czterocyfrowy numer. Podane regiony zawieraja tylko litery lacinskie, a podane numery tylko cyfry, lecz liczba czesci i ich dlugosci moga byc niepoprawne. Oczysc SKU na brzegach i zapisz wielkimi literami. Poprawne rekordy zawieraja sku, qty, region, category, serial_text i serial_number; w serial_text zachowaj zera wiodace. Bledy zawieraja product_index, oryginalny sku i reason: invalid_format przed unsupported_category. Qty jest nieujemnym intem. Zsumuj je per region-kategoria tylko z poprawnych produktow, takze zerowych.

### Zadanie 028 - Sciezki eksportu wedlug ustawien zrodla

```python
config = {"root": "data/raw", "default_format": "json"}
sources = [
    {"name": " Shop ", "date": "2026-10-17", "pages": 2},
    {"name": "CRM", "date": "2026-10-17", "pages": 0, "format": "csv"},
    {"name": "Ads", "date": "2026-10-18", "pages": 1, "enabled": False},
]
```

Dla wlaczonych zrodel przygotuj rekordy source, page i path od strony 1 do pages wlacznie. Sciezka ma postac root/source/date/page_N.format. Source oczysc i zapisz malymi literami; po normalizacji nazwy zrodel sa unikalne. Root nie konczy sie ukosnikiem. Opcjonalne enabled jest boolem z domyslnym True, a opcjonalne format stringiem z wartoscia domyslna z config; format oczysc i zapisz malymi literami. Pages jest nieujemnym intem. Pokaz tez liczbe planowanych plikow per wlaczone zrodlo, takze zero. Wylaczone zrodla nie trafiaja do zadnego wyniku. Nie tworz plikow.

### Zadanie 029 - Ocena i czyszczenie notatek

```python
tickets = [
    {"id": 1, "notes": [None, "", "   ", "  pilne  "]},
    {"id": 2, "notes": ["OK", "  zadzwonic\n jutro  "]},
    {"id": 3},
]
```

Notes jest opcjonalna lista, ktorej elementy sa stringami albo None; brak pola oznacza pusta liste. Dla kazdego zgloszenia policz elementy w czterech rozlacznych kategoriach przed czyszczeniem: null to None, empty to dokladnie pusty string, whitespace to niepusty string z samych bialych znakow, a text to pozostale stringi. Zachowaj tylko text, redukujac kazdy ciag bialych znakow do jednej spacji i usuwajac je na brzegach. Raport zawiera id, cztery liczniki, clean_notes jako liste oraz joined_notes z notatkami oddzielonymi " | ". Brak tresciwych notatek daje joined_notes=None i pusta clean_notes.

### Zadanie 030 - Raport domen bez ujawniania adresow

```python
contacts = [
    {"id": 1, "email": " Anna@Example.com "}, {"id": 2, "email": "x@example.com"},
    {"id": 3, "email": "@demo.pl"}, {"id": 4, "email": "a@b@c"},
    {"id": 5, "email": None},
]
```

Email jest opcjonalnym stringiem albo None. Oczysc go na brzegach i zapisz malymi literami. W tym uproszczonym zadaniu poprawny adres ma jeden @ i dwie niepuste czesci; dane nie zawieraja bialych znakow wewnatrz adresu. Przygotuj rekordy id, domain i masked_email z maska pierwszy_znak***@domena. Brak lub niepoprawny adres daje None w obu polach. Policz kontakty per poprawna domena i laczna liczbe niepoprawnych adresow, wliczajac brak pola i None. Zadna struktura wynikowa ani komunikat nie moze zawierac pelnego niezamaskowanego adresu.

## D. Schematy, konfiguracje i aktualizacje

### Zadanie 031 - Raport wedlug definicji kolumn

```python
columns = [("id", "ID"), ("amount", "Kwota"), ("comment", "Komentarz")]
rows = [{"id": 1, "amount": 0, "comment": None},
        {"id": 2, "amount": 50}, {"id": 3, "comment": ""}]
```

Kazda krotka columns zawiera nazwe pola wejsciowego i jego etykiete. Przygotuj dla kazdego rekordu row_index oraz liste fields w kolejnosci columns. Opis pola ma label, value i state: missing dla braku klucza, null dla None, empty dla dokladnie pustego stringa, present w pozostalych przypadkach. Zero i False sa wartosciami present. Value dla missing i null wynosi None, dla empty pusty string. Podsumuj liczbe kazdego z czterech stanow per nazwa pola z columns, takze z zerowymi licznikami. Pol spoza columns nie oceniaj.

### Zadanie 032 - Rozne wymagania dla roznych zrodel

```python
schemas = {
    "shop": {"required": {"id", "amount"}, "optional": {"comment"}},
    "crm": {"required": {"id", "email"}, "optional": {"country"}},
}
records = [
    {"source": "shop", "data": {"id": 1, "amount": 0, "debug": True}},
    {"source": "crm", "data": {"id": 2, "email": None}},
    {"source": "crm", "data": {"id": 3}},
    {"source": "ads", "data": {"id": 4}},
]
```

Dla kazdego wpisu zwroc row_index, source, status, missing_fields i unexpected_fields. Jesli source nie wystepuje w schemas, status to unknown_source, a obie kolekcje pol sa puste, bo nie ma z czym porownywac data. Dla znanego zrodla missing_fields zawiera brakujace required, a unexpected_fields klucze data spoza required i optional. Kontrolujemy tylko obecnosc, wiec istniejace None spelnia wymaganie obecnosci. Status to invalid_schema przy brakujacym required, w przeciwnym razie ready. Nieznane pola nie uniewazniaja rekordu. Data jest zawsze dictem; kolejnosc nazw pol nie jest oceniana.

### Zadanie 033 - Metryki z wartosci mieszanych

```python
rows = [
    {"source": "shop", "metrics": {"orders": 5, "revenue": 120.5, "active": True}},
    {"source": "shop", "metrics": {"orders": 0, "revenue": None, "note": "ok"}},
    {"source": "crm", "metrics": {"customers": 3, "active": False}},
]
```

Zsumuj metryki per source i nazwa pola, uwzgledniajac tylko dokladne typy int i float. Bool, None i tekst to odrzucone wartosci; raportuj dla nich row_index, source, metric i value. Poprawne zero tworzy metryke z wartoscia zero, ale bledna wartosc sama nie tworzy metryki. Dla kazdego source z rows pokaz rowniez accepted_values_count i rejected_values_count, takze zera. Zrodlo z samymi blednymi lub pustymi metrics ma puste podsumowanie kwot, ale pozostaje w statystykach zrodla. Metrics jest wymaganym dictem.

### Zadanie 034 - Pola historyczne i nowy standard

```python
aliases = {"id": ("order_id", "ID"), "amount": ("amount", "total", "TOTAL")}
rows = [
    {"order_id": 1, "ID": 99, "total": 100},
    {"ID": 2, "amount": 0, "TOTAL": 50},
    {"order_id": 3, "amount": None, "total": 20},
    {"ID": 4, "amount": False, "total": 0},
]
```

Dla kazdego pola docelowego wybierz pierwsza istniejaca wartosc rozna od None wedlug kolejnosci aliasow. Brak kandydata daje None. Zero, False i pusty string sa kandydatami, a nie brakami. Jesli co najmniej dwie istniejace wartosci rozne od None roznia sie miedzy soba, zapisz jeden konflikt z row_index, target_field i wybrana wartoscia; wybor o wyzszym priorytecie nadal obowiazuje. Wynikowe rekordy zawieraja wylacznie pola docelowe z aliases. Samego porownania wartosci nie poprzedzaj ich zamiana na tekst. Przy wykrywaniu konfliktu zgodnosc wymaga zarowno tej samej wartosci, jak i tego samego dokladnego typu: False i 0 sa konfliktem.

### Zadanie 035 - Porownanie wybranych metryk z celem

```python
report_config = {"metric": "revenue", "targets": {"PL": 100, "DE": 50}}
rows = [{"country": " pl ", "metrics": {"revenue": 120}},
        {"country": "DE", "metrics": {"revenue": 0}},
        {"country": "FR", "metrics": {"orders": 5}},
        {"country": "PL", "metrics": {"revenue": None}}]
```

Wybrana metryka wynika z report_config. Country oczysc i zapisz wielkimi literami. Kazdy wynik ma country, value, target, difference i status. Dla braku metryki value=None; dla braku celu target=None, niezaleznie od statusu. Pierwszenstwo statusow: missing_metric dla braku klucza w metrics, null_metric dla istniejacego None, no_target dla braku celu, reached dla value co najmniej target, below w pozostalych przypadkach. Difference to value minus target i powstaje tylko dla reached lub below; inaczej wynosi None. Istniejace niepuste metryki i cele sa liczbami, takze zerem.

### Zadanie 036 - Dokumenty rozliczeniowe klienta

```python
orders = [
    {"id": 1, "customer": {"name": " Anna ", "billing": {"tax_id": " PL 123 "}}},
    {"id": 2, "customer": {"name": "Jan", "billing": None}},
    {"id": 3, "customer": {"name": "Eva", "billing": {"tax_id": None}}},
    {"id": 4, "customer": {"name": "Ola"}},
]
```

W tym uproszczonym modelu dokument rozliczeniowy jest invoice, jesli klient podal niepusty numer podatkowy, w przeciwnym razie receipt. Customer i name sa wymagane. Billing jest opcjonalnym dictem albo None, tax_id opcjonalnym stringiem albo None. Numer oczysc ze wszystkich spacji i zapisz wielkimi literami przed ocena, czy jest pusty. Przygotuj rekordy order_id, customer_name, tax_id i document_type; brak poprawnego numeru daje tax_id=None. Z nazwy usun tylko spacje brzegowe. Podsumuj liczbe obu rodzajow dokumentow. Nie jest wymagana kontrola prawdziwosci numeru podatkowego.

### Zadanie 037 - Eksport z konfigurowanych sciezek

```python
fields = [
    {"name": "country", "path": ("customer", "address", "country"), "default": "UNKNOWN"},
    {"name": "email", "path": ("customer", "email"), "default": "MISSING"},
]
rows = [{"customer": {"address": {"country": "PL"}, "email": None}},
        {"customer": {"address": None}}, {"customer": "broken"}]
```

Zbuduj plaskie rekordy zgodnie z fields. Jesli na drodze brakuje klucza albo poziom posredni nie jest dictem, zapisz wartosc default. Istniejace None na koncu sciezki jest prawdziwa odczytana wartoscia i nie uruchamia default. Dodatkowo przygotuj raport indeksu rekordu i nazw pol, w ktorych zastosowano wartosc domyslna. Nazwy pol sa unikalne, sciezki sa niepustymi krotkami stringow.

### Zadanie 038 - Migracja pola total na amount

```python
rows = [
    {"id": 1, "total": 100, "debug": "trace"},
    {"id": 2, "amount": 0, "total": 50},
    {"id": 3, "amount": None, "total": 20},
    {"id": 4, "comment": "ok"},
]
```

Przygotuj nowe rekordy bez total i debug. Jesli amount istnieje, zachowaj je dokladnie, takze None i zero. W przeciwnym razie przenies istniejace total do amount; brak obu pol nie tworzy amount. Dla dwoch istniejacych roznych wartosci amount i total zapisz konflikt z id, amount i total. Porownuj wartosci przed usunieciem total, wliczajac None. Jesli debug istnieje, zachowaj jego wartosc w osobnym raporcie id, debug, takze gdy sama wartosc to None. Nie zmieniaj rows.

### Zadanie 039 - Konfiguracja z mozliwoscia resetu

```python
defaults = {"limit": 100, "enabled": True, "country": "PL"}
source = {"limit": 50, "country": "DE"}
requests = [
    {"id": 1, "overrides": {"limit": 0, "enabled": False}},
    {"id": 2, "overrides": {"limit": None}},
    {"id": 3, "overrides": {"debug": True}},
]
```

Utworz osobna konfiguracje dla kazdego request z jego id. Source nadpisuje defaults, a overrides nadpisuje source. Jawne None w overrides resetuje pole do wartosci z defaults, nie do source. Zero i False sa zwyklymi nadpisaniami. Source zawiera tylko klucze defaults i wartosci zgodnych typow. W overrides moga byc dodatkowe klucze; nie trafiaja do konfiguracji, tylko do raportu request_id, field, value. Zadne z ustawien jednego request nie moze przeniknac do konfiguracji innego. Nie zmieniaj slownikow wejsciowych.

### Zadanie 040 - Zestawienie wedlug kraju i kanalu

```python
orders = [
    {"id": 1, "country": " pl ", "channel": " WEB ", "status": "paid", "amount": 100},
    {"id": 2, "country": "PL", "channel": "web", "status": "cancelled", "amount": 50},
    {"id": 3, "country": "DE", "status": "paid", "amount": 0},
    {"id": 4, "country": "PL", "channel": None, "status": "pending", "amount": 20},
]
```

Przygotuj zestawienie country-channel z orders_count, paid_count, paid_revenue i cancelled_ids. Country jest wymaganym stringiem; oczysc go i zapisz wielkimi literami. Channel jest opcjonalnym stringiem albo None; brak, None lub pusty tekst po oczyszczeniu oznacza unknown, pozostale kanaly zapisz malymi literami. Statusy sa juz poprawnymi etykietami paid, pending lub cancelled, a kwoty nieujemnymi liczbami. Kazdy rekord tworzy lub uzupelnia grupe, takze nieoplacony. Paid z kwota zero zwieksza paid_count. Cancelled_ids zachowuje kolejnosc wejscia.

## E. Niezaleznosc struktur i porownywanie danych

### Zadanie 041 - Pierwszy i ostatni zakup klienta

```python
customers = [{"id": 1}, {"id": 2}, {"id": 3}]
orders = [
    {"id": 10, "customer_id": 1, "status": "paid", "amount": 0},
    {"id": 11, "customer_id": 2, "status": "cancelled", "amount": 80},
    {"id": 12, "customer_id": 1, "status": "paid", "amount": 120},
]
```

Orders sa w kolejnosci chronologicznej, customers maja unikalne ID, a wszystkie powiazania sa poprawne. Pokaz kazdego klienta jako customer_id, first_paid_order_id, last_paid_order_id, paid_count i paid_revenue. Uwzgledniaj tylko status paid. Przy braku paid oba ID wynosza None, licznik i suma zero. Przy jednym paid oba ID sa identyczne. Oplacone zero nadal jest zamowieniem. Wynik zachowuje kolejnosc customers, bez zmiany kolejnosci orders.

### Zadanie 042 - Rozdzielanie zamowien do kolejek

```python
orders = [
    {"id": 1, "status": "paid", "amount": 0, "country": "PL"},
    {"id": 2, "status": "cancelled", "amount": -10, "country": "PL"},
    {"id": 3, "status": "paid", "amount": -5, "country": "DE"},
    {"id": 4, "status": "pending", "amount": 100, "country": "US"},
]
queues = {"cancelled": [], "invalid_amount": [], "ready": [], "manual": []}
```

Uzupelnij queues tak, aby kazde zamowienie trafilo dokladnie do jednej kolejki. Pierwszenstwo: status cancelled do cancelled; pozostale z ujemna kwota do invalid_amount; pozostale paid z kraju PL lub DE do ready; reszta do manual. W kolejkach przechowuj nowe rekordy id i amount, w kolejnosci orders. ID zamowien sa unikalne. Pokaz licznik elementow kazdej kolejki oraz flage complete, prawdziwa tylko wtedy, gdy kazde wejsciowe ID wystepuje w kolejkach dokladnie raz. Nie zmieniaj orders.

### Zadanie 043 - Koszyki z jednego szablonu

```python
template = {"status": "new", "tags": ["web"], "items": []}
customers = [{"id": 1, "sku": "A", "qty": 2}, {"id": 2, "sku": "B", "qty": 1}]
extra = {"customer_id": 1, "tag": "priority", "sku": "C", "qty": 3}
```

Zbuduj osobny koszyk per klient z customer_id, status, tags i items wedlug template. Dodaj wskazana przez klienta pozycje jako dict sku, qty. Nastepnie wprowadz extra tylko do koszyka wskazanego klienta: dodaj tag, jesli jeszcze go nie ma, i nowa pozycje. ID klientow sa unikalne, klient z extra istnieje, a SKU z extra nie wystepuje jeszcze w jego koszyku. Template oraz koszyki pozostalych klientow nie moga zmienic sie przez aktualizacje jednego koszyka. Pokaz tez liczbe pozycji i sume sztuk kazdego klienta.

### Zadanie 044 - Zmiany miedzy dwiema wersjami zamowienia

```python
before = {"id": 44, "tags": {"web", "new"},
          "items": [{"sku": "A", "qty": 1}, {"sku": "B", "qty": 2}]}
after = {"id": 44, "tags": {"web", "vip"},
         "items": [{"sku": "A", "qty": 3}, {"sku": "C", "qty": 1}]}
```

Obie wersje dotycza tego samego zamowienia; SKU jest unikalny w kazdej liscie items. Utworz trzy listy: added_items z sku i new_qty, removed_items z sku i old_qty oraz changed_items z sku, old_qty, new_qty i difference jako new_qty minus old_qty. Nie zglaszaj pozycji bez zmiany ilosci. Added_items i changed_items zachowuja kolejnosc after, removed_items kolejnosc before. Osobno pokaz zbiory added_tags i removed_tags. Nie zmieniaj before ani after.

### Zadanie 045 - Przesylki z pozycji krotkowych

```python
shipments = [
    {"id": "S1", "lines": [("A", 2, 10, "PL"), ("B", 1, 25, "DE")]},
    {"id": "S2", "lines": [("A", 0, 10, "PL")]},
]
```

Kazda krotka zawiera sku, quantity jako nieujemny int, unit_price jako nieujemna liczbe i country jako kod kraju pochodzenia. Wszystkie ceny sa w jednej wspolnej walucie. Zbuduj plaskie rekordy shipment_id, sku, quantity, unit_price, country i line_value. Line_value oznacza wartosc wszystkich sztuk na pozycji. Osobno podsumuj sume sztuk i wartosc per przesylka oraz per kraj. Puste przesylki zachowaj z zerami, a pozycje zerowe pozostaw w liscie i podsumowaniu ich kraju.

### Zadanie 046 - Stan przetwarzania wewnatrz partii

```python
batch = ("B46", {"accepted": [], "rejected": [], "total": 0})
rows = [{"id": 1, "amount": 10}, {"id": 2, "amount": None},
        {"id": 3, "amount": 0}, {"id": 4}]
```

Uzupelnij strukture zapisana w drugim elemencie batch, zachowujac sama zewnetrzna krotke. Poprawna kwota to istniejacy nieujemny int lub float niebedacy boolem. Brak klucza amount daje missing_amount, a istniejace None, zly typ lub wartosc ujemna invalid_amount. Accepted zawiera nowe dicty batch_id, id, amount, a rejected dicty id, reason. Total to suma zaakceptowanych kwot. Rows ma pozostac bez zmian; zmieniasz tylko stan przechowywany w batch.

### Zadanie 047 - Popularnosc tagow produktow

```python
products = [
    {"sku": "A", "tags": [" SQL ", "sql", "BEGINNER", None]},
    {"sku": "B", "tags": ["sql", "", "python"]},
    {"sku": "C"},
]
```

Tags jest opcjonalna lista stringow lub None jako elementow; brak listy oznacza brak wpisow, a nie jeden blad. SKU produktow sa unikalne. Dla kazdego produktu pokaz sku, unique_tags, missing_count i duplicate_count. None oraz tekst pusty po oczyszczeniu zwiekszaja missing_count. Pozostale tagi oczysc i zapisz malymi literami. Kolejne wystapienie tego samego poprawnego tagu w jednym produkcie zwieksza duplicate_count. Osobno policz liczbe roznych produktow posiadajacych kazdy tag; wielokrotne wpisy jednego produktu licza go tylko raz.

### Zadanie 048 - Decyzja o dostepie do oferty

```python
blocked = {2}
offers = {"PL": 100, "DE": 200}
customers = [
    {"id": 1, "active": True, "country": "PL", "budget": 100},
    {"id": 2, "active": False, "country": "US", "budget": 0},
    {"id": 3, "active": True, "country": "DE", "budget": 150},
    {"id": 4, "active": True, "country": "US", "budget": 500},
]
```

Nadaj kazdemu klientowi pierwsza pasujaca decyzje: blocked, inactive, unsupported_country, insufficient_budget albo eligible. Cena zalezy od kraju, a budzet rowny cenie wystarcza. Wynik to id, decision i price; jesli kraj ma oferte, zapisz jej cene niezaleznie od decyzji, a w przeciwnym razie None. Pokaz tez liste ID w kazdej z pieciu decyzji, takze pusta, oraz liczbe eligible per kraj wystepujacy w customers, takze zero. ID klientow sa unikalne, budzety i ceny nieujemne.

### Zadanie 049 - Uzgodnienie dwoch eksportow klientow

```python
exports = {
    "shop": {("PL", 1), ("PL", 2), ("DE", 1)},
    "crm": {("PL", 2), ("PL", 3), ("DE", 1)},
}
names = {("PL", 1): "Anna", ("PL", 2): "Jan", ("PL", 3): "Ola"}
```

Przygotuj rekordy dla wszystkich par kraj-ID obecnych w dowolnym eksporcie: country, customer_id, customer_name i presence. Presence to both, shop_only albo crm_only; brak nazwy daje None. Ten sam numer ID w innym kraju oznacza innego klienta. Dla kazdego kraju z eksportow pokaz liczbe par w kazdym z trzech stanow, takze zero. Kolejnosc rekordow wynikowych nie jest oceniana. Names sluzy tylko do wzbogacenia danych i nie dodaje klientow nieobecnych w eksportach.

### Zadanie 050 - Rejestr unikalnych tras

```python
routes = [
    {"from": " waw ", "to": "BER", "carrier": "X", "active": True},
    {"from": "WAW", "to": " ber ", "carrier": "X", "active": True},
    {"from": "BER", "to": "WAW", "carrier": "X", "active": True},
    {"from": "WAW", "to": "BER", "carrier": "Y", "active": False},
]
```

Rozpatruj tylko active=True. Tozsamosc trasy wyznaczaja oczyszczone i zapisane wielkimi literami from oraz to, a takze carrier zachowany bez zmian. Kierunki przeciwne sa rozne. Zbuduj nowe oczyszczone rekordy unikalnych tras, zachowujac pierwsze aktywne wystapienie. Kolejne aktywne wystapienia tej samej trojki sa duplikatami. Policz unikalne trasy rozpoczynajace sie w kazdym porcie i duplikaty per przewoznik majacy choc jeden aktywny wpis, takze zero. Nieaktywny wpis nie trafia do zadnego licznika.

## F. Kolejnosc, wyszukiwanie i podzial pracy

### Zadanie 051 - Mapa dostepnych miejsc

```python
rooms = [
    {"id": "A", "rows": 3, "columns": 4, "blocked": {(0, 1), (2, 3)}},
    {"id": "B", "rows": 0, "columns": 2, "blocked": set()},
]
```

Dla kazdego pomieszczenia przygotuj id, map jako liste stringow kolejnych rzedow, available_count i available_labels. Znak # oznacza blokade, a . dostepne miejsce. Wspolrzedne blocked sa od zera, prawidlowe i mieszcza sie w pomieszczeniu. Etykieta dostepnego miejsca ma format id-Rnumer-Cnumer, z numerami od 1; etykiety sa w kolejnosci rzedow, a wewnatrz kolumn. Rows i columns sa nieujemnymi intami. Brak rzedow daje pusta map. Przy dodatniej liczbie rzedow i zerze kolumn map zawiera odpowiednia liczbe pustych stringow, bez etykiet.

### Zadanie 052 - Luki w numeracji per zrodlo

```python
windows = {"shop": (100, 104), "crm": (1, 3)}
records = [
    {"source": "shop", "id": 100}, {"source": "shop", "id": 102},
    {"source": "shop", "id": 102}, {"source": "shop", "id": 110},
    {"source": "crm", "id": 2},
]
```

Przygotuj raport dla kazdego klucza z windows, takze zrodla bez rekordow. Zawiera source, missing_ids z domknietego przedzialu, outside_ids jako unikalne ID poza nim i duplicate_count. Powtorzeniem jest kazde kolejne wystapienie tego samego ID w danym source, niezaleznie od tego, czy ID lezy w oknie. Wszystkie source z records maja zdefiniowane okna, ID i granice sa intami, a dolna granica nie przekracza gornej. Missing_ids przedstaw rosnaco; kolejnosc outside_ids nie jest oceniana.

### Zadanie 053 - Ostatnie udane uruchomienie procesu

```python
jobs = [
    {"name": "orders", "history": [{"id": 1, "success": True, "rows": 100},
                                  {"id": 2, "success": False, "rows": 0},
                                  {"id": 3, "success": True, "rows": 0}]},
    {"name": "customers", "history": [{"id": 4, "success": False, "rows": 10}]},
    {"name": "ads", "history": []},
]
```

History jest chronologiczna, success boolem, a rows nieujemnym intem. Dla kazdego procesu pokaz job_name, last_success_id, last_success_rows i trailing_failures. Ostatni sukces to ostatni wpis z success=True, takze z rows=0. Brak sukcesu daje None w obu polach sukcesu. Trailing_failures liczy tylko nieprzerwany ciag porazek na samym koncu historii; jesli wszystkie wpisy sa porazkami, liczy je wszystkie. Pusta historia daje zero porazek.

### Zadanie 054 - Dokladne polozenie bledu w imporcie

```python
pages = [
    {"source": "shop", "page": 1, "rows": [{"id": 1, "country": "PL"},
                                        {"id": 2, "country": ""}]},
    {"source": "shop", "page": 2, "rows": [{"id": 3, "country": None},
                                        {"id": 4, "country": " de "}]},
    {"source": "crm", "page": 1, "rows": [{"id": 5, "country": " fr "}]},
    {"source": "shop", "page": 3, "rows": []},
]
```

Country jest opcjonalnym stringiem albo None. Poprawny kod po usunieciu brzegowych bialych znakow ma dwa znaki i w wyniku jest zapisany wielkimi literami. Zaakceptowane rekordy zawieraja source, page, row_number od 1 w obrebie strony, id i country. Bledy zawieraja te same dane identyfikujace i raw_country z oryginalna wartoscia albo None przy braku klucza. Podsumuj bledy per para source-page oraz per source; sam numer strony nie jest unikalny pomiedzy zrodlami. Pary source-page na wejsciu sa unikalne. Kazda strona, takze pusta lub bezbledna, ma licznik bledow zero lub wiekszy.

### Zadanie 055 - Wycena magazynow w jednej walucie

```python
prices = {"A": {"amount": 10, "currency": "PLN"},
          "B": {"amount": 5, "currency": "EUR"},
          "D": {"amount": 3, "currency": "USD"}}
rates_to_pln = {"PLN": 1, "EUR": 4}
warehouses = [
    {"id": "W1", "stock": {"A": 3, "B": 2}},
    {"id": "W2", "stock": {"A": 0, "C": 1, "D": 2}},
    {"id": "W3", "stock": {}},
]
```

Ceny jednostkowe sa w walucie z prices, a rates_to_pln okresla liczbe PLN za jedna jednostke tej waluty. Stany sa nieujemnymi intami, ceny i przeliczniki nieujemnymi liczbami. Brak ceny daje missing_price, a brak przelicznika dla istniejacej ceny missing_rate. Taka pozycja nie ma znanej wyceny; raportuj warehouse_id, sku, qty i reason, nawet dla qty=0. Dla kazdego magazynu i osobno kazdego SKU pokaz priced_value_pln jako sume poprawnie wycenionych pozycji, unpriced_qty jako sume sztuk pozycji blednych i complete jako brak blednych pozycji. Nie prezentuj czesciowej sumy jako pelnej wyceny. Pusty magazyn ma priced_value_pln=0, unpriced_qty=0 i complete=True.

### Zadanie 056 - Pierwsze zamowienia do obslugi

```python
config = {"limit": 2, "min_amount": 100, "countries": {"PL", "DE"}}
orders = [
    {"id": 1, "status": "pending", "country": "PL", "amount": 200},
    {"id": 2, "status": "paid", "country": "PL", "amount": 100},
    {"id": 3, "status": "paid", "country": "US", "amount": 300},
    {"id": 4, "status": "paid", "country": "DE", "amount": 150},
    {"id": 5, "status": "paid", "country": "PL", "amount": 400},
]
```

Wybierz pierwsze limit zamowien paid z dozwolonego kraju i kwota od min_amount. Zachowaj kolejnosc. Zakoncz ocenianie rekordow po zapelnieniu limitu i podaj liczbe faktycznie ocenionych rekordow oraz sume kwot wybranych zamowien. Limit jest nieujemny; przy zerze nie oceniaj zadnego rekordu. Jesli brakuje kandydatow, zwroc wszystkich pasujacych.

### Zadanie 057 - Blad krytyczny zatrzymuje tylko swoja partie

```python
batches = [
    {"id": "B1", "rows": [{"id": 1, "severity": "ok"}, {"id": 2, "severity": "warning"},
                        {"id": 3, "severity": "fatal"}, {"id": 4, "severity": "ok"}]},
    {"id": "B2", "rows": [{"id": 5, "severity": "ok"}]},
]
```

Wpis ok akceptuj, warning odrzucaj i kontynuuj partie. Fatal odrzucaj i zakoncz przetwarzanie tej partii, ale kolejne partie nadal obsluz. Zbuduj zaakceptowane ID, odrzucone rekordy z batch_id i powodem oraz liczbe nieocenionych wpisow per partia. Rekord fatal jest oceniony. Niewykonane rekordy nie trafiaja do accepted ani rejected.

### Zadanie 058 - Kontakt w strukturze firmy

```python
companies = [
    {"id": "C1", "departments": [
        {"name": "sales", "people": [{"id": 1, "role": "analyst", "email": None}]},
        {"name": "data", "people": [{"id": 2, "role": "engineer", "email": " a@demo.pl "},
                                   {"id": 3, "role": "engineer", "email": "b@demo.pl"}]}]},
    {"id": "C2", "departments": []},
]
```

Znajdz per firma pierwszego engineera z niepustym emailem, wedlug kolejnosci dzialow i osob. Zapisz company_id, department, person_id i oczyszczony email malymi literami. Gdy nie ma kandydata, pozostale pola maja byc None. Osoba z inna rola nie moze byc wybrana. email jest opcjonalnym stringiem albo None. Firma bez dzialow nadal wystepuje w raporcie.

### Zadanie 059 - Paczki z limitem liczby i rozmiaru

```python
config = {"max_records": 2, "max_bytes": 10}
records = [{"id": 1, "bytes": 6}, {"id": 2, "bytes": 5},
           {"id": 3, "bytes": 2}, {"id": 4, "bytes": 11}, {"id": 5, "bytes": 0}]
```

Buduj kolejne paczki z rekordow w kolejnosci wejscia. Jesli poprawny rekord nie miesci sie w aktualnej paczce pod wzgledem liczby lub bajtow, zamknij ja i rozpocznij kolejna. Rekord wiekszy od max_bytes odrzuc, nie zamykajac przez niego paczki. Limity sa dodatnie, rozmiary nieujemne. Wynik ma zawierac ID w paczkach, rozmiar kazdej paczki i ID odrzuconych. Nie tworz pustych paczek.

### Zadanie 060 - Alerty i ich najwyzsza waznosc

```python
orders = [
    {"id": 1, "amount": 900, "country": "US", "email": None},
    {"id": 2, "amount": 20, "country": "PL", "email": "a@demo.pl"},
    {"id": 3, "amount": 600, "country": "DE", "email": ""},
]
```

Generuj wszystkie pasujace alerty w kolejnosci: high_value przy kwocie od 500, foreign_market przy kraju poza PL i DE, missing_email przy braku pola email, None lub pustym tekscie po oczyszczeniu. Email jest opcjonalnym stringiem albo None; country i amount sa wymagane i juz poprawne. Waznosc high_value to tekst medium, pozostalych high. Raport per zamowienie zawiera id, alerts i highest_severity jako jeden z tekstow none, medium, high; none nie oznacza wartosci None. Pokaz liczniki wszystkich trzech alertow, takze zera, oraz liczbe zamowien z co najmniej jednym alertem.

## G. Raporty, grupowanie i uzgadnianie

### Zadanie 061 - Dozwolone zmiany statusu

```python
allowed = {"new": {"paid", "cancelled"}, "paid": {"shipped"}, "cancelled": set(), "shipped": set()}
initial = {1: "new", 2: "paid"}
events = [
    {"id": 1, "order_id": 1, "new_status": " PAID "},
    {"id": 2, "order_id": 1, "new_status": "cancelled"},
    {"id": 3, "order_id": 2, "new_status": " SHIPPED "},
    {"id": 4, "order_id": 9, "new_status": "paid"},
]
```

Initial zawiera poczatkowe statusy zamowien i ma pozostac bez zmian; wszystkie te statusy wystepuja w allowed. Obsluz events w kolejnosci, oczyszczajac new_status na brzegach i zapisujac malymi literami. Zmiana jest poprawna tylko dla istniejacego zamowienia i przejscia dopuszczonego z jego aktualnego stanu. Priorytet odrzucenia to unknown_order przed forbidden_transition; nieznany status docelowy tez oznacza forbidden_transition. Odrzucenie nie zmienia stanu. Wynik to koncowe statusy, zaakceptowana historia event_id, order_id, old_status, new_status oraz bledy event_id, order_id, reason. Policz zaakceptowane przejscia per para old_status-new_status.

### Zadanie 062 - Sprzedaz, zwroty i wynik netto

```python
events = [
    {"country": " pl ", "kind": "sale", "amount_cents": 10000},
    {"country": "PL", "kind": "refund", "amount_cents": 2500},
    {"country": "DE", "kind": "refund", "amount_cents": 1000},
    {"country": None, "kind": "sale", "amount_cents": 0},
]
```

Kind ma jedna z wartosci sale lub refund, a amount_cents jest nieujemnym intem w groszach. Country jest opcjonalnym stringiem albo None; brak, None lub pusty tekst po oczyszczeniu daje UNKNOWN, pozostale kraje zapisz wielkimi literami. Policz per kraj sales_count, sales_cents, refunds_count, refunds_cents i net_cents jako sprzedaz minus zwroty. Zwrot pomniejsza netto, mimo dodatniej kwoty na wejsciu. Zachowaj kraje z samymi zwrotami i zerowymi zdarzeniami. W oddzielnych komunikatach prezentuj netto w PLN, a nie w groszach, do dwoch miejsc po kropce.

### Zadanie 063 - Lider sprzedazy w kazdym kraju

```python
lines = [
    {"country": "PL", "product_id": 1, "qty": 2, "price": 50},
    {"country": "PL", "product_id": 2, "qty": 1, "price": 100},
    {"country": "PL", "product_id": 1, "qty": 1, "price": 20},
    {"country": "PL", "product_id": 3, "qty": 3, "price": 40},
    {"country": "PL", "product_id": 4, "qty": 4, "price": 30},
    {"country": "PL", "product_id": 5, "qty": 4, "price": 30},
    {"country": "DE", "product_id": 2, "qty": 0, "price": 100},
]
```

Policz przychod i sztuki kazdego produktu per kraj. Nastepnie wybierz lidera kazdego kraju: wiekszy przychod wygrywa, przy remisie wieksza liczba sztuk, a dalej mniejszy product_id. Wynik liderow zawiera country, product_id, revenue i units. Zera sa poprawne, wiec kraj z samymi pozycjami zerowymi nadal ma lidera. Kolejnosc wejscia nie moze rozstrzygac remisu.

### Zadanie 064 - Klienci powyzej sredniej swojego kraju

```python
customers = [{"id": 1, "country": "PL"}, {"id": 2, "country": "PL"},
             {"id": 3, "country": "DE"}, {"id": 4, "country": "PL"}]
orders = [{"customer_id": 1, "status": "paid", "amount": 100},
          {"customer_id": 1, "status": "paid", "amount": 200},
          {"customer_id": 2, "status": "paid", "amount": 100},
          {"customer_id": 3, "status": "cancelled", "amount": 900}]
```

ID klientow sa unikalne, kraje poprawne, a wszystkie powiazania zamowien istnieja. Pokaz kazdego klienta jako customer_id, country, total_revenue, paid_count, country_average i above_average. Total_revenue i paid_count uwzgledniaja tylko paid, takze paid z kwota zero. Country_average to srednia z lacznych przychodow klientow kraju majacych choc jedno paid, a nie srednia pojedynczych zamowien. Klient bez paid nie wchodzi do sredniej, ale moze miec w raporcie srednia innych klientow swojego kraju. Above_average jest True tylko dla klienta z paid i przychodem scisle wiekszym od sredniej. Brak sredniej daje None i False.

### Zadanie 065 - Rozdzial sprzedazy pomiedzy handlowcow

```python
sellers = {1: "Anna", 2: "Jan", 3: "Eva"}
orders = [
    {"id": 1, "amount": 200, "shares": [(1, 60), (2, 40)]},
    {"id": 2, "amount": 100, "shares": [(2, 50), (3, 40)]},
    {"id": 3, "amount": 0, "shares": [(3, 100)]},
]
```

Kazda para shares oznacza seller_id i procentowy udzial w amount. Zamowienie jest poprawne, gdy wszyscy wskazani handlowcy istnieja, zadne ID nie powtarza sie w shares, udzialy sa dodatnimi intami niebedacymi boolami i sumuja sie do 100. W przeciwnym razie zapisz ID zamowienia w rejected_ids i nie przypisuj nikomu zadnej jego czesci. Kwoty sa nieujemne i w jednej walucie. Dla wszystkich zarejestrowanych sellers pokaz seller_id, seller_name, allocated_revenue i orders_count, takze zera. Zamowienie zerowe liczy sie do licznika wskazanych handlowcow. Nie zaokraglaj udzialow w trakcie sumowania; to cwiczenie podzialu przychodu, bez zasad ksiegowego podzialu groszy.

### Zadanie 066 - Wzbogacenie zamowien i kontrola powiazan

```python
customers = [{"id": "1", "name": "Anna"}, {"id": "2", "name": "Jan"}]
products = {"A": {"name": "SQL"}, "B": {"name": "Python"}}
orders = [
    {"id": 10, "customer_id": 1, "items": [("A", 2), ("X", 1)]},
    {"id": 11, "customer_id": 9, "items": [("B", 1)]},
]
```

Zbuduj plaska liste pozycji order_id, item_index, customer_name, sku, product_name i qty. ID klienta w orders jest intem, a w customers tekstem z tym samym zapisem numeru bez zer wiodacych. ID klientow sa unikalne. Nieznany klient lub produkt daje None w odpowiednim polu, ale pozycja pozostaje w wyniku. Raport unknown_customers zawiera order_id i customer_id raz na zamowienie, takze bez pozycji. Unknown_products zawiera order_id, item_index i sku dla kazdej nieznanej pozycji. Pokaz liczbe pozycji z oboma poprawnymi powiazaniami. Nie zmieniaj wejscia.

### Zadanie 067 - Klienci bez zakupow w wybranym okresie

```python
period = ("2026-10-01", "2026-11-01")
customers = [{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}]
orders = [
    {"customer_id": 1, "date": "2026-10-01", "status": "paid"},
    {"customer_id": 2, "date": "2026-09-30", "status": "paid"},
    {"customer_id": 3, "date": "2026-10-15", "status": "cancelled"},
]
```

Period zawiera poczatek i koniec, przy czym poczatek jest wczesniejszy. Daty maja poprawna postac YYYY-MM-DD i mozna porownywac je jako tekst. Poczatek nalezy do okresu, koniec nie. ID klientow sa unikalne i wszystkie zamowienia wskazuja istniejacego klienta. Pokaz tylko klientow bez paid w okresie: customer_id, all_orders_count, reason i had_paid_before_period. All_orders_count liczy wszystkie statusy ze wszystkich dat. Reason to no_orders, jesli licznik wynosi zero, albo no_paid_in_period. Flaga dotyczy wylacznie paid z data scisle przed poczatkiem okresu. Paid na koncu okresu nie spelnia warunku zakupu w okresie.

### Zadanie 068 - Wlasciciel wspolnego adresu

```python
customers = [
    {"id": 7, "email": " Team@demo.pl ", "active": True, "vip": False},
    {"id": 5, "email": "team@demo.pl", "active": True, "vip": True},
    {"id": 3, "email": "team@demo.pl", "active": True, "vip": True},
    {"id": 2, "email": None, "active": True, "vip": True},
    {"id": 1, "email": "other@demo.pl", "active": False, "vip": True},
]
```

Email jest opcjonalnym stringiem albo None; oczysc go na brzegach i zapisz malymi literami. ID klientow sa unikalne. Najpierw zaklasyfikuj brak, None i pusty adres do missing_email_ids, a pozostale nieaktywne konta do inactive_ids. Tylko pozostali sa kandydatami na wlasciciela. Dla kazdego adresu z kandydatem wybierz VIP-a przed niewipem, a przy tym samym vip mniejsze ID. Wynik zawiera email, owner_id i other_active_ids w kolejnosci customers. Adres bez aktywnego kandydata nie ma wlasciciela i nie tworzy takiego wpisu. Sam wybor owner_id musi byc niezalezny od kolejnosci kandydatow; kolejnosc list diagnostycznych i other_active_ids wynika z wejscia.

### Zadanie 069 - Odtwarzanie stanu ze zdarzen

```python
events = [
    {"action": "upsert", "id": 1, "data": {"status": "new", "amount": 100}},
    {"action": "upsert", "id": 2, "data": {"status": "paid", "amount": 0}},
    {"action": "upsert", "id": 1, "data": {"status": "paid"}},
    {"action": "delete", "id": 2}, {"action": "delete", "id": 9},
]
```

Przygotuj koncowy rejestr rekordow po ID. Upsert zastepuje caly rekord data, nie tylko jego pola, a delete usuwa wskazane ID. Usuniecie nieistniejacego rekordu zapisz w osobnym raporcie, ale kontynuuj. W historii kazdego zdarzenia podaj action, id i efekt inserted, replaced, deleted lub missing. Wszystkie akcje sa jednym z dwoch opisanych rodzajow; nie zmieniaj data w events.

### Zadanie 070 - Duplikat czy konflikt danych?

```python
events = [
    {"source": "shop", "id": 1, "status": " PAID ", "amount": "10,00"},
    {"source": "shop", "id": 1, "status": "paid", "amount": "10.00"},
    {"source": "shop", "id": 1, "status": "paid", "amount": "20.00"},
    {"source": "crm", "id": 1, "status": "new", "amount": "0"},
]
```

Tozsamosc zdarzenia wyznacza para source-id. Oczysc status na brzegach i zapisz malymi literami. Amount ma poprawny nieujemny zapis tekstowy z kropka lub przecinkiem; porownanie kwot ma zachowywac dokladnosc dziesietna, bez zaokraglania do wyswietlania. Pierwsza wersja pary trafia do accepted i pozostaje wersja odniesienia. Kazda kolejna jest duplicate, jesli status i kwota sa rowne pierwszej wersji, albo conflict w przeciwnym razie. Konflikt nie zastepuje wersji odniesienia. Raporty duplicate i conflict zawieraja event_index, source i id. Pokaz tez liczby accepted, duplicate i conflict per source, takze zerowe.

## H. Dane na kilku poziomach

### Zadanie 071 - Zamowienia, produkty i warianty

```python
orders = [
    {"id": 1, "products": [{"sku": "A", "variants": [("red", 2), ("blue", 1)]},
                          {"sku": "B", "variants": []}]},
    {"id": 2, "products": None},
    {"id": 3},
]
```

Products jest opcjonalna lista albo None; brak i None oznaczaja brak produktow. Kazdy produkt ma sku i wymagana liste variants z parami color, qty, gdzie qty jest nieujemnym intem. SKU jest unikalny w obrebie zamowienia. Zbuduj raport pozycji order_id, sku, color, qty. Produkt bez wariantow tworzy techniczny wiersz raportu z color=None i qty=0, nie pozycje sprzedazy. Zamowienie bez produktow nie tworzy wiersza pozycji. Osobne podsumowanie wszystkich zamowien zawiera order_id, products_count jako liczbe wpisow products i total_units jako sume ilosci wariantow, takze z zerami.

### Zadanie 072 - Cena z katalogu lub z pozycji

```python
catalog = {"A": 10, "B": 20}
orders = [
    {"id": 1, "items": [{"sku": "A", "qty": 2}, {"sku": "B", "price": 0}]},
    {"id": 2, "items": [{"sku": "X", "qty": 1}, {"sku": "A", "qty": None}]},
]
```

Brak qty oznacza 1. Istniejace qty musi byc nieujemnym intem niebedacym boolem; None, ujemna liczba lub inny typ uniewaznia pozycje. Zero jest poprawne. Price jest opcjonalna nieujemna liczba albo None: brak i None oznaczaja cene z catalog, a zero jest poprawnym nadpisaniem. SKU musi istniec w catalog nawet przy nadpisaniu ceny. Zbuduj raport wszystkich zamowien order_id, accepted_items_count i total_value oraz bledy order_id, item_index, sku, reason. Zglaszaj jeden powod na pozycje: invalid_quantity przed unknown_sku. Jedna bledna pozycja nie odrzuca innych; zamowienie z samymi bledami ma sume zero.

### Zadanie 073 - Kraj dostawy z wartoscia zapasowa

```python
customers = {1: {"address": {"country": "PL"}}, 2: {"address": None}}
orders = [
    {"id": 1, "customer_id": 1, "shipping": {"address": {"country": " de "}}},
    {"id": 2, "customer_id": 1, "shipping": None},
    {"id": 3, "customer_id": 1, "shipping": {"address": {"country": ""}}},
    {"id": 4, "customer_id": 2},
]
```

Kraj w shipping.address ma pierwszenstwo przed krajem adresu klienta. Shipping i address sa opcjonalnymi dictami albo None, country opcjonalnym stringiem albo None. Brak klucza lub None na sciezce zamowienia oznacza brak przekazanej informacji i uruchamia wartosc z adresu klienta. Jawny pusty tekst po oczyszczeniu oznacza natomiast swiadome wyczyszczenie kraju i nie pozwala na wartosc zapasowa. Niepusty kraj oczysc i zapisz wielkimi literami. Wynik to id, country i origin: order dla poprawnego kraju zamowienia, customer dla poprawnej wartosci zapasowej, missing gdy ostatecznie nie ma kraju. W ostatnim stanie country=None. Klienci istnieja; brak lub pusty kraj klienta nie ma kolejnego poziomu zapasowego.

### Zadanie 074 - Stan polek i przekroczona pojemnosc

```python
warehouses = {
    "W1": {"A1": {"capacity": 4, "items": [{"sku": "X", "qty": 3}, {"sku": "Y", "qty": 2}]},
           "A2": {"capacity": 2, "items": []}},
    "W2": {"B1": {"capacity": 5, "items": [{"sku": "X", "qty": 1}, {"sku": "Z", "qty": -1}]}},
}
```

Capacity i qty sa intami, pojemnosci nieujemne. Ujemna ilosc odrzuca tylko pozycje, nie cala polke. Raport polek zawiera warehouse_id, shelf, valid_units, free_capacity i over_capacity. Free_capacity to pojemnosc minus valid_units, ograniczone od dolu zerem; flaga jest True tylko przy valid_units scisle wiekszym od capacity. Bledne pozycje zapisz z warehouse_id, shelf, item_index, sku i qty. Przygotuj dwa oddzielne podsumowania poprawnych sztuk: warehouse_totals dla wszystkich magazynow, takze pustych i z samymi bledami, oraz sku_totals tylko dla SKU z przynajmniej jedna poprawna pozycja, takze zerowa.

### Zadanie 075 - Dzienne pomiary z progami jakosci

```python
sensors = [
    {"id": "S1", "limits": (-5, 20), "days": [[10, None, 30], [], [0, -2]]},
    {"id": "S2", "limits": (0, 10), "days": [[None], [5, 10]]},
]
```

Kazdy element days jest lista pomiarow jednego dnia. Kazdy pomiar jest liczba albo None; sam dzien nie jest None. Limits zawiera dolna i gorna granice wlacznie, z dolna nie wieksza od gornej. Pokaz sensor_id, day_index, missing_count, out_of_range_count, valid_count i average dla kazdego dnia, takze pustego. None jest brakiem, nie pomiarem poza zakresem. Average liczy tylko pomiary w zakresie; brak takich pomiarow daje None. Podsumuj kazdy sensor: days_count, days_with_valid_readings i srednia ze wszystkich jego poprawnych pomiarow, nie srednia ze srednich dni.

### Zadanie 076 - Przypisanie do przedzialu oferty

```python
policies = {
    "PL": [("basic", 0, 100), ("plus", 100, 300), ("premium", 300, None)],
    "DE": [("basic", 0, 200), ("promo", 150, 250)],
}
orders = [{"id": 1, "country": "PL", "amount": 100},
          {"id": 2, "country": "DE", "amount": 175},
          {"id": 3, "country": "FR", "amount": 50}]
```

Kazda krotka policies zawiera nazwe segmentu, dolna granice wlaczna i gorna wylaczna. None oznacza brak gornego ograniczenia. Nazwy segmentow w jednym kraju sa unikalne. Zwroc dla kazdego zamowienia id, segment, matched_segments i status. Statusy to unknown_policy dla kraju bez wpisu, no_match przy braku dopasowania w znanej polityce, matched dla jednego przedzialu albo ambiguous dla kilku. Segment jest nazwa tylko przy matched, poza tym None. Matched_segments zawiera wszystkie pasujace nazwy, a dla unknown_policy i no_match jest puste. Nie rozstrzygaj nakladajacych sie ofert ich kolejnoscia.

### Zadanie 077 - Cena hurtowa i minimalna wartosc zamowienia

```python
catalog = {"A": {"base": 20, "tiers": [(10, 15), (5, 18)]},
           "B": {"base": 30, "tiers": []}}
orders = [
    {"id": 1, "minimum": 100, "items": [("A", 7), ("B", 1)]},
    {"id": 2, "minimum": 50, "items": [("B", 1)]},
]
```

Kazda krotka tiers to minimalna ilosc sztuk i cena jednostkowa. Progi sa uporzadkowane od najwiekszej ilosci; dla pozycji obowiazuje pierwszy osiagniety prog, a przy braku dopasowania base. SKU istnieja i nie powtarzaja sie w jednym zamowieniu; ilosci sa dodatnimi intami, ceny i minimum nieujemnymi liczbami. Zbuduj nowe rekordy zamowien z wycenionymi pozycjami sku, qty, unit_price, line_value oraz basket_value, can_submit i missing_amount. Can_submit jest True od minimum wlacznie. Missing_amount to brakujaca kwota ograniczona od dolu zerem. Puste items daje basket_value=0, a decyzja nadal zalezy od minimum.

### Zadanie 078 - Lancuch stron i wykrywanie petli

```python
config = {"start": "first", "max_pages": 5}
pages = {
    "first": {"items": [{"id": 1}], "next": "second"},
    "second": {"items": [{"id": 2}, {"id": 1}], "next": "third"},
    "third": {"items": [], "next": "second"},
}
```

Podazaj za next, zaczynajac od start, bez rzeczywistych zapytan sieciowych. Zbuduj liste odwiedzonych stron i unikalnych rekordow po ID, zachowujac pierwsze wystapienie, oraz licznik duplikatow. Nie przetwarzaj tej samej strony ponownie. Po przeczytaniu strony kolejnosc rozstrzygania zakonczenia to: next=None daje end, juz odwiedzona nastepna strona cycle, nieistniejaca missing_page, osiagniety limit limit. max_pages jest dodatni, start istnieje. Zakoncz wraz z odpowiednim powodem.

### Zadanie 079 - Kontrola kwoty naglowka zamowienia

```python
orders = [
    {"id": 1, "total": 115, "shipping": 10, "discount": 5,
     "items": [{"sku": "A", "qty": 2, "price": 50}, {"sku": "B", "qty": 1, "price": 10}]},
    {"id": 2, "total": 80, "shipping": 0,
     "items": [{"sku": "A", "qty": 1, "price": 50}]},
]
```

Qty to nieujemna calkowita liczba sztuk, a price cena jednej sztuki. Oczekiwane total to suma wartosci wszystkich pozycji minus rabat plus dostawa. Opcjonalny discount jest nieujemnym intem albo None; brak i None daja zero. Pozostale liczby sa nieujemnymi intami, rabat nie przekracza sumy pozycji. Raport zawiera id, total, expected_total, difference jako total minus expected_total oraz matches dla dokladnej rownosci. Osobno policz wartosc pozycji per SKU, bez kwoty naglowka, dostawy ani rabatu calego zamowienia. Nie poprawiaj total na wejsciu.

### Zadanie 080 - Najlepszy dozwolony kanal kontaktu

```python
channel_priority = ("email", "sms")
customers = [
    {"id": 1, "contacts": [{"channel": "sms", "value": "+48500600700", "consent": True},
                          {"channel": "email", "value": " A@demo.pl ", "consent": True}]},
    {"id": 2, "contacts": [{"channel": "email", "value": None, "consent": True},
                          {"channel": "sms", "value": "+49100200300", "consent": False}]},
    {"id": 3, "contacts": []},
]
```

Dla kazdego klienta wybierz pierwszy kanal z channel_priority majacy co najmniej jeden niepusty kontakt z consent=True. W jego obrebie wygrywa pierwszy taki kontakt z contacts. Value jest wymaganym stringiem albo None; consent opcjonalnym boolem albo None. Brak zgody i nieznane kanaly pomijaj. W tym zadaniu nie sprawdzamy formatu adresu ani telefonu, tylko niepustosc po oczyszczeniu. Email oczysc i zapisz malymi literami, telefon oczysc tylko na brzegach. Wynik zawiera id, channel i value dla kazdego klienta; brak kandydata daje dwa None. Pokaz liczbe wybranych kontaktow per kanal z channel_priority, takze zera.

## I. Zbiory krotek i powiazania wielowymiarowe

### Zadanie 081 - Koszyki z zestawami pozycji

```python
baskets = [
    {"id": 1, "items": {("A", 2, 10), ("B", 1, 30)}, "free_shipping_from": 50},
    {"id": 2, "items": set(), "free_shipping_from": 100},
    {"id": 3, "items": {("A", 0, 10)}, "free_shipping_from": 0},
    {"id": 4, "items": {("A", 0, 10)}, "free_shipping_from": 100},
]
shipping_fee = 15
```

Kazda krotka to sku, quantity jako nieujemny int i unit_price jako nieujemna liczba. Dla kazdego koszyka pokaz id, sku_count, lines_count, total_units, items_value, shipping i final_amount. Sku_count liczy rozne SKU obecne na pozycjach, takze zerowych, a lines_count wszystkie krotki. Jesli total_units=0, nie ma czego wysylac i shipping wynosi zero, nawet przy niepustym secie pozycji. Dla dodatniej liczby sztuk dostawa jest darmowa od free_shipping_from wlacznie, w przeciwnym razie kosztuje shipping_fee. Final_amount to items_value plus shipping. Podsumuj items_value per SKU i liczbe koszykow z shipping wiekszym od zera.

### Zadanie 082 - Wymagane uprawnienia do operacji

```python
requirements = {
    "export": {("orders", "read"), ("customers", "read")},
    "health": set(),
}
users = [
    {"id": 1, "active": True, "permissions": {("orders", "read"), ("customers", "read")}},
    {"id": 2, "active": True, "permissions": {("orders", "read")}},
    {"id": 3, "active": False, "permissions": set()},
]
requests = [{"user_id": 1, "operation": "export"}, {"user_id": 2, "operation": "export"},
            {"user_id": 2, "operation": "health"}, {"user_id": 3, "operation": "health"}]
```

Dla kazdego wpisu requests przygotuj request_index, user_id, operation, allowed i missing_permissions. Allowed wymaga active=True oraz posiadania wszystkich wymaganych par. Nieaktywny uzytkownik zawsze ma allowed=False, nawet gdy missing_permissions jest puste. Kolekcje brakujacych praw pokaz takze dla nieaktywnych osob. Wszystkie operacje i konta istnieja, ID kont sa unikalne. Zbuduj licznik odmow per operacja z requirements i licznik zaakceptowanych wpisow requests per uzytkownik z users, takze zera. Kilka wpisow z ta sama para user_id-operation to kilka niezaleznych zadan dostepu.

### Zadanie 083 - Towar dostepny po rezerwacjach

```python
warehouses = [
    {"id": "W1", "stock": {("A", 5), ("B", 0)}, "reserved": {("A", 2), ("C", 1)}},
    {"id": "W2", "stock": {("A", 3)}, "reserved": {("A", 5)}},
    {"id": "W3", "stock": set()},
]
```

Stock i opcjonalne reserved sa setami par sku-ilosc; brak reserved oznacza pusty set. W kazdym secie SKU wystepuje najwyzej raz, a ilosci sa nieujemnymi intami. Rezerwacja nalezy do konkretnego magazynu: nadmiar w innym magazynie nie pokrywa jej automatycznie. Dla kazdego magazynu i kazdego SKU obecnego w ktorymkolwiek z jego dwoch zbiorow pokaz warehouse_id, sku, stock, reserved, available i shortage. Brak danej pary oznacza ilosc zero. Available to stock minus reserved, nie mniej niz zero; shortage to reserved minus stock, nie mniej niz zero. Podsumuj available i shortage per SKU jako sumy wynikow lokalnych. Pusty magazyn nie tworzy fikcyjnej pozycji SKU.

### Zadanie 084 - Cennik zalezy od rynku i uslugi

```python
tariffs = {
    ("PL", "standard"): {"currency": "PLN", "fee": 15, "free_from": 100},
    ("DE", "standard"): {"currency": "EUR", "fee": 5, "free_from": None},
    ("PL", "pickup"): {"currency": "PLN", "fee": 0, "free_from": 0},
}
orders = [{"id": 1, "country": " pl ", "amount": 120},
          {"id": 2, "country": "DE", "service": "standard", "amount": 500},
          {"id": 3, "country": "PL", "service": "pickup", "amount": 0},
          {"id": 4, "country": "FR", "amount": 50}]
```

Service jest opcjonalnym stringiem z domyslnym standard. Kraj oczysc i zapisz wielkimi literami, usluge malymi. Amount to nieujemna wartosc zamowienia wyrazona w walucie odpowiedniej taryfy; zadanie nie wymaga przewalutowania. Dla znalezionej pary kraj-usluga ustal fee i currency. Darmowa usluga obowiazuje od free_from wlacznie; None oznacza brak tego progu. Wynik kazdego zamowienia zawiera id, service, fee, currency i can_quote. Przy braku taryfy fee i currency sa None, a can_quote=False. Policz liczbe wszystkich poprawnych wycen, takze darmowych, oraz sume oplat osobno per waluta. Niewycenione zamowienia nie trafiaja do sum walut.

### Zadanie 085 - Rekomendacje z zakupow innych klientow

```python
customers = [{"id": 1, "active": True}, {"id": 2, "active": True},
             {"id": 3, "active": False}]
orders = [
    {"customer_id": 1, "status": "paid", "items": {("A", 1), ("B", 2)}},
    {"customer_id": 2, "status": "paid", "items": {("B", 1), ("C", 1)}},
    {"customer_id": 3, "status": "paid", "items": {("D", 1)}},
]
```

Uwzgledniaj tylko paid aktywnych klientow i pozycje o dodatniej ilosci. Dla kazdego aktywnego klienta ustal zbior zakupionych SKU. Jego bezposrednimi sasiadami sa inni aktywni klienci majacy z nim co najmniej jeden wspolny kupiony SKU. Rekomendacje to produkty kupione przez tych bezposrednich sasiadow, ktorych odbiorca sam nie kupil. Nie rozszerzaj rekomendacji przez kolejnych sasiadow sasiadow. Wynik zawiera customer_id i unique_recommendations dla kazdego aktywnego klienta, takze pusty zbior. ID klientow sa unikalne, powiazania poprawne. Nieaktywni nie dostarczaja rekomendacji i nie pojawiaja sie w wyniku.

### Zadanie 086 - Zgodnosc produktow z wymaganiami

```python
requirements = {("export", 2), ("search", 1)}
products = [
    {"sku": "A", "features": {("export", 1), ("export", 2), ("search", 1)}},
    {"sku": "B", "features": {("export", 1), ("search", 3)}},
    {"sku": "C", "features": set()},
]
```

Kazda para w requirements i features oznacza nazwe funkcji i dodatni calkowity numer wersji. Dostepna wersja funkcji produktu to najwiekszy numer wymieniony dla tej nazwy. Requirements zawiera najwyzej jedna pare danej nazwy. Produkt jest zgodny, gdy kazda wymagana funkcja istnieje w wersji co najmniej wymaganej. Raport zawiera sku, compatible i missing_features. Lista brakow obejmuje tylko niespelnione wymagania z feature, required_version i available_version albo None przy braku funkcji. Jej kolejnosc nie jest oceniana, bo wymagania sa zbiorem. Brak wymagan daje compatible=True i pusta liste dla kazdego produktu.

### Zadanie 087 - Kontrola par od dostawcow

```python
deliveries = [
    {"supplier": "S1", "pairs": [("A", 2), ("B", [1, 2]), ("A", 2), ("C", True)]},
    {"supplier": "S2", "pairs": [("A", 3), ("D", -1), ("E", 0)]},
]
```

Pairs jest migawka pozycji otrzymanych od dostawcy, w ktorej powtorzona identyczna para oznacza ponowne przeslanie tej samej pozycji, nie dodatkowa dostawe. Element jest zawsze krotka dwoch wartosci. Poprawna para ma niepusty string SKU i nieujemny int niebedacy boolem; podane niepuste stringi SKU nie zawieraja spacji. Niepoprawne pary zapisuj z supplier, pair_index i oryginalna para. W obrebie jednego wpisu deliveries licz identyczne poprawne pary raz. To samo SKU z inna iloscia jest inna pozycja. Wynik obejmuje sumy poprawnych nieduplikowanych ilosci per SKU i liczbe duplikatow per supplier. Jesli supplier wystapi w kilku wpisach deliveries, deduplikuj kazdy wpis niezaleznie, a liczniki dostawcy zsumuj.

### Zadanie 088 - Miesieczne paczki z zamowieniami

```python
months = [
    ("2026-09", {"orders": [
        {"id": 1, "status": "paid", "items": {("A", 2, 10), ("B", 1, 20)}},
        {"id": 2, "status": "cancelled", "items": {("A", 1, 10)}}]}),
    ("2026-10", {"orders": [
        {"id": 1, "status": "paid", "items": {("A", 1, 10)}}]}),
    ("2026-11", {"orders": []}),
]
```

Miesiace sa unikalne, a id to lokalny numer zamowienia z miesiecznego eksportu, resetowany co miesiac. Jest unikalny tylko wewnatrz jednego miesiaca. Krotka pozycji to sku, quantity jako nieujemny int i nieujemny unit_price. Przygotuj podsumowanie kazdego miesiaca: month, orders_count, paid_count i paid_items_value. Liczniki zamowien nie zaleza od liczby pozycji, wiec paid bez pozycji nadal zwieksza paid_count. Osobno pokaz przychod i liczbe roznych zamowien paid zawierajacych dany SKU per para month-sku, takze przy pozycji zerowej. Puste miesiace maja zerowe podsumowanie, ale nie tworza fikcyjnych SKU.

### Zadanie 089 - Najtansza poprawna oferta dostawy

```python
offers = {
    ("PL", "economy", 5, 10), ("PL", "express", 10, 20),
    ("PL", "pickup", None, 0), ("DE", "economy", 5, 15),
}
orders = [
    {"id": 1, "country": "PL", "items": [("A", 2, 3)], "allowed_services": {"economy", "express"}},
    {"id": 2, "country": "PL", "items": [], "allowed_services": {"pickup"}},
    {"id": 3, "country": "FR", "items": [("A", 1, 1)], "allowed_services": {"economy"}},
]
```

Oferta zawiera country, service, maksymalna wage albo None bez limitu oraz fee. Pozycja zamowienia to sku, quantity i waga jednej sztuki; liczby sa nieujemne. Oblicz laczna liczbe sztuk i wage. Gdy sztuk jest zero, niczego nie wysylamy: status=no_shipment, service=None i fee=0, niezaleznie od ofert. Dla dodatniej liczby sztuk wybierz najtansza oferte kraju, z allowed_services i wystarczajacym limitem wagi. Granica wagi jest wlaczna. Przy remisie ceny wygrywa alfabetycznie mniejsza nazwa uslugi. Raport zawiera id, total_weight, service, fee i status: quoted dla wybranej oferty, no_offer z service=None i fee=None dla braku dopasowania, albo no_shipment. Wybor oferty nie moze zalezec od kolejnosci offers.

### Zadanie 090 - Wybor magazynu z ograniczeniem rynku

```python
warehouses = {"W1": {"country": "PL", "active": True},
              "W2": {"country": "PL", "active": True},
              "W3": {"country": "DE", "active": False}}
requests = [
    {"id": 1, "country": "PL", "qty": 4, "options": {("W1", 5, 10), ("W2", 8, 10)}},
    {"id": 2, "country": "DE", "qty": 1, "options": {("W3", 9, 0)}},
    {"id": 3, "country": "PL", "qty": 1},
]
```

Options jest opcjonalnym setem krotek (warehouse_id, available_qty, handling_fee), a brak options lub None oznacza pusty set. Qty zapytania jest dodatnim intem, stany i oplaty nieujemne. ID magazynu jest unikalne w ramach options i istnieje w warehouses. Wybierz magazyn aktywny, z kraju zapytania i ze stanem wystarczajacym na cala ilosc. Priorytety to mniejsza oplata, wiekszy stan, alfabetycznie mniejszy kod. Zwroc id zapytania, warehouse_id, fee i can_fulfill. Przy braku kandydata oba pola wyceny sa None, a flaga False. Kazde zapytanie jest niezalezna wycena: nie rezerwuj towaru ani nie zmniejszaj stanu dla kolejnego zapytania.

## J. Zlozone przetwarzanie i kontrola spojnosci

### Zadanie 091 - Walidacja schematu i zaleznosci pol

```python
rows = [
    {"id": 1, "amount": 0, "status": "paid", "payment_ref": " P1 ", "country": "PL"},
    {"id": True, "amount": -10, "status": "paid", "payment_ref": None},
    {"id": 3, "amount": 100, "status": "pending", "country": "POL"},
    {"amount": "50", "status": "", "debug": True},
]
```

Sprawdz wszystkie rekordy i wszystkie pola. Wymagane id to dodatni int niebedacy boolem, amount to nieujemny int lub float niebedacy boolem, a status to string z jedna z wartosci paid, pending, cancelled po oczyszczeniu na brzegach i zapisaniu malymi literami. Country jest opcjonalnym stringiem albo None: brak i None daja UNKNOWN, podany tekst po oczyszczeniu musi miec dwa znaki. Zapisz poprawny kraj wielkimi literami. Payment_ref jest opcjonalnym stringiem albo None; oczysc go na brzegach, a pusty tekst zamien na None. Tylko status paid wymaga niepustego payment_ref.

Bledy zawieraja row_index, field i reason. Dla id, amount i status zglaszaj jeden powod na pole w kolejnosci missing, wrong_type, invalid_value. Podany tekst country o dlugosci innej niz dwa znaki po oczyszczeniu daje invalid_value. Dla payment_ref zglaszaj wylacznie required_for_paid, tylko gdy status jest poprawnym paid. Sprawdzaj pozostale pola nawet po znalezieniu bledu. Nieznane pola raportuj oddzielnie jako row_index, field, value; same nie uniewazniaja rekordu. Lista correct_rows zawiera tylko rekordy bez bledow, z polami id, amount, status, country, payment_ref. Nieznane pola nie trafiaja do correct_rows. Pokaz takze liczbe bledow walidacji per field, bez wliczania nieznanych pol.

### Zadanie 092 - Zamowienie przyjmowane tylko w calosci

```python
catalog = {"A": 10, "B": 20}
orders = [
    {"id": 1, "items": [{"sku": "A", "qty": 2}, {"sku": "B", "qty": 1}]},
    {"id": 2, "items": [{"sku": "A", "qty": 3}, {"sku": "X", "qty": 1}]},
    {"id": 3, "items": [{"sku": "B", "qty": 0}]},
    {"id": 4, "items": []},
]
```

Kazda pozycja wymaga znanego SKU i dodatniej ilosci int niebedacej boolem. Raportuj wszystkie bledy pozycji jako order_id, item_index, sku, reason; invalid_quantity i unknown_sku oceniaj niezaleznie, wiec jedna pozycja moze miec oba. Zamowienie z bledna pozycja odrzuca sie w calosci i zadna jego pozycja nie powieksza raportu sprzedazy. Pusta lista items tez odrzuca zamowienie: nie ma bledu konkretnej pozycji, ale reason zamowienia to empty_order. Dla pozostalych odrzuconych zamowien reason to invalid_items. Wynik to accepted_orders z id i total_value, rejected_orders z id i reason, item_errors oraz przychod i sztuki per SKU tylko z accepted_orders. Nie poprawiaj ilosci ani nie usuwaj po cichu wadliwej pozycji, aby przyjac reszte zamowienia.

### Zadanie 093 - Usuniecie w nowszej wersji nie moze zniknac

```python
events = [
    {"id": 1, "version": 3, "action": "delete"},
    {"id": 1, "version": 2, "action": "upsert", "data": {"status": "paid"}},
    {"id": 2, "version": 1, "action": "upsert", "data": {"status": "new"}},
    {"id": 2, "version": 4, "action": "upsert", "data": {"status": "paid"}},
    {"id": 2, "version": 4, "action": "delete"},
    {"id": 3, "version": None, "action": "upsert", "data": {"status": "new"}},
]
```

Obsluguj events po kolei. ID sa poprawnymi identyfikatorami. Version musi byc nieujemnym intem niebedacym boolem; brak, None i inny niepoprawny typ odrzucaja zdarzenie. Dla kazdego ID pamietaj najwyzsza dotad przyjeta wersje i jej akcje. Wyzsza wersja zastepuje poprzednia, przy remisie zachowaj pierwszy wpis. Delete usuwa aktywne dane, ale pozostawia wersje blokujaca starszy upsert. Pozniejszy upsert z wyzsza wersja moze przywrocic rekord. Wynik to active_records, deleted_ids i highest_versions. Policz invalid_version, older_version i equal_version w momencie oceny kazdego zdarzenia. Wczesniej przyjety wpis zastapiony nowsza wersja nie jest liczony ponownie jako odrzucony. Data wystepuje wylacznie w upsert, a akcje sa poprawne.

### Zadanie 094 - Rozliczenie platnosci i zwrotow

```python
orders = {1: {"total": "100.00", "currency": "PLN"},
          2: {"total": "50.00", "currency": "EUR"}}
transactions = [
    {"order_id": 1, "kind": "charge", "amount": "100.00", "currency": "PLN", "success": True},
    {"order_id": 1, "kind": "refund", "amount": "20.00", "currency": "PLN", "success": True},
    {"order_id": 2, "kind": "charge", "amount": "50.00", "currency": "PLN", "success": True},
    {"order_id": 9, "kind": "charge", "amount": "5.00", "currency": "EUR", "success": True},
    {"order_id": 2, "kind": "charge", "amount": "50.00", "currency": "EUR", "success": False},
]
```

Kwoty orders i transactions sa poprawnymi nieujemnymi tekstami dziesietnymi, a wyniki pieniezne maja byc Decimal. Kind jest charge albo refund. Rozliczaj tylko success=True dla istniejacego zamowienia i zgodnej waluty. Pominiete transakcje zapisuj z transaction_index, order_id i pierwszym powodem failed, unknown_order, currency_mismatch. Dla kazdego zamowienia pokaz order_id, currency, total, charges, refunds, net_paid jako charges minus refunds i remaining jako total minus net_paid. Pozostaw tez zamowienia bez wplat, z zerowymi charges i refunds. Remaining moze byc ujemne. Per waluta z orders podsumuj liczbe zamowien oraz te same kwoty total, charges, refunds, net_paid i remaining. Pominiete transakcje nie powiekszaja zadnej sumy.

### Zadanie 095 - Ustawienia dziedziczone przez rekordy

```python
defaults = {"country": "PL", "currency": "PLN", "enabled": True}
batches = [
    {"id": "B1", "settings": {"country": " de ", "currency": "EUR"},
     "rows": [{"id": 1}, {"id": 2, "settings": {"enabled": False}},
              {"id": 3, "settings": {"country": None, "currency": " usd "}}]},
    {"id": "B2", "settings": None,
     "rows": [{"id": 4, "settings": {"country": ""}}]},
]
```

Dla kazdego rekordu ustal country, currency i enabled z priorytetem jego settings, settings partii, defaults. Oba settings sa opcjonalnymi dictami albo None. Brak klucza i None jako wartosc oznaczaja dziedziczenie nizszego poziomu. Enabled jest boolem albo None; False jest jawnym nadpisaniem. Podane kraje i waluty sa stringami albo None: pusty tekst po oczyszczeniu daje UNKNOWN bez dziedziczenia, inne teksty zapisz wielkimi literami. Settings nie zawieraja innych pol. Raport wszystkich rekordow zawiera batch_id, id i trzy efektywne ustawienia. Plan eksportu grupuje tylko wlaczone rekordy per kraj-waluta; w kazdej grupie zachowaj rekordy identyfikujace batch_id i id, nie samo id. Nie sprawdzaj zgodnosci waluty z rynkiem, bo to zadanie dotyczy dziedziczenia ustawien.

### Zadanie 096 - Narastajacy wynik bez mieszania walut

```python
orders = [
    {"id": 1, "customer_id": 10, "currency": "PLN", "status": "paid", "amount": 100},
    {"id": 2, "customer_id": 10, "currency": "EUR", "status": "paid", "amount": 20},
    {"id": 3, "customer_id": 10, "currency": "PLN", "status": "cancelled", "amount": 50},
    {"id": 4, "customer_id": 10, "currency": "PLN", "status": "paid", "amount": 0},
]
```

Orders jest chronologiczne, ID zamowien unikalne, waluty juz ujednolicone, a kwoty nieujemne. Dla kazdego wpisu pokaz id, customer_id, currency, order_number od 1 w obrebie pary klient-waluta, running_paid_count i running_paid_revenue tej samej pary. Kazdy status zwieksza order_number; tylko paid zmienia pozostale dwie metryki. Paid z kwota zero zwieksza running_paid_count. Koncowe raporty per klient-waluta oraz per waluta calej firmy maja orders_count, paid_count i paid_revenue. Nie tworz jednej sumy pieniedzy z roznych walut.

### Zadanie 097 - Raport sprzedazy na grainie kraj-kategoria

```python
products = {"A": "course", "B": "ebook"}
orders = [
    {"id": 1, "customer_id": 10, "country": "PL", "status": "paid",
     "items": {("A", 1, 100), ("A", 2, 100), ("B", 1, 20)}},
    {"id": 2, "customer_id": 10, "country": "PL", "status": "paid",
     "items": {("A", 1, 100)}},
    {"id": 3, "customer_id": 20, "country": None, "status": "paid",
     "items": {("X", 1, 50), ("B", 0, 20)}},
    {"id": 4, "customer_id": 30, "status": "paid", "items": {("B", 1, 0)}},
]
```

Dla paid pokaz per kraj-kategoria units_sold, revenue, orders_count i customers_count. Ostatnie dwa pola licza rozne ID, nie pozycje. Krotka pozycji to sku, qty jako nieujemny int i price jako nieujemna cena sztuki. Nieznany SKU odrzuca tylko pozycje; raport bledu zawiera order_id, sku, qty, price. Znana pozycja z qty=0 jest poprawnym pustym wpisem: nie tworzy grupy, nie liczy klienta ani zamowienia i nie zwieksza metryk. Natomiast dodatnia ilosc z price=0 to poprawna bezplatna sprzedaz i tworzy grupe. Country jest opcjonalnym stringiem albo None; brak, None i pusty oczyszczony tekst daja UNKNOWN, pozostale kody zapisz wielkimi literami. ID zamowien sa unikalne. Kontrola porownuje sume revenue grup z wartoscia znanych dodatnich pozycji paid. Nieznane SKU nie trafiaja do zadnej z tych dwoch sum.

### Zadanie 098 - Rezerwacja wszystkiego albo niczego

```python
stock = {"W1": {"A": 3, "B": 1}, "W2": {"A": 2}}
priority = ("W1", "W2")
orders = [
    {"id": 1, "items": [("A", 4), ("B", 2)]},
    {"id": 2, "items": [("A", 4)]},
    {"id": 3, "items": [("A", 1), ("A", 1)]},
]
```

Obsluguj zamowienia w kolejnosci. Qty pozycji jest dodatnim intem, a poczatkowe stany nieujemnymi intami. Powtorzone SKU w jednym zamowieniu oznacza sumowanie zapotrzebowania. Wolno rezerwowac tylko z magazynow wymienionych w priority; ich nazwy sa unikalne i istnieja w stock. Jesli laczna dostepnosc dowolnego SKU nie wystarcza, odrzuc cale zamowienie bez zmiany stanow i raportuj kazdy niedobor jako sku, requested_qty, available_qty, missing_qty. Przy poprawnym zamowieniu przydzielaj towar w kolejnosci priority i zmniejszaj stan roboczy. Rezerwacje maja order_id, warehouse_id, sku i qty; nie tworz zerowych przydzialow. Wynik obejmuje rezerwacje, odrzucone zamowienia z niedoborami i koncowe stany wszystkich magazynow. Wejsciowy stock musi pozostac bez zmian.

### Zadanie 099 - Role, prawa dodatkowe i odebrane uprawnienia

```python
roles = {"reader": {("orders", "read")},
         "editor": {("orders", "read"), ("orders", "write")}}
users = [
    {"id": 1, "roles": ["reader"], "extra": {("customers", "read")}},
    {"id": 2, "roles": ["editor"], "disabled": {("orders", "write")}},
    {"id": 3, "roles": ["unknown"], "suspended": True},
    {"id": 4},
]
requests = [
    {"id": "R1", "user_id": 1, "permission": ("customers", "read")},
    {"id": "R2", "user_id": 2, "permission": ("orders", "write")},
    {"id": "R3", "user_id": 3, "permission": ("orders", "read")},
    {"id": "R4", "user_id": 99, "permission": ("orders", "read")},
]
```

Efektywne prawa uzytkownika to prawa znanych rol i extra, pomniejszone o disabled. Opcjonalne pole roles jest lista nazw; brak oznacza pusta liste. Extra i disabled sa opcjonalnymi setami albo None; brak i None oznaczaja brak praw. Suspended jest opcjonalnym boolem z domyslnym False. Nieznana rola daje ostrzezenie user_id i role oraz zadnych praw. Oblicz prawa i ostrzezenia dla wszystkich users, takze bez wpisow requests. Suspended blokuje dostep, ale nie usuwa efektywnych praw z raportu. Dla kazdego request pokaz id i pierwsza decyzje unknown_user, suspended, allowed, denied. Pokaz efektywne prawa wszystkich users i liczniki wszystkich czterech decyzji, takze zerowe. ID uzytkownikow sa unikalne; nie zmieniaj definicji roles.

### Zadanie 100 - Zamkniety proces od danych surowych do raportow

```python
raw_orders = [
    {"id": 1, "customer": {"id": 10}, "country": " pl ", "status": " PAID ",
     "items": {("SQL", 1, "100.00"), ("BOOK", 2, "10.00")}, "discount": "5.00"},
    {"id": 2, "customer": {"id": 20}, "country": "de", "status": "paid",
     "items": {("SQL", 1, "100,00")}, "discount": None},
    {"id": 1, "customer": {"id": 10}, "country": "PL", "status": "paid",
     "items": {("SQL", 1, "999.00")}},
    {"id": 3, "customer": {"id": 10}, "status": "pending", "items": set()},
    {"id": 4, "customer": {"id": 20}, "status": "paid", "items": {("BOOK", 0, "10.00")}},
    {"id": 5, "customer": {"id": 30}, "country": None, "status": "paid",
     "items": {("BOOK", 1, "20.00")}},
    {"id": 6, "customer": {}, "status": "paid", "items": {("SQL", 1, "10.00")}},
]
```

Przygotuj proces, ktory waliduje, normalizuje, wycenia i deduplikuje zamowienia, a nastepnie tworzy raporty. Nie zmieniaj raw_orders. Obowiazuja nastepujace reguly:

1. Rekord jest dictem. Jego id moze nie istniec lub miec niepoprawny typ; poprawne jest dodatnie int niebedace boolem.
2. Pole customer jest wymaganym dictem, ale jego id moze byc brakujace lub niepoprawne; obowiazuje ten sam warunek co dla ID zamowienia.
3. Pole status jest wymaganym stringiem. Po oczyszczeniu i ujednoliceniu liter dopuszczamy paid, pending i cancelled.
4. Pole items jest wymaganym setem krotek sku, quantity, price_text. SKU jest niepustym stringiem, price_text poprawna nieujemna liczba po oczyszczeniu spacji i ujednoliceniu separatora. Ilosc quantity moze byc niepoprawna: dopuszczamy tylko dodatnie int niebedace boolem. Niepoprawna ilosc odrzuca cale zamowienie. Pusty set pozycji jest poprawny.
5. Opcjonalny discount jest poprawnym nieujemnym tekstem liczbowym albo None. Brak i None daja zero. Rabat nie moze przekroczyc wartosci pozycji. Wszystkie wynikowe kwoty maja byc Decimal.
6. Pole country jest opcjonalnym stringiem albo None. Brak, None lub pusty oczyszczony tekst daje UNKNOWN; pozostale wartosci zapisz wielkimi literami.

Reguly 1-5 maja podana kolejnosc pierwszenstwa. Zapisz tylko pierwszy powod odrzucenia: invalid_order_id, invalid_customer_id, invalid_status, invalid_quantity lub discount_too_high. Raport bledu zawiera indeks wejscia i ID albo None dla jego braku.

Deduplikacja dotyczy tylko poprawnych zamowien: pierwsza poprawna wersja ID wygrywa. Niepoprawny wczesniejszy rekord nie blokuje pozniejszego poprawnego. Poprawne powtorzenie trafia do duplicate_ids, a nie do rejected.

Wyniki:

- clean_orders: nowe rekordy z id, customer_id, country, status, items_value, discount i final_amount;
- rejected: rekordy row_index, raw_id i reason, z oryginalnym ID, takze niepoprawnego typu, albo None przy braku klucza;
- duplicate_ids: ID poprawnych powtorzen, w kolejnosci wejscia;
- paid_report_by_country: liczba paid, przychod po rabacie, liczba unikalnych klientow i srednia wartosc paid per kraj;
- orders_by_customer: ID wszystkich zaakceptowanych zamowien kazdego klienta w kolejnosci wejscia;
- checks: record_count_matches dla rownosci liczby wejsc i sumy liczebnosci trzech rozlacznych kategorii clean_orders, rejected, duplicate_ids oraz revenue_matches dla rownosci przychodu krajow z suma final_amount zaakceptowanych paid.

Raport paid_report_by_country zawiera tylko kraje z co najmniej jednym zaakceptowanym paid, takze o kwocie zero. Srednia to przychod po rabacie podzielony przez liczbe takich zamowien w kraju. Nie tworz grup krajow na podstawie samych pending lub cancelled. Przygotuj takze czytelne komunikaty podsumowujace proces, z kwotami wyswietlanymi do dwoch miejsc po kropce. Kolejnosc elementow setow nie moze wplywac na decyzje ani kwoty.

## Forma rozwiazan

Odpowiedzia na kazde zadanie jest kod w Pythonie tworzacy wskazane struktury wynikowe i komunikaty. Nie dolaczaj odpowiedzi opisowych. Jesli zadanie nie wymaga konkretnej kolejnosci wyniku pochodzacego ze zbioru, kolejnosc ta nie jest oceniana. Pozostale listy wynikowe zachowuja kolejnosc wejscia, chyba ze polecenie ustala inna zasade. Przypadki testowe musza przestrzegac kontraktu danego zadania.

Indeksy diagnostyczne, np. row_index, item_index i transaction_index, sa liczone od 0. Numery opisane w poleceniu jako liczone od 1, np. line_number, row_number i batch_number, pozostaja liczone od 1. Kolejnosc nazw pol lub wymagan otrzymanych ze zbioru nie jest oceniana takze wtedy, gdy pokazesz je w liscie.
