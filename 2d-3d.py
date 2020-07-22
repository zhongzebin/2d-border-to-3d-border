from math import *
from scipy.optimize import fsolve
import numpy as np
import cv2
l=3.96
w=1.59
h=1.50
x0=609.5
y0=172.9
f=721.5
t_y=2.22
x_4=0
x_2=0
y_1=0
y_3=0
x_1=0
x_3=0
y_4=0
y_2=0
def fun_3(i):
    t_x,t_z,ry=i[0],i[1],i[2]
    return[
        (f*t_x+x0*t_z+(x0*w/2-f*l/2)*cos(ry*pi/180)+(w/2*f+x0*l/2)*sin(ry*pi/180))/(
                t_z+w/2*cos(ry*pi/180)+l/2*sin(ry*pi/180))-x_4,
        (f * t_x + x0 * t_z + (-x0*w/2+f*l/2) * cos(ry * pi / 180) - (w/2*f+x0*l/2) * sin(ry * pi / 180)) / (
                    t_z - w/2 * cos(ry * pi / 180) - l/2 * sin(ry * pi / 180)) - x_2,
        (f*t_y + y0 * t_z + w/2*y0 * cos(ry * pi / 180) - l/2*y0 * sin(ry * pi / 180)) / (
                t_z + w/2 * cos(ry * pi / 180) - l/2 * sin(ry * pi / 180)) - y_1
    ]
def fun_1(i):
    t_x,t_z,ry=i[0],i[1],i[2]
    return[
        (f*t_x+x0*t_z+(x0*w/2-f*l/2)*cos(ry*pi/180)+(w/2*f+x0*l/2)*sin(ry*pi/180))/(
                t_z+w/2*cos(ry*pi/180)+l/2*sin(ry*pi/180))-x_4,
        (f * t_x + x0 * t_z + (-x0*w/2+f*l/2) * cos(ry * pi / 180) - (w/2*f+x0*l/2) * sin(ry * pi / 180)) / (
                    t_z - w/2 * cos(ry * pi / 180) - l/2 * sin(ry * pi / 180)) - x_2,
        (f*t_y + y0 * t_z - w/2*y0 * cos(ry * pi / 180) + l/2*y0 * sin(ry * pi / 180)) / (
                t_z - w/2 * cos(ry * pi / 180) + l/2 * sin(ry * pi / 180)) - y_3
    ]
def fun_2(i):
    t_x,t_z,ry=i[0],i[1],i[2]
    return[
        (f*t_x+x0*t_z+(x0*w/2+f*l/2)*cos(ry*pi/180)+(w/2*f-x0*l/2)*sin(ry*pi/180))/(
                t_z+w/2*cos(ry*pi/180)-l/2*sin(ry*pi/180))-x_1,
        (f * t_x + x0 * t_z + (-x0*w/2-f*l/2) * cos(ry * pi / 180) - (w/2*f-x0*l/2) * sin(ry * pi / 180)) / (
                    t_z - w/2 * cos(ry * pi / 180) + l/2 * sin(ry * pi / 180)) - x_3,
        (f*t_y + y0 * t_z + w/2*y0 * cos(ry * pi / 180) + l/2*y0 * sin(ry * pi / 180)) / (
                t_z + w/2 * cos(ry * pi / 180) + l/2 * sin(ry * pi / 180)) - y_4
    ]
def fun_4(i):
    t_x,t_z,ry=i[0],i[1],i[2]
    return[
        (f*t_x+x0*t_z+(x0*w/2+f*l/2)*cos(ry*pi/180)+(w/2*f-x0*l/2)*sin(ry*pi/180))/(
                t_z+w/2*cos(ry*pi/180)-l/2*sin(ry*pi/180))-x_1,
        (f * t_x + x0 * t_z + (-x0*w/2-f*l/2) * cos(ry * pi / 180) - (w/2*f-x0*l/2) * sin(ry * pi / 180)) / (
                    t_z - w/2 * cos(ry * pi / 180) + l/2 * sin(ry * pi / 180)) - x_3,
        (f*t_y + y0 * t_z - w/2*y0 * cos(ry * pi / 180) - l/2*y0 * sin(ry * pi / 180)) / (
                t_z - w/2 * cos(ry * pi / 180) - l/2 * sin(ry * pi / 180)) - y_2
    ]
