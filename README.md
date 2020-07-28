# 2d-border-to-3d-border
Abstract: convert the 2d border of cars to 3d border in an image (knowing the alpha angle of the detected vehicle already)

Envirnoment: Windows 10, Pycharm 2019, Python 3.7, OpenCV 3.4.1, Numpy 1.16, Scipy 1.4

How to configure the environment?

1. install libs in python

    Use the command pip install xxx to install the libs in python

How to run this project?

1. run 2d-3d.py

Steps:

1. read image and data file

    Read image from 004007.png and data file from 004007.txt
    
    The 5th column is x_min, 7th column is x_max, 6th column is y_min, 8th column is y_max, 4th column is alpha angle
