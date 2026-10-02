from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/usuarios/login')
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('/usuarios/login?status=2')
