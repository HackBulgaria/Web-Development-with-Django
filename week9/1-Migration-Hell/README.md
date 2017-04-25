# Migration Hell

You are presented with a simple Django project, where all models are defined inside an app claled `everything`.

Your aim is to achieve the following structure:

* App `users` where `User` model is located.
* App `products` where `Product` and `Category` models are located.
* App `cart` where `Order` and `Invoice` models are located.
* App `comments` where `Comment` model is located.

Restrictions are:

* You cannot delete existing migrations
* All data **must** be preserved. Dropping tables with data without moving them elsewhere is not an option.

Hint - <https://docs.djangoproject.com/en/1.11/topics/migrations/#data-migrations>
