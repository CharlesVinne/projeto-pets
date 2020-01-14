from django.shortcuts import render

# Create your views here.
from dono.forms import DonoForm


def cadastro(request):
    form = DonoForm(request.POST or None)
    args = {
        'form':form
    }
    if form.is_valid():
        form.save()
        args['msg'] = 'Cadastro Realizado com sucesso'
        


    return render(request, 'cadastro.html', args)

def lista_gatinhos(request):
    lista_gatinhos = Dono.objects.filter().all()
    args = {'lista_gatinhos':lista_gatinhos}
    return render(request, 'listagatinhos.html', args)

