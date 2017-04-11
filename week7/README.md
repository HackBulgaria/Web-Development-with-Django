# Permissions

* Every Django project has a default permissions for every model. [Permissions](https://docs.djangoproject.com/en/1.11/topics/auth/default/#permissions-and-authorization).
* (Using mixins with class-based views) (https://docs.djangoproject.com/en/1.10/topics/class-based-views/mixins/)
* When using class-based views if you want to limit access you should use [UserPassesTestMixin](https://docs.djangoproject.com/en/1.11/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin).
You have to override `test_func` method in your own `mixin`.
