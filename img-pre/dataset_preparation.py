import os
import shutil
import random
import glob
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

pathFolder = 'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/datasetmergefile/'
os.chdir('datasetmergefile')

if os.path.isdir('train/nRSRnLIO') is False:
    os.makedirs('train/nRSRnLIO')
    os.makedirs('train/nRIOnLSR')
    os.makedirs('train/nRLRnLMR')
    os.makedirs('train/nRMRnLLR')
    os.makedirs('train/nRIRnLSO')
    os.makedirs('train/nRSOnLIR')

    os.makedirs('train/abRSRnLIO')
    os.makedirs('train/abRIOnLSR')
    os.makedirs('train/abRLRnLMR')
    os.makedirs('train/abRMRnLLR')
    os.makedirs('train/abRIRnLSO')
    os.makedirs('train/abRSOnLIR')

    os.makedirs('train/nRSRabLIO')
    os.makedirs('train/nRIOabLSR')
    os.makedirs('train/nRLRabLMR')
    os.makedirs('train/nRMRabLLR')
    os.makedirs('train/nRIRabLSO')
    os.makedirs('train/nRSOabLIR')

    os.makedirs('train/abRSRabLIO')
    os.makedirs('train/abRIOabLSR')
    os.makedirs('train/abRLRabLMR')
    os.makedirs('train/abRMRabLLR')
    os.makedirs('train/abRIRabLSO')
    os.makedirs('train/abRSOabLIR')



    os.makedirs('test/nRSRnLIO')
    os.makedirs('test/nRIOnLSR')
    os.makedirs('test/nRLRnLMR')
    os.makedirs('test/nRMRnLLR')
    os.makedirs('test/nRIRnLSO')
    os.makedirs('test/nRSOnLIR')

    os.makedirs('test/abRSRnLIO')
    os.makedirs('test/abRIOnLSR')
    os.makedirs('test/abRLRnLMR')
    os.makedirs('test/abRMRnLLR')
    os.makedirs('test/abRIRnLSO')
    os.makedirs('test/abRSOnLIR')

    os.makedirs('test/nRSRabLIO')
    os.makedirs('test/nRIOabLSR')
    os.makedirs('test/nRLRabLMR')
    os.makedirs('test/nRMRabLLR')
    os.makedirs('test/nRIRabLSO')
    os.makedirs('test/nRSOabLIR')

    os.makedirs('test/abRSRabLIO')
    os.makedirs('test/abRIOabLSR')
    os.makedirs('test/abRLRabLMR')
    os.makedirs('test/abRMRabLLR')
    os.makedirs('test/abRIRabLSO')
    os.makedirs('test/abRSOabLIR')

for i in random.sample(glob.glob('nRSRnLIO*'), 5):
    shutil.move(i, 'train/nRSRnLIO')
for i in random.sample(glob.glob('nRIOnLSR*'), 5):
    shutil.move(i, 'train/nRIOnLSR')
for i in random.sample(glob.glob('nRLRnLMR*'), 5):
    shutil.move(i, 'train/nRLRnLMR')
for i in random.sample(glob.glob('nRMRnLLR*'), 5):
    shutil.move(i, 'train/nRMRnLLR')
for i in random.sample(glob.glob('nRIRnLSO*'), 5):
    shutil.move(i, 'train/nRIRnLSO')
for i in random.sample(glob.glob('nRSOnLIR*'), 5):
    shutil.move(i, 'train/nRSOnLIR')

for i in random.sample(glob.glob('abRSRnLIO*'), 17):
    shutil.move(i, 'train/abRSRnLIO')
for i in random.sample(glob.glob('abRIOnLSR*'), 17):
    shutil.move(i, 'train/abRIOnLSR')
for i in random.sample(glob.glob('abRLRnLMR*'), 17):
    shutil.move(i, 'train/abRLRnLMR')
for i in random.sample(glob.glob('abRMRnLLR*'), 17):
    shutil.move(i, 'train/abRMRnLLR')
for i in random.sample(glob.glob('abRIRnLSO*'), 17):
    shutil.move(i, 'train/abRIRnLSO')
for i in random.sample(glob.glob('abRSOnLIR*'), 17):
    shutil.move(i, 'train/abRSOnLIR')

for i in random.sample(glob.glob('nRSRabLIO*'), 17):
    shutil.move(i, 'train/nRSRabLIO')
for i in random.sample(glob.glob('nRIOabLSR*'), 17):
    shutil.move(i, 'train/nRIOabLSR')
