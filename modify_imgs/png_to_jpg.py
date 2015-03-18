# -*- coding: utf-8 -*-
import os
import Tkinter, tkFileDialog
from PIL import Image
__author__ = 'santiagocf'


def png_to_jpg(origin, destination, file):
    print(file.split(".")[0])
    name = file.split(".")[0]
    png_path = os.path.join(origin, file)
    jpg_path = os.path.join(destination, name+".jpg")
    im_png = Image.open(png_path)
    im_png.load()
    im_jpg = Image.new("RGB", im_png.size, (255,255,255))
    im_jpg.paste(im_png,mask=im_png.split()[3])
    im_png.save(jpg_path)
    print png_path, jpg_path
    '''
    im = Image.open(r"C:\jk.png")
    bg = Image.new("RGB", im.size, (255,255,255))
    bg.paste(im,im)
    bg.save(r"C:\jk2.jpg")

    im = Image.open(os.path.join(path, file_name))
    print im.size, change_proportion(im.size[0],im.size[1])
    new_size = change_proportion(im.size[0],im.size[1])
    new_image = im.resize(new_size, Image.BICUBIC)
    return new_image
    '''


def convert_png_to_jpg(origin, destination):
    files = os.listdir(origin)
    if not os.path.exists(destination):
        os.mkdir(destination)
    for file in files:
        try:
            png_to_jpg(origin, destination, file)
        except Exception as e:
            print "sucedio un error con ", origin, file, str(e)
        '''
        try:
            png_to_jpg(os.path.join(origin, file))
            #new_file = resize_to_max(origin, file)
            #new_file.save(os.path.join(destination, file))
        except Exception:
            print Exception
            print "sucedio un error con ", origin, file
        '''


if __name__ == '__main__':
    ''' Cambiar rutas para las carpetas de origen y destino '''
    origin = r'C:\Users\santiagocf\Desktop\eventos\imagenes-app-estaticas'
    destination = r'C:\Users\santiagocf\Desktop\eventos\imagenes-app-estaticas-jpg'
    #root = Tkinter.Tk()
    #root.withdraw()

    #origin = tkFileDialog.askdirectory(title='Seleccione carpeta de origen')
    #destination = tkFileDialog.askdirectory(title='Seleccione carpeta de destino')
    print origin, destination
    convert_png_to_jpg(origin, destination)
    #modify_imgs(origin, destination)