from django import forms
from myapp.models import EventTypes


class SendEventForm(forms.Form):
    event_type = forms.ChoiceField(choices=EventTypes)
    data = forms.CharField(max_length=1000, required=False)
