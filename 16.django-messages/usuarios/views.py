from django.contrib.messages import constants
from django.shortcuts import redirect, render
from django.http import HttpResponse    
from django.contrib import messages
from .models import Usuario
from hashlib import sha256

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def cadastro(request):
    status = request.GET.get('status')
    return  render(request, 'cadastro.html', {'status': status})

def valida_cadastro(request):
    try:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        print(f'{nome} - {email} - {senha}')

        if len(nome.strip()) == 0 or len(email.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Email ou senha não podem ficar vazios !')
            return redirect('/usuarios/cadastro')

        if len(senha) < 8:
            messages.add_message(request, constants.ERROR, 'Sua senha deve ter no minimo 8 caracters !')
            return redirect('/usuarios/cadastro')

        usuario = Usuario.objects.filter(email = email)
        if len(usuario) > 0:
            messages.add_message(request, constants.ERROR, 'Email já está em uso !')
            return redirect('/usuarios/cadastro')

        senha = sha256(senha.encode()).hexdigest()    
        usuario = Usuario(
            nome=nome,
            senha=senha,
            email=email
        )

        usuario.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso !')
        return redirect('/usuarios/cadastros')
    except: 
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema !')
        return redirect('/usuarios/cadastro?status=4')

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email = email, senha = senha)

    if len(usuario) == 0:
        messages.add_message(request, constants.ERROR, 'Email ou senha invalidos !')
        return redirect('/usuarios/login/')
    elif len(usuario) > 0:
        request.session['logado'] = True
        return redirect('/plataforma/home')
    

def sair(request):
    try:
        messages.add_message(request, constants.WARNING, 'Faça login antes de acessar a plataforma')
        del request.session['logado']
    #request.session.flush()
        return redirect('/usuarios/login')
    except KeyError:
        messages.add_message(request, constants.WARNING, 'Você já está descontectado')
        return redirect('/usuarios/login')
    