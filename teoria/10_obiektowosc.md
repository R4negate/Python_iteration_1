# 10. Obiektowosc - dane i zachowania w jednym modelu

## Zanim przejdziemy do obiektowości: organizacja projektu DE

Pipeline zwykle pobiera dane, przeksztalca je, liczy metryki i przekazuje wynik dalej. W malym cwiczeniu moze to byc jeden plik. Gdy proces rosnie, rozdzielamy **odpowiedzialnosci**, a nie tworzymy osobnego pliku dla kazdej funkcji.

### Jak nazywac pliki

- Male litery i podkreslenia: `order_validation.py`, `sales_metrics.py`.
- Nazwa opisuje zawartosc: `transformations.py` zamiast `nowy.py` czy `kod2.py`.
- Do zwyklych importow unikaj spacji, myslnikow i nazw zaczynajacych sie od cyfry. Plik z cwiczeniami moze miec numer, ale modul do importowania nazwij np. `order_models.py`, nie `10-order-models.py`.
- Nie nazywaj swoich plikow `json.py`, `decimal.py` ani `datetime.py`: moga zaslonic moduly biblioteki standardowej.
- Funkcje i zmienne tez nazywamy przez `snake_case`, np. `normalize_order`, `paid_revenue`.

### Co powinno znalezc sie w ktorym pliku

Prosty projekt dla naszego raportu zamowien:

```text
commerce_pipeline/
    source_data.py
    transformations.py
    metrics.py
    reporting.py
    main.py
```

| Plik | Odpowiedzialnosc | Czego tu nie mieszamy |
|---|---|---|
| `source_data.py` | Przykladowe dane wejsciowe do cwiczenia | Obliczen i wypisywania raportu |
| `transformations.py` | Oczyszczanie tekstow, konwersje i reguly poprawnosci rekordu | Uruchamiania calego procesu |
| `metrics.py` | Liczniki, sumy i agregacje poprawnych danych | Pobierania raw i formatowania komunikatow |
| `reporting.py` | Prezentacja gotowego wyniku | Ponownego liczenia metryk |
| `main.py` | Polaczenie etapow w odpowiedniej kolejnosci | Calej logiki transformacji w jednej duzej funkcji |

`source_data.py` to wygoda do nauki. W projekcie pobierajacym dane z plikow lub API pojawi sie np. `ingestion.py` z funkcjami odczytu. Dane CSV/JSON moga byc w `data/`, ale nie sa modulami Pythona i nie importujemy ich przez `import`.

Gdy beda potrzebne, mozna dodac `config.py` z ustawieniami procesu, `validation.py` z rozbudowanymi regulami i `models.py` z klasami. Nie tworzymy pustych plikow na zapas ani jednego `utils.py` ze wszystkim.

### Maly przyklad bez klas

Kazdy blok zapisz w pliku wskazanym nad nim. 
Plik `source_data.py`:

```python
raw_orders = [
    {"id": "1", "status": " PAID ", "amount": "120,50"},
    {"id": "2", "status": "pending", "amount": "80"},
    {"id": "3", "status": "paid", "amount": "0"},
]
```

Plik `transformations.py`:

```python
from decimal import Decimal


def normalize_orders(raw_orders: list[dict]) -> list[dict]:
    return [
        {"id": int(raw["id"]), "status": raw["status"].strip().lower(), "amount": Decimal(raw["amount"].strip().replace(",", "."))}
        for raw in raw_orders
    ]
```

Plik `metrics.py`:

```python
from decimal import Decimal


def calculate_metrics(orders: list[dict]) -> dict:
    paid_count = 0
    paid_revenue = Decimal("0")
    for order in orders:
        if order["status"] == "paid":
            paid_count += 1
            paid_revenue += order["amount"]
    return {"paid_count": paid_count, "paid_revenue": paid_revenue}
```

Plik `reporting.py`:

```python
def print_report(metrics: dict) -> None:
    print(f"Paid orders: {metrics['paid_count']}")
    print(f"Paid revenue: {metrics['paid_revenue']:.2f}")
```

Plik `main.py`:

