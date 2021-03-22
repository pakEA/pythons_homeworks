import os
from shutil import copytree

root_dir = 'my_project'

for root, folders, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):
            folder_name = os.path.split(root)
            folder_path = os.path.join('my_project/templates/',
                                       folder_name[1])
            if os.path.exists(folder_path):
                break
            get_copy = copytree(root, folder_path)
