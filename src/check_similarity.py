import os
from image_similarity_measures.quality_metrics import rmse, ssim, sre
from skimage.metrics import structural_similarity
from skimage.metrics import peak_signal_noise_ratio
from sklearn.metrics import mean_absolute_error
from PIL import Image
import numpy as np
import warnings
from tqdm import tqdm
from watermark_encryption_decryption import Encrypt_Decrypt

class SimilarityCheck:
    def __init__(self, opt):
        warnings.filterwarnings("ignore", category=DeprecationWarning) 
        self.opt = opt
        self.encrypt_decrypt = Encrypt_Decrypt(opt)
        self.greater_metrics = ['ssim', 'sre']
        self.smaller_metrics = ['mae', 'rmse', 'abs']

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
            img1 = np.expand_dims(img1, axis=2)  # expand the image axis to make it 3D
            img2 = np.expand_dims(img2, axis=2)
            return rmse(img1, img2)
        elif metric_name == 'mae':
            return mean_absolute_error(img1, img2)
        elif metric_name == 'sre':
            img1 = np.expand_dims(img1, axis=2)  # expand the image axis to make it 3D
            img2 = np.expand_dims(img2, axis=2)
            return sre(img1, img2)
        elif metric_name == 'abs':
            return np.sum(np.abs(img1 - img2))

    def check_similarity_all_images(self):
        """This function checks the similarity between all the images in two folders.

        :return: None.
        """
        print("Getting the list of images similar")
        self.similarity = {}
        for file in tqdm(os.listdir(self.opt.similarity_check_path)):
            img1 = Image.open(self.opt.similarity_check_path + '/' + file)
            img1 = np.asarray(img1.convert(mode='L'))
            img1 = np.where(img1 > 127, 1, 0)  # convert img1 to binary
            img2 = self.encrypt_decrypt.get_watermark_img()
            self.similarity[file] = self.check_images_similarity(img1, img2, self.opt.similarity_metric)
    
    def copy_similar_images(self):
        """This function copies the similar images to a new folder.

        :return: None.
        """
        print("Copying the similar images to a new folder")
        if not os.path.exists(self.opt.fil_fing_images_path):
            os.makedirs(self.opt.fil_fing_images_path)
        if not os.path.exists(self.opt.fil_wat_images_path):
            os.makedirs(self.opt.fil_wat_images_path)
        print("mean similarity: ", np.mean(list(self.similarity.values())))
        for file in tqdm(self.similarity):
            if self.similarity[file] >= self.opt.similarity_threshold and self.opt.similarity_metric in self.greater_metrics:
                os.system('cp ' + self.opt.org_fing_images_path + '/' + file + ' ' + self.opt.fil_fing_images_path)
                os.system('cp ' + self.opt.org_wat_images_path + '/' + file + ' ' + self.opt.fil_wat_images_path)
            elif self.similarity[file] <= self.opt.similarity_threshold and self.opt.similarity_metric in self.smaller_metrics:
                os.system('cp ' + self.opt.org_fing_images_path + '/' + file + ' ' + self.opt.fil_fing_images_path)
                os.system('cp ' + self.opt.org_wat_images_path + '/' + file + ' ' + self.opt.fil_wat_images_path)