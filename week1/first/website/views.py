from django.http import HttpResponse
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
