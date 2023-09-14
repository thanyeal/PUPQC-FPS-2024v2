from django.shortcuts import render
from django.views import View

# Create your views here.
# Create your views here.
class ComingSoonView(View):
    def get(self, request):
        return render(request, 'coming_soon/coming_soon.html')