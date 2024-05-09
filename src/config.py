"""
Base Configurations class.

"""

import argparse

class BaseOptions():
    """This class defines options used

    It also implements several helper functions such as parsing, printing, and saving the options.
    It also gathers additional options defined if this class is inherited in another class.
    """

    def __init__(self):
        """Init the class."""


    def initialize(self, parser):
        """Define the common options."""

         # Create the parent parser
        parent_parser = argparse.ArgumentParser(add_help=False)  # Disable help for parent parser

        # Add common options
        parent_parser.add_argument('--create_encryption_key', action='store_true', help='if specified, then watermark encryption key will be generated.')
        parent_parser.add_argument('--encryption_key_path', type=str, default='../assets/encryption_key.npy', help='path of the encryption key file.')
        parent_parser.add_argument('--encrypt_watermark', action='store_true', help='if specified, then watermark will be encrypted.')
        parent_parser.add_argument('--logo_name', type=str, default='pi', help='name of the logo to be used for watermarking. options;pi, xut, hourglass, custom')
        parent_parser.add_argument('--custom_logo_path', type=str, default='', help='path of the custom logo to be used for watermarking.')
        parent_parser.add_argument('--dct_block_size', type=tuple, default=(8, 8), help='dct block size, as of now only 8*8 works')
        parent_parser.add_argument('--dwt_level', type=str, default='LL', help='which dwt block to embed the watermark. options;LL, LH, HL, HH')

        # Add subparsers
        subparser = parser.add_subparsers(dest='feature', help='Which Feature to be performed?')

        # Add subparser for watermark embedding
        watermark_embedding = subparser.add_parser('emb', parents=[parent_parser], help='Watermark Embedding - True if watermark embedding will happen.')
        watermark_embedding.add_argument('--emb_inp_dir_path', type=str, required=True, help='path of the images which needs to be watermarked.')
        watermark_embedding.add_argument('--emb_out_dir_path', type=str, required=True, help='path of the images where the watermarked images should be stored.')
        watermark_embedding.add_argument('--alpha', type=int, default=2, help='embedding strength, in the paper it is given between [1 - 2]')

        # Add subparser for watermark extraction
        watermark_extraction = subparser.add_parser('ext', parents=[parent_parser], help='Watermark Extraction - True if watermark extraction will happen.')
        watermark_extraction.add_argument('--ext_inp_dir_path', type=str, required=True, help='path of the images where watermarked images are stored.')
        watermark_extraction.add_argument('--ext_out_dir_path', type=str, required=True, help='path of the images where watermark extracted images should be stored.')

        # Add subparser for similarity check
        similarity_check = subparser.add_parser('check_similarity', help='Similarity check - True if specified, then it will filter out the images that are not similar.')
        similarity_check.add_argument('--similarity_threshold', type=float, default=0.9, help='similarity threshold, if the similarity is less than this threshold, then the image will be discarded.')
        similarity_check.add_argument('--similarity_metric', type=str, default='ssim', help='similarity metric, can be either ssim or mse or sre.')
        similarity_check.add_argument('--similarity_check_path', type=str, required=True, help='path of the folder where similarity should be checked.')
        similarity_check.add_argument('--org_fing_images_path', type=str, required=True, help='path of the images where the original fingerprint images are stored.')
        similarity_check.add_argument('--fil_fing_images_path', type=str, required=True, help='path of the folder where the filtered fingerprint images should be stored.')
        similarity_check.add_argument('--org_wat_images_path', type=str, required=True, help='path of the images where the original watermarked images are stored.')
        similarity_check.add_argument('--fil_wat_images_path', type=str, required=True, help='path of the folder where the filtered watermarked images should be stored.')

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