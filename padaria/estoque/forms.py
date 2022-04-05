from calendar import c
from pyexpat import model
from django import forms
from .models import Produtos

class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = [
            "produto",
            "quantidade",
            "preco",
        ]
        
        #fields = '_all_'
        #exclude = ['produto']