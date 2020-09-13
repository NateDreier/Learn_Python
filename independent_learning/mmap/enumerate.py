#!/usr/bin/env python3

import sys
import os
from os import path
import concurrent.futures
from shutil import copyfile
import time
import tarfile

start_time = time.time()

inputdir  = sys.argv[1]
outputdir = "foo"

perms = 0o755

if path.exists(outputdir) is False:
    try:
        os.mkdir(outputdir, perms)
    except OSError:
        print(f'Creation of this directory, {outputdir}, has failed')

for subdir, dirs, files in os.walk(inputdir):
    if path.exists(os.path.join(outputdir, subdir)) is False:
        try:
            os.mkdir(os.path.join(outputdir,subdir), perms)
        except OSError:
            print(f'Creation of this directory, {outputdir}, has failed')


def scrub_file(filename, new_path, old_path):
    copyfile(old_path, new_path)

def tar_dir():
    with tarfile.open("scrubbed.tar.gz", "w:gz") as tar:
        tar.add(outputdir, arcname=outputdir)

if __name__ == "__main__":
    for subdir, dirs, files in os.walk(inputdir):
       for file in files:
           old_path = os.path.join(subdir, file)
           new_path = os.path.join(outputdir, subdir, file)
           scrub_file(file, new_path, old_path)
    tar_dir()
    print(f'{time.time() - start_time}')
