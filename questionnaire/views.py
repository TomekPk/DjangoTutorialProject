from django.shortcuts import render
from django.http import HttpResponse

def main_view(request):
    return HttpResponse("You are at the questionnaire main_view")

def contact_view(request):
    return HttpResponse("You are at the contact_view")

def appinfo_view(request):
    return HttpResponse("You are at the appinfo_view")
    

def detail_view(request, question_id):
    return HttpResponse("You are at the detail_view and You are looking at question %s." % question_id)

def results_view(request, question_id):
    return HttpResponse("You are at the results_view and You are looking at question %s." % question_id)

def vote_view(request, question_id):
    return HttpResponse("You are at the vote_view and You are looking at question %s." % question_id)
