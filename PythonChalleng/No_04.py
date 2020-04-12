from urllib.request import urlopen
import re
import string

urLstr = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

def get_html(url):
    with urlopen(url, timeout=30) as rep:
        html = rep.read()
    # response = urlopen(url)
    # html = response.read()
    text = str(html)
    return text


start = '63579 '

for i in range(0,400):
    text = get_html(urLstr + start)
    print(i, text)
    letter = re.compile(r'([0-9])')
    letters = letter.findall(text)
    start = ''.join(letters)
    i += 1

