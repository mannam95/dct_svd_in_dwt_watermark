from check_similarity import SimilarityCheck
from config import BaseOptions
from perform_embedding import Embed
from perform_extraction import Extract
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 


if __name__ == '__main__':
    opt = BaseOptions().parse()   # get training options

    if opt.emb:
        print("Embedding")
        encrypt = Embed(opt)
        encrypt.integrate_embedding()
    elif opt.ext:
        print("Extracting")
        decrypt = Extract(opt)
        decrypt.integrate_extraction()
    elif opt.check_similarity:
        print("Checking Similarity")
        similarity_check = SimilarityCheck(opt)
        similarity_check.check_similarity_all_images()
        similarity_check.copy_similar_images()