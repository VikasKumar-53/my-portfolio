from django.shortcuts import render, redirect
from django.contrib import messages

from .models import ContactMessage

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            # 1. Save to Database
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )

            messages.success(request, "Message sent successfully! I will get back to you soon.")

            return redirect("/#contact")   # reload page cleanly

    return render(request, "index.html")