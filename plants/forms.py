from django.forms import ModelForm
from .models import PlantData


class PlantEntryForm(ModelForm):
    class Meta:
        model = PlantData
        fields = ['date_watered', 'note', 'photo']
