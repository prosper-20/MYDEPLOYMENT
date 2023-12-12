from django.urls import path
from .views import home, about, services, blog_home, blog_single


urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("blog/", blog_home, name="blog-home"),
    path("services/", services, name="services"),
    path("blog/<int:id>/", blog_single, name="blog-single")
]