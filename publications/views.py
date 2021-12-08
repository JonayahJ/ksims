# Publications Views
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from publications.models import Article

# Publication list view (main page)
class PublicationView(ListView):
    model = Article
    template_name = 'publications.html'
    ordering = ['-post_date',] # order by reverse post_date

# Post view (individual articles)
class ArticleView(DetailView):
    model = Article
    template_name = 'article.html'
