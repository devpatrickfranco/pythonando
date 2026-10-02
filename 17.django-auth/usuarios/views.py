from django.contrib.messages import constants
from django.shortcuts import redirect, render
from django.contrib import messages, auth
#from django.contrib.auth.models import User
from .models import Users as User

def login(request):
    if request.user.is_authenticated:
        return redirect('/plataforma/home')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/plataforma/home')
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})


def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    cep = request.POST.get('cep')
    rua = request.POST.get('rua')
    numero = request.POST.get('numero')

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Email ou senha não podem ficar vazios !')
        return redirect('/usuarios/cadastro/')

    if len(senha) < 8:
        messages.add_message(request, constants.ERROR, 'Sua senha deve ter no minimo 8 caracters !')
        return redirect('/usuarios/cadastro/')

    if User.objects.filter(email=email).exists():
        messages.add_message(request, constants.ERROR, 'Email já está em uso !')
        return redirect('/usuarios/cadastro/')

    if User.objects.filter(username=nome).exists():
        messages.add_message(request, constants.ERROR, 'Nome de usuario já está em uso !')
        return redirect('/usuarios/cadastro/')

    try:
        usuario = User.objects.create_user(username=nome, 
                        email=email, 
                        password=senha,cep=cep, 
                        numero=numero,
                        rua=rua,
                        usuario=usuario)
        usuario.save()
        
        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso !')
        return redirect('/usuarios/cadastro/')
    except Exception as e:
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema !')
        print(e)
        return redirect('/usuarios/cadastro/')


def valida_login(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')

    usuario = auth.authenticate(request, username=nome, password=senha)

    if not usuario:
        messages.add_message(request, constants.ERROR, 'Usuario ou senha invalidos !')
        return redirect('/usuarios/login/')

    auth.login(request, usuario)
    return redirect('/plataforma/home')


def sair(request):
    auth.logout(request)
    messages.add_message(request, constants.WARNING, 'Você saiu da plataforma')
    return redirect('/usuarios/login')
