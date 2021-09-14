from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class NameForm(forms.Form):
    sold_date = forms.DateField(
        label='When was the prescription sold?', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'autofocus': True}))
    days_early = forms.IntegerField(label='How many days early?', widget=forms.TextInput(
        attrs={'value': 2, 'class': 'form-control'}))
    days_supply = forms.IntegerField(
        label='What is the days supply?', widget=forms.TextInput(attrs={'value': 30, 'class': 'form-control'}))
