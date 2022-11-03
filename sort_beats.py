import os
import time
import shutil

def month_str(month):
    month_arr = ['1 - janvier','2 - fevrier','3 - mars','4 - avril','5 - mai','6 - juin','7 - juillet','8 - aout','9 - septembre','10 - octobre','11 - novembre','12 - decembre']
    return month_arr[month-1]
        
        
my_path = "C:/Users/liban/Documents/Image-Line/FL Studio/Projects/"

files_list = os.listdir(my_path)

# print (files_list)

for file in files_list:
    file_path = my_path + file
    file_creation_date = time.localtime(os.path.getctime(file_path))

    if (not os.path.exists(my_path + str(file_creation_date.tm_year))):
        print(os.path.exists(my_path + str(file_creation_date.tm_year)))
        os.mkdir(my_path + str(file_creation_date.tm_year))
    if(not os.path.exists(my_path + "/" + str(file_creation_date.tm_year) + "/" + month_str(file_creation_date.tm_mon))):
        os.mkdir(my_path + "/" + str(file_creation_date.tm_year) + "/" + month_str(file_creation_date.tm_mon))
    
    if(file_path != my_path + str(file_creation_date.tm_year)):
        shutil.move(file_path, my_path + "/" + str(file_creation_date.tm_year) + "/" + month_str(file_creation_date.tm_mon))

# add exception for certain file
# expection_files = ['Backup','Templates','Project bones']
        

print("fin")
