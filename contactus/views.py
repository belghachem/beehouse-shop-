from django.shortcuts import render
from django.core.mail import send_mail

def contact(request):        
    return render(request, 'contactus/contactus.html')