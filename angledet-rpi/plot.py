import matplotlib.pyplot as plt
import numpy as np
import time
import os
import subprocess
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
#import scipy.linalg as linalg
import math 

pitch1=[]
roll1=[]
pitch2=[]
roll2=[]
def getangle():

    try:
        f=open('data','r')
    except:
        print("please start angledet process!")
        exit()

    data=f.readlines()
    #print(data)
    # pitch1=[]
    # roll1=[]
    # pitch2=[]
    # roll2=[]
    for d in data:
        pitch,roll=d[2:-1].split(',')
        if d.startswith('1:'):
            pitch1.append(float(pitch))
            roll1.append(float(roll))
        elif d.startswith('2:'):
            pitch2.append(float(pitch))
            roll2.append(float(roll))
#os.system("./angledet")
# def rotate_mat(axis, radian):
#     return linalg.expm(np.cross(np.eye(3), axis / linalg.norm(axis) * radian))
def rotate_mat(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = np.asarray(axis)
    axis = axis / math.sqrt(np.dot(axis, axis))
    a = math.cos(theta / 2.0)
    b, c, d = -axis * math.sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])

def show_position(pitch,roll,fig=2):
    #plt.clf()
    fig = plt.figure(fig,figsize=(5,3))
    plt.clf()
    ax = fig.gca(projection='3d')
    axis_x, axis_y, axis_z = [1,0,0], [0,1,0], [0, 0, 1]#分别是x,y和z轴,也可以自定义旋转轴
    #yaw = 2 #pi/4
    rot_matrix_x = rotate_mat(axis_x, math.radians(roll))
    rot_matrix_y = rotate_mat(axis_y, math.radians(pitch))

    old_coor=np.array([[0,0,-1],[0,0,1]])
    new_coor=np.dot(old_coor, rot_matrix_x)
    new_coor=np.dot(new_coor, rot_matrix_y)
    #print(new_coor)
    x = [new_coor[0][0],new_coor[1][0]]
    y = [new_coor[0][1], new_coor[1][1]]
    z = [new_coor[0][2], new_coor[1][2]]
    ax.plot(x, y, z, color='red',linewidth=10)
    ax.set_ylim(-1.5,1.5)
    ax.set_xlim(-1.5,1.5)
    ax.set_zlim(-1.5,1.5)
    #plt.zlim(-10,10)
    #plt.show()
    plt.pause(1)
#if(os.path.exists('/home/pi/angledet/data')):
#    os.remove('/home/pi/angledet/data')
#subprocess.Popen("/home/pi/angledet/angledet")
#time.sleep(3)
#plt.figure(figsize=(16,16))
#plt.ylim(0,720)
while True:
    pitch1=[]
    roll1=[]
    pitch2=[]
    roll2=[]
    getangle()
#    print(pitch1,roll1,pitch2,roll2)
    #plt.clf()
    show_position(pitch1[-1],roll1[-1],fig=2)
    show_position(pitch2[-1],roll2[-1],fig=3)
    x1=[x for x in range(0,len(pitch1))]
    x2=[x for x in range(0,len(pitch2))]
#    plt.figure(figsize=(16,16))
    #plt.clf()
    plt.figure(1,figsize=(16,3))
    plt.clf()
    plt.suptitle('sensors')
    plt.subplot(121)
    plt.plot(x1,pitch1, color='green', label='sensor1 pitch')
    plt.plot(x1,roll1,color='red', label='sensor1 roll')
    plt.ylim(-190,190)
    plt.legend()
    plt.subplot(122)
    #plt.plot(x1,roll1,color='red', label='sensor1 roll')
    plt.plot(x2,pitch2, color='green', label='sensor2 pitch')
    plt.plot(x2,roll2,color='red', label='sensor2 roll')
    plt.ylim(-190,190)
    plt.legend()
    #plt.subplot(223)
    #plt.plot(x2,pitch2, color='green', label='sensor2 pitch')
    #plt.ylim(-100,100)
    #plt.legend()
    #plt.subplot(224)
    #plt.plot(x2,roll2,color='red', label='sensor2 roll')
    #plt.ylim(-190,190)
    #plt.legend()
    #plt.clf()
    #plt.show()
    #plt.draw()
    #time.sleep(1)
    plt.pause(1)


