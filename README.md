# GreenLeaf - Plant Care

GreenLeaf is a plant watering schedule app built using Django.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/j-scoop/plant-tracker.git
$ cd plant-tracker
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv /venv/
$ venv/Scripts/activate.bat
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/gocardless/`.