```python
from source_data import raw_orders
from transformations import normalize_orders
from metrics import calculate_metrics
from reporting import print_report


def main() -> None:
    orders = normalize_orders(raw_orders)
    metrics = calculate_metrics(orders)
    print_report(metrics)


if __name__ == "__main__":
    main()
```

Z terminala w katalogu `commerce_pipeline` uruchom `python main.py`. Wynik: 2 paid i przychod 120.50. 

```text
main -> dane -> transformacja -> metryki -> prezentacja
```

### Gdzie w tym miejsce na obiektowosc?

Podzial na pliki nie wymaga klas: powyzszy pipeline dziala funkcjami. Jednak za chwile zbudujemy `Order` jako klasę, jego definicja moze trafic do `models.py`. Transformacja bedzie zwracac obiekty (instancje klasy) zamiast dictow, a `main.py` nadal polaczy etapy.

## Po co nam obiektowosc

Do tej pory dane zamowienia trzymalismy w slowniku, a dotyczace go operacje w funkcjach. Klasa pozwala polaczyc je w jednym modelu, np. Order z metoda is_paid(). W tej lekcji przejdziemy od znanego slownika do obiektu zamowienia i wykorzystamy go w pipeline.

## 1. Punkt wyjscia: dict i funkcja

```python
order = {"order_id": 1001, "status": "paid"}


def is_paid(order: dict) -> bool:
    return order["status"] == "paid"


print(is_paid(order))
```

Jeden slownik przechowuje dane danego zamówienia, a funkcja otrzymuje go jako argument i pyta o status. Wynik to True.

## 2. Klasa to wlasny typ, obiekt to konkretna instancja

**Klasa jest definicją danego rodzaju obiektów w programie.** Opisujemy w niej, jakie dane chcemy przechowywac w tych obiektach i jakie operacje beda mogly wykonywac. Dla klasy `Order` tym rodzajem rzeczy jest zamowienie.

Zacznijmy od pytania: co wiemy o pojedynczym zamowieniu i co chcemy z nim robic?

| Co opisuje Order? | Przyklady | Znaczenie |
|---|---|---|
| Dane, czyli atrybuty obiektu | order_id, customer_id, total_amount, status | Numer zamowienia, klient, kwota i aktualny status |
| Zachowania, czyli metody | is_paid(), mark_paid() | Sprawdzenie, czy zamowienie jest oplacone, i oznaczenie go jako oplacone |

Wartosci atrybutow tworza **stan konkretnego obiektu**. Przykladowo jedno zamowienie moze miec numer 1001, kwote 120.50 i status pending, a drugie numer 1002, kwote 0 i status paid. Oba zamowienia są typem Order (instancją klasy Order), ale przechowuja inne dane.

Metody korzystaja z tych danych. Is_paid ma sprawdzac status tego zamowienia, na ktorym zostala wywolana. Mark_paid ma zmieniac jego status. Oznaczenie pierwszego jako oplaconego nie powinno samo zmienic drugiego.

```text
Klasa Order: wspolna definicja danych i zachowan

    pierwszy obiekt   :              drugi obiekt:
    -order_id: 1001                  -order_id: 1002
    -total_amount: 120.50            -total_amount: 0
    -status: pending                 -status: paid

    is_paid() -> False              is_paid() -> True
```

Najpierw zbudujemy pusty szkielet klasy, a w kolejnych sekcjach dodamy dane i zachowania:

```python
class Order:
    pass


first_order = Order()
second_order = Order()
print(type(first_order))
print(first_order is second_order)
```

`class Order:` definiuje klase o nazwie Order. Wciecie wyznacza jej zawartosc. `pass` jest instrukcja, ktora nic nie robi; pozwala chwilowo zostawic puste cialo klasy.

`Order()` tworzy nowy obiekt, zwany tez instancja. `first_order` jest nazwa wskazujaca na ten obiekt. Drugie wywolanie tworzy kolejny obiekt, wiec porownanie tozsamosci daje False. Porownujemy tutaj dwa obiekty, nie ich biznesowe numery zamowien.

Poniewaz w ciele klasy jest na razie tylko pass, te obiekty nie maja jeszcze naszych atrybutow order_id czy status ani metod is_paid i mark_paid. Nazwanie klasy Order nie tworzy tych elementow automatycznie. Teraz dopiero nauczymy sie je definiowac.

