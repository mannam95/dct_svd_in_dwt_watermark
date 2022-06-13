import numpy as np
import config

def apply_svd(data: np.ndarray):
    """
    This function does svd

    :param data: 2D array with input data.
    :return: Returns the u,s,v matrices.
    """ 
    u, s, v = np.linalg.svd(data, full_matrices=True)
    return (u, s, v)

def modify_singular_values(s1, s2, watermark_encrypted):
    """
    This function modifies the largest singular values

    :param s1: first singular values of split modulation matrix
    :param s2: second singular values of split modulation matrix
    :param watermark_encrypted: encrypted watermark
    :return: Returns the modified singular values
    """ 
    largest_s1_index = list(s1).index(max(list(s1)))
    largest_s2_index = list(s2).index(max(list(s2)))

    maxs1, maxs2 = s1[largest_s1_index], s1[largest_s2_index] # In paper termed as lambda1, theta1 largest singular values.
    mean_e = (maxs1 + maxs2)/2 # In paper termed as E.

    alpha = config.alpha
    new_maxs1, new_maxs2 = None, None

    # This loop runs for 32*32 watermakr image dimensions
    for i, idata in enumerate(watermark_encrypted):
        for j, jdata in enumerate(idata):
            if jdata == 1:
                new_maxs1 = mean_e * alpha
                new_maxs2 = mean_e / alpha
            else:
                new_maxs1 = mean_e / alpha
                new_maxs2 = mean_e * alpha
    
    # Modify the singular values
    s1[largest_s1_index] = new_maxs1
    s2[largest_s2_index] = new_maxs2

    return (s1, s2)