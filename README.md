# Novel Hybrid watermarking approach of DCT and SVD in DWT domain

* This is the un-official implementation of the paper titled [A novel hybrid of DCT and SVD in DWT domain
for robust and invisible blind image watermarking
with optimal embedding strength](https://link.springer.com/article/10.1007/s11042-017-4941-1) by Xiao-bing et al.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## How to use?

- It is good to start with [watermarking_embedding_demo.ipynb](https://github.com/mannam95/watermark_dct_svd_in_dwt/blob/main/src/watermarking_embedding_demo.ipynb) file
- It is good to start with [watermarking_extraction_demo.ipynb](https://github.com/mannam95/watermark_dct_svd_in_dwt/blob/main/src/watermarking_extraction_demo.ipynb) file

## Prerequisites

* How to setup Python environment
* Knowledge signal processing
    * Discrete Cosine Transform(DCT),
    * Discrete Wavelet Transform(DWT),
    * Discrete Fourier Transform(DFT),
    * Singular Value Decomposition(SVD)
* How watermarking algorithms work?.

## Installing

* Clone the repository or download and unzip it.    
* Install the packages mentioned in `environment.yml`
   ```
    #Do this in the project folder console.
    conda env create -f env.yml
  ```

## Usage
 * Watermark Embedding
   - `python main.py --emb --emb_inp_dir_path="images-directory" --emb_out_dir_path="save-directory"`
 * Watermark Extraction
   - `python main.py --ext --ext_inp_dir_path="embeded-images-directory" --ext_out_dir_path="extracted-images-directory"`
 * Apart from the above options, onw can check additional options by running
   - `python main.py --help`
 * There re additional features which have been implemented for my use-case. Those can be ignore if not required.
 

## Code Style Enforcements
  
* Used `flake8` for enforcing code style.
   ```
    #Do this in the project folder console.
    flake8 --ignore E501 .

## Code structure
- Most of the files are self-understood by name.
- Every function has the documentation.
- The documentation is followed by `docstring` pattern

## Pull Request
- You are always welcome to contribute to this repository by sending a [pull request](https://help.github.com/articles/about-pull-requests/).
- Please run `flake8 --ignore E501 .` before you commit the code. 
- Please also add the documentation for the implementations/corrections.

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