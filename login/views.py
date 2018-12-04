from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_inicio(request):
    if request.user.is_authenticated:
        return redirect('articulos')
    return render(request, 'pages-signin.html')


def login_papeleria(request):
    if request.user.is_authenticated:
        return redirect('articulos')

    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            # request.session.set_expiry(300)
            login(request, user)
            return redirect('articulos')
        else:
            return render(request, 'pages-signin.html', {'error': 'Usuario no válido'})
    return render(request, 'pages-signin.html')


def logout_papeleria(request):
    logout(request)
    return redirect('login')
