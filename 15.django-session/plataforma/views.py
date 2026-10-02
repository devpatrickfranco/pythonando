from django.http import HttpResponse
from django.shortcuts import redirect, render

def home(request):
    if request.session['logado']:
        return render(request, 'home.html')
    else:
        return redirect('/usuarios/login?status=2')