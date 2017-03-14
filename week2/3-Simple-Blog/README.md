# Simple Blog

A web development course with any framework won't be complete if we don't implement a very simple blog.

But with a little twist. All content will be markdown-driven.

## Models

We want to support the following models:

* `BlogPost` and we want to know
  * What's the title? Make it unique.
  * When it was created?
  * When it was updated?
  * What's the content?
  * What are the tags for that post? One post can have many tags. One tag can have many posts. **hint, hint**
* `Tag` - a simple model holding tag names.
* `Comment` - a simple model holding comment information.
  * What's the email of the author of that comment
  * What's the creation date of that comment?
  * What's the content of that comment?

## Views

We will support 3 very simple views:

### Index view - a list of all blog posts

Create a table showing all blog posts. There should be a link for detail view for each of the posts.

### Detail view for a given blog article

Identified by a primary key, we need to have a view, where we can see the content of the article.

The magic here is that the content should be rendered as a markdown.

For that purpose, create your own `markdown` custom template filter:

```
{% autoescape off %}
  {{ post.content|markdown }}
{% endautoescape %}
```

**Here, we should be able to see & post comments for that post.**

### Post create view

A simple form, where we can create new blog posts. We should be able to add tags from here.

## Hints

* <https://docs.djangoproject.com/en/1.10/howto/custom-template-tags/>
* <https://docs.djangoproject.com/en/1.10/topics/db/examples/many_to_many/>
* <https://pypi.python.org/pypi/Markdown>
