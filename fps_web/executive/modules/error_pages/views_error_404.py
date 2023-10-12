from django.shortcuts import render

def error_page_404(request):
    return render(request, 'error_pages/page_404.html')