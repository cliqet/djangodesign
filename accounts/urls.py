from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import home, login, register, profile

urlpatterns = [
    path('', home, name='accounts_home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/', profile, name='profile')
]
