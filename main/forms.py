from django import forms
from .models import Fitback

class Fitback(forms.Fitback):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fitback_date'].label = 'Дата отзыва'

    fitback_date = forms.DateField(widget=forms)