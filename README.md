# blood_pressure_monitor
Prosta aplikacja służąca do sprawdzania oraz monitorowania swoich pomiarów ciśnień krwi

## v0.1
W początkowej wersji aplikacja ma umożliwiać użytkownikom:
* dodawanie pomiarów ciśnienia
* wyświetlanie dodanych pomiarów
* wyświetlanie wykresów generowanych na postawie dodanych pomiarów
* proste sprawdzanie poprawności pomiarów

## Dalsze cele
- generowanie możliwych do pobrania wykresów oraz tabel z pomiarami
- dodanie własnego lekarza
- wysyłanie wprowadzonych pomiarów bezpośrednio do lekarza

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