## 3. Atrybut: wartosc dostepna przez obiekt

```python
class Order:
    pass


order = Order()
order.order_id = 1001
order.status = "pending"
print(order.order_id)
print(order.status)
```

Najpierw tworzymy obiekt. Potem `order.order_id = 1001` ustawia na nim atrybut order_id, a kolejna linia atrybut status..

Reczne dopisywanie atrybutow jest mozliwe, ale latwo pominac pole. Gdy nikt nie ustawi amount, odczyt `order.amount` zglosi AttributeError. Chcemy inicjalizowac wymagane pola w jednym miejscu:

## 4. `__init__`: przygotowanie stanu nowego obiektu (tak zwany konstruktor klasy)

```python
class Order:
    def __init__(self, order_id: int, status: str) -> None:
        self.order_id = order_id
        self.status = status


order = Order(1001, "pending")
print(order.order_id, order.status)
```

Przy `Order(1001, "pending")` Python tworzy obiekt i wywoluje jego `__init__`, aby go zainicjalizowac. Na tym etapie nie musisz znac technicznego mechanizmu tworzenia obiektu. Wazne rozroznienie: `__init__` ustawia stan; nie zwraca gotowego obiektu przez return.

## 5. Metoda: funkcja wywolywana na obiekcie

```python
class Order:
    def __init__(self, order_id: int, status: str) -> None:
        self.order_id = order_id
        self.status = status

    def is_paid(self) -> bool:
        return self.status == "paid"


first = Order(1001, "paid")
second = Order(1002, "pending")
print(first.is_paid())
print(second.is_paid())
```

Metoda ta zwraca wynik status == "paid" przez return.

## 9. `__repr__` i `__str__`: obiekt widoczny jako tekst

Bez wlasnej reprezentacji funkcji `__str__` funkcja 'print()' obiektu zwykle pokazuje opis techniczny w rodzaju `<__main__.Order object at ...>`. Nie widzimy wtedy biznesowego ID ani statusu.

`__str__` odpowiada na pytanie „Jak pokazać ten obiekt komuś, kto chce po prostu przeczytać informację?”  

`__str__` określa, jak obiekt ma wyglądać jako czytelny komunikat, np. Import shop: 3 rows. Python korzysta z niej przy print(run) i str(run).  


`__repr__` odpowiada na pytanie „Jak opisać obiekt, żebym podczas sprawdzania kodu widział jego klasę i wartości pól? czyli widzisz nazwę klasy, nazwy atrybutów i ich wartości  

`__repr__` określa, jak pokazać obiekt podczas sprawdzania kodu, np. ImportRun(source='shop', rows_count=3): jaka to klasa i jakie wartości zawiera. Python korzysta z niej przy repr(run) oraz przy wyświetlaniu elementów listy, np. print([run]).  

```python
class ImportRun:
    def __init__(self, source: str, rows_count: int) -> None:
        self.source = source
        self.rows_count = rows_count

    def __repr__(self) -> str:
        return f"ImportRun(source={self.source!r}, rows_count={self.rows_count})"

    def __str__(self) -> str:
        return f"Import {self.source}: {self.rows_count} rows"


run = ImportRun("shop", 3)
print(run)
print(repr(run))
```

wypisze: 
```
Import shop: 3 rows
ImportRun(source='shop', rows_count=3)
```

## 10. Gotowy model Order

