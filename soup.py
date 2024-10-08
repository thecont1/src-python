import re
import requests
from bs4 import BeautifulSoup

def list_unique_domains(target=''):
    # Take a url as input. Does not check for validity. If blank, uses default url.
    if target == '': 
        target = "https://thecontrarian.in/"
    
    # this fakes the identity of this program to appear like a Safari browser on Mac OS
    # otherwise most websites will block this program because it is basically a bot
    headers = {
    'User-Agent': r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                  r'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 '
                  r'Safari/537.36'}
    
    # parse the webpage into a BeautifulSoup object  
    soup = BeautifulSoup(requests.get(target, headers=headers).content, 'html.parser')
    
    # store all href data (i.e. urls) appearing within <a> tags 
    urls = [ u['href'] for u in soup.find_all('a') ]
    
    # compile a regex expression to extract domain names from any valid http(s) url
    search_pattern = re.compile(r"(?:h?t?t?p?s?\:?\/?\/?)(\w+\.\w+\.?\w*\.?\w*)(?:\/)")
    
    # list expression to extract domain names out of hrefs and store them in a Set 
    unique_domain_names = { match.group(1) for u in urls 
           if (match := search_pattern.search(u)) is not None }
    
    return unique_domain_names

if __name__ == '__main__':
    for d in list_unique_domains(input()):
        print(d[4:] if d.find('www') == 0 else d)
