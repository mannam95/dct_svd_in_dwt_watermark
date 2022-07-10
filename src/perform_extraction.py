import os
from matplotlib import cm, pyplot as plt
import numpy as np
import config
from PIL import Image
from dct import apply_2d_dct_all_blocks, get_watermarkbits_from_dct_blocks
from dwt import dwt_2d
from helpers import create_non_overlapping_blocks
from pathlib import Path
from watermark_encryption_decryption import watermark_image_decryption


def integrate_extraction():
    """
    This function does all the integration for watermark extraction

    :param None.
    :return: Returns the embedded watermark image
    """

    # This loop runs for all the files presented in the given dirctory
    for index, file in enumerate(os.listdir(config.embedded_images_path)):

        img = Image.open(config.embedded_images_path + file)  # open the image.
        img = np.asarray(img.convert(mode='L'))  # convert the image to grayscale.
        LL, (LH, HL, HH) = dwt_2d(img, 'haar')  # get the coefficients of DWT transform.
        non_overlapping_blocks = create_non_overlapping_blocks(LL, config.dct_block_size)  # get the non-overlapping blocks.
        dct_blocks = apply_2d_dct_all_blocks(non_overlapping_blocks)  # applies dct to all the non-overlapping blocks
        watermark_bits = get_watermarkbits_from_dct_blocks(dct_blocks)  # get the watermark bits from the dct blocks.
        original_watermark_image = watermark_image_decryption(watermark_bits)  # get the original watermark image.
        Path(config.extracted_images_path).mkdir(parents=True, exist_ok=True)  # create the extracted images path.
        filename = Path(file).stem  # get the filename.
        plt.imsave(config.extracted_images_path + filename + ".jpeg", original_watermark_image, cmap=cm.gray)  # save the image.
