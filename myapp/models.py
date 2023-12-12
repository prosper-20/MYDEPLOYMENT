from django.db import models



class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="service_images")

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_images")
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Appointment(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    dob = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return  self.name
