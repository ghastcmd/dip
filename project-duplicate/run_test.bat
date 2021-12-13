@echo off
if not exist test mkdir test 

if not exist test/butterfly_GT.bmp \
copy data/butterfly_GT.bmp test

if not exist test/ppt3.bmp \
copy data/ppt3.bmp test

if not exist test/zebra.bmp \
copy data/zebra.bmp test

echo First is the trained, second is the downloaded

echo --------
echo Scale x2
echo butterfly_GT
py src/test.py --weights-file output/x2/best.pth --image-file test/butterfly_GT.bmp --scale 2
py src/test.py --weights-file weights/srcnn_x2.pth --image-file test/butterfly_GT.bmp --scale 2

echo ppt3
py src/test.py --weights-file output/x2/best.pth --image-file test/ppt3.bmp --scale 2
py src/test.py --weights-file weights/srcnn_x2.pth --image-file test/ppt3.bmp --scale 2

echo zebra
py src/test.py --weights-file output/x2/best.pth --image-file test/zebra.bmp --scale 2
py src/test.py --weights-file weights/srcnn_x2.pth --image-file test/zebra.bmp --scale 2

echo --------
echo Scale x3
echo butterfly_GT
py src/test.py --weights-file output/x3/best.pth --image-file test/butterfly_GT.bmp --scale 3
py src/test.py --weights-file weights/srcnn_x3.pth --image-file test/butterfly_GT.bmp --scale 3

echo ppt3
py src/test.py --weights-file output/x3/best.pth --image-file test/ppt3.bmp --scale 3
py src/test.py --weights-file weights/srcnn_x3.pth --image-file test/ppt3.bmp --scale 3

echo zebra
py src/test.py --weights-file output/x3/best.pth --image-file test/zebra.bmp --scale 3
py src/test.py --weights-file weights/srcnn_x3.pth --image-file test/zebra.bmp --scale 3

echo --------
echo Scale x4
echo butterfly_GT
py src/test.py --weights-file output/x4/best.pth --image-file test/butterfly_GT.bmp --scale 4
py src/test.py --weights-file weights/srcnn_x4.pth --image-file test/butterfly_GT.bmp --scale 4

echo ppt3
py src/test.py --weights-file output/x4/best.pth --image-file test/ppt3.bmp --scale 4
py src/test.py --weights-file weights/srcnn_x4.pth --image-file test/ppt3.bmp --scale 4

echo zebra
py src/test.py --weights-file output/x4/best.pth --image-file test/zebra.bmp --scale 4
py src/test.py --weights-file weights/srcnn_x4.pth --image-file test/zebra.bmp --scale 4



