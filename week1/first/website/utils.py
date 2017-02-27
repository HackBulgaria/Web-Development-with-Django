from collections import deque
from django.core import urlresolvers


def list_urls():
    """
    Simple listing of URLs, using BFS strategy
    We either have a resolver with url_patterns or a concrete matcher.
    """
    result = []
    urls = urlresolvers.get_resolver().url_patterns
    urls = deque(urls)

    while urls:
        url = urls.pop()

        if not hasattr(url, 'url_patterns'):
            result.append(url)
            continue

        for item in url.url_patterns:
            urls.appendleft(item)

    return result
