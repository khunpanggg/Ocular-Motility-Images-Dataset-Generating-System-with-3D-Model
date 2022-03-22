import numpy as np
import cv2
import os
from natsort import natsorted

path1 = 'RSR_OVER/'

# path2 = ''
# path3 = ''
# path4 = ''
# path5 = ''
# path6 = ''
# path7 = ''
# path8 = ''
# path9 = ''
# path10 = ''
# path11 = ''
# path12 = ''
# path13 = ''
# path14 = ''
# path15 = ''
# path16 = ''
# path17 = ''
# path18 = ''
# path19 = ''


#create folder
dataset_home_new = 'datasetmergefile_project_RSR_OVER/'
os.makedirs(dataset_home_new, exist_ok=True)


#divide a picture to box
#label 1
box1 = [file for file in natsorted(os.listdir(path1))]

# #label 2
# box2 = [file for file in natsorted(os.listdir(path2))]

# #label 3
# box3 = [file for file in natsorted(os.listdir(path3))]

# #label 4
# box4 = [file for file in natsorted(os.listdir(path4))]

# #label 5
# box5 = [file for file in natsorted(os.listdir(path5))]

# #label 6
# box6 = [file for file in natsorted(os.listdir(path6))]

# #label 7
# box7 = [file for file in natsorted(os.listdir(path7))]

# #label 8
# box8 = [file for file in natsorted(os.listdir(path8))]

# #label 9
# box9 = [file for file in natsorted(os.listdir(path9))]

# #label 10
# box10 = [file for file in natsorted(os.listdir(path10))]

# #label 11
# box11 = [file for file in natsorted(os.listdir(path11))]

# #label 12
# box12 = [file for file in natsorted(os.listdir(path12))]

# #label 13
# box13 = [file for file in natsorted(os.listdir(path13))]

# #label 14
# box14 = [file for file in natsorted(os.listdir(path14))]

# #label 15
# box15 = [file for file in natsorted(os.listdir(path15))]

# #label 16
# box16 = [file for file in natsorted(os.listdir(path16))]

# #label 17
# box17 = [file for file in natsorted(os.listdir(path17))]

# #label 18
# box18 = [file for file in natsorted(os.listdir(path18))]

# #label 19
# box19 = [file for file in natsorted(os.listdir(path19))]


#seperate a picture to position box
#label 1
box1_l1 = [box1[i] for i in range(0, len(box1), 9)]

box2_l1 = [box1[i] for i in range(1, len(box1), 9)]

box3_l1 = [box1[i] for i in range(2, len(box1), 9)]

box4_l1 = [box1[i] for i in range(3, len(box1), 9)]

box5_l1 = [box1[i] for i in range(4, len(box1), 9)]

box6_l1 = [box1[i] for i in range(5, len(box1), 9)]

box7_l1 = [box1[i] for i in range(6, len(box1), 9)]

box8_l1 = [box1[i] for i in range(7, len(box1), 9)]

box9_l1 = [box1[i] for i in range(8, len(box1), 9)]

# #label 2
# box1_l2 = [box2[i] for i in range(0, len(box2), 9)]

# box2_l2 = [box2[i] for i in range(1, len(box2), 9)]

# box3_l2 = [box2[i] for i in range(2, len(box2), 9)]

# box4_l2 = [box2[i] for i in range(3, len(box2), 9)]

# box5_l2 = [box2[i] for i in range(4, len(box2), 9)]

# box6_l2 = [box2[i] for i in range(5, len(box2), 9)]

# box7_l2 = [box2[i] for i in range(6, len(box2), 9)]

# box8_l2 = [box2[i] for i in range(7, len(box2), 9)]

# box9_l2 = [box2[i] for i in range(8, len(box2), 9)]

# #label 3
# box1_l3 = [box3[i] for i in range(0, len(box3), 9)]

# box2_l3 = [box3[i] for i in range(1, len(box3), 9)]

# box3_l3 = [box3[i] for i in range(2, len(box3), 9)]

# box4_l3 = [box3[i] for i in range(3, len(box3), 9)]

# box5_l3 = [box3[i] for i in range(4, len(box3), 9)]

# box6_l3 = [box3[i] for i in range(5, len(box3), 9)]

# box7_l3 = [box3[i] for i in range(6, len(box3), 9)]

# box8_l3 = [box3[i] for i in range(7, len(box3), 9)]

# box9_l3 = [box3[i] for i in range(8, len(box3), 9)]

# #label 4
# box1_l4 = [box4[i] for i in range(0, len(box4), 9)]

# box2_l4 = [box4[i] for i in range(1, len(box4), 9)]

