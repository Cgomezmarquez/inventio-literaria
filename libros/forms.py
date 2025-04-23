from django.forms import ModelForm
from .models import Recomendacion

class RecomendacionForm(ModelForm):
    class Meta:
        model = Recomendacion
        fields = "__all__"
        


