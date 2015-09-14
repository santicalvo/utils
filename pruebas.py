#!/usr/bin/env python
import os
from utility_functions.download_file import download_file

if __name__ == '__main__':
    url = "http://tararea.me/Documentos.zip"
    #url = "https://github.com/santicalvo/gestor_lugares/archive/master.zip"
    destination = os.getcwd()
    download_file(url, destination)