# box3_l4 = [box4[i] for i in range(2, len(box4), 9)]

# box4_l4 = [box4[i] for i in range(3, len(box4), 9)]

# box5_l4 = [box4[i] for i in range(4, len(box4), 9)]

# box6_l4 = [box4[i] for i in range(5, len(box4), 9)]

# box7_l4 = [box4[i] for i in range(6, len(box4), 9)]

# box8_l4 = [box4[i] for i in range(7, len(box4), 9)]

# box9_l4 = [box4[i] for i in range(8, len(box4), 9)]

# #label 5
# box1_l5 = [box5[i] for i in range(0, len(box5), 9)]

# box2_l5 = [box5[i] for i in range(1, len(box5), 9)]

# box3_l5 = [box5[i] for i in range(2, len(box5), 9)]

# box4_l5 = [box5[i] for i in range(3, len(box5), 9)]

# box5_l5 = [box5[i] for i in range(4, len(box5), 9)]

# box6_l5 = [box5[i] for i in range(5, len(box5), 9)]

# box7_l5 = [box5[i] for i in range(6, len(box5), 9)]

# box8_l5 = [box5[i] for i in range(7, len(box5), 9)]

# box9_l5 = [box5[i] for i in range(8, len(box5), 9)]

# #label 6
# box1_l6 = [box6[i] for i in range(0, len(box6), 9)]

# box2_l6 = [box6[i] for i in range(1, len(box6), 9)]

# box3_l6 = [box6[i] for i in range(2, len(box6), 9)]

# box4_l6 = [box6[i] for i in range(3, len(box6), 9)]

# box5_l6 = [box6[i] for i in range(4, len(box6), 9)]

# box6_l6 = [box6[i] for i in range(5, len(box6), 9)]

# box7_l6 = [box6[i] for i in range(6, len(box6), 9)]

# box8_l6 = [box6[i] for i in range(7, len(box6), 9)]

# box9_l6 = [box6[i] for i in range(8, len(box6), 9)]

# #label 7
# box1_l7 = [box7[i] for i in range(0, len(box7), 9)]

# box2_l7 = [box7[i] for i in range(1, len(box7), 9)]

# box3_l7 = [box7[i] for i in range(2, len(box7), 9)]

# box4_l7 = [box7[i] for i in range(3, len(box7), 9)]

# box5_l7 = [box7[i] for i in range(4, len(box7), 9)]

# box6_l7 = [box7[i] for i in range(5, len(box7), 9)]

# box7_l7 = [box7[i] for i in range(6, len(box7), 9)]

# box8_l7 = [box7[i] for i in range(7, len(box7), 9)]

# box9_l7 = [box7[i] for i in range(8, len(box7), 9)]

# #label 8
# box1_l8 = [box8[i] for i in range(0, len(box8), 9)]

# box2_l8 = [box8[i] for i in range(1, len(box8), 9)]

# box3_l8 = [box8[i] for i in range(2, len(box8), 9)]

# box4_l8 = [box8[i] for i in range(3, len(box8), 9)]

# box5_l8 = [box8[i] for i in range(4, len(box8), 9)]

# box6_l8 = [box8[i] for i in range(5, len(box8), 9)]

# box7_l8 = [box8[i] for i in range(6, len(box8), 9)]

# box8_l8 = [box8[i] for i in range(7, len(box8), 9)]

# box9_l8 = [box8[i] for i in range(8, len(box8), 9)]

# #label 9
# box1_l9 = [box9[i] for i in range(0, len(box9), 9)]

# box2_l9 = [box9[i] for i in range(1, len(box9), 9)]

# box3_l9 = [box9[i] for i in range(2, len(box9), 9)]

# box4_l9 = [box9[i] for i in range(3, len(box9), 9)]

# box5_l9 = [box9[i] for i in range(4, len(box9), 9)]

# box6_l9 = [box9[i] for i in range(5, len(box9), 9)]

# box7_l9 = [box9[i] for i in range(6, len(box9), 9)]

# box8_l9 = [box9[i] for i in range(7, len(box9), 9)]

# box9_l9 = [box9[i] for i in range(8, len(box9), 9)]

# #label 10
# box1_l10 = [box10[i] for i in range(0, len(box10), 9)]

# box2_l10 = [box10[i] for i in range(1, len(box10), 9)]

# box3_l10 = [box10[i] for i in range(2, len(box10), 9)]

# box4_l10 = [box10[i] for i in range(3, len(box10), 9)]

# box5_l10 = [box10[i] for i in range(4, len(box10), 9)]

# box6_l10 = [box10[i] for i in range(5, len(box10), 9)]