def convert_3d(x_min,x_max,y_min,y_max,alpha):
    global x_4,x_2,y_1,y_3,x_1,x_3,y_4,y_2
    print('alpha:' + str(alpha))
    if(alpha>90 and alpha<180):
        x_2=x_min
        y_1=y_max
        x_4=x_max
        r=fsolve(fun_3,np.array([-3,7,90]))
    if(alpha<0 and alpha>-90):
        x_2=x_max
        x_4=x_min
        y_3=y_max
        r = fsolve(fun_1, np.array([-3, 7, -90]))
    if(alpha<-90 and alpha>-180):
        x_3=x_max
        y_4=y_max
        x_1=x_min
        r = fsolve(fun_2, np.array([3, 7, -90]))
    if(alpha>0 and alpha<90):
        y_2=y_max
        x_1=x_max
        x_3=x_min
        r = fsolve(fun_4, np.array([-3, 7, 90]))
    print(r)
    t_x, t_z, ry = r[0], r[1], r[2]
    corner=np.mat([[l/2,l/2,-l/2,-l/2,l/2,l/2,-l/2,-l/2],[0,0,0,0,-h,-h,-h,-h],[w/2,-w/2,-w/2,w/2,w/2,-w/2,-w/2,w/2]])
    R=np.mat([[cos(ry/180*pi),0,sin(ry/180*pi)],[0,1,0],[-sin(ry/180*pi),0,cos(ry/180*pi)]])
    t=np.mat([[t_x],[t_y],[t_z]])
    corner_3d=R*corner+t
    K=np.mat([[f,0,x0],[0,f,y0],[0,0,1]])
    corner_2d=K*corner_3d
    corner_2d[0,:]=corner_2d[0,:]/corner_2d[2,:]
    corner_2d[1,:]=corner_2d[1,:]/corner_2d[2,:]
    print('x4:'+str(corner_2d[0,3]))
    print('y1:'+str(corner_2d[1,0]))
    for i in range(0,3):
        cv2.line(org,(int(corner_2d[0,i]),int(corner_2d[1,i])),(int(corner_2d[0,i+1]),int(corner_2d[1,i+1])),(255,0,0),2)
    cv2.line(org, (int(corner_2d[0, 0]), int(corner_2d[1, 0])),
             (int(corner_2d[0, 3]), int(corner_2d[1, 3])), (255, 0, 0), 2)
    for i in range(4,7):
        cv2.line(org,(int(corner_2d[0,i]),int(corner_2d[1,i])),(int(corner_2d[0,i+1]),int(corner_2d[1,i+1])),(255,0,0),2)
    cv2.line(org, (int(corner_2d[0, 4]), int(corner_2d[1, 4])),
             (int(corner_2d[0, 7]), int(corner_2d[1, 7])), (255, 0, 0), 2)
    for i in range(0,4):
        cv2.line(org,(int(corner_2d[0,i]),int(corner_2d[1,i])),(int(corner_2d[0,i+4]),int(corner_2d[1,i+4])),(255,0,0),2)
org=cv2.imread('004007.png')
file=open('004007.txt')
for line in file:
    data=line.split()
    convert_3d(float(data[4]),float(data[6]),float(data[5]),float(data[7]),float(data[3])/pi*180)
convert_3d(226.86,349.49,206.8,301.64,1.77/pi*180)
#(x_min,y_min),(x_max,y_max)
cv2.imwrite('ans.jpg',org)
cv2.imshow('test',org)
cv2.waitKey(0)