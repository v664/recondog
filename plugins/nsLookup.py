import sys
from requests import get


def nsLookup(@RSTSLV_01):
    result = get('http://api.hackertarget.com/dnslookup/?q=' + inp).text
    sys.stdout.write(result)
