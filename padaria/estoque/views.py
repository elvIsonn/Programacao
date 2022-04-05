from django.shortcuts import render

from .forms import ProdutosForm

# Create your views here.
def produto(request):
    print(request.method)
    form = ProdutosForm()
    template_name = "produtos.html"
    contex = {
        "produto": form
    }
    return render(request, template_name, contex)