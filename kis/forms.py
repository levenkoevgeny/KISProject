from django.forms import ModelForm

from .models import Cadet


class CadetForm(ModelForm):
    class Meta:
        model = Cadet
        fields = '__all__'