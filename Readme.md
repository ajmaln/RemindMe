# Remind Me
A TODO app created using Django Framework

### Installation

Create virtualenv

```bash
virtualenv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Do migrations

```bash
./manage.py makemigrations
./manage.py makemigrations todo
./manage.py migrate
```

### Running

Start development server

```bash
./manage.py runserver
```
