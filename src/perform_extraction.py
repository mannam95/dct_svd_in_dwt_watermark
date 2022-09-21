import os
from matplotlib import cm, pyplot as plt
import numpy as np
from PIL import Image
from dct import apply_2d_dct_all_blocks, get_watermarkbits_from_dct_blocks
from dwt import dwt_2d
from helpers import create_non_overlapping_blocks
from pathlib import Path
from watermark_encryption_decryption import Encrypt_Decrypt


class Extract():
    """This class defines config options.

    It also implement a function which will integrate the extracting.
    """

    def __init__(self, options):
        """Init the class."""
        self.options = options
        self.encrypt_decrypt = Encrypt_Decrypt(options)


    def integrate_extraction(self):
        """
        This function does all the integration for watermark extraction

        :param None.
        :return: Returns the embedded watermark image
        """

        # This loop runs for all the files presented in the given dirctory
        for index, file in enumerate(os.listdir(self.options.emb_dir_path)):

            # open the image.
            img = Image.open(self.options.emb_dir_path + '/' + file)

            # convert the image to grayscale.
            img = np.asarray(img.convert(mode='L'))

            # get the coefficients of DWT transform.
            LL, (LH, HL, HH) = dwt_2d(img, 'haar')

            # get the non-overlapping blocks.
            non_overlapping_blocks = create_non_overlapping_blocks(HL, self.options.dct_block_size)

            # applies dct to all the non-overlapping blocks
            dct_blocks = apply_2d_dct_all_blocks(non_overlapping_blocks)

            # get the watermark bits from the dct blocks.
            watermark_bits = get_watermarkbits_from_dct_blocks(dct_blocks)

            # get the original watermark image.
            original_watermark_image = self.encrypt_decrypt.watermark_image_decryption(watermark_bits)

            # create the extracted images path.
            if not os.path.exists(self.options.ext_dir_path):
                os.makedirs(self.options.ext_dir_path)
            
            # save the extracted image.
            filename = Path(file).stem  # get the filename.
            plt.imsave(self.options.ext_dir_path + '/' + filename + '.jpeg', original_watermark_image, cmap=cm.gray)  # save the image.
