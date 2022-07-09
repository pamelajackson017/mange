from django.shortcuts import redirect
from django.core.exceptions import MiddlewareNotUsed
from django.conf import settings


def hello():
    return redirect("http://www.example.com", code=302)
