from django import forms

from procedures.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    date = forms.ChoiceField(choices=(), widget=forms.DateInput(attrs={
        'type': 'date', 'class': 'form-control py-4'}))
    time = forms.ChoiceField(choices=(), widget=forms.Select(attrs={
        'type': 'time','class': 'form-control py-4'}))

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'date','time')