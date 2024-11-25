from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string
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
    # "december": "Learn Django for at least 20 min.",
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request=request, template_name="challenges/index.html", context={"months": months})


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request=request,
                      template_name="challenges/challenge.html", 
                      context={
                          "month_name": month,
                          "text": challenge_text
                      })
    except:
        return HttpResponseNotFound("<h1>This month is not supported.</h1>")


def monthly_challenge_by_number(request, month):
    if month <= 12:
        redirect_month = list(monthly_challenges.keys())[month-1]
        redirect_path = reverse(viewname="monthly_challenges", args=[redirect_month])    # constructing the path /challenges/<month>
        return HttpResponseRedirect(redirect_path)
    return HttpResponseNotFound("<h1>This month is not supported.</h1>")
