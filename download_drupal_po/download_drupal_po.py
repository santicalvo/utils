import os
from urllib2 import urlopen, URLError, HTTPError
from bs4 import BeautifulSoup
#source_code = """<span class="UserName"><a href="#">Martin Elias</a></span>"""

def get_modules(path=''):
    return os.listdir(path)

def get_drupal_translation_links(html, url='http://ftp.drupal.org/files/translations/7.x/'):
    soup = BeautifulSoup(html)
    links = soup.find_all('a')
    names = []
    hrefs = []
    for link in links:
        hrefs.append(url + link.get('href'))
        names.append(link.get_text()[:-1])
        #parsed_links.append( {'link': url + link.get('href'), 'name' : link.get_text()[:-1]})

    return (hrefs, names)

def get_drupal_translation_list(url='http://ftp.drupal.org/files/translations/7.x/'):
    response = urlopen(url)
    html = response.read()
    return html

def dlfile(url, path):
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


def get_downloadable_modules(html):
    links, names = get_drupal_translation_links(html)
    drupal_modules = get_modules(modules_path)
    downloadable_modules = []
    for module in drupal_modules:
        try:
            b = names.index(module)
            #print b, module, links[b], names[b]
            downloadable_modules.append({'module' : module, 'link' : links[b] })
        except:
            pass
    return downloadable_modules

def get_all_pos(url):
    po_list = get_drupal_translation_list(url)
    return po_list

def download_all_pos(module_url, module_name, path='po'):
    print module_url
    try:
        module_path = path+'/'+module_name
        os.makedirs(module_path)
    except:
        pass
    pos = get_all_pos(module_url)
    soup = BeautifulSoup(pos)
    links = soup.find_all('a')
    es_gl_pos = []
    for link in links:
        href = link.get('href')
        print href
        if href[-5:] == 'es.po' or href[-5:] == 'gl.po':
            po_url = module_url  + href
            es_gl_pos.append( (po_url, module_path+'/'+href) )
            #dlfile(po_url, module_path+'/'+href)
        #print module_url+'/'+link.get('href')
    last_two = es_gl_pos[-2:]
    for es_gl_po in last_two:
        dlfile(es_gl_po[0], es_gl_po[1])

    '''
    if not os.path.exists(path):
        os.mkdir(path)
    if not os.path.exists(os.path.join(module_name, path)):
        os.mkdir(os.path.join(module_name, path))
    '''


if __name__ == '__main__':
    #url = 'http://ftp.drupal.org/files/translations/7.x/ckeditor/ckeditor-7.x-1.9.gl.po'
    modules_path = 'I:\\xampp\\htdocs\\igcweb\\sites\\all\\modules\\contrib'
    #dlfile(url)
    html = get_drupal_translation_list()
    downloadable_modules = get_downloadable_modules(html)
    for d in downloadable_modules:
        download_all_pos(d['link'], d['module'])
        #break


