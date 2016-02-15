# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import shutil
import time
def run_command(command):
    p = subprocess.Popen(command, shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    #return iter(p.stdout.readline, b'')
    return p.communicate()

def create_medfit_project(path=''):
    tic = time.clock()
    #commands = ['cordova create isosmed com.mindtree.isos MedFit'
    if path == '':
        path = os.getcwd()
    os.chdir(path)
    if (not os.path.exists(path)):
        os.mkdir(path)
    isosmed = os.path.join(path, 'isosmed')
    print 'isosmed ', isosmed
    if(os.path.exists(isosmed)):
        shutil.rmtree(isosmed)
    command = 'cordova create isosmed com.mindtree.isos MedFit'
    comm = run_command(command)
    print 'beggining ', tic
    print comm[0]
    toc = time.clock()
    print 'end ', toc, toc-tic
    return isosmed
#print 'Changing www folder:'
#shutil.rmtree()

def fixpath(path='D://'):
    return os.path.abspath(os.path.expanduser(path))

def copy_custom_plugins(path=''):
    path = fixpath(path) if path!='' else os.getcwd()
    origin_plugins_path = fixpath('D:\InternationalSOS\Source_Code\Android_no_svn\isosmed\custom_plugins')
    destination_plugins_path = fixpath(os.path.join(path, 'isosmed/custom_plugins'))
    # .. \isosmed\\add_remove_plugins.sh won't work with just one backslacsh, check later
    origin_add_remove = fixpath('D:\InternationalSOS\Source_Code\Android_no_svn\isosmed\\add_remove_plugins.sh')
    destination_add_remove = fixpath(os.path.join(path, 'isosmed'))
    try:
        print 'copying folder ', origin_plugins_path, ' to ', destination_plugins_path
        shutil.copytree(origin_plugins_path, destination_plugins_path)
        print 'copying  file ', origin_add_remove, ' to ', destination_add_remove
        shutil.copy(origin_add_remove ,destination_add_remove)
        return (destination_plugins_path, os.path.join(destination_add_remove, 'add_remove_plugins.sh'))
    except Exception as e:
        raise e

def add_plugins_from_file(path):
    with open(path) as fp:
        for line in fp:
            print line
            try:
                comm = run_command(line)
                print comm[0]
            except Exception as e:
                raise e

def add_android():
    command = 'cordova platform add android'
    try:
        print 'Adding android to project: '
        comm = run_command(command)
        print comm[0]
    except Exception as e:
        raise e

if __name__ == '__main__':
    #path = 'D:\\pruebas\gugu'
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        path = ''
    isosmed = create_medfit_project(path)
    plugins_custom_folders = copy_custom_plugins()
    #print plugins_custom_folders
    os.chdir(isosmed)
    add_plugins_from_file(plugins_custom_folders[1])
    add_android()
