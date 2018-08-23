from django.shortcuts import render
from news.models import News

def home_page(request):
    news = News.objects.all().order_by('-date_created')
    return render(request, 'home.html',{'news':news})