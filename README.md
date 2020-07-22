# blood_pressure_monitor
Prosta aplikacja służąca do prowadzenia prostego dziennika pomiarów ciśnień krwi.

Główne możliwości:
* dodawanie pomiarów ciśnienia
* wyświetlanie dodanych pomiarów
* wyświetlanie wykresów generowanych na postawie dodanych pomiarów
* proste sprawdzanie poprawności pomiarów
* generowanie plików w formatach PDF lub CSV z wprowadzonymi wcześniej danymi
* podanie danych lekarza w celu ułatwienia późniejszego udostępniania swoich wyników
* wysyłanie wprowadzonych pomiarów bezpośrednio do lekarza (jako załącznik w formacie PDF)

## Deploy:
Aplikacja działa pod adresem:
```bash
https://pressure-monitor.herokuapp.com/
```

## Instalacja i uruchomienie
- Utwórz wirutalne środowisko
```bash
virtualenv vnev
```
- Aktywuj stworzone środowisko (Windows)
```bash
venv\Scripts\activate
```
- Sklonuj repozytorium
```bash
git clone https://github.com/JakubWolak/blood_pressure_monitor.git
```
- Zainstaluj wymagane biblioteki
```bash
pip install -r requirements.txt
```
- Wykonaj migracje
```bash
python manage.py migrate
```
- Uruchom serwer
```bash
python manage.py runserver
```
- Gotowe
