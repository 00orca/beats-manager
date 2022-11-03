import os
import time
import shutil

my_path = "your_path"

files_list = os.listdir(my_path)

# print (files_list)

for file in files_list:
    file_path = my_path + file
    file_creation_date = time.gmtime(os.path.getctime(file_path))

    if (not os.path.exists(my_path + str(file_creation_date.tm_year))):
        print(os.path.exists(my_path + str(file_creation_date.tm_year)))
        os.mkdir(my_path + str(file_creation_date.tm_year))
    if(not os.path.exists(my_path + "/" + str(file_creation_date.tm_year) + "/" + str(file_creation_date.tm_mon))):
        os.mkdir(my_path + "/" + str(file_creation_date.tm_year) + "/" + str(file_creation_date.tm_mon))
    
    if(file_path != my_path + str(file_creation_date.tm_year)):
        shutil.move(file_path, my_path + "/" + str(file_creation_date.tm_year) + "/" + str(file_creation_date.tm_mon))

# add exception for certain file
# expection_files = ['Backup','Templates','Project bones']
        

print("fin")