# box7_l10 = [box10[i] for i in range(6, len(box10), 9)]

# box8_l10 = [box10[i] for i in range(7, len(box10), 9)]

# box9_l10 = [box10[i] for i in range(8, len(box10), 9)]

# #label 11
# box1_l11 = [box11[i] for i in range(0, len(box11), 9)]

# box2_l11 = [box11[i] for i in range(1, len(box11), 9)]

# box3_l11 = [box11[i] for i in range(2, len(box11), 9)]

# box4_l11 = [box11[i] for i in range(3, len(box11), 9)]

# box5_l11 = [box11[i] for i in range(4, len(box11), 9)]

# box6_l11 = [box11[i] for i in range(5, len(box11), 9)]

# box7_l11 = [box11[i] for i in range(6, len(box11), 9)]

# box8_l11 = [box11[i] for i in range(7, len(box11), 9)]

# box9_l11 = [box11[i] for i in range(8, len(box11), 9)]

# #label 12
# box1_l12 = [box12[i] for i in range(0, len(box12), 9)]

# box2_l12 = [box12[i] for i in range(1, len(box12), 9)]

# box3_l12 = [box12[i] for i in range(2, len(box12), 9)]

# box4_l12 = [box12[i] for i in range(3, len(box12), 9)]

# box5_l12 = [box12[i] for i in range(4, len(box12), 9)]

# box6_l12 = [box12[i] for i in range(5, len(box12), 9)]

# box7_l12 = [box12[i] for i in range(6, len(box12), 9)]

# box8_l12 = [box12[i] for i in range(7, len(box12), 9)]

# box9_l12 = [box12[i] for i in range(8, len(box12), 9)]

# #label 13
# box1_l13 = [box13[i] for i in range(0, len(box13), 9)]

# box2_l13 = [box13[i] for i in range(1, len(box13), 9)]

# box3_l13 = [box13[i] for i in range(2, len(box13), 9)]

# box4_l13 = [box13[i] for i in range(3, len(box13), 9)]

# box5_l13 = [box13[i] for i in range(4, len(box13), 9)]

# box6_l13 = [box13[i] for i in range(5, len(box13), 9)]

# box7_l13 = [box13[i] for i in range(6, len(box13), 9)]

# box8_l13 = [box13[i] for i in range(7, len(box13), 9)]

# box9_l13 = [box13[i] for i in range(8, len(box13), 9)]

# #label 14
# box1_l14 = [box14[i] for i in range(0, len(box14), 9)]

# box2_l14 = [box14[i] for i in range(1, len(box14), 9)]

# box3_l14 = [box14[i] for i in range(2, len(box14), 9)]

# box4_l14 = [box14[i] for i in range(3, len(box14), 9)]

# box5_l14 = [box14[i] for i in range(4, len(box14), 9)]

# box6_l14 = [box14[i] for i in range(5, len(box14), 9)]

# box7_l14 = [box14[i] for i in range(6, len(box14), 9)]

# box8_l14 = [box14[i] for i in range(7, len(box14), 9)]

# box9_l14 = [box14[i] for i in range(8, len(box14), 9)]

# #label 15
# box1_l15 = [box15[i] for i in range(0, len(box15), 9)]

# box2_l15 = [box15[i] for i in range(1, len(box15), 9)]

# box3_l15 = [box15[i] for i in range(2, len(box15), 9)]

# box4_l15 = [box15[i] for i in range(3, len(box15), 9)]

# box5_l15 = [box15[i] for i in range(4, len(box15), 9)]

# box6_l15 = [box15[i] for i in range(5, len(box15), 9)]

# box7_l15 = [box15[i] for i in range(6, len(box15), 9)]

# box8_l15 = [box15[i] for i in range(7, len(box15), 9)]

# box9_l15 = [box15[i] for i in range(8, len(box15), 9)]

# #label 16
# box1_l16 = [box16[i] for i in range(0, len(box16), 9)]

# box2_l16 = [box16[i] for i in range(1, len(box16), 9)]

# box3_l16 = [box16[i] for i in range(2, len(box16), 9)]

# box4_l16 = [box16[i] for i in range(3, len(box16), 9)]

# box5_l16 = [box16[i] for i in range(4, len(box16), 9)]

# box6_l16 = [box16[i] for i in range(5, len(box16), 9)]

# box7_l16 = [box16[i] for i in range(6, len(box16), 9)]

# box8_l16 = [box16[i] for i in range(7, len(box16), 9)]

# box9_l16 = [box16[i] for i in range(8, len(box16), 9)]

# #label 17
# box1_l17 = [box17[i] for i in range(0, len(box17), 9)]

