# Contact views
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Inquiry form link
def inquiry(request):
    if request.method == 'POST':
        name = request.POST['name']
        user_email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(
            name=name, 
            email=user_email, 
            subject=subject,
            message=message, 
        )

        #getting superuser email address
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        # Sending an email
        send_mail(
            subject + ' from ' + name, # subject
            message, # message
            user_email, # from field
            ['jonayah@thinkhalcyon.com'], # to field
            fail_silently=False,
        )

        contact.save()
        messages.success(request, "Thank you for reaching out! I'll be in touch shortly.")

        return redirect('thankyou') # Return to contact page

# Thank You page
def thankyou(request):
    return render(request, "thankyou.html", {})