from django import forms

from .models import Offer


class OfferCreateModelForm(forms.ModelForm):

    class Meta:
        model = Offer
        fields = ('title', 'description', 'category', 'image')
