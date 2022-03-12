
from .models import Client
from django.forms import ModelForm


class ClientForm(ModelForm):
      class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'password']
        # fields = '__all__'
