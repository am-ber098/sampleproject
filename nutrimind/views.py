from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect 
from django.urls import reverse
from .models import User, Recommendation, UserProfile, PsychologicalCondition
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .forms import UserProfileForm
import json
 

def layout(request):
    return render (request, "nutrimind/layout.html")


def saved_profile_view(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        psychological_condition = user_profile.psychological_condition
        recommendations = Recommendation.objects.filter(psychological_condition=psychological_condition)

        return render(request, 'nutrimind/saveprofile.html', {
            'user_profile': user_profile,
            'recommendations': recommendations,
        })
    else:
        return redirect('login')


def profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'age': 0,
            'weight': 0.0,
        }
    )

   
    psychological_condition = user_profile.psychological_condition
    recommendations = Recommendation.objects.filter(psychological_condition=psychological_condition)

    return render(request, "nutrimind/profile.html", {
        'profile_form': UserProfileForm(instance=user_profile),
        'user_profile': user_profile,
        'psychological_condition': psychological_condition,
        'recommendations': recommendations,
    })

def index(request):
    user_profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'age': 0,
            'weight': 0.0,
        }
    )

    profile_form = UserProfileForm(instance=user_profile)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=user_profile)
        
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            psychological_condition = request.POST.get('psychological_condition')
            profile.psychological_condition_id = int(psychological_condition) 
            profile.save() 

            # Render the profile view instead of redirecting
            return profile_view(request)  

    return render(request, "nutrimind/index.html", {'profile_form': profile_form})

def recommendation_view(request):
    if request.method == 'GET':
        psychological_condition_id = request.GET.get('psychological_condition_id')
        try:
            psychological_condition = PsychologicalCondition.objects.get(id=psychological_condition_id)
            recommendations = Recommendation.objects.filter(psychological_condition=psychological_condition)
            return render(request, 'nutrimind/recommendation.html', {
                'recommendations': recommendations,
                'psychological_condition': psychological_condition,
            })
        except PsychologicalCondition.DoesNotExist:
            return render(request, 'nutrimind/index.html', {
                'error_message': 'Selected psychological condition not found.'
            })

def login_view(request):
    if request.method == "POST":

        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

       
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "nutrimind/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "nutrimind/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("layout"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]


        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "nutrimind/register.html", {
                "message": "Passwords must match."
            })

        
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "nutrimind/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("layout"))
    else:
        return render(request, "nutrimind/register.html")
