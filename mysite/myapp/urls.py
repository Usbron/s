from django.urls import path

from myapp.views import index, indexItem
from django.contrib.auth import views as auth_views, login

from myapp.views import register

from myapp.views import user_login

app_name = "myapp"

urlpatterns = [
    path("", index, name="index"),
    path("<int:my_id>/", indexItem, name="detail"),

    path('register/', register, name='register'),
    path('login/', user_login, name='login'),

]