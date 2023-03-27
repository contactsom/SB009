import urllib.request

text = urllib.request.urlopen("http://www.textfiles.com/etext/AUTHORS/SHAKESPEARE/shakespeare-romeo-48.txt").read().decode('utf8')

print(text)
