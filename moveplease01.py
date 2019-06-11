#!/usr/bin/env python3

import shutil, os

os.chdir('/home/student/mycode/')

shutil.move('raynor.obj', 'ceph_storage/')

xname = input('what would you like to rename kerrigan.obj to??\n')

shutil.move('ceph_storage/kerrigan.obj', f'ceph_storage/{xname}')

print('done!')
