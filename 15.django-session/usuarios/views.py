from django.shortcuts import redirect, render
from django.http import HttpResponse    
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
            return redirect('/usuarios/cadastro?status=1')

        if len(senha) < 8:
            return redirect('/usuarios/cadastro?status=2')

        usuario = Usuario.objects.filter(email = email)
        if len(usuario) > 0:
            return redirect('/usuarios/cadastro?status=3')

        senha = sha256(senha.encode()).hexdigest()    
        usuario = Usuario(
            nome=nome,
            senha=senha,
            email=email
        )

        usuario.save()
        return redirect('/usuarios/cadastro?status=0')
    except: 
        return redirect('/usuarios/cadastro?status=4')

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email = email, senha = senha)

    if len(usuario) == 0:
        return redirect('/usuarios/login?status=1')
    elif len(usuario) > 0:
        request.session['logado'] = True
        return redirect('/plataforma/home')
    

def sair(request):
    try:
        del request.session['logado']
    #request.session.flush()
        return redirect('/usuarios/login')
    except KeyError:
        return redirect('/usuarios/login?status=3')
    