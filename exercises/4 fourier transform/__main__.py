import cv2
import numpy as np
import matplotlib.pyplot as plt

def get_fft_image(image):
    f = np.fft.fft2(image)
    return np.fft.fftshift(f)

def get_magnitude_spectrum(fshift_image):
    return 20 * np.log(np.abs(fshift_image))

def crop_map(map, size, set):
    size = size // 2
    rows, cols = map.shape
    crow, ccol = rows//2, cols//2
    map[crow-size:crow+size+1, ccol-size:ccol+size+1] = set

def get_ifft_image(repr):
    rep = np.fft.ifftshift(repr)
    rep = np.fft.ifft2(rep)
    return np.real(rep)

def get_line(image):
    shifted_fft_image = get_fft_image(image)
    magnitude_spectrum = get_magnitude_spectrum(shifted_fft_image)
    
    cropped_map = shifted_fft_image.copy()
    crop_map(cropped_map, 30, 0)
    edge_detection = get_ifft_image(cropped_map)
    
    mask = np.zeros(image.shape, np.uint8)
    crop_map(mask, 30, 1)
    without_edges = shifted_fft_image.copy() * mask
    without_edges = get_ifft_image(without_edges)
    
    return magnitude_spectrum, edge_detection, without_edges

def plot_line(title, image, ms, ed, we):
    orig_t = [title + ' original', image]
    
    ms_t = [title + ' ms', ms]
    
    ed_t = [title + ' ed', ed]
    
    we_t = [title + ' we', we]
    return orig_t, ms_t, ed_t, we_t
    
line = 1

def plot_from_image(title, image):
    ms, ed, we = get_line(image)
    
    return plot_line(title, image, ms, ed, we)

IMGS = []

def add_image(title, image):
    IMGS.append([title, image])

def get_fft_mean_value(image):
    fft_image = get_fft_image(image)
    spectrum = get_magnitude_spectrum(fft_image)
    return np.mean(spectrum)

def plot_images():
    fig = plt.figure(figsize=(5,5))
    row_count = len(IMGS)
    for j, values in enumerate(IMGS):
        line = plot_from_image(values[0], values[1])
        for i, val in enumerate(line):
            fig.add_subplot(row_count, 4, j * 4 + i + 1)
            plt.title(val[0])
            plt.imshow(val[1])
    
    for title, img in IMGS:
        print(title, 'blur values', get_fft_mean_value(img))
    
    plt.show()

octopus_img = cv2.imread('octopus.jpg',0)
parrot_img = cv2.imread('parrot.jpg',0)
squid_img = cv2.imread('squid.jpg',0)

add_image('Octopus', octopus_img)
add_image('Parrot', parrot_img)
add_image('Squid', squid_img)

plot_images()

# cv2.waitKey()
