#!/bin/bash

echo "Starting the script"

# Declare all variables
ROOT_DIR=/home/srinath/Documents/srinath/Master_Thesis/data/model_data/dct_svd_in_dwd/alp_5_HL_xut_2k
ORG_FING_DATA_2K=$ROOT_DIR/org_fing_data_2k
ORG_WAT_DATA_2K=$ROOT_DIR/org_wat_data_2k
WAT_REC_2K=$ROOT_DIR/wat_rec_2k
ORG_FING_DATA_2K_FIL=$ROOT_DIR/org_fing_data_2k_fil
ORG_WAT_DATA_2K_FIL=$ROOT_DIR/org_wat_data_2k_fil
ORG_FING_DATA_2K_FIL_1K=$ROOT_DIR/org_fing_data_2k_fil_1k
ORG_WAT_DATA_2K_FIL_1K=$ROOT_DIR/org_wat_data_2k_fil_1k
AB=$ROOT_DIR/AB
ALPHA=5
SIMILARITY_TR=0.03
SIMILARITY_METRIC=mae


# Activate the conda environment
echo "Activating the dct-svd-in-dwt conda environment"
conda activate dct-svd-in-dwt

# Change the directory to 'dct_svd_in_dwt_watermark' github repo
cd /home/srinath/Documents/git/dct_svd_in_dwt_watermark/src

# Run the python script for embedding watermark
echo "Running Embedding watermark script"
python main.py --emb --alpha=$ALPHA --emb_inp_dir_path=$ORG_FING_DATA_2K --emb_out_dir_path=$ORG_WAT_DATA_2K --dwt_level=HL --is_first_logo

# Run the python script for extracting watermark
echo "Running Extracting watermark script"
python main.py --ext --ext_inp_dir_path=$ORG_WAT_DATA_2K --ext_out_dir_path=$WAT_REC_2K --dwt_level=HL --is_first_logo

# Run the python script for checking similarity
echo "Running Checking similarity script"
python main.py --check_similarity --similarity_check_path $WAT_REC_2K --org_fing_images_path $ORG_FING_DATA_2K --fil_fing_images_path $ORG_FING_DATA_2K_FIL --org_wat_images_path $ORG_WAT_DATA_2K --fil_wat_images_path $ORG_WAT_DATA_2K_FIL --is_first_logo --similarity_threshold $SIMILARITY_TR --similarity_metric $SIMILARITY_METRIC


echo "Creating directories for 1k images"
# create the directories for train, test and val data
# make dirs for finger print images
mkdir -p $ORG_FING_DATA_2K_FIL_1K/train
mkdir -p $ORG_FING_DATA_2K_FIL_1K/test
mkdir -p $ORG_FING_DATA_2K_FIL_1K/val

# make dirs for watermarked images
mkdir -p $ORG_WAT_DATA_2K_FIL_1K/train
mkdir -p $ORG_WAT_DATA_2K_FIL_1K/test
mkdir -p $ORG_WAT_DATA_2K_FIL_1K/val


echo "Copying 1k images from 2k images"
# Copy first 1000 images from the filtered images to train, test and val directories
# copy finger print images
find $ORG_FING_DATA_2K_FIL/ -maxdepth 1 -type f |head -1000|xargs cp -t $ORG_FING_DATA_2K_FIL_1K/train
find $ORG_FING_DATA_2K_FIL_1K/train/ -maxdepth 1 -type f |head -36|xargs cp -t $ORG_FING_DATA_2K_FIL_1K/test
find $ORG_FING_DATA_2K_FIL_1K/train/ -maxdepth 1 -type f |tail -36|xargs cp -t $ORG_FING_DATA_2K_FIL_1K/val

# copy watermarked images
find $ORG_WAT_DATA_2K_FIL/ -maxdepth 1 -type f |head -1000|xargs cp -t $ORG_WAT_DATA_2K_FIL_1K/train
find $ORG_WAT_DATA_2K_FIL_1K/train/ -maxdepth 1 -type f |head -36|xargs cp -t $ORG_WAT_DATA_2K_FIL_1K/test
find $ORG_WAT_DATA_2K_FIL_1K/train/ -maxdepth 1 -type f |tail -36|xargs cp -t $ORG_WAT_DATA_2K_FIL_1K/val


# Change the directory to 'pytorch-CycleGAN-and-pix2pix' github repo
cd /home/srinath/Documents/git/pytorch-CycleGAN-and-pix2pix

# Conda deactivate
conda deactivate

# conda activate the pix2pix2 environment
conda activate pix2pix2

# Run the pix2pix script for combining finger print and watermarked images
echo "Running pix2pix combine script"
python datasets/combine_A_and_B.py --fold_A=$ORG_FING_DATA_2K_FIL_1K --fold_B=$ORG_WAT_DATA_2K_FIL_1K --fold_AB=$AB


# Conda deactivate
conda deactivate

echo "All done"