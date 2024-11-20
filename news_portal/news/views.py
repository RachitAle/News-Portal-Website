
from django.shortcuts import render
from .models import Article

def home(request):
    articles = Article.objects.all()  
    return render(request, 'news/home.html', {'articles': articles})

def article_detail(request, id):
    article = Article.objects.get(pk=id)  
    return render(request, 'news/article.html', {'article': article})
