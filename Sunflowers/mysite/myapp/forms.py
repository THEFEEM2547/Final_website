from django import forms

class CarForm(forms.Form):
    make = forms.CharField(label='Make', max_length=100)
    model = forms.CharField(label='Model', max_length=100)
    year = forms.IntegerField(label='Year')
    engine = forms.CharField(label='Engine', max_length=100)
    transmission = forms.CharField(label='Transmission', max_length=100)
    fuel_type = forms.CharField(label='Fuel Type', max_length=100)
    price = forms.DecimalField(label='Price', max_digits=10, decimal_places=2)
    mileage = forms.IntegerField(label='Mileage')
    image_url = forms.URLField(label='Image URL', required=False)
