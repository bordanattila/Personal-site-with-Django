from django.shortcuts import render

# Create your views here.


def starting_page(request):
    return render(request, 'blog/index.html')


def posts(request):
    return render(request, "blog/posts_page.html")


def post_detail(request):
    pass