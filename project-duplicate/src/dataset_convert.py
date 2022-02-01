from re import I
import PIL.Image as pil_image
import h5py
import numpy as np
import argparse

def conv_train_file(dataset_input, dataset_output):
    high_res_images: list = []
    low_res_images: list = []
    
    with h5py.File(dataset_input, 'r') as hdf:
        for image in hdf['hr']:
            out_img = pil_image.fromarray(image).convert('RGB')
            
            out_img = out_img.resize(((out_img.width // 2) * 2, (out_img.height // 2) * 2))
            high_res_images.append(np.array(out_img.copy().convert('F')))
            
            out_img = out_img.resize((out_img.width // 2, out_img.height // 2))
            low_res_images.append(np.array(out_img.convert('F')))

    with h5py.File(dataset_output, 'w') as hdf:
        hdf.create_dataset('hr', data=np.array(high_res_images))
        hdf.create_dataset('lr', data=np.array(low_res_images))

def conv_test_file(dataset_input, dataset_output):
    high_res_images = {}
    low_res_images = {}

    with h5py.File('./dataset/Set5_x2.h5', 'r') as hdf:
        for index in [str(x) for x in range(5)]:
            image = hdf['hr'][index][:,:]
            
            out_shape = image.shape
            out_img = pil_image.fromarray(image).convert('RGB')
            
            out_img = out_img.resize(((out_img.width // 2) * 2, (out_img.height // 2) * 2))
            high_res_images[index] = np.array(out_img.copy().convert('F')).reshape(out_shape)
            
            out_img = out_img.resize((out_img.width // 2, out_img.height // 2))
            low_res_images[index] = np.array(out_img.convert('F')).reshape((out_shape[0]//2,out_shape[1]//2))
        
    with h5py.File('./output/Set5_x2_converted.h5', 'w') as hdf:
        lr_imgs = hdf.create_group('lr')
        hr_imgs = hdf.create_group('hr')
        for index in [str(x) for x in range(5)]:
            lr_imgs.create_dataset(index, data=np.array(low_res_images[index]))
            hr_imgs.create_dataset(index, data=np.array(high_res_images[index]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset-file', type=str, required=True)
    parser.add_argument('--output-file', type=str, required=True)
    args = parser.parse_args()
    
    is_train_file = False
    
    with h5py.File(args.dataset_file, 'r') as hdf:
        try:
            _ = hdf['hr']['0'][:,:]
        except:
            is_train_file = True
    
    if is_train_file:
        conv_train_file(args.dataset_file, args.output_file)
    else:
        conv_test_file(args.dataset_file, args.output_file) 