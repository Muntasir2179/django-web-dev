from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day.",
    "march": "Learn Django for at least 20 min.",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day.",
    "june": "Learn Django for at least 20 min.",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day.",
    "september": "Learn Django for at least 20 min.",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day.",
    "december": "Learn Django for at least 20 min.",
}

def monthly_challenge(request, month):
    try:
        return HttpResponse(monthly_challenges[month])
    except:
        return HttpResponseNotFound("This month is not supported.")


def monthly_challenge_by_number(request, month):
    if month <= 12:
        redirect_month = list(monthly_challenges.keys())[month-1]
        return HttpResponseRedirect("/challenges/" + redirect_month)
    return HttpResponseNotFound("This month is not supported.")