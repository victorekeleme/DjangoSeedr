from django import forms
from .models import Link


class MagnetLink(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('m_link',)
