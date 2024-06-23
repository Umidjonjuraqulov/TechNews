from django.contrib import admin

# Register your models here.
from .models import NewsArticle, PopularArticle, SelectedReview, BlockChainArticle



admin.site.register(NewsArticle)
admin.site.register(PopularArticle)
admin.site.register(SelectedReview)
admin.site.register(BlockChainArticle)