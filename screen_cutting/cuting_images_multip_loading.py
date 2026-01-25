
from PIL import Image
import os
from tqdm import tqdm

"""
Couper plusieurs images en deux depuis un dossier, utilisé pur les captures à deux ecran
creer les dossier
"""

#source
path_image          = "C:/Pictures/Screenshots/Sceenshots 25-26/"

#destination
path_ma_capture     = "C:/Pictures/Screenshots/Screen voulu/"
path_non_voulu      = "C:/Pictures/Screenshots/Screen non voulu/"


def cuting(file_path,filename):
    image = Image.open(file_path)

    width, height = image.size

    # print("width : ", width)
    # print("height : ", height)

    left_image = image.crop((0, 0, width // 2, height))
    right_image = image.crop((width // 2, 0, width, height))

    # ici on sauvgarde les deux partis de l'image
    left_image.save(path_non_voulu + filename)
    right_image.save(path_ma_capture + filename)    


# si je veux pas tqdm --> for filename in os.listdir(path_image):
for filename in tqdm(os.listdir(path_image), desc="Processing Images", unit="image"):

    image_to_cut = os.path.join(path_image, filename)
    
    # print(image_to_cut)
    cuting(image_to_cut,filename)
        

print("Done and done")
