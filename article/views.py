from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

def allArticle(request, pk):
	article = Article.objects.get(pk=int(pk))
	
	add = int(article.num1)+int(article.num2)
	minus = int(article.num1)-int(article.num2)
	mult = int(article.num1)*int(article.num2)

	return render(request,'show_article.html',{
				'title':str(article.title),
				'article':str(article.content),
				'add':add,
				'minus':minus,
				'mult':mult,
			})


# Create your views here.
