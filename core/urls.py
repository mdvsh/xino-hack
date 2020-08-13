from django.urls import path
from .views import Homepage
from . import views

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('login/', views.login_function, name='login'),
    path('registration/', views.register_function, name='registration'),
    path("activate/<uidb64>/<token>", views.activate_account, name="activate"),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
]
