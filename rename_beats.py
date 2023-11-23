import os
import re
# import librosa
# import numpy as np

def rename_files(path, producer):
    files_list = os.listdir(path)

    for file in files_list:
        if file.endswith('.wav') and not os.path.isdir(path + file):
            bpm, file_name = extract_bpm_and_name(file)
            rename_file(path, file, bpm, file_name, producer)

def extract_bpm_and_name(file):
    file_no_extension = file.split('.')[0]
    bpm_match = re.search(r'\d{2,3}bpm', file_no_extension, re.IGNORECASE)
    bpm = bpm_match.group() if bpm_match else ''
    file_name = file_no_extension.replace(bpm, '')
    return bpm, file_name

def rename_file(path, file, bpm, file_name, producer):
    new_file_name = f'{file_name} [{bpm}] {producer}.wav'
    if not file.find(new_file_name):
        print(new_file_name)
        os.rename(path + file, path + new_file_name)

# def find_key(path, file):


# Usage
my_path = "C:/Users/liban/Documents/Image-Line/FL Studio/Projects/2023/9 - septembre/"
producer_name = '@00orca'
rename_files(my_path, producer_name)