# box2_l17 = [box17[i] for i in range(1, len(box17), 9)]

# box3_l17 = [box17[i] for i in range(2, len(box17), 9)]

# box4_l17 = [box17[i] for i in range(3, len(box17), 9)]

# box5_l17 = [box17[i] for i in range(4, len(box17), 9)]

# box6_l17 = [box17[i] for i in range(5, len(box17), 9)]

# box7_l17 = [box17[i] for i in range(6, len(box17), 9)]

# box8_l17 = [box17[i] for i in range(7, len(box17), 9)]

# box9_l17 = [box17[i] for i in range(8, len(box17), 9)]

# #label 18
# box1_l18 = [box18[i] for i in range(0, len(box18), 9)]

# box2_l18 = [box18[i] for i in range(1, len(box18), 9)]

# box3_l18 = [box18[i] for i in range(2, len(box18), 9)]

# box4_l18 = [box18[i] for i in range(3, len(box18), 9)]

# box5_l18 = [box18[i] for i in range(4, len(box18), 9)]

# box6_l18 = [box18[i] for i in range(5, len(box18), 9)]

# box7_l18 = [box18[i] for i in range(6, len(box18), 9)]

# box8_l18 = [box18[i] for i in range(7, len(box18), 9)]

# box9_l18 = [box18[i] for i in range(8, len(box18), 9)]

# #label 19
# box1_l19 = [box19[i] for i in range(0, len(box19), 9)]

# box2_l19 = [box19[i] for i in range(1, len(box19), 9)]

# box3_l19 = [box19[i] for i in range(2, len(box19), 9)]

# box4_l19 = [box19[i] for i in range(3, len(box19), 9)]

# box5_l19 = [box19[i] for i in range(4, len(box19), 9)]

# box6_l19 = [box19[i] for i in range(5, len(box19), 9)]

# box7_l19 = [box19[i] for i in range(6, len(box19), 9)]

# box8_l19 = [box19[i] for i in range(7, len(box19), 9)]

# box9_l19 = [box19[i] for i in range(8, len(box19), 9)]


print(box1)
print(box1_l1)
print(box2_l1)
print(box3_l1)
print(box4_l1)
print(box5_l1)
print(box6_l1)
print(box7_l1)
print(box8_l1)
print(box9_l1)


#packing image
#label1(normal)
for n in range(len(box1_l1)):
    img1 = cv2.imread(path1+box1_l1[n])
    img2 = cv2.imread(path1+box2_l1[n])
    img3 = cv2.imread(path1+box3_l1[n])
    img4 = cv2.imread(path1+box4_l1[n])
    img5 = cv2.imread(path1+box5_l1[n])
    img6 = cv2.imread(path1+box6_l1[n])
    img7 = cv2.imread(path1+box7_l1[n])
    img8 = cv2.imread(path1+box8_l1[n])
    img9 = cv2.imread(path1+box9_l1[n])

    row1 = np.hstack((img1, img2, img3))
    row2 = np.hstack((img4, img5, img6))
    row3 = np.hstack((img7, img8, img9))

    ver = np.vstack((row1, row2, row3))
    ver = cv2.resize(ver, (1280, 720))
    cv2.imwrite(dataset_home_new + 'abRSR' + str(n+1) + '.jpg', ver)
    # cv2.imshow('ver', ver)
    # cv2.waitKey(0)

# #label2(abRSR)
# for n in range(len(box1_l2)):
#     img1 = cv2.imread(path2+box1_l2[n])
#     img2 = cv2.imread(path2+box2_l2[n])
#     img3 = cv2.imread(path2+box3_l2[n])
#     img4 = cv2.imread(path2+box4_l2[n])
#     img5 = cv2.imread(path2+box5_l2[n])
#     img6 = cv2.imread(path2+box6_l2[n])
#     img7 = cv2.imread(path2+box7_l2[n])
#     img8 = cv2.imread(path2+box8_l2[n])
#     img9 = cv2.imread(path2+box9_l2[n])

#     row1 = np.hstack((img1, img2, img3))
#     row2 = np.hstack((img4, img5, img6))
#     row3 = np.hstack((img7, img8, img9))

#     ver = np.vstack((row1, row2, row3))
#     ver = cv2.resize(ver, (640, 360))
#     cv2.imwrite(dataset_home_new + 'abRSR.' + str(n+1) + '.jpg', ver)
#     # cv2.imshow('ver', ver)
#     # cv2.waitKey(0)

