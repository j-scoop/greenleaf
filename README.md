# GreenLeaf - Plant Care

GreenLeaf is a plant watering schedule app built using Django. You can use it to keep track of your plants, 
simply add them to your profile and log their status, last watered and add any notes.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/j-scoop/plant-tracker.git
$ cd plant-tracker
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv ./venv/
$ venv/Scripts/activate.bat
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```

Create a .env file in your project directory and place your SECRET_KEY inside it:
```sh
SECRET_KEY = '*6weiv*lnf2(e%kno0mnnkb1ozsmbh7177a%la=yj$1i&ruai$'
```

Note: it is recommended you generate your own unique SECRET_KEY. This can be done in the Python
console by doing the following:

```sh
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
```

Create the database tables:

```sh
(venv)$ py manage.py makemigrations

(venv)$ py manage.py migrate
```

You can then run the development server:
```sh
(venv)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

From here you can make Register an account and start adding your plants!
