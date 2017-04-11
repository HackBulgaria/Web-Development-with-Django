
We will use a `HackLX` project from last week and update it like so:

* In model `Offer` add field `status` with the following choices `pending`, `approved` and `rejected`.

* Add view `PendingOffers` which contains offers with status `pending`.

* Add view `ApprovedAndRejectedOffers` which contains offers with status `approved` and `rejected`.

** Write custom querysets for the last views! **

Thinking about `mixins`:

* Only approved offers will display on index page.

* Only logged user can create offer.

* Only user who created offer can edit/delete it.

* Only superuser can approve/reject offers in `PendingOffers` view.

* Every user has a `ApprovedAndRejectedOffers` view with his own offers.
