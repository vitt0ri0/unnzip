
# Config
work_dir = '~/Downloads'
prakt_dir = '~/praktikum'

from os import listdir

if __name__ == '__main__':
    for file in listdir(work_dir):
        filename, ext = file.split('.')

        user, hw_name = filename.split('__')

        str(hw_name).strip()
        if ext == '.zip':

        if file.split()[1] == '.zip':


    pass