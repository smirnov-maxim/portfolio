from django.shortcuts import render
from django.http import HttpResponse, request


def main_page(request):
    return render(request, 'portfolio/main_page.html')

