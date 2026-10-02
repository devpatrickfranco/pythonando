from email import message
import html
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.contrib import messages
from django.contrib.messages import constants

from .models import Clientes

def cadastro(request):
    return HttpResponse('Hello, world!')

def clientes(request):

    if request.method == 'GET':
        
        nome = request.GET.get('nome')
        clientes = Clientes.objects.all()    

        if nome:
            clientes = clientes.filter(nome__icontains=nome)

        return render(request, 'clientes.html', {'clientes': clientes})
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        queixa = request.POST.get('queixa')

        if len(nome) < 3:
            
            messages.add_message(request, constants.ERROR, 'Nome menor que 3 caracteres')
            return redirect('clientes')

        if queixa not in {'D', 'A'}:
            messages.add_message(request, constants.ERROR, 'Selecione uma opção: Depressão ou Ansiedade')
            return redirect('clientes')
        
        usuario = Clientes.objects.filter(email=email)
        
        if usuario.exists():
            messages.add_message(request, constants.ERROR, 'Esse email já está em uso')
            return redirect('clientes')


        try:
            cliente = Clientes(
                nome=nome,
                email=email,
                queixa=queixa
            )

            cliente.save()

            messages.add_message(request, constants.SUCCESS, 'Cliente cadastrado!')
            return redirect('clientes')

        except Exception as e:
            print('ERRO:', e)
            return HttpResponse(f'Erro ao salvar: {e}')

def ver_cliente(request, id):
    cliente = Clientes.objects.get(id=id)
    
    if request.method == 'GET':
        return render(request, 'ver_cliente.html', {'cliente': cliente})
    
    elif request.method == 'POST':
        foto = request.FILES.get('foto')

        cliente.foto = foto
        cliente.save()
                    
        return redirect(f'/usuarios/ver_cliente/{id}')

