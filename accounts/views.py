from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def log_in(request):
    if request.method == 'POST':
       form = AuthenticationForm(data=request.POST)
       if form.is_valid():
           #get user admin from database
           user = form.get_user()
           login(request,user)
           if 'next' in request.POST:
               return redirect(request.POST.get('next'))
           else:
               return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
        
        
