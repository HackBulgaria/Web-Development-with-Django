# Django Calculator

Write a dead-simple django application, which exposes simple calculator API that responds either in plain text or JSON.

We will need to support the following urls:

* `/calculator/add/<a>/<b>/` -> returns the sum of `a` and `b` (integers)
* `/calculator/multiply/<a>/<b>/` -> returns the product of `a` and `b` (integers)
* `/calculator/power/<a>/<b>/` -> returns `a^b` (integers)
* `/calculator/fact/<n>/`-> returns `n!`


All views should support taking extra `?format=json` GET parameter. If we have that parameter, the response should be JSON in the following format:

```
{
  result: <the result here>
}
```

## Boostrap

All urls should be routed from a `calculator` app.

1. `django-admin startproject django_calculator`
2. `cd django_calculator && python manage.py startapp calculator`

## Testing

There's a dead simple `test_client.py` which will run some tests against `http://localhost:8000`. All you need to do:

1. `pip install -r requirements.txt`
2. `python test_client.py`
