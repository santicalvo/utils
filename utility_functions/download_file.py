#!/usr/bin/env python
import os, sys
import urllib2
#from urllib2 import urlopen, URLError, HTTPError
#from bs4 import BeautifulSoup

def download_file(file_url, path=None):
    if path == None:
        temp_filename = os.path.join(os.getcwd(), os.path.basename(file_url))
    else:
        temp_filename = os.path.join(path, os.path.basename(file_url))
    f = open(temp_filename, 'wb')
    remote_file = urllib2.urlopen(file_url)

    try:
        total_size = remote_file.info().getheader('Content-Length').strip()
        header = True
    except AttributeError:
        header = False # a response doesn't always include the "Content-Length" header

    if header:
        total_size = int(total_size)

    bytes_so_far = 0

    while True:
        buffer = remote_file.read(8192)
        if not buffer:
            sys.stdout.write('\n')
            break

        bytes_so_far += len(buffer)
        f.write(buffer)
        if not header:
            total_size = bytes_so_far # unknown size

        percent = float(bytes_so_far) / total_size
        percent = round(percent*100, 2)
        sys.stdout.write( "Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent) )
        sys.stdout.flush()