# #label3(abLSR)
# for n in range(len(box1_l3)):
#     img1 = cv2.imread(path3+box1_l3[n])
#     img2 = cv2.imread(path3+box2_l3[n])
#     img3 = cv2.imread(path3+box3_l3[n])
#     img4 = cv2.imread(path3+box4_l3[n])
#     img5 = cv2.imread(path3+box5_l3[n])
#     img6 = cv2.imread(path3+box6_l3[n])
#     img7 = cv2.imread(path3+box7_l3[n])
#     img8 = cv2.imread(path3+box8_l3[n])
#     img9 = cv2.imread(path3+box9_l3[n])

#     row1 = np.hstack((img1, img2, img3))
#     row2 = np.hstack((img4, img5, img6))
#     row3 = np.hstack((img7, img8, img9))

#     ver = np.vstack((row1, row2, row3))
#     ver = cv2.resize(ver, (640, 360))
#     cv2.imwrite(dataset_home_new + 'abLSR.' + str(n+1) + '.jpg', ver)
#     # cv2.imshow('ver', ver)
#     # cv2.waitKey(0)

# #label4(abSR)
# for n in range(len(box1_l4)):
#     img1 = cv2.imread(path4+box1_l4[n])
#     img2 = cv2.imread(path4+box2_l4[n])
#     img3 = cv2.imread(path4+box3_l4[n])
#     img4 = cv2.imread(path4+box4_l4[n])
#     img5 = cv2.imread(path4+box5_l4[n])
#     img6 = cv2.imread(path4+box6_l4[n])
#     img7 = cv2.imread(path4+box7_l4[n])
#     img8 = cv2.imread(path4+box8_l4[n])
#     img9 = cv2.imread(path4+box9_l4[n])

#     row1 = np.hstack((img1, img2, img3))
#     row2 = np.hstack((img4, img5, img6))
#     row3 = np.hstack((img7, img8, img9))

#     ver = np.vstack((row1, row2, row3))
#     ver = cv2.resize(ver, (640, 360))
#     cv2.imwrite(dataset_home_new + 'abSR.' + str(n+1) + '.jpg', ver)
#     # cv2.imshow('ver', ver)
#     # cv2.waitKey(0)

# #label5(abRIO)
# for n in range(len(box1_l5)):
#     img1 = cv2.imread(path5+box1_l5[n])
#     img2 = cv2.imread(path5+box2_l5[n])
#     img3 = cv2.imread(path5+box3_l5[n])
#     img4 = cv2.imread(path5+box4_l5[n])
#     img5 = cv2.imread(path5+box5_l5[n])
#     img6 = cv2.imread(path5+box6_l5[n])
#     img7 = cv2.imread(path5+box7_l5[n])
#     img8 = cv2.imread(path5+box8_l5[n])
#     img9 = cv2.imread(path5+box9_l5[n])

#     row1 = np.hstack((img1, img2, img3))
#     row2 = np.hstack((img4, img5, img6))
#     row3 = np.hstack((img7, img8, img9))

#     ver = np.vstack((row1, row2, row3))
#     ver = cv2.resize(ver, (640, 360))
#     cv2.imwrite(dataset_home_new + 'abRIO.' + str(n+1) + '.jpg', ver)
#     # cv2.imshow('ver', ver)
#     # cv2.waitKey(0)

# #label6(abLIO)
# for n in range(len(box1_l6)):
#     img1 = cv2.imread(path6+box1_l6[n])
#     img2 = cv2.imread(path6+box2_l6[n])
#     img3 = cv2.imread(path6+box3_l6[n])
#     img4 = cv2.imread(path6+box4_l6[n])
#     img5 = cv2.imread(path6+box5_l6[n])
#     img6 = cv2.imread(path6+box6_l6[n])
#     img7 = cv2.imread(path6+box7_l6[n])
#     img8 = cv2.imread(path6+box8_l6[n])
#     img9 = cv2.imread(path6+box9_l6[n])

#     row1 = np.hstack((img1, img2, img3))
#     row2 = np.hstack((img4, img5, img6))
#     row3 = np.hstack((img7, img8, img9))

#     ver = np.vstack((row1, row2, row3))
#     ver = cv2.resize(ver, (640, 360))
#     cv2.imwrite(dataset_home_new + 'abLIO.' + str(n+1) + '.jpg', ver)
#     # cv2.imshow('ver', ver)
#     # cv2.waitKey(0)

# #label7(abIO)
# for n in range(len(box1_l7)):
#     img1 = cv2.imread(path7+box1_l7[n])
#     img2 = cv2.imread(path7+box2_l7[n])
#     img3 = cv2.imread(path7+box3_l7[n])
#     img4 = cv2.imread(path7+box4_l7[n])
#     img5 = cv2.imread(path7+box5_l7[n])
#     img6 = cv2.imread(path7+box6_l7[n])
#     img7 = cv2.imread(path7+box7_l7[n])
#     img8 = cv2.imread(path7+box8_l7[n])
#     img9 = cv2.imread(path7+box9_l7[n])

