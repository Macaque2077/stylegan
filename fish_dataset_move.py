import os, sys
from shutil import copy, copyfile
import cv2

# file_location = r"C:\Users\youk3\OneDrive\Desktop\Thesis\kaggle_fish_data\Fish_Dataset\Fish_Dataset"

def create_dataset(file_location):
    count = 0000
    folder_count = 0
    total_folders = 0

    for folder in os.listdir(r"{}".format(file_location)):
        if os.path.isdir("{}\{}".format(file_location,folder)):
                total_folders += 1

    for folder in os.listdir(r"{}".format(file_location)):
        
        if os.path.isdir("r{}\{}".format(file_location,folder)):
            folder_count += 1
            print("processing {}/{}".format(folder_count, total_folders))
            for image in os.listdir(r"{}\{}\{}".format(file_location,folder,folder)):
                count += 1 
                src = r"{}\{}\{}\{}".format(file_location,folder,folder,image)
                dst = r"C:\Users\youk3\OneDrive\Desktop\Thesis\git_projects\stylegan\datasets\fish\images\{}.png".format(count)
                
                
                # resize image
                full_img = cv2.imread(src)
                dim = (256, 256)
                resized = cv2.resize(full_img, dim, interpolation = cv2.INTER_AREA)
                cv2.imwrite(dst, resized)
                

                label_src = r"{}\{}\{} GT\{}".format(file_location,folder,folder,image)
                label_dst = r"C:\Users\youk3\OneDrive\Desktop\Thesis\git_projects\stylegan\datasets\fish\labels\{}.png".format(count)
                # resize image
                full_lbl = cv2.imread(label_src)
                lbl_resized = cv2.resize(full_lbl, dim, interpolation = cv2.INTER_AREA)
                cv2.imwrite(label_dst, lbl_resized)

if __name__ == "__main__":
    create_dataset(sys.argv)