from django.shortcuts import render

def awards_recog(request):
    return render(request, 'executive/pages/awards_recog.html')