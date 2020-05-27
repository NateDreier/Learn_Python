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
    image = f"{img}:{t}"

    print(f"Pulling, retagging, saving and rmi'ing: {image}")
    # Pulls the container
    cli.pull(f"{image}")
    # Tags the container with the new tag
    cli.tag(f"{image}", f"{repository}/{img}", f"{t}")

    new_image_name = f"{image}.tar"
    im = cli.get_image(f"{image}")
    with open(os.path.join(current_dir, "move", new_image_name), "wb+") as f:
        for chunk in im:
            f.write(chunk)

    # Deletes all downloaded images
    cli.remove_image(f"{image}")
    cli.remove_image(f"{repository}/{image}")


with concurrent.futures.ProcessPoolExecutor() as executor:
    f = open(sys.argv[1], "r")
    lines = f.readlines()
    executor.map(the_whole_shebang, lines)
