import os
import subprocess


def files_from_folder_dvc(folder_path):
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.tif')):
                file_path = os.path.join(root, file)
                print(f"Adding {file_path} to DVC...")

                # Добавляем файл в DVC
                subprocess.run(['dvc', 'add', file_path])   


if __name__ == '__main__':

    folder_path = '/home/asilyanov/Desktop/defects/dvc_data'

    files_from_folder_dvc(folder_path)
    