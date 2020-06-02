#!/usr/bin/env python3

import sys
import os
from os import path
import concurrent.futures  # https://docs.python.org/3/library/concurrent.futures.html
import docker  # https://docker-py.readthedocs.io/en/stable/

cli = docker.APIClient(base_url="unix://var/run/docker.sock")
current_dir = os.getcwd()
repository = sys.argv[2]
tar_dir = os.path.join(current_dir, "move")


if path.exists(tar_dir) is not True:
    os.mkdir(tar_dir)


def the_whole_shebang(image: str):
    """TODO: add in logic to split out if there is "/", ports etc"""
    """Takes in string, splits it out to image and tag"""
    img_t = image.split(":")
    img = img_t[0].strip()
    t = img_t[1].strip()
    image = f"{img}:{t}"

    print(f"Pulling, retagging, saving and rmi'ing: {image}")
    # Pulls the container
    cli.pull(image)
    # Tags the container with the new tag
    cli.tag(image, f"{repository}/{img}", t)

    new_image_name = f"{img}{t}.tar"
    im = cli.get_image(image)
    with open(os.path.join(tar_dir, new_image_name), "wb+") as f:
        for chunk in im:
            f.write(chunk)

    # Deletes all downloaded images
    cli.remove_image(image)
    cli.remove_image(f"{repository}/{image}")


if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        """Utilizes the concurrent.futures library to run this with multiprocess.
        reads in the file and passes in each line to the_whole_shebang"""
        """TODO: pass in a string so that I can eliminate the redundant image var
        in the_whole_shebang function"""
        f = open(sys.argv[1], "r")
        lines = f.readlines()
        executor.map(the_whole_shebang, lines)
