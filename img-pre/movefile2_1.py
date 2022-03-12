from os import makedirs
from os import listdir
from shutil import copyfile

path1 = 'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/1/scale_(2)'
path2 = 'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/1/scale_(-2)'
path3 = 'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/1/scale_(4)'
path4 = 'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/1/scale_(-4)'

path5 = 'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/2/scale_(2)'
path6 = 'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/2/scale_(-2)'
path7 = 'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/2/scale_(4)'
path8 = 'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/2/scale_(-4)'

path9 = 'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/3/scale_(1)'
path10 = 'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/3/scale_(-1)'
path11 = 'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/3/scale_(3)'
path12 = 'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/3/scale_(-3)'

path = 'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/normal'


number = 1
dataset_home_new = 'dataset/'
labeldirs = [
    'nRSRnLIO/', 'abRSRnLIO/', 'nRSRabLIO/', 'abRSRabLIO/',
    'nRIOnLSR/', 'abRIOnLSR/', 'nRIOabLSR/', 'abRIOabLSR/',
    'nRLRnLMR/', 'abRLRnLMR/', 'nRLRabLMR/', 'abRLRabLMR/',
    'nRMRnLLR/', 'abRMRnLLR/', 'nRMRabLLR/', 'abRMRabLLR/',
    'nRIRnLSO/', 'abRIRnLSO/', 'nRIRabLSO/', 'abRIRabLSO/',
    'nRSOnLIR/', 'abRSOnLIR/', 'nRSOabLIR', 'abRSOabLIR/'
    ]
    
for labeldir in labeldirs:
    number += 1
    newdir = dataset_home_new + labeldir
    makedirs(newdir, exist_ok=True)
    print(number)
    number += 1
print('create new folder is success.')

for file in listdir(path):
    print('in')
    src = path + '/' + file
    if file.startswith('nRSRnLIO'):
        dst = dataset_home_new + 'nRSRnLIO/' + file
        copyfile(src,dst)
        print('in1')
    elif file.startswith('nRIOnLSR'):
        dst = dataset_home_new + 'nRIOnLSR/' + file
        copyfile(src,dst)
    elif file.startswith('nRLRnLMR'):
        dst = dataset_home_new + 'nRLRnLMR/' + file
        copyfile(src,dst)
    elif file.startswith('nRMRnLLR'):
        dst = dataset_home_new + 'nRMRnLLR/' + file
        copyfile(src,dst)
    elif file.startswith('nRIRnLSO'):
        dst = dataset_home_new + 'nRIRnLSO/' + file
        copyfile(src,dst)
    elif file.startswith('nRSOnLIR'):
        dst = dataset_home_new + 'nRSOnLIR/' + file
        copyfile(src,dst)

for file in listdir(path1):
    src = path1 + '/' + file
    if file.startswith('abRSRnLIO'):
        dst = dataset_home_new + 'abRSRnLIO/' + file
        copyfile(src,dst)
    elif file.startswith('abRIOnLSR'):
        dst = dataset_home_new + 'abRIOnLSR/' + file
        copyfile(src,dst)
    elif file.startswith('abRLRnLMR'):
        dst = dataset_home_new + 'abRLRnLMR/' + file
        copyfile(src,dst)
    elif file.startswith('abRMRnLLR'):
        dst = dataset_home_new + 'abRMRnLLR/' + file
        copyfile(src,dst)
    elif file.startswith('abRIRnLSO'):
        dst = dataset_home_new + 'abRIRnLSO/' + file
        copyfile(src,dst)
    elif file.startswith('abRSOnLIR'):
        dst = dataset_home_new + 'abRSOnLIR/' + file
        copyfile(src,dst)

for file in listdir(path2):
    src = path2 + '/' + file
    if file.startswith('abRSRnLIO'):
        dst = dataset_home_new + 'abRSRnLIO/' + file
        copyfile(src,dst)
    elif file.startswith('abRIOnLSR'):
        dst = dataset_home_new + 'abRIOnLSR/' + file
        copyfile(src,dst)
    elif file.startswith('abRLRnLMR'):
        dst = dataset_home_new + 'abRLRnLMR/' + file
        copyfile(src,dst)
    elif file.startswith('abRMRnLLR'):
        dst = dataset_home_new + 'abRMRnLLR/' + file
        copyfile(src,dst)
    elif file.startswith('abRIRnLSO'):
        dst = dataset_home_new + 'abRIRnLSO/' + file
        copyfile(src,dst)
    elif file.startswith('abRSOnLIR'):
        dst = dataset_home_new + 'abRSOnLIR/' + file
        copyfile(src,dst)