#     row1 = np.hstack((img1, img2, img3))
#     row2 = np.hstack((img4, img5, img6))
#     row3 = np.hstack((img7, img8, img9))

#     ver = np.vstack((row1, row2, row3))
#     ver = cv2.resize(ver, (640, 360))
#     cv2.imwrite(dataset_home_new + 'abIO.' + str(n+1) + '.jpg', ver)
#     # cv2.imshow('ver', ver)
#     # cv2.waitKey(0)

# #label8(abRLR)
# for n in range(len(box1_l8)):
#     img1 = cv2.imread(path8+box1_l8[n])
#     img2 = cv2.imread(path8+box2_l8[n])
#     img3 = cv2.imread(path8+box3_l8[n])
#     img4 = cv2.imread(path8+box4_l8[n])
#     img5 = cv2.imread(path8+box5_l8[n])
#     img6 = cv2.imread(path8+box6_l8[n])
#     img7 = cv2.imread(path8+box7_l8[n])
#     img8 = cv2.imread(path8+box8_l8[n])
#     img9 = cv2.imread(path8+box9_l8[n])

#     row1 = np.hstack((img1, img2, img3))
#     row2 = np.hstack((img4, img5, img6))
#     row3 = np.hstack((img7, img8, img9))

#     ver = np.vstack((row1, row2, row3))
#     ver = cv2.resize(ver, (640, 360))
#     cv2.imwrite(dataset_home_new + 'abRLR.' + str(n+1) + '.jpg', ver)
#     # cv2.imshow('ver', ver)
#     # cv2.waitKey(0)

# #label9(abLLR)
# for n in range(len(box1_l9)):
#     img1 = cv2.imread(path9+box1_l9[n])
#     img2 = cv2.imread(path9+box2_l9[n])
#     img3 = cv2.imread(path9+box3_l9[n])
#     img4 = cv2.imread(path9+box4_l9[n])
#     img5 = cv2.imread(path9+box5_l9[n])
#     img6 = cv2.imread(path9+box6_l9[n])
#     img7 = cv2.imread(path9+box7_l9[n])
#     img8 = cv2.imread(path9+box8_l9[n])
#     img9 = cv2.imread(path9+box9_l9[n])

#     row1 = np.hstack((img1, img2, img3))
#     row2 = np.hstack((img4, img5, img6))
#     row3 = np.hstack((img7, img8, img9))

#     ver = np.vstack((row1, row2, row3))
#     ver = cv2.resize(ver, (640, 360))
#     cv2.imwrite(dataset_home_new + 'abLLR.' + str(n+1) + '.jpg', ver)
#     # cv2.imshow('ver', ver)
#     # cv2.waitKey(0)

# #label10(abLR)
# for n in range(len(box1_l10)):
#     img1 = cv2.imread(path10+box1_l10[n])
#     img2 = cv2.imread(path10+box2_l10[n])
#     img3 = cv2.imread(path10+box3_l10[n])
#     img4 = cv2.imread(path10+box4_l10[n])
#     img5 = cv2.imread(path10+box5_l10[n])
#     img6 = cv2.imread(path10+box6_l10[n])
#     img7 = cv2.imread(path10+box7_l10[n])
#     img8 = cv2.imread(path10+box8_l10[n])
#     img9 = cv2.imread(path10+box9_l10[n])

#     row1 = np.hstack((img1, img2, img3))
#     row2 = np.hstack((img4, img5, img6))
#     row3 = np.hstack((img7, img8, img9))

#     ver = np.vstack((row1, row2, row3))
#     ver = cv2.resize(ver, (640, 360))
#     cv2.imwrite(dataset_home_new + 'abLR.' + str(n+1) + '.jpg', ver)
#     # cv2.imshow('ver', ver)
#     # cv2.waitKey(0)

# #label11(abRMR)
# for n in range(len(box1_l11)):
#     img1 = cv2.imread(path11+box1_l11[n])
#     img2 = cv2.imread(path11+box2_l11[n])
#     img3 = cv2.imread(path11+box3_l11[n])
#     img4 = cv2.imread(path11+box4_l11[n])
#     img5 = cv2.imread(path11+box5_l11[n])
#     img6 = cv2.imread(path11+box6_l11[n])
#     img7 = cv2.imread(path11+box7_l11[n])
#     img8 = cv2.imread(path11+box8_l11[n])
#     img9 = cv2.imread(path11+box9_l11[n])

