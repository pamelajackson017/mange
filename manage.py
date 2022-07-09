from django.shortcuts import redirect
from django.core.exceptions import MiddlewareNotUsed
from django.conf import settings


class CanonicalDomainMiddleware(object):

    """Middleware that redirects to a canonical domain."""

   
            if request.is_secure():
                canonical_url = "https://stackoverflow.com/questions/14343812/redirecting-to-url-in-flask"
            else:
                canonical_url = "https://stackoverflow.com/questions/14343812/redirecting-to-url-in-flask"
            canonical_url += settings.SITE_DOMAIN + request.get_full_path()
            return redirect(canonical_url, permanent=True)
