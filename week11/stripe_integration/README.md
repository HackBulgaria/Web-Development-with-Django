## Integrating Stripe Payment with Django

Educational django project with Stripe integration
---

### Initial setup
* Create repo
* Add db, Python & Emacs files

### Checkout `users` app
* `BaseUser` with email & password
* Custom managers
* Changed `AUTH_USER_MODEL`

### Create magazine
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

### Setup Celery
* Create `celery.py`
* Import app in `__init__.py`
* Create dummy task
* Run celery in separate terminal
