from django.contrib.auth.views import LoginView
from django.contrib import messages

class CustomLoginView(LoginView):
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, "Invalid webmail and password!")
        # print(self.request.session.get('messages'))
        # print("hello invalid")
        return response

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Successfully logged in!")
        # print(self.request.session.get('messages'))
        # print("hello valid")
        return response