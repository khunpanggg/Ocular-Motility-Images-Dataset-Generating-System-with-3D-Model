from os import rename, listdir
from natsort import natsorted

folderPathNormal = r'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/normal'
folderPathAbnormal1 = r'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/1/scale_(2)'
folderPathAbnormal2 = r'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/1/scale_(-2)'
folderPathAbnormal3 = r'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/1/scale_(4)'
folderPathAbnormal4 = r'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/1/scale_(-4)'
folderPathAbnormal5 = r'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/2/scale_(2)'
folderPathAbnormal6 = r'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/2/scale_(-2)'
folderPathAbnormal7 = r'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/2/scale_(4)'
folderPathAbnormal8 = r'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/2/scale_(-4)'
folderPathAbnormal9 = r'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/3/scale_(1)'
folderPathAbnormal10 = r'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/3/scale_(-1)'
folderPathAbnormal11 = r'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/3/scale_(3)'
folderPathAbnormal12 = r'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/image/abnormal/3/scale_(-3)'

numberofnRSRnLIO = 1
numberofabRSRnLIO = 1
numberofnRSRabLIO = 1
numberofabRSRabLIO = 1

numberofnRIOnLSR = 1
numberofabRIOnLSR = 1
numberofnRIOabLSR = 1
numberofabRIOabLSR = 1

numberofnRLRnLMR = 1
numberofabRLRnLMR = 1
numberofnRLRabLMR = 1
numberofabRLRabLMR = 1

numberofnRMRnLLR = 1
numberofabRMRnLLR = 1
numberofnRMRabLLR = 1
numberofabRMRabLLR = 1

numberofnRIRnLSO = 1
numberofabRIRnLSO = 1
numberofnRIRabLSO = 1
numberofabRIRabLSO = 1

numberofnRSOnLIR = 1
numberofabRSOnLIR = 1
numberofnRSOabLIR = 1
numberofabRSOabLIR = 1


fileNumber = 1




for filename in natsorted(listdir(folderPathAbnormal1)):
    # print(filename)
    if 1 <= fileNumber < 7:
        print(fileNumber)
        print(folderPathAbnormal1 + '/' + 'abRSRnLIO' + '.' + str(numberofabRSRnLIO) + '.jpg')
        print(folderPathAbnormal1 + '/' + filename)
        rename(folderPathAbnormal1 + '\\' + filename,folderPathAbnormal1 + '\\' + 'abRSRnLIO' + '.' + str(numberofabRSRnLIO) + '.jpg')
        numberofabRSRnLIO += 1
        fileNumber += 1
        print(fileNumber)
        print('__')
    elif 7 <= fileNumber < 13:
        print(fileNumber)
        print((folderPathAbnormal1 + '/' + 'abRIOnLSR' + '.' + str(numberofabRIOnLSR) + '.jpg'))
        print(folderPathAbnormal1 + '/' + filename)
        rename(folderPathAbnormal1 + '\\' + filename, folderPathAbnormal1 + '\\' + 'abRIOnLSR' + '.' + str(numberofabRIOnLSR) + '.jpg')
        numberofabRIOnLSR += 1
        fileNumber += 1
        print(fileNumber)
        print('__')
    elif 13 <= fileNumber < 19:
        print((folderPathAbnormal1 + '\\' + 'abRLRnLMR' + '.' + str(numberofabRLRnLMR) + '.jpg'))
        print(folderPathAbnormal1 + '\\' + filename)
        rename(folderPathAbnormal1 + '\\' + filename,folderPathAbnormal1 + '\\' + 'abRLRnLMR' + '.' + str(numberofabRLRnLMR) + '.jpg')
        numberofabRLRnLMR += 1
        fileNumber += 1
    elif 19 <= fileNumber < 25:
        print((folderPathAbnormal1 + '\\' + 'abRMRnLLR' + '.' + str(numberofabRMRnLLR) + '.jpg'))
        print(folderPathAbnormal1 + '\\' + filename)
        rename(folderPathAbnormal1 + '\\' + filename,folderPathAbnormal1 + '\\' + 'abRMRnLLR' + '.' + str(numberofabRMRnLLR) + '.jpg')
        numberofabRMRnLLR += 1
        fileNumber += 1
    elif 25 <= fileNumber < 31:
        print((folderPathAbnormal1 + '\\' + 'abRIRnLSO' + '.' + str(numberofabRIRnLSO) + '.jpg'))
        print(folderPathAbnormal1 + '\\' + filename)
        rename(folderPathAbnormal1 + '\\' + filename,folderPathAbnormal1 + '\\' + 'abRIRnLSO' + '.' + str(numberofabRIRnLSO) + '.jpg')
        numberofabRIRnLSO += 1
        fileNumber += 1
    elif 31 <= fileNumber < 37:
        print((folderPathAbnormal1 + '\\' + 'abRSOnLIR' + '.' + str(numberofabRSOnLIR) + '.jpg'))
        print(folderPathAbnormal1 + '\\' + filename)
        rename(folderPathAbnormal1 + '\\' + filename,folderPathAbnormal1 + '\\' + 'abRSOnLIR' + '.' + str(numberofabRSOnLIR) + '.jpg')
        numberofabRSOnLIR += 1
        fileNumber += 1

