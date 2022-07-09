from django.shortcuts import redirect
from django.core.exceptions import MiddlewareNotUsed
from django.conf import settings


class CanonicalDomainMiddleware(object):

    """Middleware that redirects to a canonical domain."""

    def __init__(self, get_response):
        self.get_response = get_response
        if settings.DEBUG or not settings.SITE_DOMAIN:
            raise MiddlewareNotUsed

    def __call__(self, request):
     
                canonical_url = "https://stackoverflow.com/questions/14343812/redirecting-to-url-in-flask"
            return redirect(canonical_url, permanent=True)
