from django.shortcuts import redirect
from django.core.exceptions import MiddlewareNotUsed
from django.conf import settings


class CanonicalDomainMiddleware(object):

   @app.route('/')
def redirect_to_link():
    # return redirect method, NOTE: replace google.com with the link u want
    return redirect('https://google.com')
