# Blog

Our blog should have a private and public post blogs.

Therefore your tasks are:

## Models

  Update  `BlogPost` model with new boolean field - `is_private`. It will be `False` for public posts and `True` for private, by default `False`.

## Custom QuerySets

  Write custom QuerySet for `BlogPost` model:

    * `get_public_posts` -> return all public posts

    * `get_private_posts` -> return all private posts

## Views
  * `index` - lists public blog posts
            - logged user can see private posts, too

  * `create_blog_post` - only logged user can create blog post

## Tests
  If you use postgre for database, you should create a test db.
  Create new folder in blog app - `tests`.
  Write tests for - `services`, `querysets`, `views` in different files.

  Execute tests with - `python manage.py test`

  In case of need use debugger- `import ipdb; ipdb.set_trace()`

## Hints

* <https://docs.djangoproject.com/en/1.10/topics/testing/tools/>
* <https://docs.djangoproject.com/en/1.10/topics/testing/overview/>
* <https://docs.djangoproject.com/en/1.10/topics/db/managers/>
* <http://factoryboy.readthedocs.io/en/latest/recipes.html/>
