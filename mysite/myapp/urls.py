from django.urls import path

from myapp.views import index, indexItem
from django.contrib.auth import views as auth_views, login

from myapp.views import register, user_login, profile_view

app_name = "myapp"

urlpatterns = [
    path("", index, name="index"),
    path("<int:my_id>/", indexItem, name="detail"),

    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('profile/', profile_view, name='profile'),

]