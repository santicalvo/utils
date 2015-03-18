# -*- coding: utf-8 -*-
import os
import Tkinter, tkFileDialog
from PIL import Image
__author__ = 'santiagocf'
# Mayor tamaño en píxeles a partir del que redimensionamos
MAX = 1280

def change_proportion(w, h):
    '''
    Ajusta la proporción a partir del valor definido en MAX
    :param w: ancho
    :param h: alto
    :return: tupla con el nuevo ancho y alto
    '''
    if(w>MAX or h>MAX):
        if(w >= h):
            h = (h * MAX)/w
            w = MAX
        elif(h>w):
            w = (w * MAX)/h
            h = MAX
    return (w, h)


def resize_to_max(path, file_name):
    '''
    Lee una imagen y la redimensiona
    :param path: ruta a la carpeta del archivo
    :param file_name: nombre de archivo
    :return: nueva imagen
    '''

    im = Image.open(os.path.join(path, file_name))
    print im.size, change_proportion(im.size[0],im.size[1])
    new_size = change_proportion(im.size[0],im.size[1])
    new_image = im.resize(new_size, Image.BICUBIC)
    return new_image


def resize_img(origin, destination):
    '''
    lee una carpeta y redimensiona las imágenes que encuentre en ellas...
    No se hace comprobación de tipo!!!!
    :param origin: ruta a la carpeta con las imagenes de origen
    :param destination: ruta a la carpeta con las imágenes de destino
    :return:
    '''
    files = os.listdir(origin)
    if not os.path.exists(destination):
        os.mkdir(destination)
    for file in files:
        try:
            new_file = resize_to_max(origin, file)
            new_file.save(os.path.join(destination, file))
        except Exception:
            print "sucedio un error con ", origin, file



if __name__ == '__main__':
    ''' Cambiar rutas para las carpetas de origen y destino '''
    origin = 'C:\\Users\\santiagocf\\Desktop\\redimension\\origen'
    destination = 'C:\\Users\\santiagocf\\Desktop\\redimension\\destino'
    root = Tkinter.Tk()
    root.withdraw()

    origin = tkFileDialog.askdirectory(title='Seleccione carpeta de origen')
    destination = tkFileDialog.askdirectory(title='Seleccione carpeta de destino')
    print origin, destination
    #modify_imgs(origin, destination)