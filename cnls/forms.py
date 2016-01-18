from django import forms

from .models import Action

class ActionForm(forms.ModelForm):

    class Meta:
        model = Action
        fields = ('titre', 'organisme','date_debut','contact')
