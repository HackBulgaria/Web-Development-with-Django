# 1-PDF-Generation

You task is to create a simple python & celery project that reads a website and downloads it as a pdf:

```shell
$ python pdfthis.py download https://hackbulgaria.com
PDF for https://hackbulgaria will be generated. Check with this UUID: 8fba6dfd-3327-427a-87be-afd94a8efb0d
$ python pdfthis.py check 8fba6dfd-3327-427a-87be-afd94a8efb0d
PDF for https://hackbulgaria.com is located in downloads/hackbulgaria_com.pdf
```

One important things:

* `pdfthis.py` should not block! The main idea is to have Celery tasks that will do the heavy-lifting.

## PDF Generation

For pdf generation, use this - <https://pypi.python.org/pypi/pdfkit/0.4.1>
