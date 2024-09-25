from django import forms
from .models import NewsModel,AppointmentModel,ContactModel



class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = '__all__'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = AppointmentModel
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
