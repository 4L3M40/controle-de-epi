from django import forms
from .models import Colaborador

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ["nome", "cpf", "matricula", "ativo"]
        widgets = {
            "nome": forms.TextInput(attrs={"class":"form-control"}),
            "cpf": forms.TextInput(attrs={"class":"form-control", "maxlength":"11"}),
            "matricula": forms.TextInput(attrs={"class":"form-control"}),
            "ativo": forms.CheckboxInput(attrs={"class":"form-check-input"}),
        }
