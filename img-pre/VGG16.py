from ntpath import join
from pickletools import optimize
from xml.etree.ElementInclude import include
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import tensorflow as tf
import numpy as np
import cv2
import os
import keras
from tqdm import tqdm
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



width = 224
num_classes = 24
trainPath = 'dataset_seperate/train/'
testPath = 'dataset_seperate/test/'
trainImg = [trainPath+i for i in os.listdir(trainPath) if os.listdir(os.path.join(trainPath, i))]
testImg = [testPath+i for i in os.listdir(testPath) if os.listdir(os.path.join(testPath, i))]

def img2datasAndlabels(path):
    Rawimgs = []
    labels = []
    c = 0
    for imagePath in (path):
        for item in tqdm(os.listdir(imagePath)):
            file = os.path.join(imagePath, item)
            c+=1
            l = imagePath.split('/')[2]
            if l == 'nRSRnLIO':
                labels.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            elif l == 'nRIOnLSR':
                labels.append([0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            elif l == 'nRLRnLMR':
                labels.append([0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            elif l == 'nRMRnLLR':
                labels.append([0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            elif l == 'nRIRnLSO':
                labels.append([0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            elif l == 'nRSOnLIR':
                labels.append([0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            
            elif l == 'abRSRnLIO':
                labels.append([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            elif l == 'abRIOnLSR':
                labels.append([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            elif l == 'abRLRnLMR':
                labels.append([0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            elif l == 'abRMRnLLR':
                labels.append([0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            elif l == 'abRIRnLSO':
                labels.append([0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
            elif l == 'abRSOnLIR':
                labels.append([0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0])

            elif l == 'nRSRabLIO':
                labels.append([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0])
            elif l == 'nRIOabLSR':
                labels.append([0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0])
            elif l == 'nRLRabLMR':
                labels.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0])
            elif l == 'nRMRabLLR':
                labels.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0])
            elif l == 'nRIRabLSO':
                labels.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])
            elif l == 'nRSOabLIR':
                labels.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0])

            elif l == 'abRSRabLIO':
                labels.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0])
            elif l == 'abRIOabLSR':
                labels.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0])
            elif l == 'abRLRabLMR':
                labels.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0])
            elif l == 'abRMRabLLR':
                labels.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0])
            elif l == 'abRIRabLSO':
                labels.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0])
            elif l == 'abRSOabLIR':
                labels.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
            img = cv2.imread(file, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (width,width))
            Rawimgs.append(img)
    return Rawimgs, labels

x_train, y_train = img2datasAndlabels(trainImg)
x_test, y_test = img2datasAndlabels(testImg)

x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255



print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


SIZE = [224,224]
base_model = tf.keras.applications.VGG16(input_shape = SIZE + [3], include_top = False, weights = 'imagenet')

base_model.trainable = False

base_model.summary()

model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.Conv2D(128, (3,3), activation='relu', input_shape = (width,width,3)),
    tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    tf.keras.layers.Dropout(0.25),
    tf.keras.layers.Dense(16),
    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(num_classes, activation='softmax')
])

model.summary()

model.compile(optimizer = tf.keras.optimizers.Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
batch_size = 32
epochs = 45

history = model.fit(x_train, y_train, batch_size = batch_size, epochs=epochs, validation_data=(x_test, y_test))

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()
# "Loss"
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()

testPath = 'dataset_seperate/test/'

# each of labels
testImg = [testPath + f for f in os.listdir(testPath) if os.listdir(os.path.join(testPath, f))]
rimg = []
true_box = 0
false_box = 0
for imagePath in (testImg):
    for item in (os.listdir(imagePath)):
        #each of file in folder
        file = os.path.join(imagePath, item)
        if item.split('.')[0] != "":
            img = cv2.imread(file , cv2.COLOR_BGR2RGB)
            ori = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img ,(width,width))
            rimg = np.array(img)
            rimg = rimg.astype('float32')
            rimg /= 255
            rimg = np.reshape(rimg ,(1,224,224,3))
            predict = model.predict(rimg)
            label = [
                'nRSRnLIO', 'nRIOnLSR', 'nRLRnLMR', 'nRMRnLLR', 'nRIRnLSO', 'nRSOnLIR',
                'abRSRnLIO', 'abRIOnLSR', 'abRLRnLMR', 'abRMRnLLR', 'abRIRnLSO', 'abRSOnLIR',
                'nRSRabLIO', 'nRIOabLSR', 'nRLRabLMR', 'nRMRabLLR', 'nRIRabLSO', 'nRSOabLIR',
                'abRSRabLIO', 'abRIOabLSR', 'abRLRabLMR', 'abRMRabLLR', 'abRIRabLSO', 'abRSOabLIR'
                ]
            result = label[np.argmax(predict)]
            # print(predict)

            item_final = str(item).split('.')[-3]
            result_final = str(result)
            print('real:'+str(item))
            print('predict:'+str(result))
            if item_final == result_final:
                print('true')
                print('___')
                true_box += 1
            elif item_final != result_final:
                print('false')
                print('___')
                false_box += 1
    print('true box = ' + str(true_box))
    print('false box = ' + str(false_box))
            # print(item_final)
            # print(result)
            # plt.imshow(ori)
            # plt.show()

x_test_plot = model.predict_classes(x_test, batch_size=128, verbose=0)
y_test_plot = np.argmax(y_test, axis=1)
metrics = pd.DataFrame(model.history.history)

print(classification_report(y_test_plot, x_test_plot))

# prediction = model.predict_classes(x_test)
confusion = confusion_matrix(y_test_plot, x_test_plot)
print(confusion)


ax = sns.heatmap(confusion, annot=True, cmap='Blues')


ax.set_title('Confusion Matrix')
ax.set_xlabel('\nPredicted')
ax.set_xlabel('True')

ax.xaxis.set_ticklabels(['nRSRnLIO','nRIOnLSR', 'nRLRnLMR', 'nRMRnLLR', 'nRIRnLSO', 'nRSOnLIR',
                'abRSRnLIO', 'abRIOnLSR', 'abRLRnLMR', 'abRMRnLLR', 'abRIRnLSO', 'abRSOnLIR',
                'nRSRabLIO', 'nRIOabLSR', 'nRLRabLMR', 'nRMRabLLR', 'nRIRabLSO', 'nRSOabLIR',
                'abRSRabLIO', 'abRIOabLSR', 'abRLRabLMR', 'abRMRabLLR', 'abRIRabLSO', 'abRSOabLIR'])

ax.yaxis.set_ticklabels(['nRSRnLIO','nRIOnLSR', 'nRLRnLMR', 'nRMRnLLR', 'nRIRnLSO', 'nRSOnLIR',
                'abRSRnLIO', 'abRIOnLSR', 'abRLRnLMR', 'abRMRnLLR', 'abRIRnLSO', 'abRSOnLIR',
                'nRSRabLIO', 'nRIOabLSR', 'nRLRabLMR', 'nRMRabLLR', 'nRIRabLSO', 'nRSOabLIR',
                'abRSRabLIO', 'abRIOabLSR', 'abRLRabLMR', 'abRMRabLLR', 'abRIRabLSO', 'abRSOabLIR'])
plt.show()



