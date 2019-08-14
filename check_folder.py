import os
import argparse
from colorama import init, Fore, Back, Style

# Initialize colorama
init()

parser = argparse.ArgumentParser(description='Check for non image files in input folder and move them to output folder.')
parser.add_argument('input_folder', type=str, help='defines the folder that is searched')
parser.add_argument('output_folder', type=str, help='defines the folder non images get copied to')

args = parser.parse_args()

input_folder = args.input_folder
output_folder = args.output_folder

files = []
extensions = ['.jpg','.jpeg','.png','.cr2','.bmp','.tif','.raw','.gif']


print(Fore.BLUE + "Input folder: " + Fore.GREEN + input_folder)
print(Fore.BLUE + "Output folder: " + Fore.GREEN + output_folder)
print("")
print(Fore.GREEN + "Checking for files...")

# Check all files on input_folder
# r=root, d=directories, f = files
for r, d, f in os.walk(input_folder):
    for file in f:
        filename, file_extension = os.path.splitext(file)
        if file_extension.lower() in extensions:
            continue
        else:
            files.append(os.path.join(r, file))

print(str(len(files)) + " files will be moved...")
print("")

# determine output_path and where it matches
path_parts_input = input_folder.split('\\')
path_parts_output = output_folder.split('\\')
min_len_paths = min(len(path_parts_input), len(path_parts_output))
path_start = 1

for i in range(min_len_paths):
    if path_parts_input[i] == path_parts_output[i]:
        path_start += 1

# move found files
for f in files:
    file_parts = f.split('\\')[path_start:-1]
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
    
    new_file_path = output_folder + '\\' + '\\'.join(f.split('\\')[path_start:])
    os.rename(f, new_file_path)

print('Files were moved!')