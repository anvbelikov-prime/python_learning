import urllib.parse
import urllib.request

url = urllib.parse.urlparse('https://abc.belikov.net:80/library/index.php?param=value#fragment')
print(url)
print(url.port)
print(url.hostname)
print(url.path)
print(url.username)

t = ('http', 'abc.belikov.com', 'library/index.php', 'param=value', 'fragment')
print(urllib.parse.urlunsplit(t))

qs = 'param1=val1&param2=val2&par3=value3'

print(urllib.parse.parse_qs(qs))
print(urllib.parse.parse_qsl(qs))

params = {'par1': 'val1', 'par2': 'val2'}
print(urllib.parse.urlencode(params))

print(urllib.parse.urljoin('https://abc.belikov.org', 'library/index.php'))

u = urllib.request.urlopen('http://google.com')
resp = u.read()
print(resp)