```python
from decimal import Decimal


class Order:
    def __init__(self, order_id: int, customer_id: int, total_amount: Decimal, status: str, country: str = "UNKNOWN") -> None:
        if type(order_id) is not int or type(customer_id) is not int:
            raise TypeError("IDs must be int, not bool")
        if order_id <= 0 or customer_id <= 0:
            raise ValueError("IDs must be positive")
        if not isinstance(total_amount, Decimal):
            raise TypeError("Amount must be Decimal")
        if not total_amount.is_finite() or total_amount < 0:
            raise ValueError("Amount must be finite and non-negative")
        if not isinstance(status, str) or not isinstance(country, str):
            raise TypeError("Status and country must be text")
        normalized_status = status.strip().lower()
        if normalized_status not in {"paid", "pending", "cancelled"}:
            raise ValueError("Unsupported status")
        self.order_id = order_id
        self.customer_id = customer_id
        self.total_amount = total_amount
        self.status = normalized_status
        self.country = country.strip().upper() or "UNKNOWN"

    def is_paid(self) -> bool:
        return self.status == "paid"

    def mark_paid(self) -> None:
        if self.status == "cancelled":
            raise ValueError("Cancelled order cannot be paid")
        self.status = "paid"

    def get_segment(self) -> str:
        if self.total_amount >= Decimal("300"):
            return "high"
        return "standard"

    def to_dict(self) -> dict:
        return {"order_id": self.order_id, "customer_id": self.customer_id, "total_amount": self.total_amount, "status": self.status, "country": self.country, "is_paid": self.is_paid()}

    def __repr__(self) -> str:
        return f"Order(order_id={self.order_id}, customer_id={self.customer_id}, total_amount={self.total_amount!r}, status={self.status!r}, country={self.country!r})"


order = Order(1001, 7, Decimal("120.50"), " PAID ", " pl ")
print(order)
print(order.is_paid(), order.get_segment())
```

### Co robi kazda czesc?

- `__init__` - sprawdza dane przed zapisaniem ich w obiekcie: dodatnie ID typu int (bez bool), skonczona nieujemna kwota Decimal oraz tekstowy status i kraj. Zly typ powoduje TypeError, a niedozwolona wartosc ValueError.
- `status.strip().lower()` - usuwa brzegowe spacje i zamienia status na male litery. Dopuszczamy tylko paid, pending i cancelled.
- `self.order_id = order_id` i kolejne przypisania - zapisuja dane jako atrybuty konkretnego zamowienia. Kraj jest oczyszczany i zamieniany na wielkie litery; pusty tekst daje UNKNOWN. Pominiety argument country tez ma domyslne UNKNOWN, ale None nie jest dozwolone.
- `is_paid()` - zwraca True albo False na podstawie aktualnego statusu, bez zmiany obiektu.
- `mark_paid()` - zmienia status na paid. Dla cancelled zglasza ValueError przed zmiana; przy sukcesie zwraca None.
- `get_segment()` - zwraca high dla kwoty co najmniej 300, a standard ponizej. Nie zmienia danych ani nie sprawdza statusu.
- `to_dict()` - zwraca nowy slownik z danymi zamowienia i aktualna flaga is_paid. Kwota nadal jest Decimal; to nie jest jeszcze tekst JSON.
- `__repr__()` - zwraca czytelny opis klasy i jej pol. Tutaj nie mamy wlasnego __str__, wiec print(order) korzysta z tego opisu. Zapis !r pokazuje reprezentacje wartosci, np. string w cudzyslowach.
- `Order(...)` na koncu - tworzy konkretne zamowienie: ID 1001, klient 7, kwota 120.50, status paid i kraj PL. Ostatnia linia wypisuje True oraz standard.

Walidacja dziala podczas inicjalizacji. Publiczne atrybuty nadal mozna zmienic bezposrednio, omijajac reguly zapisane w metodach.

## 17. Dodatkowo: co oznacza dziedziczenie i polimorfizm

Dziedziczenie pozwala zdefiniowac klase na podstawie innej.

```python
class TextReporter:
    def render(self, count: int) -> str:
        return f"Rows: {count}"


class ShortReporter(TextReporter):
    def render(self, count: int) -> str:
        return f"rows={count}"


reporters = [TextReporter(), ShortReporter()]
for reporter in reporters:
    print(reporter.render(3))
```

ShortReporter dziedziczy po TextReporter i nadpisuje render. 

## 18. Kiedy klasa, a kiedy prostsze rozwiazanie

| Potrzeba | Rozsadny punkt wyjscia |
|---|---|
| Surowy rekord z JSON | dict |
| Jedna niezalezna normalizacja | funkcja |
| Model z kilkoma spojnymi regulami | klasa, np. Order |
| Obiekt przechowujacy konfiguracje i stan kolejnych operacji | klasa, np. klient API |

