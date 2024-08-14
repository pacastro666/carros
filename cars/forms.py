from django import forms
from cars.models import Car



class CarModelForm(forms.ModelForm):
    class Meta:
        model =Car
        fields = '__all__'
    
    def clean_value(self):
        value =self.cleaned_data.get('value')
        if value <20000:
            self.add_error('value','valor minimo do carro deve ser R$20.000,00')
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year <1975:
            self.add_error('factory_year','o ano não pode ser menor que 1975')
        return factory_year



