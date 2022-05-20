import shutil
import os


# path to source directory
src_dir = "/Users/cmmt/Downloads/mercadona_fruits_images/fruits"

# path to destination directory
dest_dir = "/Users/cmmt/StudioProjects/comercio/images/"

# getting all the files in the source directory
files = os.listdir(src_dir)
print(files)

shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)