## 19. Zapis @: dekoratory i dataclass

### 19.1. Zaczynamy od problemu: znowu piszemy te same metody

Potrafimy juz utworzyc klase zamowienia. Zobacz uproszczony przyklad:

```python
from decimal import Decimal


class Order:
    def __init__(self, order_id: int, total_amount: Decimal, status: str) -> None:
        self.order_id = order_id
        self.total_amount = total_amount
        self.status = status

    def __repr__(self) -> str:
        return f"Order(order_id={self.order_id}, total_amount={self.total_amount!r}, status={self.status!r})"

    def is_paid(self) -> bool:
        return self.status == "paid"


order = Order(1001, Decimal("120.50"), "paid")
print(order)
print(order.is_paid())
```

Wynik:

```text
Order(order_id=1001, total_amount=Decimal('120.50'), status='paid')
True
```

W tym kodzie sa dwie rozne rzeczy:

- `__init__` i `__repr__` wykonuja powtarzalna prace: zapisuja przekazane pola i pokazuja je jako tekst.
- `is_paid()` zawiera nasza regule dotyczaca zamowienia.

Przy nastepnej klasie, np. Product, znowu napisalibysmy podobne przypisania i opis pol. Czy mozemy podac liste pol, a te powtarzalne metody dostac automatycznie? Wlasnie do tego przyda sie gotowe narzedzie `dataclass`.

### 19.3.  @dataclass

Mozemy zapisac `@dataclass` bezposrednio nad definicja klasy:

```python
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Order:
    order_id: int
    total_amount: Decimal
    status: str

    def is_paid(self) -> bool:
        return self.status == "paid"


order = Order(1001, Decimal("120.50"), "paid")
print(order)
print(order.is_paid())
```

Dzieki temu niektóre powtarzalne funkcje zostaną za nas utworzone automatycznie 

```text
Order(order_id=1001, total_amount=Decimal('120.50'), status='paid')
True
```

**Taki zapis z @ nazywamy zastosowaniem dekoratora.** W tym przykladzie oznacza: po zdefiniowaniu klasy zastosuj do niej funkcje dataclass.

Dekorator to narzedzie stosowane przy definicji klasy lub funkcji, ktore moze ja uzupelnic albo zmienic sposob korzystania z niej. Tutaj konkretny efekt juz widzisz: dataclass przygotowala init i repr na podstawie pol. Inne dekoratory, ktore poznamy dalej, beda sluzyc innym zadaniom.

`@dataclass` dotyczy klasy bezposrednio pod nim. Nie dotyczy calego pliku i nie oznacza dodatkowego pola zamowienia. Stosujemy go przy definiowaniu klasy, a nie recznie przed kazdym tworzeniem Order.

### 19.4. Co dostajemy, a co nadal piszemy sami?

Domyslnie dataclass przygotowuje m.in.:

| Metoda | Co robi dla naszych danych? |
|---|---|
| `__init__` | przyjmuje order_id, total_amount i status oraz zapisuje je na obiekcie |
| `__repr__` | tworzy opis Order z wartosciami pol |
| `__eq__` | pozwala porownywac wartosci pol dwoch obiektow tej samej klasy przez == |

Ostatnia metoda jest dla nas nowoscia. Po ostatniej definicji Order uruchom:

```python
same_values = Order(1001, Decimal("120.50"), "paid")
print(order == same_values)
print(order is same_values)
```

Wynik: True i False. Obiekty maja rowne wartosci pol, ale nadal sa dwiema instancjami. Dataclass nie usuwa duplikatow i nie pilnuje unikalnego order_id. Rownosc dotyczy tutaj wszystkich pol, nie samego ID.

### 19.6. Potrzebujemy sprawdzen: __post_init__

W sekcji 10 sprawdzalismy dane w recznie napisanym init. Teraz init przygotowuje za nas dataclass. Gdzie umiescic sprawdzenie dodatniego ID lub poprawnego statusu?

Mozemy napisac metode `__post_init__`. Init wygenerowany przez dataclass wywola ja po zapisaniu pol:

```text
Order(1001, kwota, status)
    -> wygenerowany init zapisuje pola na self
    -> nasze post_init sprawdza i oczyszcza te pola
    -> otrzymujemy przygotowany obiekt albo wyjatek
```

