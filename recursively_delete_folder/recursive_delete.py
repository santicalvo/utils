import sys, os, shutil

def recursive_delete(folder_name, folder_root):
    origin = -len(folder_name)
    folders = []
    for root, dirs, files in os.walk(folder_root):
        if(root[origin:] == '.svn'):
            folders.append(root)
    for folder in folders:
        try:
            if(os.path.exists(folder)):
                print 'removing folder ', folder
                shutil.rmtree(folder)
            else:
                print 'doesn\'t exist', folder
        except Exception as e:
            print e.message

if __name__ == '__main__':
    l = len(sys.argv)
    if l >= 3:
        folder_name = sys.argv[1]
        folder_root = os.path.join(os.getcwd(),sys.argv[2])
    elif l == 2:
        folder_name = sys.argv[1]
        folder_root = os.getcwd()
    else:
        print 'Ussage: python recursive_delete.py <folder_to_delete> [root_folder]'
        exit(0)

    recursive_delete(folder_name, folder_root)