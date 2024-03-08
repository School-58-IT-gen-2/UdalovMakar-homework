def domain_name(url: str):
    url = url.replace('www.', '').replace('http://', '').replace('https://', '')
    return url[:url.find('.')]

print(domain_name("http://www.zombie-bites.com" ))