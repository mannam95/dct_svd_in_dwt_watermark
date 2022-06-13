# Set this to true if there is no encryption key
generate_enc_key = False

# Path where the encryption key is stored
global_enc_key_path = '../assets/encryption_key.npy'

# give the path of the images which needs to be watermarked
train_images_path = "../assets/images/"

# give the path of the images which needs to be watermarked
embedded_images_path = "../assets/embedded_images/"

# give the path of the images which needs to be watermarked
extracted_images_path = "../assets/extracted_images/"

# specify the dct block size
dct_block_size = (8, 8)

# specify the alpha parameter
# embedding strength, in the paper it is given as [1 - 2]
alpha = 5