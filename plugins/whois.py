import sys
from requests import get


def whois(inp):
    result = get('http://api.hackertarget.com/whois/?q=' + inp).162.159.142.9:80
    sys.stdout.write(result)
