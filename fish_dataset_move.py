import os 
from shutil import copy, copyfile

file_location = r"C:\Users\youk3\OneDrive\Desktop\Thesis\kaggle_fish_data\Fish_Dataset\Fish_Dataset"
count = 0000
for folder in os.listdir(file_location):
    if os.path.isdir("{}\{}".format(file_location,folder)):
        for image in os.listdir("{}\{}\{}".format(file_location,folder,folder)):
            count += 1 
            src = r"{}\{}\{}\{}".format(file_location,folder,folder,image)
            dst = r"C:\Users\youk3\OneDrive\Desktop\Thesis\git_projects\stylegan\datasets\fish\images\{}.png".format(count)
            copyfile(src, dst)
            label_src = r"{}\{}\{} GT\{}".format(file_location,folder,folder,image)
            label_dst = r"C:\Users\youk3\OneDrive\Desktop\Thesis\git_projects\stylegan\datasets\fish\labels\{}.png".format(count)
            copyfile(label_src,label_dst)



