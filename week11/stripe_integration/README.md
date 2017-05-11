# Integrating Stripe Payment with Django

## Things to do before we begin
* Explore `users` app. It has:
* `BaseUser` with email & password
* Custom managers
* Changed `AUTH_USER_MODEL`

## Simple plan for today:

### Create magazine app
* Create `Magazine` & `Article` models. Register in admin
* Create magazine & article list views
* Create urls. Register them
* Create templates outside apps. Add settings

### Add LoginRequiredMixin
* Add `/login` url. Add template
* Add `/logout` url
* Add `LoginRequiredMixin`

### Create payments module
* Create Stripe account
* Add `CreateCustomerView`
* Use Stripe's embeded card info modal
* Create `BuyArticleView`
* Create `RefundArticleView`

### Setup Celery
* Create `celery.py`
* Import app in `__init__.py`
* Create dummy task
* Run celery in separate terminal

### Tests
* Unit tests
* *Integration* tests. Mocking

## Bonus
* Subscriptions
