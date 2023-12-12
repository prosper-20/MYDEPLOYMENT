from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, Post, Appointment
from django.contrib import messages

def home(request):
    if request.method == "POST":
        name = request.POST.get("patient-name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        dob = request.POST.get("dob")
        appointment_date = request.POST.get("appoinment-date")
        message = request.POST.get("message")

        Appointment.objects.create(name=name, phone=phone,
                                   email=email, dob=dob, date=appointment_date,
                                   message=message)
        messages.success(request, "Appointment Successfully booked!")
        return redirect("/")

    all_services = Service.objects.all()
    all_posts = Post.objects.all()
    context = {
        "all_services": all_services,
        "all_posts": all_posts
    }
    return render(request, "myapp/index.html", context)


def about(request):
    if request.method == "POST":
        name = request.POST.get("patient-name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        dob = request.POST.get("dob")
        appointment_date = request.POST.get("appoinment-date")
        message = request.POST.get("message")

        Appointment.objects.create(name=name, phone=phone,
                                   email=email, dob=dob, date=appointment_date,
                                   message=message)
        messages.success(request, "Appointment Successfully booked!")
        return redirect("/")
    return render(request, "myapp/about.html")


def services(request):
    all_services = Service.objects.all()
    context = {
        "all_services": all_services,

    }
    return render(request, "myapp/services.html", context)



def blog_home(request):
    return render(request, "myapp/blog-home.html")

def blog_single(request, id):
    single_post = get_object_or_404(Post, id=id)
    context = {"single_post": single_post}
    return render(request, "myapp/blog-single.html", context)
