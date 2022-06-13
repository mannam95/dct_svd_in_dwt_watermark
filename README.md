# Novel Hybrid watermarking approach of DCT and SVD in DWT domain

* This is the un-official implementation of the paper titled [A novel hybrid of DCT and SVD in DWT domain
for robust and invisible blind image watermarking
with optimal embedding strength](https://link.springer.com/article/10.1007/s11042-017-4941-1) by Xiao-bing et al.

## Current status of the implementation(In-Progress)
* DWT - Completed.
* Logistic chaotic key generation - Completed.
* Watermark encryption, decryption - Completed.
* DCT - Completed.
* SVD - Completed.
* Watermarking embedding - Completed.
* Watermarking Extraction - Inverse of the above process - Completed.
* Currently with alpha 2 is performing good - Should check further - In Progress.
* Need to check the code for any mistake - In Progress.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## How to use?

It is good to start with [watermarking_embedding_demo.ipynb](https://github.com/mannam95/watermark_dct_svd_in_dwt/blob/main/src/watermarking_embedding_demo.ipynb) file


## Prerequisites

* How to setup Python environment
* Little signal processing knowledge
    * Discrete Cosine Transform(DCT),
    * Discrete Wavelet Transform(DWT),
    * Discrete Fourier Transform(DFT),
    * Singular Value Decomposition(SVD)
* Watermarking Algorithms.

## Installing

* Clone the repository or download and unzip it.    
* Install the packages mentioned in `environment.yml`
   ```
    #Do this in the project folder console.
    conda env create -f environment.yml
  ```

## Citation
If you use this code for your research, please cite the paper this code is based on: <a href="https://link.springer.com/article/10.1007/s11042-017-4941-1">A novel hybrid of DCT and SVD in DWT domain
for robust and invisible blind image watermarking
with optimal embedding strength</a>:

```
@article{Kang2018,
   title = {A novel hybrid of DCT and SVD in DWT domain for robust and invisible blind image watermarking with optimal embedding strength},
   volume = {77},
   author = {Xiao bing Kang and Fan Zhao and Guang feng Lin and Ya jun Chen},
   doi = {10.1007/S11042-017-4941-1/TABLES/3},
   issn = {15737721},
   issue = {11},
   journal = {Multimedia Tools and Applications},
   keywords = {Discrete cosine transform,Discrete wavelet transform,Least squares curve fitting,Logistic chaotic map,Robust blind watermarking,Singular value decomposition},
   month = {6},
   pages = {13197-13224},
   publisher = {Springer New York LLC},
   url = {https://link.springer.com/article/10.1007/s11042-017-4941-1},
   year = {2018}
```