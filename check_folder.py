import os
import argparse

parser = argparse.ArgumentParser(description='Check for non image files in input folder and move them to output folder.')
parser.add_argument('input_folder', type=str, help='defines the folder that is searched')
parser.add_argument('output_folder', type=str, help='defines the folder non images get copied to')

args = parser.parse_args()

input_folder = args.input_folder
output_folder = args.output_folder

files = []
extensions = ['.jpg','.jpeg','.png','.cr2','.bmp','.tif','.raw','.gif']
# r=root, d=directories, f = files
for r, d, f in os.walk(input_folder):
    for file in f:
        filename, file_extension = os.path.splitext(file)
        if file_extension.lower() in extensions:
            continue
        else:
            files.append(os.path.join(r, file))

for f in files:
    file_parts = f.split('\\')[1:-1]
    file_folder = '\\'.join(file_parts)
    new_folder = output_folder + '\\' + file_folder
    create_path = ''

    for part in new_folder.split('\\'):
        if create_path == '':
            create_path = part
        else:
            create_path = create_path + '\\' + part

        if not os.path.isdir(create_path):
            os.mkdir(create_path)
    
    new_file_path = output_folder + '\\' + '\\'.join(f.split('\\')[1:])
    os.rename(f, new_file_path)

print('Files were moved!')