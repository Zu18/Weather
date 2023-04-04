from django import forms


class CoordinateForm(forms.Form):
    latitude = forms.DecimalField(decimal_places=2)
    longitude = forms.DecimalField(decimal_places=2)