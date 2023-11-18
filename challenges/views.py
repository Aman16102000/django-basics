from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

# dict to store key value pair
challenges = {
    "january": "Focus on yourself",
    "february": "Learn a new skill",
    "march": "Practice gratitude daily",
    "april": "Exercise regularly",
    "may": "Read a book outside your comfort zone",
    "june": "Connect with nature",
    "july": "Meditate for at least 10 minutes every day",
    "august": "Write a journal entry each day",
    "september": "Try a new hobby",
    "october": "Set and achieve a small goal",
    "november": "Express gratitude to someone each day",
    "december": "Reflect on the past year and set goals for the new year",
}


def monthly_challenge_text(request, month):
    try:
        challenge_text = challenges[month]
        return render(request,"challenges/challenge.html",{
            "challenge_text": challenge_text,
            "month":month
        })
    except KeyError:
        print(KeyError)
        
        return HttpResponseNotFound("Enter valid month name")
    


def monthly_challenge_number(request, month):
    months_list = list(challenges.keys())
    if month > 12:
        return HttpResponseNotFound("<h1>Not a valid month number</h1>")
    forwarding_month = months_list[month - 1]

    redirect_path = reverse("month-challenge-url", args=[forwarding_month])
    print(redirect_path)

    return HttpResponseRedirect(redirect_path)


def all_months_list(request):
    all_months_list = list(challenges.keys())
    response_of_all_months = ""
    for x in all_months_list:
        redirect_path = reverse("month-challenge-url", args=[x])
        response_of_all_months += f"<li><a href={redirect_path}>{x}</a></li>"
    response_of_all_months = f"<ol>{response_of_all_months}</ol>"
    return HttpResponse(response_of_all_months)
