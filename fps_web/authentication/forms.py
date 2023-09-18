# validation.py
from django.http import JsonResponse
from executive.models import User
from validate_email import validate_email
import json
from django.views import View


class EmailValidation(View):
    # def __init__(self):
        # self.email = None  # Initialize password attribute

    def post(self, request):
        data = json.loads(request.body)
        email = data.get('email')

        # Check if the email is valid using validate_email module
        if not validate_email(email):
            return JsonResponse({'email_error': 'This is not a valid PUPQC webmail'}, status=400)

        # Check if the email domain matches '@gmail.com'
        if email.endswith('@gmail.com'):
            return JsonResponse({'gmail_error': 'Sorry, Google account is restricted'}, status=400)

        # Check if the email domain matches '@yahoo.com'
        if email.endswith('@yahoo.com'):
            return JsonResponse({'yahoo_error': 'Sorry, Yahoo account is restricted'}, status=400)

        # Check if the email domain doesnt matches '@pup.edu.ph'
        if not email.endswith('@pup.edu.ph'):
            return JsonResponse({'webmail_error': 'Email domain must be valid webmail'}, status=400)
        
        # Check if the email is already registered
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Webmail is already taken'}, status=409)

        # Check if the email is already registered
        if validate_email(email):
            return JsonResponse({'email_valid': 'Im good with  ' + email + ' :)'}, status=200)
        
        # self.email = email
        return email

class PasswValidation(View):
    # def __init__(self):
        # self.password = None  # Initialize password attribute

    def post(self, request):
        data = json.loads(request.body)
        password = data.get('password')

        if not password:
            return JsonResponse({'password_error': 'Password is required'}, status=400)

        # Check if the password has at least one uppercase letter
        if not any(char.isupper() for char in password):
            return JsonResponse({'password_error': 'Password must contain at least one uppercase letter'}, status=400)

        # Check if the password has at least one lowercase letter
        if not any(char.islower() for char in password):
            return JsonResponse({'password_error': 'Password must contain at least one lowercase letter'}, status=400)

        # Check if the password has at least one digit (0-9)
        if not any(char.isdigit() for char in password):
            return JsonResponse({'password_error': 'Password must contain at least one digit (0-9)'}, status=400)

        # Check if password is atleast 8 characters
        if len(password) < 8:
            return JsonResponse({'password_error': 'Password must be at least 8 characters long'}, status=400)

        # If the password passes all validation checks, you can return a success response
        if password:
            return JsonResponse({'passw_valid': 'Password acknowledged! ' + password}, status=200)
        
        # self.password = password
        return password

class LogEmail(View):
    def post(self, request):
        data = json.loads(request.body)
        webmail = data.get('webmail')

        if not validate_email(webmail):
            return JsonResponse({'webmail_error': 'This webmail is invalid'}, status=400)  

        if webmail.endswith('@gmail.com'):
            return JsonResponse({'loggmail_error': 'Sorry, Google account is restricted'}, status=409)

        if webmail.endswith('@yahoo.com'):
            return JsonResponse({'logyahoo_error': 'Sorry, Yahoo account is restricted'}, status=409)

        if not webmail.endswith('@pup.edu.ph'):
            return JsonResponse({'pupwebmail_error': 'Email domain must be valid webmail'}, status=400)  

        if not User.objects.filter(email=webmail).exists():
            return JsonResponse({'webmail_invalid': '&nbsp;&nbsp;&nbsp;' + "✖  &nbsp; Seems like you're not yet registered"}, status=409)
        
        if  User.objects.filter(email=webmail).exists():
            return JsonResponse({'webmail_valid': '&nbsp;&nbsp;&nbsp;' + '✔ &nbsp; Valid webmail'}, status=200)  


        return webmail

class LogPassw(View):
    
    def post(self, request):
        data = json.loads(request.body)
        webpass = data.get('webpass')

        if not webpass:
            return JsonResponse({'webpass_error': 'Password is required'}, status=400)

        # Check if the webpass has at least one uppercase letter
        if not any(char.isupper() for char in webpass):
            return JsonResponse({'webpass_upper': 'Password must contain at least one uppercase letter'}, status=400)

        # Check if the webpass has at least one lowercase letter
        if not any(char.islower() for char in webpass):
            return JsonResponse({'webpass_lower': 'Password must contain at least one lowercase letter'}, status=400)

        # Check if the webpass has at least one digit (0-9)
        if not any(char.isdigit() for char in webpass):
            return JsonResponse({'webpass_number': 'Password must contain at least one digit (0-9)'}, status=400)

        # Check if webpass is atleast 8 characters
        if len(webpass) < 8:
            return JsonResponse({'webpass_len': 'Password must be at least 8 characters long'}, status=400)

        # If the webpass passes all validation checks, you can return a success response
        if webpass:
            return JsonResponse({'webpass_valid': 'Password acknowledged! ' + webpass}, status=200)

        return webpass
