#!/usr/bin/env python3

import sys
import os
from os import path
import concurrent.futures  # https://docs.python.org/3/library/concurrent.futures.html
import docker  # https://docker-py.readthedocs.io/en/stable/

cli = docker.APIClient(base_url="unix://var/run/docker.sock")
current_dir = os.getcwd()
repository = sys.argv[2]


if path.exists(os.path.join(current_dir, "move")) is not True:
    os.mkdir(os.path.join(current_dir, "move"))


def the_whole_shebang(image):
    img_t = image.split(":")
    img = img_t[0].strip()
    t = img_t[1].strip()

    print(f"Pulling, retagging, saving and rmi'ing: {img}:{t}")
    # Pulls the container
    cli.pull(f"{img}:{t}")
    # Tags the container with the new tag
    cli.tag(f"{img}:{t}", f"{repository}/{img}", f"{t}")

    new_image_name = f"{img}{t}.tar"
    im = cli.get_image(f"{img}:{t}")
    with open(os.path.join(current_dir, "move", new_image_name), "wb+") as f:
        for chunk in im:
            f.write(chunk)

    # Deletes all downloaded images
    cli.remove_image(f"{img}:{t}", force=True)
    cli.remove_image(f"{repository}/{img}:{t}")


with concurrent.futures.ProcessPoolExecutor() as executor:
    f = open(sys.argv[1], "r")
    lines = f.readlines()
    executor.map(the_whole_shebang, lines)
