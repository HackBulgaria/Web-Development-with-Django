from django.contrib.auth.decorators import user_passes_test


def anonymous_required(function=None, profile_url=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: not u.is_authenticated,
        login_url=profile_url,
        redirect_field_name=None
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
