from django import forms

from .models import Lead


class AddLeadForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'rows': 1, 'cols': 33,'placeholder':'Введите описание'}))

    class Meta:
        model = Lead
        fields = ('name', 'email', 'description', 'priority', 'status',)
