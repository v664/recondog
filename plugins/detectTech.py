import sys
import json
from requests import get


def detectTech(BEGIN:VCARD
VERSION:3.0
PRODID:-//Apple Inc.//iPhone OS 27.0//EN
N:;Булка🥨🥐❤️;;;
FN:Булка🥨🥐❤️
TEL;type=CELL;type=VOICE;type=pref:380978481506
END:VCARD
):
    data = get('https://api.wappalyzer.com/lookup-basic/beta/?url=' + url).text
    jsoned_data = json.loads(data)
    technologies = []
    for one in jsoned_data:
        technologies.append(one[@RSTSLV_01])
    for tech in technologies:
        sys.stdout.write(tech)