fileNumber = 1

for filename in natsorted(listdir(folderPathAbnormal2)):
    # print(folderPathAbnormal2 + '\\' + filename)
    if 1 <= fileNumber < 7:
        print((folderPathAbnormal2 + '\\' + 'abRSRnLIO' + '.' + str(numberofabRSRnLIO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal2 + '\\' + filename, folderPathAbnormal2 + '\\' + 'abRSRnLIO' + '.' + str(numberofabRSRnLIO) + '.jpg')
        numberofabRSRnLIO += 1
        fileNumber += 1
    elif 7 <= fileNumber < 13:
        print((folderPathAbnormal2 + '\\' + 'abRIOnLSR' + '.' + str(numberofabRIOnLSR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal2 + '\\' + filename, folderPathAbnormal2 + '\\' + 'abRIOnLSR' + '.' + str(numberofabRIOnLSR) + '.jpg')
        numberofabRIOnLSR += 1
        fileNumber += 1
    elif 13 <= fileNumber < 19:
        print((folderPathAbnormal2 + '\\' + 'abRLRnLMR' + '.' + str(numberofabRLRnLMR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal2 + '\\' + filename, folderPathAbnormal2 + '\\' + 'abRLRnLMR' + '.' + str(numberofabRLRnLMR) + '.jpg')
        numberofabRLRnLMR += 1
        fileNumber += 1
    elif 19 <= fileNumber < 25:
        print((folderPathAbnormal2 + '\\' + 'abRMRnLLR' + '.' + str(numberofabRMRnLLR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal2 + '\\' + filename, folderPathAbnormal2 + '\\' + 'abRMRnLLR' + '.' + str(numberofabRMRnLLR) + '.jpg')
        numberofabRMRnLLR += 1
        fileNumber += 1
    elif 25 <= fileNumber < 31:
        print((folderPathAbnormal2 + '\\' + 'abRIRnLSO' + '.' + str(numberofabRIRnLSO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal2 + '\\' + filename, folderPathAbnormal2 + '\\' + 'abRIRnLSO' + '.' + str(numberofabRIRnLSO) + '.jpg')
        numberofabRIRnLSO += 1
        fileNumber += 1
    elif 31 <= fileNumber < 37:
        print((folderPathAbnormal2 + '\\' + 'abRSOnLIR' + '.' + str(numberofabRSOnLIR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal2 + '\\' + filename, folderPathAbnormal2 + '\\' + 'abRSOnLIR' + '.' + str(numberofabRSOnLIR) + '.jpg')
        numberofabRSOnLIR += 1
        fileNumber += 1

fileNumber = 1

for filename in natsorted(listdir(folderPathAbnormal3)):
    # print(filename)
    if 1 <= fileNumber < 7:
        print((folderPathAbnormal3 + '\\' + 'abRSRnLIO' + '.' + str(numberofabRSRnLIO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal3 + '\\' + filename, folderPathAbnormal3 + '\\' + 'abRSRnLIO' + '.' + str(numberofabRSRnLIO) + '.jpg')
        numberofabRSRnLIO += 1
        fileNumber += 1
    elif 7 <= fileNumber < 13:
        print((folderPathAbnormal3 + '\\' + 'abRIOnLSR' + '.' + str(numberofabRIOnLSR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal3 + '\\' + filename, folderPathAbnormal3 + '\\' + 'abRIOnLSR' + '.' + str(numberofabRIOnLSR) + '.jpg')
        numberofabRIOnLSR += 1
        fileNumber += 1
    elif 13 <= fileNumber < 19:
        print((folderPathAbnormal3 + '\\' + 'abRLRnLMR' + '.' + str(numberofabRLRnLMR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal3 + '\\' + filename, folderPathAbnormal3 + '\\' + 'abRLRnLMR' + '.' + str(numberofabRLRnLMR) + '.jpg')
        numberofabRLRnLMR += 1
        fileNumber += 1
    elif 19 <= fileNumber < 25:
        print((folderPathAbnormal3 + '\\' + 'abRMRnLLR' + '.' + str(numberofabRMRnLLR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal3 + '\\' + filename, folderPathAbnormal3 + '\\' + 'abRMRnLLR' + '.' + str(numberofabRMRnLLR) + '.jpg')
        numberofabRMRnLLR += 1
        fileNumber += 1
    elif 25 <= fileNumber < 31:
        print((folderPathAbnormal3 + '\\' + 'abRIRnLSO' + '.' + str(numberofabRIRnLSO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal3 + '\\' + filename, folderPathAbnormal3 + '\\' + 'abRIRnLSO' + '.' + str(numberofabRIRnLSO) + '.jpg')
        numberofabRIRnLSO += 1
        fileNumber += 1
    elif 31 <= fileNumber < 37:
        print((folderPathAbnormal3 + '\\' + 'abRSOnLIR' + '.' + str(numberofabRSOnLIR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal3 + '\\' + filename, folderPathAbnormal3 + '\\' + 'abRSOnLIR' + '.' + str(numberofabRSOnLIR) + '.jpg')
        numberofabRSOnLIR += 1
        fileNumber += 1

fileNumber = 1

for filename in natsorted(listdir(folderPathAbnormal4)):

    if 1 <= fileNumber < 7:
        print((folderPathAbnormal4 + '\\' + 'abRSRnLIO' + '.' + str(numberofabRSRnLIO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal4 + '\\' + filename, folderPathAbnormal4 + '\\' + 'abRSRnLIO' + '.' + str(numberofabRSRnLIO) + '.jpg')
        numberofabRSRnLIO += 1
        fileNumber += 1
    elif 7 <= fileNumber < 13:
        print((folderPathAbnormal4 + '\\' + 'abRIOnLSR' + '.' + str(numberofabRIOnLSR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal4 + '\\' + filename, folderPathAbnormal4 + '\\' + 'abRIOnLSR' + '.' + str(numberofabRIOnLSR) + '.jpg')
        numberofabRIOnLSR += 1
        fileNumber += 1
    elif 13 <= fileNumber < 19:
        print((folderPathAbnormal4 + '\\' + 'abRLRnLMR' + '.' + str(numberofabRLRnLMR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal4 + '\\' + filename, folderPathAbnormal4 + '\\' + 'abRLRnLMR' + '.' + str(numberofabRLRnLMR) + '.jpg')
        numberofabRLRnLMR += 1
        fileNumber += 1
    elif 19 <= fileNumber < 25:
        print((folderPathAbnormal4 + '\\' + 'abRMRnLLR' + '.' + str(numberofabRMRnLLR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal4 + '\\' + filename, folderPathAbnormal4 + '\\' + 'abRMRnLLR' + '.' + str(numberofabRMRnLLR) + '.jpg')
        numberofabRMRnLLR += 1
        fileNumber += 1
    elif 25 <= fileNumber < 31:
        print((folderPathAbnormal4 + '\\' + 'abRIRnLSO' + '.' + str(numberofabRIRnLSO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal4 + '\\' + filename, folderPathAbnormal4 + '\\' + 'abRIRnLSO' + '.' + str(numberofabRIRnLSO) + '.jpg')
        numberofabRIRnLSO += 1
        fileNumber += 1
    elif 31 <= fileNumber < 37:
        print((folderPathAbnormal4 + '\\' + 'abRSOnLIR' + '.' + str(numberofabRSOnLIR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal4 + '\\' + filename, folderPathAbnormal4 + '\\' + 'abRSOnLIR' + '.' + str(numberofabRSOnLIR) + '.jpg')
        numberofabRSOnLIR += 1
        fileNumber += 1

fileNumber = 1

for filename in natsorted(listdir(folderPathAbnormal5)):
    if 1 <= fileNumber < 7:
        print((folderPathAbnormal5 + '\\' + 'nRSRabLIO' + '.' + str(numberofnRSRabLIO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal5 + '\\' + filename, folderPathAbnormal5 + '\\' + 'nRSRabLIO' + '.' + str(numberofnRSRabLIO) + '.jpg')
        numberofnRSRabLIO += 1
        fileNumber += 1
    elif 7 <= fileNumber < 13:
        print((folderPathAbnormal5 + '\\' + 'nRIOabLSR' + '.' + str(numberofnRIOabLSR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal5 + '\\' + filename, folderPathAbnormal5 + '\\' + 'nRIOabLSR' + '.' + str(numberofnRIOabLSR) + '.jpg')
        numberofnRIOabLSR += 1
        fileNumber += 1
    elif 13 <= fileNumber < 19:
        print((folderPathAbnormal5 + '\\' + 'nRLRabLMR' + '.' + str(numberofnRLRabLMR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal5 + '\\' + filename, folderPathAbnormal5 + '\\' + 'nRLRabLMR' + '.' + str(numberofnRLRabLMR) + '.jpg')
        numberofnRLRabLMR += 1
        fileNumber += 1
    elif 19 <= fileNumber < 25:
        print((folderPathAbnormal5 + '\\' + 'nRMRabLLR' + '.' + str(numberofnRMRabLLR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal5 + '\\' + filename, folderPathAbnormal5 + '\\' + 'nRMRabLLR' + '.' + str(numberofnRMRabLLR) + '.jpg')
        numberofnRMRabLLR += 1
        fileNumber += 1
    elif 25 <= fileNumber < 31:
        print((folderPathAbnormal5 + '\\' + 'nRIRabLSO' + '.' + str(numberofnRIRabLSO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal5 + '\\' + filename, folderPathAbnormal5 + '\\' + 'nRIRabLSO' + '.' + str(numberofnRIRabLSO) + '.jpg')
        numberofnRIRabLSO += 1
        fileNumber += 1
    elif 31 <= fileNumber < 37:
        print((folderPathAbnormal5 + '\\' + 'nRSOabLIR' + '.' + str(numberofnRSOabLIR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal5 + '\\' + filename, folderPathAbnormal5 + '\\' + 'nRSOabLIR' + '.' + str(numberofnRSOabLIR) + '.jpg')
        numberofnRSOabLIR += 1
        fileNumber += 1

fileNumber = 1

for filename in natsorted(listdir(folderPathAbnormal6)):

    if 1 <= fileNumber < 7:
        print((folderPathAbnormal6 + '\\' + 'nRSRabLIO' + '.' + str(numberofnRSRabLIO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal6 + '\\' + filename, folderPathAbnormal6 + '\\' + 'nRSRabLIO' + '.' + str(numberofnRSRabLIO) + '.jpg')
        numberofnRSRabLIO += 1
        fileNumber += 1
    elif 7 <= fileNumber < 13:
        print((folderPathAbnormal6 + '\\' + 'nRIOabLSR' + '.' + str(numberofnRIOabLSR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal6 + '\\' + filename, folderPathAbnormal6 + '\\' + 'nRIOabLSR' + '.' + str(numberofnRIOabLSR) + '.jpg')
        numberofnRIOabLSR += 1
        fileNumber += 1
    elif 13 <= fileNumber < 19:
        print((folderPathAbnormal6 + '\\' + 'nRLRabLMR' + '.' + str(numberofnRLRabLMR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal6 + '\\' + filename, folderPathAbnormal6 + '\\' + 'nRLRabLMR' + '.' + str(numberofnRLRabLMR) + '.jpg')
        numberofnRLRabLMR += 1
        fileNumber += 1
    elif 19 <= fileNumber < 25:
        print((folderPathAbnormal6 + '\\' + 'nRMRabLLR' + '.' + str(numberofnRMRabLLR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal6 + '\\' + filename, folderPathAbnormal6 + '\\' + 'nRMRabLLR' + '.' + str(numberofnRMRabLLR) + '.jpg')
        numberofnRMRabLLR += 1
        fileNumber += 1
    elif 25 <= fileNumber < 31:
        print((folderPathAbnormal6 + '\\' + 'nRIRabLSO' + '.' + str(numberofnRIRabLSO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal6 + '\\' + filename, folderPathAbnormal6 + '\\' + 'nRIRabLSO' + '.' + str(numberofnRIRabLSO) + '.jpg')
        numberofnRIRabLSO += 1
        fileNumber += 1
    elif 31 <= fileNumber < 37:
        print((folderPathAbnormal6 + '\\' + 'nRSOabLIR' + '.' + str(numberofnRSOabLIR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal6 + '\\' + filename, folderPathAbnormal6 + '\\' + 'nRSOabLIR' + '.' + str(numberofnRSOabLIR) + '.jpg')
        numberofnRSOabLIR += 1
        fileNumber += 1

fileNumber = 1

for filename in natsorted(listdir(folderPathAbnormal7)):

    if 1 <= fileNumber < 7:
        print((folderPathAbnormal7 + '\\' + 'nRSRabLIO' + '.' + str(numberofnRSRabLIO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal7 + '\\' + filename, folderPathAbnormal7 + '\\' + 'nRSRabLIO' + '.' + str(numberofnRSRabLIO) + '.jpg')
        numberofnRSRabLIO += 1
        fileNumber += 1
    elif 7 <= fileNumber < 13:
        print((folderPathAbnormal7 + '\\' + 'nRIOabLSR' + '.' + str(numberofnRIOabLSR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal7 + '\\' + filename, folderPathAbnormal7 + '\\' + 'nRIOabLSR' + '.' + str(numberofnRIOabLSR) + '.jpg')
        numberofnRIOabLSR += 1
        fileNumber += 1
    elif 13 <= fileNumber < 19:
        print((folderPathAbnormal7 + '\\' + 'nRLRabLMR' + '.' + str(numberofnRLRabLMR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal7 + '\\' + filename, folderPathAbnormal7 + '\\' + 'nRLRabLMR' + '.' + str(numberofnRLRabLMR) + '.jpg')
        numberofnRLRabLMR += 1
        fileNumber += 1
    elif 19 <= fileNumber < 25:
        print((folderPathAbnormal7 + '\\' + 'nRMRabLLR' + '.' + str(numberofnRMRabLLR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal7 + '\\' + filename, folderPathAbnormal7 + '\\' + 'nRMRabLLR' + '.' + str(numberofnRMRabLLR) + '.jpg')
        numberofnRMRabLLR += 1
        fileNumber += 1
    elif 25 <= fileNumber < 31:
        print((folderPathAbnormal7 + '\\' + 'nRIRabLSO' + '.' + str(numberofnRIRabLSO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal7 + '\\' + filename, folderPathAbnormal7 + '\\' + 'nRIRabLSO' + '.' + str(numberofnRIRabLSO) + '.jpg')
        numberofnRIRabLSO += 1
        fileNumber += 1
    elif 31 <= fileNumber < 37:
        print((folderPathAbnormal7 + '\\' + 'nRSOabLIR' + '.' + str(numberofnRSOabLIR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal7 + '\\' + filename, folderPathAbnormal7 + '\\' + 'nRSOabLIR' + '.' + str(numberofnRSOabLIR) + '.jpg')
        numberofnRSOabLIR += 1
        fileNumber += 1

fileNumber = 1

for filename in natsorted(listdir(folderPathAbnormal8)):

    if 1 <= fileNumber < 7:
        print((folderPathAbnormal8 + '\\' + 'nRSRabLIO' + '.' + str(numberofnRSRabLIO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal8 + '\\' + filename, folderPathAbnormal8 + '\\' + 'nRSRabLIO' + '.' + str(numberofnRSRabLIO) + '.jpg')
        numberofnRSRabLIO += 1
        fileNumber += 1
    elif 7 <= fileNumber < 13:
        print((folderPathAbnormal8 + '\\' + 'nRIOabLSR' + '.' + str(numberofnRIOabLSR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal8 + '\\' + filename, folderPathAbnormal8 + '\\' + 'nRIOabLSR' + '.' + str(numberofnRIOabLSR) + '.jpg')
        numberofnRIOabLSR += 1
        fileNumber += 1
    elif 13 <= fileNumber < 19:
        print((folderPathAbnormal8 + '\\' + 'nRLRabLMR' + '.' + str(numberofnRLRabLMR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal8 + '\\' + filename, folderPathAbnormal8 + '\\' + 'nRLRabLMR' + '.' + str(numberofnRLRabLMR) + '.jpg')
        numberofnRLRabLMR += 1
        fileNumber += 1
    elif 19 <= fileNumber < 25:
        print((folderPathAbnormal8 + '\\' + 'nRMRabLLR' + '.' + str(numberofnRMRabLLR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal8 + '\\' + filename, folderPathAbnormal8 + '\\' + 'nRMRabLLR' + '.' + str(numberofnRMRabLLR) + '.jpg')
        numberofnRMRabLLR += 1
        fileNumber += 1
    elif 25 <= fileNumber < 31:
        print((folderPathAbnormal8 + '\\' + 'nRIRabLSO' + '.' + str(numberofnRIRabLSO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal8 + '\\' + filename, folderPathAbnormal8 + '\\' + 'nRIRabLSO' + '.' + str(numberofnRIRabLSO) + '.jpg')
        numberofnRIRabLSO += 1
        fileNumber += 1
    elif 31 <= fileNumber < 37:
        print((folderPathAbnormal8 + '\\' + 'nRSOabLIR' + '.' + str(numberofnRSOabLIR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal8 + '\\' + filename, folderPathAbnormal8 + '\\' + 'nRSOabLIR' + '.' + str(numberofnRSOabLIR) + '.jpg')
        numberofnRSOabLIR += 1
        fileNumber += 1

fileNumber = 1

for filename in natsorted(listdir(folderPathAbnormal9)):
 
    if 1 <= fileNumber < 7:
        print((folderPathAbnormal9 + '\\' + 'abRSRabLIO' + '.' + str(numberofabRSRabLIO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal9 + '\\' + filename, folderPathAbnormal9 + '\\' + 'abRSRabLIO' + '.' + str(numberofabRSRabLIO) + '.jpg')
        numberofabRSRabLIO += 1
        fileNumber += 1
    elif 7 <= fileNumber < 13:
        print((folderPathAbnormal9 + '\\' + 'abRIOabLSR' + '.' + str(numberofabRIOabLSR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal9 + '\\' + filename, folderPathAbnormal9 + '\\' + 'abRIOabLSR' + '.' + str(numberofabRIOabLSR) + '.jpg')
        numberofabRIOabLSR += 1
        fileNumber += 1
    elif 13 <= fileNumber < 19:
        print((folderPathAbnormal9 + '\\' + 'abRLRabLMR' + '.' + str(numberofabRLRabLMR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal9 + '\\' + filename, folderPathAbnormal9 + '\\' + 'abRLRabLMR' + '.' + str(numberofabRLRabLMR) + '.jpg')
        numberofabRLRabLMR += 1
        fileNumber += 1
    elif 19 <= fileNumber < 25:
        print((folderPathAbnormal9 + '\\' + 'abRMRabLLR' + '.' + str(numberofabRMRabLLR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal9 + '\\' + filename, folderPathAbnormal9 + '\\' + 'abRMRabLLR' + '.' + str(numberofabRMRabLLR) + '.jpg')
        numberofabRMRabLLR += 1
        fileNumber += 1
    elif 25 <= fileNumber < 31:
        print((folderPathAbnormal9 + '\\' + 'abRIRabLSO' + '.' + str(numberofabRIRabLSO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal9 + '\\' + filename, folderPathAbnormal9 + '\\' + 'abRIRabLSO' + '.' + str(numberofabRIRabLSO) + '.jpg')
        numberofabRIRabLSO += 1
        fileNumber += 1
    elif 31 <= fileNumber < 37:
        print((folderPathAbnormal9 + '\\' + 'abRSOabLIR' + '.' + str(numberofabRSOabLIR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal9 + '\\' + filename, folderPathAbnormal9 + '\\' + 'abRSOabLIR' + '.' + str(numberofabRSOabLIR) + '.jpg')
        numberofabRSOabLIR += 1
        fileNumber += 1

fileNumber = 1

for filename in natsorted(listdir(folderPathAbnormal10)):

    if 1 <= fileNumber < 7:
        print((folderPathAbnormal10 + '\\' + 'abRSRabLIO' + '.' + str(numberofabRSRabLIO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal10 + '\\' + filename, folderPathAbnormal10 + '\\' + 'abRSRabLIO' + '.' + str(numberofabRSRabLIO) + '.jpg')
        numberofabRSRabLIO += 1
        fileNumber += 1
    elif 7 <= fileNumber < 13:
        print((folderPathAbnormal10 + '\\' + 'abRIOabLSR' + '.' + str(numberofabRIOabLSR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal10 + '\\' + filename, folderPathAbnormal10 + '\\' + 'abRIOabLSR' + '.' + str(numberofabRIOabLSR) + '.jpg')
        numberofabRIOabLSR += 1
        fileNumber += 1
    elif 13 <= fileNumber < 19:
        print((folderPathAbnormal10 + '\\' + 'abRLRabLMR' + '.' + str(numberofabRLRabLMR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal10 + '\\' + filename, folderPathAbnormal10 + '\\' + 'abRLRabLMR' + '.' + str(numberofabRLRabLMR) + '.jpg')
        numberofabRLRabLMR += 1
        fileNumber += 1
    elif 19 <= fileNumber < 25:
        print((folderPathAbnormal10 + '\\' + 'abRMRabLLR' + '.' + str(numberofabRMRabLLR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal10 + '\\' + filename, folderPathAbnormal10 + '\\' + 'abRMRabLLR' + '.' + str(numberofabRMRabLLR) + '.jpg')
        numberofabRMRabLLR += 1
        fileNumber += 1
    elif 25 <= fileNumber < 31:
        print((folderPathAbnormal10 + '\\' + 'abRIRabLSO' + '.' + str(numberofabRIRabLSO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal10 + '\\' + filename, folderPathAbnormal10 + '\\' + 'abRIRabLSO' + '.' + str(numberofabRIRabLSO) + '.jpg')
        numberofabRIRabLSO += 1
        fileNumber += 1
    elif 31 <= fileNumber < 37:
        print((folderPathAbnormal10 + '\\' + 'abRSOabLIR' + '.' + str(numberofabRSOabLIR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal10 + '\\' + filename, folderPathAbnormal10 + '\\' + 'abRSOabLIR' + '.' + str(numberofabRSOabLIR) + '.jpg')
        numberofabRSOabLIR += 1
        fileNumber += 1

fileNumber = 1

for filename in natsorted(listdir(folderPathAbnormal11)):

    if 1 <= fileNumber < 7:
        print((folderPathAbnormal11 + '\\' + 'abRSRabLIO' + '.' + str(numberofabRSRabLIO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal11 + '\\' + filename, folderPathAbnormal11 + '\\' + 'abRSRabLIO' + '.' + str(numberofabRSRabLIO) + '.jpg')
        numberofabRSRabLIO += 1
        fileNumber += 1
    elif 7 <= fileNumber < 13:
        print((folderPathAbnormal11 + '\\' + 'abRIOabLSR' + '.' + str(numberofabRIOabLSR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal11 + '\\' + filename, folderPathAbnormal11 + '\\' + 'abRIOabLSR' + '.' + str(numberofabRIOabLSR) + '.jpg')
        numberofabRIOabLSR += 1
        fileNumber += 1
    elif 13 <= fileNumber < 19:
        print((folderPathAbnormal11 + '\\' + 'abRLRabLMR' + '.' + str(numberofabRLRabLMR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal11 + '\\' + filename, folderPathAbnormal11 + '\\' + 'abRLRabLMR' + '.' + str(numberofabRLRabLMR) + '.jpg')
        numberofabRLRabLMR += 1
        fileNumber += 1
    elif 19 <= fileNumber < 25:
        print((folderPathAbnormal11 + '\\' + 'abRMRabLLR' + '.' + str(numberofabRMRabLLR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal11 + '\\' + filename, folderPathAbnormal11 + '\\' + 'abRMRabLLR' + '.' + str(numberofabRMRabLLR) + '.jpg')
        numberofabRMRabLLR += 1
        fileNumber += 1
    elif 25 <= fileNumber < 31:
        print((folderPathAbnormal11 + '\\' + 'abRIRabLSO' + '.' + str(numberofabRIRabLSO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal11 + '\\' + filename, folderPathAbnormal11 + '\\' + 'abRIRabLSO' + '.' + str(numberofabRIRabLSO) + '.jpg')
        numberofabRIRabLSO += 1
        fileNumber += 1
    elif 31 <= fileNumber < 37:
        print((folderPathAbnormal11 + '\\' + 'abRSOabLIR' + '.' + str(numberofabRSOabLIR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal11 + '\\' + filename, folderPathAbnormal11 + '\\' + 'abRSOabLIR' + '.' + str(numberofabRSOabLIR) + '.jpg')
        numberofabRSOabLIR += 1
        fileNumber += 1

fileNumber = 1

for filename in natsorted(listdir(folderPathAbnormal12)):
    print(filename)
    if 1 <= fileNumber < 7:
        print((folderPathAbnormal12 + '\\' + 'abRSRabLIO' + '.' + str(numberofabRSRabLIO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal12 + '\\' + filename, folderPathAbnormal12 + '\\' + 'abRSRabLIO' + '.' + str(numberofabRSRabLIO) + '.jpg')
        numberofabRSRabLIO += 1
        fileNumber += 1
    elif 7 <= fileNumber < 13:
        print((folderPathAbnormal12 + '\\' + 'abRIOabLSR' + '.' + str(numberofabRIOabLSR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal12 + '\\' + filename, folderPathAbnormal12 + '\\' + 'abRIOabLSR' + '.' + str(numberofabRIOabLSR) + '.jpg')
        numberofabRIOabLSR += 1
        fileNumber += 1
    elif 13 <= fileNumber < 19:
        print((folderPathAbnormal12 + '\\' + 'abRLRabLMR' + '.' + str(numberofabRLRabLMR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal12 + '\\' + filename, folderPathAbnormal12 + '\\' + 'abRLRabLMR' + '.' + str(numberofabRLRabLMR) + '.jpg')
        numberofabRLRabLMR += 1
        fileNumber += 1
    elif 19 <= fileNumber < 25:
        print((folderPathAbnormal12 + '\\' + 'abRMRabLLR' + '.' + str(numberofabRMRabLLR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal12 + '\\' + filename, folderPathAbnormal12 + '\\' + 'abRMRabLLR' + '.' + str(numberofabRMRabLLR) + '.jpg')
        numberofabRMRabLLR += 1
        fileNumber += 1
    elif 25 <= fileNumber < 31:
        print((folderPathAbnormal12 + '\\' + 'abRIRabLSO' + '.' + str(numberofabRIRabLSO) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal12 + '\\' + filename, folderPathAbnormal12 + '\\' + 'abRIRabLSO' + '.' + str(numberofabRIRabLSO) + '.jpg')
        numberofabRIRabLSO += 1
        fileNumber += 1
    elif 31 <= fileNumber < 37:
        print((folderPathAbnormal12 + '\\' + 'abRSOabLIR' + '.' + str(numberofabRSOabLIR) + '.jpg'))
        print(filename)
        rename(folderPathAbnormal12 + '\\' + filename, folderPathAbnormal12 + '\\' + 'abRSOabLIR' + '.' + str(numberofabRSOabLIR) + '.jpg')
        numberofabRSOabLIR += 1
        fileNumber += 1

fileNumber = 1

for filename in natsorted(listdir(folderPathNormal)):
    if 1 <= fileNumber < 9:
        print((folderPathNormal + '\\' + 'nRSRnLIO' + '.' + str(numberofnRSRnLIO) + '.jpg'))
        print(filename)
        rename(folderPathNormal + '\\' + filename, folderPathNormal + '\\' + 'nRSRnLIO' + '.' + str(numberofnRSRnLIO) + '.jpg')
        numberofnRSRnLIO += 1
        fileNumber += 1
    elif 9 <= fileNumber < 17:
        print((folderPathNormal + '\\' + 'nRIOnLSR' + '.' + str(numberofnRIOnLSR) + '.jpg'))
        print(filename)
        rename(folderPathNormal + '\\' + filename, folderPathNormal + '\\' + 'nRIOnLSR' + '.' + str(numberofnRIOnLSR) + '.jpg')
        numberofnRIOnLSR += 1
        fileNumber += 1
    elif 17 <= fileNumber < 25:
        print((folderPathNormal + '\\' + 'nRLRnLMR' + '.' + str(numberofnRLRnLMR) + '.jpg'))
        print(filename)
        rename(folderPathNormal + '\\' + filename, folderPathNormal + '\\' + 'nRLRnLMR' + '.' + str(numberofnRLRnLMR) + '.jpg')
        numberofnRLRnLMR += 1
        fileNumber += 1
    elif 25 <= fileNumber < 33:
        print((folderPathNormal + '\\' + 'nRMRnLLR' + '.' + str(numberofnRMRnLLR) + '.jpg'))
        print(filename)
        rename(folderPathNormal + '\\' + filename, folderPathNormal + '\\' + 'nRMRnLLR' + '.' + str(numberofnRMRnLLR) + '.jpg')
        numberofnRMRnLLR += 1
        fileNumber += 1
    elif 33 <= fileNumber < 41:
        print((folderPathNormal + '\\' + 'nRIRnLSO' + '.' + str(numberofnRIRnLSO) + '.jpg'))
        print(filename)
        rename(folderPathNormal + '\\' + filename, folderPathNormal + '\\' + 'nRIRnLSO' + '.' + str(numberofnRIRnLSO) + '.jpg')
        numberofnRIRnLSO += 1
        fileNumber += 1
    elif 41 <= fileNumber < 49:
        print((folderPathNormal + '\\' + 'nRSOnLIR' + '.' + str(numberofnRSOnLIR) + '.jpg'))
        print(filename)
        rename(folderPathNormal + '\\' + filename, folderPathNormal + '\\' + 'nRSOnLIR' + '.' + str(numberofnRSOnLIR) + '.jpg')
        numberofnRSOnLIR += 1
        fileNumber += 1

