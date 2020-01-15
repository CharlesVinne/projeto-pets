from django.shortcuts import render

# Create your views here.
from cachorros.forms import CachorroForm

def cadastro(request):
    form = CachorroForm (request.POST or None)
    args = {
        'form':form
    }
    if form.is_valid():
        form.save()
        args['msg'] = 'Cadastro realizado com sucesso'
        


    return render(request, 'cadastro_cachorro.html', args)