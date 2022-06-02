import sys
import os
from PIL import Image

# TODO 1: grab first and second argument with sys
parent_dir = sys.argv[1]  # should be Pokedex/
dest_dir = sys.argv[2]  # should be new/

# parent_dir = "./Pokedex"
# dest_dir = "./new"
# TODO 2: check if '\new' exists, if not create it
if not os.path.exists(dest_dir):
	os.mkdir(dest_dir)

# TODO 3: loop through pokedex
for file in os.listdir(parent_dir):
	img = Image.open(f"{parent_dir}/{file}")
	# TODO 4: convert images to png
	clean_name = os.path.splitext(file)[0]
	img.save(f"{dest_dir}/{clean_name}.png", "png")

