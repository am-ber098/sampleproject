
from django.urls import path

from . import views
from nutrimind.views import saved_profile_view
urlpatterns = [
    path ("", views.layout, name="layout"),
    path("index", views.index, name="index"),
    path("profile", views.profile_view, name="profile"),
    path('save-profile/', views.saved_profile_view, name='save_profile'),
    path("recommendation", views.recommendation_view, name="recommendation"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("loguser", views.loguser_view, name="loguser")
    
]

