from django.contrib.auth.base_user import BaseUserManager


class BaseUserManager(BaseUserManager):
    use_in_migrations = True  # use in migrations with `RunPython`

    def _create_user(self, email, password, **kwargs):
        email = self.normalize_email(email)

        user = self.model(email=email, **kwargs)
        user.is_staff = kwargs.get('is_superuser', False)

        if password is None or password.strip() == '':
            user.set_unusable_password()
        else:
            user.set_password(password)

        user.save(using=self._db)

        return user

    def create(self, email, password, **kwargs):
        kwargs.setdefault('is_superuser', False)

        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **kwargs)


class AuthorManager(BaseUserManager):
    """Managers are inherited only if the inherited class is `abstract=true`"""


class BuyerManager(BaseUserManager):
    """Managers are inherited only if the inherited class is `abstract=true`"""
