from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Padarias

# Create your views here.
def index(request):
    padarias = Padarias.objects.all() # o select objects.filter e o obejcts.all retornar uma lista query set 
    print(padarias)
    for padaria in padarias:
        print(padaria.nome, padaria.endereco, padaria.telefone)
    template_nome = 'index.html'
    context = {
        'nome': 'UGB',
        'padarias': padarias
    } 
    return render(request, template_nome, context)