```python
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Order:
    order_id: int
    total_amount: Decimal
    status: str

    def __post_init__(self) -> None:
        if type(self.order_id) is not int:
            raise TypeError("Order ID must be int, not bool")
        if self.order_id <= 0:
            raise ValueError("Order ID must be positive")
        if not isinstance(self.total_amount, Decimal):
            raise TypeError("Amount must be Decimal")
        if not self.total_amount.is_finite() or self.total_amount < 0:
            raise ValueError("Amount must be finite and non-negative")
        if not isinstance(self.status, str):
            raise TypeError("Status must be text")
        self.status = self.status.strip().lower()
        if self.status not in {"paid", "pending", "cancelled"}:
            raise ValueError("Unsupported status")

    def is_paid(self) -> bool:
        return self.status == "paid"


order = Order(1001, Decimal("120.50"), " PAID ")
print(order.status, order.is_paid())

try:
    Order(1002, Decimal("-1"), "paid")
except ValueError as exc:
    print(f"Odrzucono: {exc}")
```

Wynik:

```text
paid True
Odrzucono: Amount must be finite and non-negative
```

Odczytujemy `self.status`, bo wygenerowany init zapisal juz wartosc na obiekcie. Nie wywolujemy post_init recznie po kazdej instancji.

Przepisalismy mniej technicznych przypisan, ale reguly nadal sa naszym kodem. Jesli przerabiasz pelny model z sekcji 10, zachowaj tez jego pozostale pola, sprawdzenia i metody. Ten mniejszy przyklad pokazuje tylko mechanizm.

Automatyczne wywolanie post_init pochodzi z wygenerowanego init. Jesli napiszesz wlasny init, musisz sam zadbac o potrzebne wywolania. Tak jak w zwyklej klasie sprawdzenie podczas tworzenia nie kontroluje kazdej pozniejszej zmiany publicznego pola.

### 19.7. Chcemy przekazac dane dalej: asdict

Dalszy etap raportu moze potrzebowac slownika zamiast obiektu. Dla dataclass gotowa funkcja `asdict` przygotowuje slownik z jej pol. Po ostatnim przykladzie:

```python
from dataclasses import asdict

row = asdict(order)
print(row)
print("is_paid" in row)
```

Wynik:

```text
{'order_id': 1001, 'total_amount': Decimal('120.50'), 'status': 'paid'}
False
```

Asdict odczytuje pola, ale nie wywoluje is_paid. Nasz reczny to_dict z sekcji 10 celowo dodawal wynik tej metody, wiec oba sposoby nie sa identyczne. Kwota nadal jest Decimal: otrzymalismy dict, nie gotowy tekst JSON.


### 19.9. Konfiguracja, ktorej nie chcemy zmieniac w trakcie procesu

Przy konfiguracji mozemy chciec ustalic source i batch_size na poczatku, a potem zablokowac przypadkowe przypisanie nowych wartosci. Do tego sluzy opcja `frozen=True`:

```python
from dataclasses import dataclass, FrozenInstanceError


@dataclass(frozen=True)
class ExportConfig:
    source: str
    batch_size: int = 500


config = ExportConfig("shop")
try:
    config.batch_size = 100
except FrozenInstanceError:
    print("Nie mozna zmienic batch_size")
print(config.batch_size)
```

Wynik: komunikat o braku mozliwosci zmiany, potem 500.

Nawiasy przy dataclass podaja ustawienia dekoratora. Frozen=True ogranicza zwykle przypisania do pol po utworzeniu obiektu. To nie walidacja: bez wlasnych sprawdzen nadal moglibysmy utworzyc konfiguracje z blednym rozmiarem. Nie zamraza tez automatycznie zawartosci zagniezdzonych list.

### 19.10. Chcemy czytac obliczenie jak pole: @property

Pozycja zamowienia ma ilosc i cene. Sume mozemy liczyc znana juz metoda:

```python
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class OrderLine:
    quantity: int
    unit_price: Decimal

    def total_amount(self) -> Decimal:
        return self.quantity * self.unit_price


line = OrderLine(2, Decimal("10.50"))
print(line.total_amount())
```

