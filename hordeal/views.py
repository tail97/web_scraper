from django.shortcuts import render
from .models import Deal

def index(requests):
    deals = Deal.objects.all().order_by("-cdate")
    return render(requests, "hordeal/index.html", {"deals": deals})