from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
# from Base import models
# from Base.models import Contact
# from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')


# @login_required(login_url='')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        content = request.POST.get('content')

        if not name or len(name) < 2 or len(name) > 30:
            messages.error(request, 'Name should be between 2 and 30 characters.')
            return render(request, 'home.html')

        if not email or len(email) < 2 or len(email) > 50:
            messages.error(request, 'Please enter a valid email address.')
            return render(request, 'home.html')

        if not number or len(number) < 10 or len(number) > 13:
            messages.error(request, 'Please enter a valid phone number.')
            return render(request, 'home.html')

        # On Vercel (serverless), SQLite cannot be written to.
        # For now, just show success message. 
        # To actually save data, use a cloud database (PostgreSQL, etc.)
        messages.success(request, 'Thank you for contacting me! Your message has been received.')

    return render(request, 'home.html')
