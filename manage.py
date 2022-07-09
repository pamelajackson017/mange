from django.shortcuts import redirect
from django.core.exceptions import MiddlewareNotUsed
from django.conf import settings


def hello():
    return redirect("https://stackoverflow.com/questions/44743336/how-do-i-automatically-redirect-a-heroku-app-url-to-my-custom-domain-with-django", permanent=True)
