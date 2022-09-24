#!/bin/bash

echo "Starting the script"

# Declare all variables
TEST_DIR=/home/srinath/Documents/srinath/Master_Thesis/data/crossmatch_andrey_512_seeds1-50000/test_set_last_1k/test/.
ROOT_DIR=/home/srinath/Documents/srinath/Master_Thesis/data/test_set/dct_svd_in_dwt
ALPHA=5
DWT_LEVEL=HL
NEW_DIR=$ROOT_DIR/alp_${ALPHA}_${DWT_LEVEL}_xut
ORG_FING_DATA=$NEW_DIR/org_fing_data
ORG_FING_DATA_TEST=$ORG_FING_DATA/test
ORG_WAT_DATA=$NEW_DIR/org_wat_data
ORG_WAT_DATA_TEST=$ORG_WAT_DATA/test
AB=$NEW_DIR/AB


# Create the new directory
mkdir -p $ORG_FING_DATA_TEST

# copy directory to another directory
cp -r $TEST_DIR $ORG_FING_DATA_TEST


# Activate the conda environment
echo "Activating the dct-svd-in-dwt conda environment"
conda activate dct-svd-in-dwt

# Change the directory to 'dct_svd_in_dwt_watermark' github repo
cd /home/srinath/Documents/git/dct_svd_in_dwt_watermark/src

# Run the python script for embedding watermark
echo "Running Embedding watermark script"
python main.py --emb --alpha=$ALPHA --emb_inp_dir_path=$ORG_FING_DATA_TEST --emb_out_dir_path=$ORG_WAT_DATA_TEST --dwt_level=$DWT_LEVEL --is_first_logo


# Change the directory to 'pytorch-CycleGAN-and-pix2pix' github repo
cd /home/srinath/Documents/git/pytorch-CycleGAN-and-pix2pix

# Conda deactivate
conda deactivate

# conda activate the pix2pix2 environment
conda activate pix2pix2

# Run the pix2pix script for combining finger print and watermarked images
echo "Running pix2pix combine script"
python datasets/combine_A_and_B.py --fold_A=$ORG_FING_DATA --fold_B=$ORG_WAT_DATA --fold_AB=$AB

# Conda deactivate
conda deactivate

# Move AB to test
mv $AB/test $NEW_DIR

# Remove all the directories
rm -r $ORG_FING_DATA $ORG_WAT_DATA $AB

echo "All done"