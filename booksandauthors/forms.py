from django.forms import ModelForm
from django.forms import modelformset_factory

from .models import Author


# A regular form, not a formset
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
