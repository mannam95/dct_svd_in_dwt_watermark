"""
Base Configurations class.

Written by Srinath Mannam
"""

import argparse
from email.policy import default

class BaseOptions():
    """This class defines options used during both training and test time.

    It also implements several helper functions such as parsing, printing, and saving the options.
    It also gathers additional options defined in <modify_commandline_options> functions in both dataset class and model class.
    """

    def __init__(self):
        """Init the class."""


    def initialize(self, parser):
        """Define the common options that are used in both training and test."""

        # Watermark Embedding options
        parser.add_argument('--emb', action='store_true', help='Embedding - True if embedding should happen.')
        parser.add_argument('--emb_inp_dir_path', type=str, default='../assets/images', help='path of the images which needs to be watermarked.')
        parser.add_argument('--emb_out_dir_path', type=str, default='../assets/embedded_images', help='path of the images where the watermarked images should be stored.')
        parser.add_argument('--alpha', type=int, default=2, help='embedding strength, in the paper it is given between [1 - 2]')

        # Watermark Extraction options
        parser.add_argument('--ext', action='store_true', help='Extraction - True if embedding should happen.')
        parser.add_argument('--ext_inp_dir_path', type=str, default='../assets/embedded_images', help='path of the images where watermarked images are stored.')
        parser.add_argument('--ext_out_dir_path', type=str, default='../assets/extracted_images', help='path of the images where watermark extracted images should be stored.')

        # Similarity check options
        parser.add_argument('--check_similarity', action='store_true', help='if specified, then it will filter out the images that are not similar.')
        parser.add_argument('--similarity_threshold', type=float, default=0.9, help='similarity threshold, if the similarity is less than this threshold, then the image will be discarded.')
        parser.add_argument('--similarity_metric', type=str, default='ssim', help='similarity metric, can be either ssim or mse or sre.')
        parser.add_argument('--similarity_check_path', type=str, default='../assets/embedded_images', help='path of the folder where similarity should be checked.')
        parser.add_argument('--org_fing_images_path', type=str, default='', help='path of the images where the original fingerprint images are stored.')
        parser.add_argument('--fil_fing_images_path', type=str, default='', help='path of the folder where the filtered fingerprint images should be stored.')
        parser.add_argument('--org_wat_images_path', type=str, default='', help='path of the images where the original watermarked images are stored.')
        parser.add_argument('--fil_wat_images_path', type=str, default='', help='path of the folder where the filtered watermarked images should be stored.')

        # Common options
        parser.add_argument('--gen_enc_key', action='store_true', help='if specified, then watermark encryption key will be generated.')
        parser.add_argument('--enc_key_path', type=str, default='../assets/encryption_key.npy', help='path of the images which needs to be watermarked.')
        parser.add_argument('--is_enc_watermark', action='store_false', help='if specified, then watermark will not be encrypted.')
        parser.add_argument('--is_first_logo', action='store_false', help='if specified, then first logo will be used.')
        parser.add_argument('--dct_block_size', type=tuple, default=(8, 8), help='dct block size, as of now only 8*8 works')
        parser.add_argument('--dwt_level', type=str, default='LL', help='which dwt block to embed the watermark')

        return parser


    def gather_options(self):
        """Initialize our parser with basic options.
        Modify defalut values if needed with command line arguments.
        """
        parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser = self.initialize(parser)

        # get the basic options
        opt, _ = parser.parse_known_args()

        # save and return the parser
        self.parser = parser
        return parser.parse_args()


    def print_options(self, opt):
        """Print and save options

        It will print both current options and default values(if different).
        """
        message = ''
        message += '----------------- Options ---------------\n'
        for k, v in sorted(vars(opt).items()):
            comment = ''
            default = self.parser.get_default(k)
            if v != default:
                comment = '\t[default: %s]' % str(default)
            message += '{:>25}: {:<30}{}\n'.format(str(k), str(v), comment)
        message += '----------------- End -------------------'
        print(message)


    def parse(self):
        """Parse our options."""
        opt = self.gather_options()

        self.print_options(opt)

        self.opt = opt
        return self.opt
