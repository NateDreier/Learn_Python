#!/usr/bin/env python3

import sys
import os
from os import path
import concurrent.futures
from shutil import copyfile
import time
import tarfile
import zipfile

#TODO: change the naming scheme of scrubbed_dir/tar to be the name of the tar with scrubbed prepended

start_time = time.time()

to_scrub  = sys.argv[1]
scrub_dir = "TO_SCRUB"
scrubbed_dir = "SCRUBBED"

perms = 0o755

if path.exists(scrub_dir) is False:
    try:
        os.mkdir(scrubbed_dir, perms)
    except OSError:
        print(f'Creation of this directory, {scrubbed_dir}, has failed')
if path.exists(scrubbed_dir) is False:
    try:
        os.mkdir(scrubbed_dir, perms)
    except OSError:
        print(f'Creation of this directory, {scrubbed_dir}, has failed')
def setup_dir():
    for subdir, dirs, files in os.walk(scrub_dir):
        if path.exists(os.path.join(scrubbed_dir, subdir)) is False:
            try:
                os.mkdir(os.path.join(scrubbed_dir,subdir), perms)
            except OSError:
                print(f'Creation of this directory, {scrubbed_dir}, has failed')

def scrub_file(new_path, old_path):
    copyfile(old_path, new_path)
    print("yay")

def tar_dir():
    with tarfile.open("scrubbed.tar.gz", "w:gz") as tar:
        tar.add(scrubbed_dir, arcname=outputdir)

def unzipper(unzip):
    with zipfile.ZipFile(to_scrub, 'r') as zip:
        print("unzipping...")
        zip.extractall(scrub_dir)

if __name__ == "__main__":
    if to_scrub.endswith(".zip"):
        unzipper(to_scrub)
    setup_dir()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        print("moving files..")
        for subdir, dirs, files in os.walk(scrub_dir):
            for file in files:
                old_path = os.path.join(subdir, file)
                new_path = os.path.join(scrubbed_dir, subdir, file)
                #executor.submit(scrub_file, file, new_path, old_path)
                scrub_file(new_path, old_path)
    print(f'{time.time() - start_time}')

