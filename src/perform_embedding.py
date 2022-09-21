import os
import numpy as np
from PIL import Image
from dct import apply_2d_dct_all_blocks, apply_inverse_2d_dct_all_blocks, update_dct_blocks
from dwt import dwt_2d, idwt_2d
from helpers import create_image_from_overlapping_blocks, create_non_overlapping_blocks
from watermark_encryption_decryption import Encrypt_Decrypt


class Embed():
    """This class defines config options.

    It also implement a function which will integrate the embedding.
    """

    def __init__(self, options):
        """Init the class."""
        self.options = options
        self.encrypt_decrypt = Encrypt_Decrypt(options)


    def integrate_embedding(self):
        """
        This function does all the integration for watermark embedding

        :param options: config options.
        :return: Returns the embedded watermark image
        """

        # Watermark encrypted
        wat_enc = self.encrypt_decrypt.watermark_image_encryption()

        # This loop runs for all the files presented in the given dirctory
        for file in os.listdir(self.options.inp_dir_path):
            
            # open the image.
            img = Image.open(self.options.inp_dir_path + '/' + file)

            # convert the image to grayscale.
            img = np.asarray(img.convert(mode='L'))

            # get the coefficients of DWT transform
            LL, (LH, HL, HH) = dwt_2d(img, 'haar')

            # creates non-overlapping blocks.
            non_overlapping_blocks = create_non_overlapping_blocks(HL, self.options.dct_block_size)

            # applies dct to all the non-overlapping blocks.
            dct_blocks = apply_2d_dct_all_blocks(non_overlapping_blocks)

            # modifies the dct blocks as per the paper, main embedding.
            new_dct_blocks = update_dct_blocks(dct_blocks, wat_enc, self.options.alpha)

            # perform inverse 2d dct transform on the modified dct blocks.
            idct_blocks = apply_inverse_2d_dct_all_blocks(new_dct_blocks)

            # get the modified LL band.
            iHL = create_image_from_overlapping_blocks(idct_blocks, HL.shape)

            # perform inverse DWT transform.
            embedded_image = idwt_2d(coeffs=(LL, (LH, iHL, HH)))

            # create the directory for saving embedded images.
            if not os.path.exists(self.options.emb_dir_path):
                os.makedirs(self.options.emb_dir_path)

            # Save thq embedded image.
            # plt.imsave(config.embedded_images_path + "test.png", embedded_image, cmap=cm.gray)
            im = Image.fromarray(embedded_image)
            im.convert("L").save(self.options.emb_dir_path + "/" + file)
