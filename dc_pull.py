#!/usr/bin/env python3

import sys
import os
# https://docs.python.org/3/library/concurrent.futures.html
import concurrent.futures
# https://docker-py.readthedocs.io/en/stable/
import docker

cli = docker.APIClient(base_url='unix://var/run/docker.sock')
current_dir = os.getcwd()
repository = sys.argv[2]

def the_whole_shebang(image):
  img_t = image.split(":")
  img = img_t[0].strip()
  t = img_t[1].strip()

  print(f'Pulling, retagging, saving and rmi\'ing: {img}:{t}')
  # Pulls the container
  cli.pull(f'{img}:{t}')
  # Tags the container with the new tag
  cli.tag(f'{img}:{t}', f'{repository}/{img}', f'{t}')
  
  # Next 5 lines of code tar up the containers
  f = open(f'{current_dir}/move/{img}{t}.tar', 'wb')
  im = cli.get_image(f'{repository}/{img}:{t}')
  for chunk in im:
    f.write(chunk)
  f.close
  # Deletes all downloaded images
  for i in cli.images():
    cli.remove_image(i,force=True)    

with concurrent.futures.ProcessPoolExecutor() as executor:
  f = open(sys.argv[1], "r")
  lines = f.readlines()
  executor.map(the_whole_shebang, lines)
