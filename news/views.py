from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import News
from .import forms

@login_required(login_url='/accounts/login/')
def create_news(request):
    if request.method == 'POST':
        form = forms.CreateNews(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('home')
    else:
        form = forms.CreateNews()
    return render(request, 'news/news_create.html',{'form':form})

def news_detail(request,slug):
    news = News.objects.get(slug=slug)
    return render(request, 'news/details.html', {'news':news})
