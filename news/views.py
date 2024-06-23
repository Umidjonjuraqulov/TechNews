from django.shortcuts import render

# Create your views here.
from .models import NewsArticle, PopularArticle, SelectedReview, BlockChainArticle



def home(request):
    news_articles = NewsArticle.objects.all()
    popular_articles = PopularArticle.objects.all()
    selected_reviews = SelectedReview.objects.all()
    context = {
        'news_articles': news_articles,
        'popular_articles': popular_articles,
        'selected_reviews': selected_reviews
    }
    return render(request, 'news/home.html', context)

def news(request):
    news_articles = NewsArticle.objects.all()
    context = {
        'news_articles': news_articles
    }
    return render(request, 'news/news.html', context)


def blockchain(request):
    blockchain_articles = BlockChainArticle.objects.all()
    context = {
        'blockchain_articles': blockchain_articles
    }
    return render(request, 'news/blockchain.html', context)