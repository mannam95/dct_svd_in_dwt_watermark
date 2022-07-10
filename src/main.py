from config import BaseOptions
from perform_embedding import Embed
from perform_extraction import Extract


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
