import os

main_folder = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']

for el in folders:
    main_folder_path = os.path.join(main_folder, el)
    if not os.path.exists(main_folder_path):
        os.makedirs(main_folder_path)
