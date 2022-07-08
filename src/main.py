import argparse
import sys
from perform_embedding import integrate_embedding
from perform_extraction import integrate_extraction

parser = argparse.ArgumentParser()

parser.add_argument('--emb', help='Embedding - True or False', action=argparse.BooleanOptionalAction)
parser.add_argument('--ext', help='Extraction - True or False', action=argparse.BooleanOptionalAction)
parser.set_defaults(embedding=False)
parser.set_defaults(extraction=False)

args = parser.parse_args()

if len(sys.argv) <= 1:
    print("No arguments supplied!")
    print("Please check by running 'python main.py -h'")
    exit(1)


if __name__ == '__main__':
    if args.emb:
        print("Embedding")
        integrate_embedding()
    elif args.ext:
        print("Extracting")
        integrate_extraction()
