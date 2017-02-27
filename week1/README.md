# Week 1

Getting ready:

* Be on Linux or Mac.
* Install latest Python (`3.5` or `3.6` will do)
* Get familiar with the concept of [`virtualenv`](https://virtualenv.pypa.io/en/stable/)
  * We recommend using [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/) for ease of management of virtual envs.
* Install Django (in a virtual env) - `pip install Django`
* [Check the official tutorial](https://docs.djangoproject.com/en/1.10/intro/tutorial01/)


## What is Django?

Agenda for the first week. Will show the bullets step by step with debugger.

* Create new django project - `django-admin startproject first`
* Key parts - `manage.py`, `first/settings.py`, `first/urls.py` and `first/wsgi.py` 
* `python manage.py runserver`
  * Setups Django.
  * Gets `first.wsgi.application` and starts listening at port `8000`.
  * When request comes, WSGI Application handles it.
  * Middlewares are executed - code before view.
  * `first.urls.urlpatterns` is checked for a match. Returns view which executes.
  * Middlewares are executed - code after view.
  * Response is constructed and returned.


Docs for further reading:

* <https://docs.djangoproject.com/en/1.10/topics/http/urls/>
* <https://docs.djangoproject.com/en/1.10/topics/http/middleware/>
* <https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/>
