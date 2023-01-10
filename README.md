# ResGate

## Setup
Install pipenv:
```bash
pip install pipenv
```
Clone the repo:
```bash
git clone https://github.com/samarth-saxena/resgate-code.git
```
Activate a shell in virtual environment: 
```bash
pipenv shell
```
Install requirements (inside virtual environment):
```bash
pip install -r requirements.txt
```

## Data population
Run in the following order:
```bash
python manage.py runscript load_labs
python manage.py runscript load_users
python manage.py runscript load_profdomains
```