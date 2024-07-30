from django.shortcuts import render


def index(request):
    return render(request, "app/index.html")


def article(request, num):
    return render(request, f"app/article_{num}.html")


