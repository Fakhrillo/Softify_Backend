# Softify Backend

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Fakhrillo/Softify_Backend.git
$ cd Softify_Backend
```

Create .env and add necessary environment variables (important one is `SECRET_KEY`)

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv env (python on Windows)
$ source env/bin/activate (env\Scripts\activate on Windows)
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py makemigrations && python manage.py migrate
(env)$ python manage.py createsuperuser (create super user to access admin page)
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/admin/`.

If you are using Windows you may run into problems with GDAL integration, to fix this issue you need to install GDAL, just search on Google

## Walkthrough

This was intended for Softify my first work place's website this is just a simple Django backend project, you may find some features interesting and integrate it to your application