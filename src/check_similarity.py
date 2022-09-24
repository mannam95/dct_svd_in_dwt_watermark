import os
from image_similarity_measures.quality_metrics import rmse, ssim, sre
from skimage.metrics import structural_similarity
from PIL import Image
import numpy as np
import warnings

from watermark_encryption_decryption import Encrypt_Decrypt

class SimilarityCheck:
    def __init__(self, opt):
        warnings.filterwarnings("ignore", category=DeprecationWarning) 
        self.opt = opt
        self.encrypt_decrypt = Encrypt_Decrypt(opt)

    def check_images_similarity(self, img1, img2, metric_name = 'ssim'):
        """This function checks the similarity between two images.

        :param img1: Image 1.
        :param img2: Image 2.
        :param metric_name: The metric name to be used for similarity check.
        :return: Returns the similarity between two images.
        """
        if metric_name == 'ssim':
            return ssim(img1, img2)
        elif metric_name == 'rmse':
            return rmse(img1, img2)
        elif metric_name == 'sre':
            return sre(img1, img2)


    def check_similarity_all_images(self):
        """This function checks the similarity between all the images in two folders.

        :return: None.
        """
        self.similarity = {}
        for file in os.listdir(self.opt.similarity_check_path ):
            img1 = Image.open(self.opt.similarity_check_path + '/' + file)
            img1 = np.asarray(img1.convert(mode='L'))
            img2 = self.encrypt_decrypt.watermark_image_encryption()
            self.similarity[file] = self.check_images_similarity(img1, img2, self.opt.similarity_metric)
    
    def copy_similar_images(self):
        """This function copies the similar images to a new folder.

        :return: None.
        """
        if not os.path.exists(self.opt.fil_fing_images_path):
            os.makedirs(self.opt.fil_fing_images_path)
        if not os.path.exists(self.opt.fil_wat_images_path):
            os.makedirs(self.opt.fil_wat_images_path)
        for file in self.similarity:
            if self.similarity[file] >= self.opt.similarity_threshold:
                os.system('cp ' + self.opt.org_fing_images_path + '/' + file + ' ' + self.opt.fil_fing_images_path)
                os.system('cp ' + self.opt.org_wat_images_path + '/' + file + ' ' + self.opt.fil_wat_images_path)