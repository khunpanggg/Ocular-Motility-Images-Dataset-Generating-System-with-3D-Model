import os
import shutil
import random
import glob
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# pathFolder = 'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/datasetmergefile/'
os.chdir('datasetmergefile_mix_pack9')

if os.path.isdir('train/normal') is False:
    os.makedirs('train/normal')
    os.makedirs('train/abRnL')
    os.makedirs('train/nRabL')
    os.makedirs('train/abRabL')

    os.makedirs('test/normal')
    os.makedirs('test/abRnL')
    os.makedirs('test/nRabL')
    os.makedirs('test/abRabL')

for i in random.sample(glob.glob('normal*'), 5):
    shutil.move(i, 'train/normal')

for i in random.sample(glob.glob('abRnL*'), 17):
    shutil.move(i, 'train/abRnL')

for i in random.sample(glob.glob('nRabL*'), 17):
    shutil.move(i, 'train/nRabL')

for i in random.sample(glob.glob('abRabL*'), 17):
    shutil.move(i, 'train/abRabL')



for i in random.sample(glob.glob('normal*'), 3):
    shutil.move(i, 'test/normal')

for i in random.sample(glob.glob('abRnL*'), 7):
    shutil.move(i, 'test/abRnL')

for i in random.sample(glob.glob('nRabL*'), 7):
    shutil.move(i, 'test/nRabL')

for i in random.sample(glob.glob('abRabL*'), 7):
    shutil.move(i, 'test/abRabL')

os.chdir('../../')
