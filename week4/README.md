# Week 4 - Users & Authentication

* We will take a deep-dive into [Django's Auth system](https://docs.djangoproject.com/en/1.10/topics/auth/)
* We will be using [Django's session system](https://docs.djangoproject.com/en/1.10/topics/http/sessions/)

## Thigns to show

* User models from `django.contrib.auth` - `AbstractBaseUser`, `AbstractUser`, `User`, `AnonymousUser`
* `AbstractBaseSession` and `Session` from `django.contrib.sessions`
* `django_session` database
* What happens when we `authenticate` and `login`
* How session is attached to every request as a cookie and `request.session`
* `@login_required` decorator
* Implement `@anonymous_required`