Wynik: 21.00. Czasem chcemy czytac taka kwote jak pole rekordu: `line.total_amount`, ale nadal obliczac ja z aktualnej ilosci i ceny, zamiast przechowywac stara sume.

Dodajemy `@property` nad ta metoda:

```python
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class OrderLine:
    quantity: int
    unit_price: Decimal

    @property
    def total_amount(self) -> Decimal:
        return self.quantity * self.unit_price


line = OrderLine(2, Decimal("10.50"))
print(line.total_amount)
line.quantity = 3
print(line.total_amount)
```

Wynik: 21.00, a potem 31.50. Property oznacza tutaj: **przy odczycie tej nazwy wykonaj metode i oddaj jej wynik**. Dlatego nie dopisujemy nawiasow.

Bez property zwykla metoda tez liczylaby aktualna sume, ale wywolywalibysmy ja przez nawiasy. Property zmienia sposob korzystania z obliczenia, a nie zasady mnozenia.

W tym przykladzie przygotowalismy tylko odczyt total_amount, nie obsluge przypisywania do niego wartosci. Zmieniamy quantity lub unit_price, a wynik jest liczony ponownie.

### 19.11. Chcemy tworzyc obiekt z surowego rekordu: @classmethod

Wczesniej tworzylismy obiekt przez `Order(id, kwota, status)`. Surowy rekord ma jednak stringi, ktore trzeba zamienic. Mozemy udostepnic nazwany sposob tworzenia: `Order.from_raw(raw)`.

Ponizej jest osobny, uproszczony przyklad. Raw zawiera poprawne wymagane stringi: dodatnie ID, skonczona nieujemna kwote oraz dozwolony status po oczyszczeniu. Pokazujemy miejsce tworzenia obiektu, nie kolejny pelny walidator.

```python
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Order:
    order_id: int
    total_amount: Decimal
    status: str

    @classmethod
    def from_raw(cls, raw: dict) -> "Order":
        return cls(
            order_id=int(raw["id"]),
            total_amount=Decimal(raw["amount"].strip().replace(",", ".")),
            status=raw["status"].strip().lower(),
        )


raw = {"id": "1001", "amount": "120,50", "status": " PAID "}
order = Order.from_raw(raw)
print(order)
```

Wynik:

```text
Order(order_id=1001, total_amount=Decimal('120.50'), status='paid')
```

`@classmethod` sprawia, ze Python przekazuje do metody klase jako pierwszy argument. Zwyczajowo nazywamy go `cls`.

- Przy wywolaniu `Order.from_raw(raw)` parametr cls wskazuje Order.
- `cls(...)` tworzy instancje tej otrzymanej klasy.
- Nie ma self, bo do utworzenia nowego zamowienia nie potrzebujemy istniejacego zamowienia.

Adnotacja `"Order"` po strzalce opisuje typ wyniku, nie zwracany string. Zapis tekstowy pozwala wskazac klase podczas jej definiowania.

From_raw mogloby tez byc zwykla funkcja w module. Metoda klasowa jest jednym ze sposobow umieszczenia takiej operacji przy modelu.

### 19.12. Pomocnik nie potrzebuje ani obiektu, ani klasy: @staticmethod

Oczyszczenie samego tekstu statusu nie wymaga gotowego zamowienia. Wystarczy przekazany string. Jesli chcemy miec taki pomocnik w klasie, mozemy oznaczyc go jako metode statyczna:

```python
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Order:
    order_id: int
    total_amount: Decimal
    status: str

    @staticmethod
    def normalize_status(raw_status: str) -> str:
        return raw_status.strip().lower()


print(Order.normalize_status(" PAID "))
```

Wynik: paid.

`@staticmethod` oznacza, ze Python nie dodaje automatycznie ani self, ani cls. Metoda otrzymuje tylko przekazany tekst. Nie tworzymy w tym celu Order i nie zmieniamy statusu zadnego istniejacego zamowienia.

Taka normalizacja moze pozostac zwykla funkcja w transformations.py. Metoda statyczna daje mozliwosc umieszczenia jej przy modelu, ale nie jest obowiazkiem.