#     row1 = np.hstack((img1, img2, img3))
#     row2 = np.hstack((img4, img5, img6))
#     row3 = np.hstack((img7, img8, img9))

#     ver = np.vstack((row1, row2, row3))
#     ver = cv2.resize(ver, (640, 360))
#     cv2.imwrite(dataset_home_new + 'abRMR.' + str(n+1) + '.jpg', ver)
#     # cv2.imshow('ver', ver)
#     # cv2.waitKey(0)

# #label12(abLMR)
# for n in range(len(box1_l12)):
#     img1 = cv2.imread(path12+box1_l12[n])
#     img2 = cv2.imread(path12+box2_l12[n])
#     img3 = cv2.imread(path12+box3_l12[n])
#     img4 = cv2.imread(path12+box4_l12[n])
#     img5 = cv2.imread(path12+box5_l12[n])
#     img6 = cv2.imread(path12+box6_l12[n])
#     img7 = cv2.imread(path12+box7_l12[n])
#     img8 = cv2.imread(path12+box8_l12[n])
#     img9 = cv2.imread(path12+box9_l12[n])

#     row1 = np.hstack((img1, img2, img3))
#     row2 = np.hstack((img4, img5, img6))
#     row3 = np.hstack((img7, img8, img9))

#     ver = np.vstack((row1, row2, row3))
#     ver = cv2.resize(ver, (640, 360))
#     cv2.imwrite(dataset_home_new + 'abLMR.' + str(n+1) + '.jpg', ver)
#     # cv2.imshow('ver', ver)
#     # cv2.waitKey(0)

# #label13(abMR)
# for n in range(len(box1_l13)):
#     img1 = cv2.imread(path13+box1_l13[n])
#     img2 = cv2.imread(path13+box2_l13[n])
#     img3 = cv2.imread(path13+box3_l13[n])
#     img4 = cv2.imread(path13+box4_l13[n])
#     img5 = cv2.imread(path13+box5_l13[n])
#     img6 = cv2.imread(path13+box6_l13[n])
#     img7 = cv2.imread(path13+box7_l13[n])
#     img8 = cv2.imread(path13+box8_l13[n])
#     img9 = cv2.imread(path13+box9_l13[n])

#     row1 = np.hstack((img1, img2, img3))
#     row2 = np.hstack((img4, img5, img6))
#     row3 = np.hstack((img7, img8, img9))

#     ver = np.vstack((row1, row2, row3))
#     ver = cv2.resize(ver, (640, 360))
#     cv2.imwrite(dataset_home_new + 'abMR.' + str(n+1) + '.jpg', ver)
#     # cv2.imshow('ver', ver)
#     # cv2.waitKey(0)

# #label14(abRIR)
# for n in range(len(box1_l14)):
#     img1 = cv2.imread(path14+box1_l14[n])
#     img2 = cv2.imread(path14+box2_l14[n])
#     img3 = cv2.imread(path14+box3_l14[n])
#     img4 = cv2.imread(path14+box4_l14[n])
#     img5 = cv2.imread(path14+box5_l14[n])
#     img6 = cv2.imread(path14+box6_l14[n])
#     img7 = cv2.imread(path14+box7_l14[n])
#     img8 = cv2.imread(path14+box8_l14[n])
#     img9 = cv2.imread(path14+box9_l14[n])

#     row1 = np.hstack((img1, img2, img3))
#     row2 = np.hstack((img4, img5, img6))
#     row3 = np.hstack((img7, img8, img9))

#     ver = np.vstack((row1, row2, row3))
#     ver = cv2.resize(ver, (640, 360))
#     cv2.imwrite(dataset_home_new + 'abRIR.' + str(n+1) + '.jpg', ver)
#     # cv2.imshow('ver', ver)
#     # cv2.waitKey(0)

# #label15(abLIR)
# for n in range(len(box1_l15)):
#     img1 = cv2.imread(path15+box1_l15[n])
#     img2 = cv2.imread(path15+box2_l15[n])
#     img3 = cv2.imread(path15+box3_l15[n])
#     img4 = cv2.imread(path15+box4_l15[n])
#     img5 = cv2.imread(path15+box5_l15[n])
#     img6 = cv2.imread(path15+box6_l15[n])
#     img7 = cv2.imread(path15+box7_l15[n])
#     img8 = cv2.imread(path15+box8_l15[n])
#     img9 = cv2.imread(path15+box9_l15[n])

#     row1 = np.hstack((img1, img2, img3))
#     row2 = np.hstack((img4, img5, img6))
#     row3 = np.hstack((img7, img8, img9))

