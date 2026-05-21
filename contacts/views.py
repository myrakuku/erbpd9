from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

def contact(request):
    if request.method == "POST":
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        doctor_email = request.POST['doctor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
        if has_contacted:
            messages.error(request, "You have already made an inquiry for this clinic")
            return redirect("listings:listing", listing_id=listing_id)
            
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        send_mail(
            "Clinic Inquiry",
            "There has been an inquiry for " + listing + ". Sign into the admin panel for more info.",
            "admin@clinic.com",
            [doctor_email],
            fail_silently=False
        )
        messages.success(request, "Your request has been submitted!")
    return redirect("listings:listing", listing_id=listing_id)