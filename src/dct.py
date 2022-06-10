import scipy.fftpack
# import scipy

# Refer https://docs.scipy.org/doc/scipy/reference/generated/scipy.fftpack.dct.html
# Refer https://inst.eecs.berkeley.edu/~ee123/sp16/Sections/JPEG_DCT_Demo.html


def dct_2d(data):
    """
    This function does 2D Discrete Cosine Transform(DCT).

    :param data: 2D array with input data.
    :return: Return the Discrete Cosine Transform.
    """ 
    return scipy.fftpack.dct( scipy.fftpack.dct( data, axis=0, norm='ortho' ), axis=1, norm='ortho' )

def idct_2d(data):
    """
    This function does 2D inverse Discrete Cosine Transform(DCT).

    :param data: 2D array with dct coefficient matrix.
    :return: Return the original data by performing inverse Discrete Cosine Transform.
    """ 
    return scipy.fftpack.idct( scipy.fftpack.idct( data, axis=0 , norm='ortho'), axis=1 , norm='ortho')