import os
from matplotlib import cm, pyplot as plt
import numpy as np
import config
from PIL import Image
from dct import apply_2d_dct_all_blocks, get_watermarkbits_from_dct_blocks
from dwt import dwt_2d
from helpers import create_non_overlapping_blocks
from pathlib import Path
from watermark_encryption import watermark_image_decryption
from pathlib import Path


def integrate_extraction():
    """
    This function does all the integration for watermark extraction

    :param None.
    :return: Returns the embedded watermark image
    """ 

    # This loop runs for all the files presented in the given dirctory
    for index, file in enumerate(os.listdir(config.embedded_images_path)):

        img = Image.open(config.embedded_images_path + file)

        img = np.asarray(img.convert(mode='L'))

        # img = np.asarray(img.resize((256, 256)))

        LL, (LH, HL, HH) = dwt_2d(img, 'haar') # get the coefficients of DWT transform

        non_overlapping_blocks = create_non_overlapping_blocks(LL, config.dct_block_size) # creates non-overlapping blocks
        
        dct_blocks = apply_2d_dct_all_blocks(non_overlapping_blocks) # applies dct to all the non-overlapping blocks

        watermark_bits = get_watermarkbits_from_dct_blocks(dct_blocks) # gets the watermark bits

        original_watermark_image = watermark_image_decryption(watermark_bits) # gets the decrypted watermark original image

        Path(config.extracted_images_path).mkdir(parents=True, exist_ok=True) # create the extracted images path

        filename = Path(file).stem
        plt.imsave(config.extracted_images_path + filename +".jpeg", original_watermark_image, cmap=cm.gray)

        # im = Image.fromarray(original_watermark_image)

        # im.convert("L").save(config.extracted_images_path + "watermark_"+ str(index) +".jpeg")