from django import forms

from web.models import house


class filter_form(forms.ModelForm):
    class Meta:
        model = house
        fields = '__all__'