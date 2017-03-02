import json
from math import factorial

from django.http import HttpResponse, JsonResponse
from django.utils.html import escape

from .utils import list_urls

table = """
<table>
  <thead>
    <th>Pattern</th>
    <th>Name</th>
    <th>Lookup string</th>
  </thead>

  <tbody>
    {}
  </tbody>
</table>
"""

row = """
<tr>
  <td>{pattern}</td>
  <td>{name}</td>
  <td>{lookup_str}</td>
</tr>
"""

def index(request):
    urls = list_urls()
    contents = []

    for url in urls:
        contents.append(row.format(pattern=escape(url.regex.pattern),
                                   name=url.name,
                                   lookup_str=url.lookup_str))

    contents = "".join(contents)
    return HttpResponse(table.format(contents))


"""
{
    "input": 5
}
"""
def fact(request):
    if request.method == 'POST':
        body = request.body.decode('utf-8')
        body = json.loads(body)
        n = body['input']

        return JsonResponse({'result': factorial(n)})

    return HttpResponse(status=405)
