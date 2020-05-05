import numpy as np
from anue_labels import labels
from imageio import imread
import glob
from argparse import ArgumentParser
import random
import time
import PIL.Image

def get_level_id(label, level):
    if level == 2:
        return label.level3Id
    elif level == 1:
        return label.level2Id
    elif level == 0:
        return label.level1Id
    else:
        return label.id

def get_ids(label, level):
    id_list = []
    for l in labels:
        if get_level_id(l, level) == label:
            id_list.append(l.level3Id)
    return id_list

num_labels = [7, 16, 26]

colors = [
    [(128, 64, 128), (244, 35, 232), (220, 20, 60), (0, 0, 230), (220, 190, 40), (70, 70, 70), (70, 130, 180), (0, 0, 0)],
    [(128, 64, 128), (250, 170, 160), (244, 35, 232), (230, 150, 140), (220, 20, 60), (255, 0, 0), (0, 0, 230), (255, 204, 54), (0, 0, 70), (220, 190, 40), (190, 153, 153), (174, 64, 67), (153, 153, 153), (70, 70, 70), (107, 142, 35), (70, 130, 180),(0, 0, 0)],
    [(128, 64, 128), (250, 170, 160), (244, 35, 232), (230, 150, 140), (220, 20, 60), (255, 0, 0), (0, 50, 50), (119, 11, 32), (255, 204, 54), (0, 0, 120), (0, 0, 70), (0, 60, 100), (0, 0, 90), (220, 190, 40), (102, 102, 156), (190, 153, 153), (180, 165, 180), (174, 64, 67), (220, 220, 0), (250, 170, 30), (153, 153, 153), (169, 187, 214), (70, 70, 70), (150, 100, 100), (107, 142, 35), (70, 130, 180), (0, 0, 0)],
    [(128, 64, 128), (250, 170, 160), (81, 0, 81), (244, 35, 232), (230, 150, 140), (152, 251, 152), (220, 20, 60), (246, 198, 145), (255, 0, 0), (0, 0, 230), (119, 11, 32), (255, 204, 54), (0, 0, 142), (0, 0, 70), (0, 60, 100), (0, 0, 90), (0, 0, 110), (0, 80, 100), (136, 143, 153), (220, 190, 40), (102, 102, 156), (190, 153, 153), (180, 165, 180), (174, 64, 67), (220, 220, 0), (250, 170, 30), (153, 153, 153), (153, 153, 153), (169, 187, 214), (70, 70, 70), (150, 100, 100), (150, 120, 90), (107, 142, 35), (70, 130, 180), (169, 187, 214), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 142)]
    ]

def get_image(label_mask, level):
    h, w = label_mask.shape
    image = np.zeros((h,w,3), dtype=np.uint8)
    for l in range(num_labels[level]):
        id_list = get_ids(l, level)
        for id in id_list:
            indices = label_mask == id
            for i in range(3):
                image[indices,i] = colors[level][l][i]
    return image

def get_masks(label_path):
    image_path = label_path.replace('gtFine', 'leftImg8bit').replace('_labellevel3Ids','')
    label_mask = imread(label_path)
    image = imread(image_path)
    imgs = [image]
    for i in range(3):
        imgs.append(get_image(label_mask,3-i-1))
    return imgs

def view_image(label_paths, h, w):
    canvas = PIL.Image.new('RGB', (w*4, h*len(label_paths)), 'white')
    for row, label_path in enumerate(label_paths):
        images = get_masks(label_path)
        for col, image in enumerate(images):
            canvas.paste(PIL.Image.fromarray(image, 'RGB'), ((col* w, row*h)))
    return canvas

def get_args():
    parser = ArgumentParser()
    parser.add_argument('--data-dir', default="")
    args = parser.parse_args()
    return args

# The main method
def main(args):
    label_path_list = [
        "/home/meenu/Desktop/ddp/code/autonue/idd_segmentation_1/gtFine/train/0/005626_gtFine_labellevel3Ids.png", 
        "/home/meenu/Desktop/ddp/code/autonue/idd_segmentation_1/gtFine/train/0/021541_gtFine_labellevel3Ids.png",
        "/home/meenu/Desktop/ddp/code/autonue/idd_segmentation_1/gtFine/train/0/012449_gtFine_labellevel3Ids.png"]
    label_size = imread(label_path_list[0]).shape
    canvas = view_image(label_path_list, label_size[0], label_size[1])
    canvas.save("/home/meenu/Desktop/ddp-thesis/plots/idd_label_hierarchy.png")

if __name__ == "__main__":
    args = get_args()
    main(args)




