from urllib.request import urlopen
import re

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'

response = urlopen(url)
html = response.read()
text = str(html)
pattern = re.compile(r'<!--(.+)-->')
result = pattern.findall(text)
result = result[0]
result = str(result).replace("\\n", "")
result = str(result).replace("find rare characters in the mess below", "")



letter = re.compile(r'[a-zA-Z0-9]')
letters = letter.findall(result)
msg = ''.join(letters)
print(msg)