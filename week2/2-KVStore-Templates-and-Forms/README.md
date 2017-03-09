# Extending our Key-Value store with templates and forms

Continuing from the last iteration of our key-value store, now we want to add some HTML, using Django's template language.

## `/api/*`

First, we need to separate our API views from our HTML views.

We want the following changes:

* `/storage/create-user/` -> `/api/storage/create-user/`
* `/storage/<user-identifier>/` -> `/api/storage/<user-identifier>/`
* `/storage/<user-identifier>/<key>/` -> `/api/storage/<user-identifier>/<key>/`

The behaviour stays the same.

## Extending the models

We want to store creation time for both our users and each key-value pair. Use [`DateTimeField`](https://docs.djangoproject.com/en/1.10/ref/models/fields/#django.db.models.DateTimeField)

Usually, this field is named `created_at`

## HTML Views

We want to introduce new views which will serve HTML:

## Index view - `/`

Our index view, matching `/` will show analytics for our system:

* Total number of users we have.
* Total number of keys stored in our database.
* A histogram of all keys.

Also, put a table listing all users. Each user should be a clickable link, pointing to a detail view.

For that, try using [`{% url ... %}`](https://docs.djangoproject.com/en/1.10/ref/templates/builtins/#url)

## User detail view - `/user-detail/<user-identifier>/`

In this user detail view, we want to display a table with all key-value pairs for the given user.

If we pass `identifier` for non-existing user, raise 404.

This view should contain a link for the add key view for that user.

## Add key view - `/add-key/<user-identifier/`

This view should display a simple form for inputing key and value. When submitting this form, we should add the new key-value pair for that given user.

**If everything is successful, redirect back to the detail view for that `identifier`.**

If we pass `identifier` for non-existing user, raise 404.