#     ver = np.vstack((row1, row2, row3))
#     ver = cv2.resize(ver, (640, 360))
#     cv2.imwrite(dataset_home_new + 'abLIR.' + str(n+1) + '.jpg', ver)
#     # cv2.imshow('ver', ver)
#     # cv2.waitKey(0)

# #label16(abIR)
# for n in range(len(box1_l16)):
#     img1 = cv2.imread(path16+box1_l16[n])
#     img2 = cv2.imread(path16+box2_l16[n])
#     img3 = cv2.imread(path16+box3_l16[n])
#     img4 = cv2.imread(path16+box4_l16[n])
#     img5 = cv2.imread(path16+box5_l16[n])
#     img6 = cv2.imread(path16+box6_l16[n])
#     img7 = cv2.imread(path16+box7_l16[n])
#     img8 = cv2.imread(path16+box8_l16[n])
#     img9 = cv2.imread(path16+box9_l16[n])

#     row1 = np.hstack((img1, img2, img3))
#     row2 = np.hstack((img4, img5, img6))
#     row3 = np.hstack((img7, img8, img9))

#     ver = np.vstack((row1, row2, row3))
#     ver = cv2.resize(ver, (640, 360))
#     cv2.imwrite(dataset_home_new + 'abIR.' + str(n+1) + '.jpg', ver)
#     # cv2.imshow('ver', ver)
#     # cv2.waitKey(0)

# #label17(abRSO)
# for n in range(len(box1_l17)):
#     img1 = cv2.imread(path17+box1_l17[n])
#     img2 = cv2.imread(path17+box2_l17[n])
#     img3 = cv2.imread(path17+box3_l17[n])
#     img4 = cv2.imread(path17+box4_l17[n])
#     img5 = cv2.imread(path17+box5_l17[n])
#     img6 = cv2.imread(path17+box6_l17[n])
#     img7 = cv2.imread(path17+box7_l17[n])
#     img8 = cv2.imread(path17+box8_l17[n])
#     img9 = cv2.imread(path17+box9_l17[n])

#     row1 = np.hstack((img1, img2, img3))
#     row2 = np.hstack((img4, img5, img6))
#     row3 = np.hstack((img7, img8, img9))

#     ver = np.vstack((row1, row2, row3))
#     ver = cv2.resize(ver, (640, 360))
#     cv2.imwrite(dataset_home_new + 'abRSO.' + str(n+1) + '.jpg', ver)
#     # cv2.imshow('ver', ver)
#     # cv2.waitKey(0)

# #label18(abLSO)
# for n in range(len(box1_l18)):
#     img1 = cv2.imread(path18+box1_l18[n])
#     img2 = cv2.imread(path18+box2_l18[n])
#     img3 = cv2.imread(path18+box3_l18[n])
#     img4 = cv2.imread(path18+box4_l18[n])
#     img5 = cv2.imread(path18+box5_l18[n])
#     img6 = cv2.imread(path18+box6_l18[n])
#     img7 = cv2.imread(path18+box7_l18[n])
#     img8 = cv2.imread(path18+box8_l18[n])
#     img9 = cv2.imread(path18+box9_l18[n])

#     row1 = np.hstack((img1, img2, img3))
#     row2 = np.hstack((img4, img5, img6))
#     row3 = np.hstack((img7, img8, img9))

#     ver = np.vstack((row1, row2, row3))
#     ver = cv2.resize(ver, (640, 360))
#     cv2.imwrite(dataset_home_new + 'abLSO.' + str(n+1) + '.jpg', ver)
#     # cv2.imshow('ver', ver)
#     # cv2.waitKey(0)\

# #label19(abSO)
# for n in range(len(box1_l19)):
#     img1 = cv2.imread(path19+box1_l19[n])
#     img2 = cv2.imread(path19+box2_l19[n])
#     img3 = cv2.imread(path19+box3_l19[n])
#     img4 = cv2.imread(path19+box4_l19[n])
#     img5 = cv2.imread(path19+box5_l19[n])
#     img6 = cv2.imread(path19+box6_l19[n])
#     img7 = cv2.imread(path19+box7_l19[n])
#     img8 = cv2.imread(path19+box8_l19[n])
#     img9 = cv2.imread(path19+box9_l19[n])

#     row1 = np.hstack((img1, img2, img3))
#     row2 = np.hstack((img4, img5, img6))
#     row3 = np.hstack((img7, img8, img9))

#     ver = np.vstack((row1, row2, row3))
#     ver = cv2.resize(ver, (640, 360))
#     cv2.imwrite(dataset_home_new + 'abSO.' + str(n+1) + '.jpg', ver)
#     # cv2.imshow('ver', ver)
#     # cv2.waitKey(0)
