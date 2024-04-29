from typing import Any
from django.http import HttpResponsePermanentRedirect

class Htaccess:
    def __init__(self,res):
        self.res = res 

    def __call__(self,req):
        host = req.get_host()
        if host == 'www.bookovie.ir':
            return HttpResponsePermanentRedirect('https://bookovie.ir'+req.path)
        return self.res(req)