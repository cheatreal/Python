import httplib
from PIL import Image
from pytesser import *

FILENAME = "Captcha.png"
URL = "#"
RESOURCE = "/START/prob/prob_files/prob25_img.php"
RESOURCE2 = "/START/prob/prob_files/prob25_ok.php?lcm="
PARAMS = None
HEADERS = {"Content-Type":"application/x-www-form-urlencoded", "Accept":"*/*", "Cookie": "PHPSESSID=qr8foajbbp7st6kpv2antnc9f0"}

def httpRequest(URL, RESOURCE, PARAMS, HEADERS):
        conn = httplib.HTTPConnection(URL)
        conn.request('GET', RESOURCE, PARAMS, HEADERS)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data

# Save Captcha Image
def saveImage(FILENAME, URL, RESOURCE, PARAMS, HEADERS):
        fp = open(FILENAME, "wb")
        data = httpRequest(URL, RESOURCE, PARAMS, HEADERS)
        fp.write(data)
        fp.close()

        
# Load Captcha Image
def captchaToString(FILENAME):
        im = Image.open(FILENAME)
        data = image_to_string(im)
        return data

# Wargame
def solve(data):
        try:
                # Here
        except Exception:
                pass
        
while(True):
        saveImage(FILENAME, URL, RESOURCE, PARAMS, HEADERS)
        data = captchaToString(FILENAME)
        #print "[+] Captcha\n"
        #print data
        solve(data)
        
        
        
        
        
   
        