for file in listdir(path3):
    src = path3 + '/' + file
    if file.startswith('abRSRnLIO'):
        dst = dataset_home_new + 'abRSRnLIO/' + file
        copyfile(src,dst)
    elif file.startswith('abRIOnLSR'):
        dst = dataset_home_new + 'abRIOnLSR/' + file
        copyfile(src,dst)
    elif file.startswith('abRLRnLMR'):
        dst = dataset_home_new + 'abRLRnLMR/' + file
        copyfile(src,dst)
    elif file.startswith('abRMRnLLR'):
        dst = dataset_home_new + 'abRMRnLLR/' + file
        copyfile(src,dst)
    elif file.startswith('abRIRnLSO'):
        dst = dataset_home_new + 'abRIRnLSO/' + file
        copyfile(src,dst)
    elif file.startswith('abRSOnLIR'):
        dst = dataset_home_new + 'abRSOnLIR/' + file
        copyfile(src,dst)

for file in listdir(path4):
    src = path4 + '/' + file
    if file.startswith('abRSRnLIO'):
        dst = dataset_home_new + 'abRSRnLIO/' + file
        copyfile(src,dst)
    elif file.startswith('abRIOnLSR'):
        dst = dataset_home_new + 'abRIOnLSR/' + file
        copyfile(src,dst)
    elif file.startswith('abRLRnLMR'):
        dst = dataset_home_new + 'abRLRnLMR/' + file
        copyfile(src,dst)
    elif file.startswith('abRMRnLLR'):
        dst = dataset_home_new + 'abRMRnLLR/' + file
        copyfile(src,dst)
    elif file.startswith('abRIRnLSO'):
        dst = dataset_home_new + 'abRIRnLSO/' + file
        copyfile(src,dst)
    elif file.startswith('abRSOnLIR'):
        dst = dataset_home_new + 'abRSOnLIR/' + file
        copyfile(src,dst)

for file in listdir(path5):
    src = path5 + '/' + file
    if file.startswith('nRSRabLIO'):
        dst = dataset_home_new + 'nRSRabLIO/' + file
        copyfile(src,dst)
    elif file.startswith('nRIOabLSR'):
        dst = dataset_home_new + 'nRIOabLSR/' + file
        copyfile(src,dst)
    elif file.startswith('nRLRabLMR'):
        dst = dataset_home_new + 'nRLRabLMR/' + file
        copyfile(src,dst)
    elif file.startswith('nRMRabLLR'):
        dst = dataset_home_new + 'nRMRabLLR/' + file
        copyfile(src,dst)
    elif file.startswith('nRIRabLSO'):
        dst = dataset_home_new + 'nRIRabLSO/' + file
        copyfile(src,dst)
    elif file.startswith('nRSOabLIR'):
        dst = dataset_home_new + 'nRSOabLIR/' + file
        copyfile(src,dst)

for file in listdir(path6):
    src = path6 + '/' + file
    if file.startswith('nRSRabLIO'):
        dst = dataset_home_new + 'nRSRabLIO/' + file
        copyfile(src,dst)
    elif file.startswith('nRIOabLSR'):
        dst = dataset_home_new + 'nRIOabLSR/' + file
        copyfile(src,dst)
    elif file.startswith('nRLRabLMR'):
        dst = dataset_home_new + 'nRLRabLMR/' + file
        copyfile(src,dst)
    elif file.startswith('nRMRabLLR'):
        dst = dataset_home_new + 'nRMRabLLR/' + file
        copyfile(src,dst)
    elif file.startswith('nRIRabLSO'):
        dst = dataset_home_new + 'nRIRabLSO/' + file
        copyfile(src,dst)
    elif file.startswith('nRSOabLIR'):
        dst = dataset_home_new + 'nRSOabLIR/' + file
        copyfile(src,dst)

for file in listdir(path7):
    src = path7 + '/' + file
    if file.startswith('nRSRabLIO'):
        dst = dataset_home_new + 'nRSRabLIO/' + file
        copyfile(src,dst)
    elif file.startswith('nRIOabLSR'):
        dst = dataset_home_new + 'nRIOabLSR/' + file
        copyfile(src,dst)
    elif file.startswith('nRLRabLMR'):
        dst = dataset_home_new + 'nRLRabLMR/' + file
        copyfile(src,dst)
    elif file.startswith('nRMRabLLR'):
        dst = dataset_home_new + 'nRMRabLLR/' + file
        copyfile(src,dst)
    elif file.startswith('nRIRabLSO'):
        dst = dataset_home_new + 'nRIRabLSO/' + file
        copyfile(src,dst)
    elif file.startswith('nRSOabLIR'):
        dst = dataset_home_new + 'nRSOabLIR/' + file
        copyfile(src,dst)