for i in random.sample(glob.glob('nRLRabLMR*'), 17):
    shutil.move(i, 'train/nRLRabLMR')
for i in random.sample(glob.glob('nRMRabLLR*'), 17):
    shutil.move(i, 'train/nRMRabLLR')
for i in random.sample(glob.glob('nRIRabLSO*'), 17):
    shutil.move(i, 'train/nRIRabLSO')
for i in random.sample(glob.glob('nRSOabLIR*'), 17):
    shutil.move(i, 'train/nRSOabLIR')

for i in random.sample(glob.glob('abRSRabLIO*'), 17):
    shutil.move(i, 'train/abRSRabLIO')
for i in random.sample(glob.glob('abRIOabLSR*'), 17):
    shutil.move(i, 'train/abRIOabLSR')
for i in random.sample(glob.glob('abRLRabLMR*'), 17):
    shutil.move(i, 'train/abRLRabLMR')
for i in random.sample(glob.glob('abRMRabLLR*'), 17):
    shutil.move(i, 'train/abRMRabLLR')
for i in random.sample(glob.glob('abRIRabLSO*'), 17):
    shutil.move(i, 'train/abRIRabLSO')
for i in random.sample(glob.glob('abRSOabLIR*'), 17):
    shutil.move(i, 'train/abRSOabLIR')




for i in random.sample(glob.glob('nRSRnLIO*'), 3):
    shutil.move(i, 'test/nRSRnLIO')
for i in random.sample(glob.glob('nRIOnLSR*'), 3):
    shutil.move(i, 'test/nRIOnLSR')
for i in random.sample(glob.glob('nRLRnLMR*'), 3):
    shutil.move(i, 'test/nRLRnLMR')
for i in random.sample(glob.glob('nRMRnLLR*'), 3):
    shutil.move(i, 'test/nRMRnLLR')
for i in random.sample(glob.glob('nRIRnLSO*'), 3):
    shutil.move(i, 'test/nRIRnLSO')
for i in random.sample(glob.glob('nRSOnLIR*'), 3):
    shutil.move(i, 'test/nRSOnLIR')

for i in random.sample(glob.glob('abRSRnLIO*'), 7):
    shutil.move(i, 'test/abRSRnLIO')
for i in random.sample(glob.glob('abRIOnLSR*'), 7):
    shutil.move(i, 'test/abRIOnLSR')
for i in random.sample(glob.glob('abRLRnLMR*'), 7):
    shutil.move(i, 'test/abRLRnLMR')
for i in random.sample(glob.glob('abRMRnLLR*'), 7):
    shutil.move(i, 'test/abRMRnLLR')
for i in random.sample(glob.glob('abRIRnLSO*'), 7):
    shutil.move(i, 'test/abRIRnLSO')
for i in random.sample(glob.glob('abRSOnLIR*'), 7):
    shutil.move(i, 'test/abRSOnLIR')

for i in random.sample(glob.glob('nRSRabLIO*'), 7):
    shutil.move(i, 'test/nRSRabLIO')
for i in random.sample(glob.glob('nRIOabLSR*'), 7):
    shutil.move(i, 'test/nRIOabLSR')
for i in random.sample(glob.glob('nRLRabLMR*'), 7):
    shutil.move(i, 'test/nRLRabLMR')
for i in random.sample(glob.glob('nRMRabLLR*'), 7):
    shutil.move(i, 'test/nRMRabLLR')
for i in random.sample(glob.glob('nRIRabLSO*'), 7):
    shutil.move(i, 'test/nRIRabLSO')
for i in random.sample(glob.glob('nRSOabLIR*'), 7):
    shutil.move(i, 'test/nRSOabLIR')

for i in random.sample(glob.glob('abRSRabLIO*'), 7):
    shutil.move(i, 'test/abRSRabLIO')
for i in random.sample(glob.glob('abRIOabLSR*'), 7):
    shutil.move(i, 'test/abRIOabLSR')
for i in random.sample(glob.glob('abRLRabLMR*'), 7):
    shutil.move(i, 'test/abRLRabLMR')
for i in random.sample(glob.glob('abRMRabLLR*'), 7):
    shutil.move(i, 'test/abRMRabLLR')
for i in random.sample(glob.glob('abRIRabLSO*'), 7):
    shutil.move(i, 'test/abRIRabLSO')
for i in random.sample(glob.glob('abRSOabLIR*'), 7):
    shutil.move(i, 'test/abRSOabLIR')

os.chdir('../../')
