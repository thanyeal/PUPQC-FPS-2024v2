from django.shortcuts import render

def error_page_500(request):
    return render(request, 'error_pages/page_500.html')