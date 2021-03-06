import glob
import os
import sys

# change these settings
index = "1"
if len(index)!=0:
    index = "_"+index

data_path = "../idd_segmentation"+index
list_path = "../list/idd"

train_image_path = data_path+"/leftImg8bit/train/"
train_label_path = data_path+"/gtFine/train/"

val_image_path = data_path+"/leftImg8bit/val/"
val_label_path = data_path+"/gtFine/val/"

test_image_path = data_path+"/leftImg8bit/test/"

train_image_names = sorted(glob.glob(train_image_path+"*/*"))
train_label_names = sorted(glob.glob(train_label_path+"*/*_gtFine_labellevel3Ids.png"))

val_image_names = sorted(glob.glob(val_image_path+"*/*"))
val_label_names = sorted(glob.glob(val_label_path+"*/*_gtFine_labellevel3Ids.png"))

test_image_names = sorted(glob.glob(test_image_path+"*/*"))

if len(train_image_names) != len(train_label_names):
    sys.exit("Train image size and label size are not same")

if len(val_image_names) != len(val_label_names):
    sys.exit("Val image size and label size are not same")

train_size = len(train_image_names)
val_size = len(val_image_names)
test_size = len(test_image_names)

print("Number of train images ", len(train_image_names))
print("Number of train labels ", len(train_label_names))
print("Number of val images ", len(val_image_names))
print("Number of val labels ", len(val_label_names))
print("Number of test images ", len(test_image_names))

# create directory
if not os.path.exists(list_path):
    os.makedirs(list_path)

# write to file
train_f = open(list_path+"/train"+index+".lst", "w")
val_f = open(list_path+"/val"+index+".lst", "w")
test_f = open(list_path+"/test"+index+".lst", "w")

for i in range(train_size):
    train_image_name = os.path.split(train_image_names[i])[1]
    pos = train_image_name.find("_")
    train_image_name = train_image_name[:pos]

    train_label_name = os.path.split(train_label_names[i])[1]
    pos = train_label_name.find("_")
    train_label_name = train_label_name[:pos]

    if train_image_name != train_label_name:
        print("Ignoring ", train_image_name, train_label_name)

    train_entry = ""
    train_entry+=train_image_names[i]
    train_entry+=3*" "
    train_entry+=train_label_names[i]

    train_f.write(train_entry)
    train_f.write("\n")

for i in range(val_size):
    val_image_name = os.path.split(val_image_names[i])[1]
    pos = val_image_name.find("_")
    val_image_name = val_image_name[:pos]

    val_label_name = os.path.split(val_label_names[i])[1]
    pos = val_label_name.find("_")
    val_label_name = val_label_name[:pos]

    if val_image_name != val_label_name:
        print("Ignoring ", val_image_name, val_label_name)

    val_entry = ""
    val_entry+=val_image_names[i]
    val_entry+=3*" "
    val_entry+=val_label_names[i]

    val_f.write(val_entry)
    val_f.write("\n")

for i in range(test_size):
    test_entry = ""
    test_entry+=test_image_names[i]

    test_f.write(test_entry)
    test_f.write("\n")


