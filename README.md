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
    
2. definition of alpha

    ![image](https://github.com/zhongzebin/2d-border-to-3d-border/blob/master/images%20for%20readme/alpha.PNG)
    
3. catagorize according to alpha

    ![image](https://github.com/zhongzebin/2d-border-to-3d-border/blob/master/images%20for%20readme/catagorize.PNG)
    
4. calculate points' coordinates (3 of them)

5. definition of rotation matrix

    ![image](https://github.com/zhongzebin/2d-border-to-3d-border/blob/master/images%20for%20readme/function1.PNG)
    
6. definition of introvert matrix

    ![image](https://github.com/zhongzebin/2d-border-to-3d-border/blob/master/images%20for%20readme/function3.PNG)
    
6. slove rotation and translation equation

    ![image](https://github.com/zhongzebin/2d-border-to-3d-border/blob/master/images%20for%20readme/function2.PNG)
    
    I suppose the length of a car is 3.96m, the width is 1.59m and the height is 1.5m. Thus, I can calculate the x_w, x_y and x_z which are points in the world coordinates. Since the camera is 