for file in listdir(path8):
    src = path8 + '/' + file
    if file.startswith('nRSRabLIO'):
        dst = dataset_home_new + 'nRSRabLIO/' + file
        copyfile(src,dst)
    elif file.startswith('nRIOabLSR'):
        dst = dataset_home_new + 'nRIOabLSR/' + file
        copyfile(src,dst)
    elif file.startswith('nRLRabLMR'):
        dst = dataset_home_new + 'nRLRabLMR/' + file
        copyfile(src,dst)
    elif file.startswith('nRMRabLLR'):
        dst = dataset_home_new + 'nRMRabLLR/' + file
        copyfile(src,dst)
    elif file.startswith('nRIRabLSO'):
        dst = dataset_home_new + 'nRIRabLSO/' + file
        copyfile(src,dst)
    elif file.startswith('nRSOabLIR'):
        dst = dataset_home_new + 'nRSOabLIR/' + file
        copyfile(src,dst)

for file in listdir(path9):
    src = path9 + '/' + file
    if file.startswith('abRSRabLIO'):
        dst = dataset_home_new + 'abRSRabLIO/' + file
        copyfile(src,dst)
    elif file.startswith('abRIOabLSR'):
        dst = dataset_home_new + 'abRIOabLSR/' + file
        copyfile(src,dst)
    elif file.startswith('abRLRabLMR'):
        dst = dataset_home_new + 'abRLRabLMR/' + file
        copyfile(src,dst)
    elif file.startswith('abRMRabLLR'):
        dst = dataset_home_new + 'abRMRabLLR/' + file
        copyfile(src,dst)
    elif file.startswith('abRIRabLSO'):
        dst = dataset_home_new + 'abRIRabLSO/' + file
        copyfile(src,dst)
    elif file.startswith('abRSOabLIR'):
        dst = dataset_home_new + 'abRSOabLIR/' + file
        copyfile(src,dst)

for file in listdir(path10):
    src = path10 + '/' + file
    if file.startswith('abRSRabLIO'):
        dst = dataset_home_new + 'abRSRabLIO/' + file
        copyfile(src,dst)
    elif file.startswith('abRIOabLSR'):
        dst = dataset_home_new + 'abRIOabLSR/' + file
        copyfile(src,dst)
    elif file.startswith('abRLRabLMR'):
        dst = dataset_home_new + 'abRLRabLMR/' + file
        copyfile(src,dst)
    elif file.startswith('abRMRabLLR'):
        dst = dataset_home_new + 'abRMRabLLR/' + file
        copyfile(src,dst)
    elif file.startswith('abRIRabLSO'):
        dst = dataset_home_new + 'abRIRabLSO/' + file
        copyfile(src,dst)
    elif file.startswith('abRSOabLIR'):
        dst = dataset_home_new + 'abRSOabLIR/' + file
        copyfile(src,dst)

for file in listdir(path11):
    src = path11 + '/' + file
    if file.startswith('abRSRabLIO'):
        dst = dataset_home_new + 'abRSRabLIO/' + file
        copyfile(src,dst)
    elif file.startswith('abRIOabLSR'):
        dst = dataset_home_new + 'abRIOabLSR/' + file
        copyfile(src,dst)
    elif file.startswith('abRLRabLMR'):
        dst = dataset_home_new + 'abRLRabLMR/' + file
        copyfile(src,dst)
    elif file.startswith('abRMRabLLR'):
        dst = dataset_home_new + 'abRMRabLLR/' + file
        copyfile(src,dst)
    elif file.startswith('abRIRabLSO'):
        dst = dataset_home_new + 'abRIRabLSO/' + file
        copyfile(src,dst)
    elif file.startswith('abRSOabLIR'):
        dst = dataset_home_new + 'abRSOabLIR/' + file
        copyfile(src,dst)

for file in listdir(path12):
    src = path12 + '/' + file
    if file.startswith('abRSRabLIO'):
        dst = dataset_home_new + 'abRSRabLIO/' + file
        copyfile(src,dst)
    elif file.startswith('abRIOabLSR'):
        dst = dataset_home_new + 'abRIOabLSR/' + file
        copyfile(src,dst)
    elif file.startswith('abRLRabLMR'):
        dst = dataset_home_new + 'abRLRabLMR/' + file
        copyfile(src,dst)
    elif file.startswith('abRMRabLLR'):
        dst = dataset_home_new + 'abRMRabLLR/' + file
        copyfile(src,dst)
    elif file.startswith('abRIRabLSO'):
        dst = dataset_home_new + 'abRIRabLSO/' + file
        copyfile(src,dst)
    elif file.startswith('abRSOabLIR'):
        dst = dataset_home_new + 'abRSOabLIR/' + file
        copyfile(src,dst)

