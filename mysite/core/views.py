from cgitb import html
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    nome = 'Elvis Ribeiro de Oliveira'
    html = f'''
    <html>
    <head>
    </head>
    <body>
        <h1>{nome}</h1>
    </body>
    </html>
    '''
    return HttpResponse(html)
