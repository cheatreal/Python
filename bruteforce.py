import sys
import hashlib
import itertools
CHOICES = "0123456789abcdefghijklmnopqrstuvwxyz"
Max = 5

for length in range(0,Max+1):
    for choice in itertools.product(CHOICES,repeat = length):
        #password = '0'*(MaxLength - length)
        password = "admin"
        password += ''.join(choice)
        password += "31337"
        #print password
        if hashlib.md5(password).hexdigest().upper() == "A0F60D70FAD9DC9846D971FD61D2B7A0":
                    print password
