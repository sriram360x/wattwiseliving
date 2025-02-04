from django.urls import path
from .import views
from .views import home

urlpatterns = [
    path("", home, name="home"),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('calculator/', views.calculator, name='calculator'),
    path('energyusage/', views.energyusage, name='energyusage'),
    path('costsavings/', views.costsavings, name='costsavings'),
    path('sustainability/', views.sustainability, name='sustainability'),
]