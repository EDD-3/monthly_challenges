from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!",
}


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"challenge_text": challenge_text, "month": month},
        )
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")


def monthly_challenge_by_number(request, month):

    if month > len(monthly_challenges):
        return HttpResponseNotFound("Invalid month!")
    months = list(monthly_challenges.keys())
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def index(request):

    list_of_months = ""
    for month in monthly_challenges.keys():
        month_path = reverse("month-challenge", args=[month])
        list_of_months += f"<li><a href='{month_path}'>{month.title()}</a></li>"

    response_data = f"<ul>{list_of_months}<ul/>"
    return HttpResponse(response_data)
