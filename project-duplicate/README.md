# Important warning

The expansion of the project (using the new upscaling method) is **only featured** with the **x2 scale**.

# Project duplicate of a pytorch implementation of SRCNN

The original repository can be found in this [link](https://github.com/yjn870/SRCNN-pytorch).

The original README can be found [here](./ORIGINAL_README.md).

The report for the issues encountered can be found [here](./REPORT.md)

# The extension of the project

The professor from the discipline told us to expand the chosen project with more funcionality, to do so, I chose to implement a layer on the neural network model that can upscale the image, instead of using the bicubic method to upscale; and that, as seen in my research, can increase the performance of the super-resolution for quite a bit.

This branch of the repository have all the necessary tools for using this new upscaling method. All you have to do is convert the train dataset and the eval dataset, and then train the model. To this, you will have to see this [section](To Conver the dataset).

## To convert the dataset

```bash
python src/dataset_convert.py --dataset-file "PATH/dataset.h5" \
               --output-file "PATH/dataset_converted.h5" \
```

## Requirements

- PyTorch 1.0.0
- Numpy 1.15.4
- Pillow 5.4.1
- h5py 2.8.0
- tqdm 4.30.0

Although the requirements are more or less outdated, I ran the scripts with updated libraries and it ran perfectly.

- Python 3.9.9
- PyTorch 1.10.0+cu113
- Numpy 1.21.4
- Pillow 8.4.0
- h5py 3.6.0
- tqdm 4.62.3

There is a requirements.txt script that gets all the required libraries. If you want to install the pytorch separately, there is the `requirements_wo_pytorch.txt`.

If the pytorch installation from the `requirements.txt` do not work, or if you want to install the version for the gpu, visit their [website](https://pytorch.org/get-started/locally/) for a better installation guide.

# Training

These are the links for the datasets training datasets and evals:

| Dataset | Scale | Type | Link |
|---------|-------|------|------|
| 91-image | 2 | Train | [Download](https://www.dropbox.com/s/2hsah93sxgegsry/91-image_x2.h5?dl=0) |
| 91-image | 3 | Train | [Download](https://www.dropbox.com/s/curldmdf11iqakd/91-image_x3.h5?dl=0) |
| 91-image | 4 | Train | [Download](https://www.dropbox.com/s/22afykv4amfxeio/91-image_x4.h5?dl=0) |
| Set5 | 2 | Eval | [Download](https://www.dropbox.com/s/r8qs6tp395hgh8g/Set5_x2.h5?dl=0) |
| Set5 | 3 | Eval | [Download](https://www.dropbox.com/s/58ywjac4te3kbqq/Set5_x3.h5?dl=0) |
| Set5 | 4 | Eval | [Download](https://www.dropbox.com/s/0rz86yn3nnrodlb/Set5_x4.h5?dl=0) |

Example usage for training:

```bash
python src/train.py --train-file "PATH_TO_FOLDER/91-image_x3.h5" \
                --eval-file "PATH_TO_FOLDER/Set5_x3.h5" \
                --outputs-dir "PATH_TO_FOLDER/outputs" \
                --scale 3 \
                --lr 1e-4 \
                --batch-size 16 \
                --num-epochs 400 \
                --num-workers 8 \
                --seed 123
```

# Test/usage

Pre-trained weights can be downloaded from the links below.

| Model | Scale | Link |
|-------|-------|------|
| 9-5-5 | 2 | [Download](https://www.dropbox.com/s/rxluu1y8ptjm4rn/srcnn_x2.pth?dl=0) |
| 9-5-5 | 3 | [Download](https://www.dropbox.com/s/zn4fdobm2kw0c58/srcnn_x3.pth?dl=0) |
| 9-5-5 | 4 | [Download](https://www.dropbox.com/s/pd5b2ketm0oamhj/srcnn_x4.pth?dl=0) |

```bash
python src/test.py --weights-file "PATH_TO_FOLDER/srcnn_x3.pth" \
               --image-file "data/butterfly_GT.bmp" \
               --scale 3
```