#!/usr/bin/env python
import os
from urllib2 import urlopen, URLError, HTTPError
from bs4 import BeautifulSoup

def download_file(url, path):
    # Open the url
    try:
        f = urlopen(url)
        print "downloading " + url + " to path " + path
        # Open our local file for writing
        with open(path, "w") as local_file:
            local_file.write(f.read())
        '''
        with open(os.path.basename(url), "wb") as local_file:
            local_file.write(f.read())
        '''
    #handle errors
    except HTTPError, e:
        print "HTTP Error:", e.code, url
    except URLError, e:
        print "URL Error:", e.reason, url

def get_links_from_url(url):
    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    links = soup.find_all('a')
    linkslist = []
    for link in links:
        txt = link.get_text()[:-1]
        if txt != '..':
            linkslist.append({
                "href": url + link.get('href'),
                "name": link.get_text()[:-1]
            })
    return linkslist

# get leaked links from punica's inquiry
def get_punica_links():
    url = "http://www.anonprotest.com/trama-punica/"
    links_and_names = get_links_from_url(url)
    punica_links = []
    for link in links_and_names:
        child_links = get_links_from_url(link['href'])
        for child_link in child_links:
            punica_links.append(child_link)
            print 'we got link: ', child_link
    return punica_links

def download_punica_links(path="download"):
    links = get_punica_links()
    if not os.path.exists(path):
        print 'creating destination dir'
        os.mkdir(path)

    for link in links:
        destination = path + '/' + link['href'].rsplit('/',1)[1]
        download_file(link['href'], destination)


if __name__ == '__main__':
    download_punica_links()