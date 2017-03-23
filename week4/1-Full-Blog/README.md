# A complete blog with theme

We are going to make a complete blog this time. We are going to use [the following theme](https://my.pcloud.com/publink/show?code=kZTA9UZ0XYiQJcgn3HkDl9tlTxwepweasl7)

## Features

This is an upgrade of [the previous blog problem](https://github.com/HackBulgaria/Web-Development-with-Django/tree/master/week3/1-Simple-Blog) with the following additions:

* For the index page, list the articles as follows: <http://www.inspirothemes.com/polo-v2/home-blog-v4.html#>
  * Ignore the header carousel. We want be using it.
* For a specific blog post, use the following theme: <http://www.inspirothemes.com/polo-v2/blog-post.html>. Comments included!
  * Again, ignore all header images

## Authors

We want to support authors. One blog post can have multiple authors. Authors should be valid Django users (`django.contrib.auth.models.User`)

Make sure to display the authors when listing blog posts or displaying a specific post.

## Blog administration

For blog administration, we are going to use the built-in Django admin:

* Blog posts will be created from the admin site.
* Users will be created from the command line (`createsuperuser`).

## Static files

The big question here is, who is going to serve the static files? (css, js, etc.)

* One way to do it is not to serve static files at all - use CDNs and link them.
* Another way is to use Django's built-in `staticfiles` app - <https://docs.djangoproject.com/en/1.10/howto/static-files/>
