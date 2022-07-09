#!/usr/bin/env python
import os
import sys

@app.route('/')
def hello():
 #   os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")
return redirect("https://www.qovery.com/", permanent=True)
 


