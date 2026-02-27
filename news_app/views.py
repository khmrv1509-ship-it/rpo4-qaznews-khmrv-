from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Adv
from django.db.models import Q
import random



def home_page(request):
    hot_posts = Post.objects.all().order_by('-created_at')[:4]
    last_posts = Post.objects.all().order_by('-created_at')[4:10]

    ads_list = list(Adv.objects.all())
    advs = random.sample(ads_list, min(len(ads_list), 4))

    context = {
        'hot_posts': hot_posts,
        'last_posts': last_posts,
        'advs': advs
    }
    return render(request, "index.html", context)

def news_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category).order_by('-created_at')

    ads_list = list(Adv.objects.all())
    advs = random.sample(ads_list, min(len(ads_list), 4))

    context = {
        'category': category,
        'posts': posts,
        'advs': advs
    }
    return render(request, "news-by-category.html", context)

def search_page(request):
    ads_list = list(Adv.objects.all())
    advs = random.sample(ads_list, min(len(ads_list), 4))

    context = {
        'advs': advs
    }
    return render(request, "search.html", context)

def search_results(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    ads_list = list(Adv.objects.all())
    advs = random.sample(ads_list, min(len(ads_list), 4))

    context = {
        'query': query,
        'results': results,
        'advs': advs
    }
    return render(request, "search-results.html", context)

def read_news_page(request, pk):
    post = get_object_or_404(Post, pk=pk)

    ads_list = list(Adv.objects.all())
    advs = random.sample(ads_list, min(len(ads_list), 4))

    context = {
        'post': post,
        'advs': advs,
    }
    return render(request, "read-news.html", context)

def all_news(request):
    posts = Post.objects.all()

    ads_list = list(Adv.objects.all())
    advs = random.sample(ads_list, min(len(ads_list), 4))

    context = {
        'posts': posts,
        'advs': advs
    }
    return render(request, "all-news.html", context)
