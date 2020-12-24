from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.forum),
    path('register', views.RegisterFormView.as_view()),
    path('login', views.LoginFormView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('add_post', views.add_post),
    path('add', views.add),
]