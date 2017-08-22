from django.shortcuts import render
from django.http import HttpResponse

def main_view(request):
    return HttpResponse("You are at the questionnaire main_view")

def contact_view(request):
    return HttpResponse("You are at the contact_view")

def appinfo_view(request):
    return HttpResponse("You are at the appinfo_view")
    
