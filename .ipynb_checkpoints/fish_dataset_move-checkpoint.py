import os, sys, random
from shutil import copy, copyfile
import cv2

# file_location = r"C:\Users\youk3\OneDrive\Desktop\Thesis\kaggle_fish_data\Fish_Dataset\"

def create_dataset(file_location):
    count = 0000
    holdout_count = 0
    folder_count = 0
    total_folders = 0
    test_percent = .10  
    in_files = {}
    
    print(file_location)
    for folder in os.listdir(r"{}".format(file_location)):
        if os.path.isdir("{}\{}".format(file_location,folder)):
                total_folders += 1
            
    print(total_folders)
    for folder in os.listdir(r"{}".format(file_location)):
        if os.path.isdir("{}\{}".format(file_location,folder)):
            folder_count += 1
            print("processing {}/{}".format(folder_count, total_folders))
            for image in os.listdir(r"{}\{}\{}".format(file_location,folder,folder)):
                if random.random() < test_percent:
                    src = r"{}\{}\{}\{}".format(file_location,folder,folder,image)
                    dst = r"C:\Users\youk3\OneDrive\Desktop\Thesis\git_projects\stylegan\datasets\fish_holdout\images\{}.png".format(count)
                    
                    
                    # resize image
                    full_img = cv2.imread(src)
                    dim = (256, 256)
                    resized = cv2.resize(full_img, dim, interpolation = cv2.INTER_AREA)
                    cv2.imwrite(dst, resized)
                    

                    label_src = r"{}\{}\{} GT\{}".format(file_location,folder,folder,image)
                    label_dst = r"C:\Users\youk3\OneDrive\Desktop\Thesis\git_projects\stylegan\datasets\fish_holdout\labels\{}.png".format(count)
                    # resize image
                    full_lbl = cv2.imread(label_src)
                    lbl_resized = cv2.resize(full_lbl, dim, interpolation = cv2.INTER_AREA)
                    cv2.imwrite(label_dst, lbl_resized)
                    in_files[holdout_count] = "{}\{}\{}\{}".format(file_location,folder,folder,image)
                    holdout_count += 1
                    
                else: 
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
                    count += 1 
    print("train size = ", count)
    print("holdout size = ", holdout_count)
    failed_images = []
    for key in in_files.keys():
        if not os.path.isfile(r"C:\Users\youk3\OneDrive\Desktop\Thesis\git_projects\stylegan\datasets\fish_holdout\images\{}.png".format(image)):
            failed_images.append(key)
    
    for fail in failed_images:
        print(in_files[fail])


# pass the location of the parent folder of the images and the image labels 
if __name__ == "__main__":
    create_dataset(sys.argv[1])
    # this created 
    # 8106 train
    # 894 count, but actually only created 805 holdout images