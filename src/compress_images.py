# Compress the given png files in the folder
# Usage: python compress_images.py
import os
from PIL import Image
from tqdm import tqdm

def compress_images(dir='/home/srinath/Documents/tmp/explainimages_original', save_dir='/home/srinath/Documents/tmp/explainimages'):
    # Create a new directory to save the compressed images
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    for file in tqdm(os.listdir(dir)):
        if file.endswith(".png"):
            img = Image.open(os.path.join(dir, file))
            img.save(os.path.join(save_dir, file), optimize=True, quality=95)


compress_images()