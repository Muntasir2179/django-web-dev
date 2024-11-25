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
    "december": "Learn Django for at least 20 min.",
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly_challenges", args=[month])
        list_items += f"""<li><a href="{month_path}">{capitalized_month}</a></li>"""

    # content = """
    # <ul>
    #     <li><a href="/challenges/january">January</a></li>
    #     <li><a href="/challenges/february">February</a></li>
    #     <li><a href="/challenges/march">March</a></li>
    #     <li><a href="/challenges/april">April</a></li>
    #     <li><a href="/challenges/may">May</a></li>
    #     <li><a href="/challenges/june">June</a></li>
    #     <li><a href="/challenges/july">July</a></li>
    #     <li><a href="/challenges/august">August</a></li>
    #     <li><a href="/challenges/september">September</a></li>
    #     <li><a href="/challenges/october">October</a></li>
    #     <li><a href="/challenges/november">November</a></li>
    #     <li><a href="/challenges/december">December</a></li>
    # </ul>
    # """
    return HttpResponse(list_items)


def monthly_challenge(request, month):
    try:
        return render(request=request, template_name="challenges/challenge.html")
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported.</h1>")


def monthly_challenge_by_number(request, month):
    if month <= 12:
        redirect_month = list(monthly_challenges.keys())[month-1]
        redirect_path = reverse(viewname="monthly_challenges", args=[redirect_month])    # constructing the path /challenges/<month>
        return HttpResponseRedirect(redirect_path)
    return HttpResponseNotFound("<h1>This month is not supported.</h1>")
