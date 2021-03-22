import os

root_dir = 'my_project'

dict_files = {'100': '',
              '1000': '',
              '10000': '',
              '100000': ''}

for root, dirs, files in os.walk(root_dir):
    for file in files:
        file_path = os.path.join(root, file)
        file_size = os.stat(file_path).st_size
