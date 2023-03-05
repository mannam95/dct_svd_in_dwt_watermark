#!/bin/bash

echo "Starting the script"



# Declare all variables
# path where the original images are stored
TRAIN_DIR=/home/yourpath

# path where the watermarked images are stored
ROOT_DIR=/home/yourpath

WAT_TRAIN_DIR=$ROOT_DIR/wm_data/train
WAT_RC_TRAIN_DIR=$ROOT_DIR/wm_rc_data/train
FIL_FPS_TRAIN_DATA_DIR=$ROOT_DIR/fil_fps_data/train
FIL_WM_TRAIN_DATA_DIR=$ROOT_DIR/fil_wm_data/train


ALPHA=10
SIMILARITY_TR=0.03
SIMILARITY_METRIC=mae
LEVEL=LL
LOGO=pi


# Activate the conda environment
echo "Activating the dct-svd-in-dwt conda environment"
source /home/srinath/miniconda3/etc/profile.d/conda.sh
conda activate dct-svd-in-dwt

# Change the directory to 'dct_svd_in_dwt_watermark' github repo
cd /home/srinath/Documents/git/dct_svd_in_dwt_watermark/src

# Run the python script for embedding watermark
echo "Running Embedding watermark script"
python main.py --emb --alpha=$ALPHA --emb_inp_dir_path=$TRAIN_DIR --emb_out_dir_path=$WAT_TRAIN_DIR --dwt_level=$LEVEL --logo_name=$LOGO


# Run the python script for extracting watermark
echo "Running Extracting watermark script"
python main.py --ext --ext_inp_dir_path=$WAT_TRAIN_DIR --ext_out_dir_path=$WAT_RC_TRAIN_DIR --dwt_level=$LEVEL --logo_name=$LOGO


# Run the python script for checking similarity
echo "Running Checking similarity script"
python main.py --check_similarity --similarity_check_path $WAT_RC_TRAIN_DIR --org_fing_images_path $TRAIN_DIR --fil_fing_images_path $FIL_FPS_TRAIN_DATA_DIR --org_wat_images_path $WAT_TRAIN_DIR --fil_wat_images_path $FIL_WM_TRAIN_DATA_DIR --similarity_threshold $SIMILARITY_TR --similarity_metric $SIMILARITY_METRIC --logo_name=$LOGO


echo "All done"