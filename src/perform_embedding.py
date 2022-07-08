import os
import numpy as np
import config
from PIL import Image
from dct import apply_2d_dct_all_blocks, apply_inverse_2d_dct_all_blocks, update_dct_blocks
from dwt import dwt_2d, idwt_2d
from helpers import create_image_from_overlapping_blocks, create_non_overlapping_blocks
from pathlib import Path

from watermark_encryption import watermark_image_encryption


def integrate_embedding():
    """
    This function does all the integration for watermark embedding

    :param data: 2D array with input data.
    :return: Returns the embedded watermark image
    """

    # Watermark encrypted
    wat_enc = watermark_image_encryption()

    # This loop runs for all the files presented in the given dirctory
    for file in os.listdir(config.train_images_path):

        img = Image.open(config.train_images_path + file)  # open the image.
        img = np.asarray(img.convert(mode='L'))  # convert the image to grayscale.
        LL, (LH, HL, HH) = dwt_2d(img, 'haar')  # get the coefficients of DWT transform
        non_overlapping_blocks = create_non_overlapping_blocks(LL, config.dct_block_size)  # creates non-overlapping blocks.
        dct_blocks = apply_2d_dct_all_blocks(non_overlapping_blocks)  # applies dct to all the non-overlapping blocks.
        new_dct_blocks = update_dct_blocks(dct_blocks, wat_enc)  # modifies the dct blocks as per the paper, main embedding.
        idct_blocks = apply_inverse_2d_dct_all_blocks(new_dct_blocks)  # perform inverse 2d dct transform on the modified dct blocks.
        iLL = create_image_from_overlapping_blocks(idct_blocks, LL.shape)  # get the modified LL band.
        embedded_image = idwt_2d(coeffs=(iLL, (LH, HL, HH)))  # perform inverse DWT transform.
        Path(config.embedded_images_path).mkdir(parents=True, exist_ok=True)  # create the embedded images path.
        # plt.imsave(config.embedded_images_path + "test.png", embedded_image, cmap=cm.gray)
        im = Image.fromarray(embedded_image)
        im.convert("L").save(config.embedded_images_path + file)
