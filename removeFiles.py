#This program deletes files in a given folder that are older than 30 days.
import time;
import os, shutil;

path = input('Enter the name of the file or folder to be cleaned: ')
realtime = time.time() / 86400
ctime = os.stat(path).st_ctime / 86400

if os.path.exists(path):
    os.walk(path)
    os.path.join(path)
    if realtime - ctime > 30:
        name, ext = os.path.splitext(path)
        ext = ext[1:]
        if ext == '':
            shutil.rmtree()
        else:
            os.remove(path)
    else:
        print('The selected item has not exceeded 30 days.')
else:
    print('Invalid input.')