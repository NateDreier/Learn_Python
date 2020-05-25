#!/usr/bin/env python3

import sys
import os
import concurrent.futures
import docker

cli = docker.APIClient(base_url='unix://var/run/docker.sock')
current_dir = os.getcwd()
repository = sys.argv[2]

def the_whole_shebang(image):
  img_tag = image.split(":")
  img = img_tag[0].strip()
  t = img_tag[1].strip()

  print(f'Pulling, retagging, saving and rmi\'ing: {img}:{t}')
  cli.pull(f'{img}:{t}')
  cli.tag(f'{img}:{t}', f'{repository}/{img}', f'{t}')
  
  f = open(f'{current_dir}/move/{img}{t}.tar', 'wb')
  im = cli.get_image(f'{repository}/{img}:{t}')
  for chunk in im:
    f.write(chunk)
  f.close
  for i in cli.images():
    cli.remove_image(i,force=True)    

with concurrent.futures.ProcessPoolExecutor() as executor:
  f = open(sys.argv[1], "r")
  lines = f.readlines()
  executor.map(the_whole_shebang, lines)
