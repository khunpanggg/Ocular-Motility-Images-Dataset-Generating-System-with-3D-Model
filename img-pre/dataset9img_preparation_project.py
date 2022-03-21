import os
import shutil
import random
import glob
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

pathFolder = 'C:/Users/PiLab/Documents/wipawapat_folder/VGG_TEST/datasetmergefile_mix_pack9_project/'
os.chdir('datasetmergefile_mix_pack9_project')

if os.path.isdir('train/normal') is False:
    os.makedirs('train/normal')
    os.makedirs('train/abRSR')
    os.makedirs('train/abLSR')
    os.makedirs('train/abSR')
    os.makedirs('train/abRIO')
    os.makedirs('train/abLIO')
    os.makedirs('train/abIO')
    os.makedirs('train/abRLR')
    os.makedirs('train/abLLR')
    os.makedirs('train/abLR')
    os.makedirs('train/abRMR')
    os.makedirs('train/abLMR')
    os.makedirs('train/abMR')
    os.makedirs('train/abRIR')
    os.makedirs('train/abLIR')
    os.makedirs('train/abIR')
    os.makedirs('train/abRSO')
    os.makedirs('train/abLSO')
    os.makedirs('train/abSO')

    os.makedirs('test/normal')
    os.makedirs('test/abRSR')
    os.makedirs('test/abLSR')
    os.makedirs('test/abSR')
    os.makedirs('test/abRIO')
    os.makedirs('test/abLIO')
    os.makedirs('test/abIO')
    os.makedirs('test/abRLR')
    os.makedirs('test/abLLR')
    os.makedirs('test/abLR')
    os.makedirs('test/abRMR')
    os.makedirs('test/abLMR')
    os.makedirs('test/abMR')
    os.makedirs('test/abRIR')
    os.makedirs('test/abLIR')
    os.makedirs('test/abIR')
    os.makedirs('test/abRSO')
    os.makedirs('test/abLSO')
    os.makedirs('test/abSO')

    

#move file to folder directory
for i in random.sample(glob.glob('normal*'), 4):
    shutil.move(i, 'train/normal')

# for i in random.sample(glob.glob('abRSR*'), 17):
#     shutil.move(i, 'train/abRSR')

# for i in random.sample(glob.glob('abLSR*'), 17):
#     shutil.move(i, 'train/abLSR')

# for i in random.sample(glob.glob('abSR*'), 17):
#     shutil.move(i, 'train/abSR')

# for i in random.sample(glob.glob('abRIO*'), 17):
#     shutil.move(i, 'train/abRIO')

# for i in random.sample(glob.glob('abLIO*'), 17):
#     shutil.move(i, 'train/abLIO')

# for i in random.sample(glob.glob('abIO*'), 17):
#     shutil.move(i, 'train/abIO')

# for i in random.sample(glob.glob('abRLR*'), 17):
#     shutil.move(i, 'train/abRLR')

# for i in random.sample(glob.glob('abLLR*'), 17):
#     shutil.move(i, 'train/abLLR')

# for i in random.sample(glob.glob('abLR*'), 17):
#     shutil.move(i, 'train/abLR')

# for i in random.sample(glob.glob('abRMR*'), 17):
#     shutil.move(i, 'train/abRMR')

# for i in random.sample(glob.glob('abLMR*'), 17):
#     shutil.move(i, 'train/abLMR')

# for i in random.sample(glob.glob('abMR*'), 17):
#     shutil.move(i, 'train/abMR')

# for i in random.sample(glob.glob('abRIR*'), 17):
#     shutil.move(i, 'train/abRIR')

# for i in random.sample(glob.glob('abLIR*'), 17):
#     shutil.move(i, 'train/abLIR')

# for i in random.sample(glob.glob('abIR*'), 17):
#     shutil.move(i, 'train/abIR')

# for i in random.sample(glob.glob('abRSO*'), 17):
#     shutil.move(i, 'train/abRSO')

# for i in random.sample(glob.glob('abLSO*'), 17):
#     shutil.move(i, 'train/abLSO')

# for i in random.sample(glob.glob('abSO*'), 17):
#     shutil.move(i, 'train/abSO')


for i in random.sample(glob.glob('normal*'),1):
    shutil.move(i, 'test/normal')

# for i in random.sample(glob.glob('abRSR*'), 17):
#     shutil.move(i, 'test/abRSR')

# for i in random.sample(glob.glob('abLSR*'), 17):
#     shutil.move(i, 'test/abLSR')

# for i in random.sample(glob.glob('abSR*'), 17):
#     shutil.move(i, 'test/abSR')

# for i in random.sample(glob.glob('abRIO*'), 17):
#     shutil.move(i, 'test/abRIO')

# for i in random.sample(glob.glob('abLIO*'), 17):
#     shutil.move(i, 'test/abLIO')

# for i in random.sample(glob.glob('abIO*'), 17):
#     shutil.move(i, 'test/abIO')

# for i in random.sample(glob.glob('abRLR*'), 17):
#     shutil.move(i, 'test/abRLR')

# for i in random.sample(glob.glob('abLLR*'), 17):
#     shutil.move(i, 'test/abLLR')

# for i in random.sample(glob.glob('abLR*'), 17):
#     shutil.move(i, 'test/abLR')

# for i in random.sample(glob.glob('abRMR*'), 17):
#     shutil.move(i, 'test/abRMR')

# for i in random.sample(glob.glob('abLMR*'), 17):
#     shutil.move(i, 'test/abLMR')

# for i in random.sample(glob.glob('abMR*'), 17):
#     shutil.move(i, 'test/abMR')

# for i in random.sample(glob.glob('abRIR*'), 17):
#     shutil.move(i, 'test/abRIR')

# for i in random.sample(glob.glob('abLIR*'), 17):
#     shutil.move(i, 'test/abLIR')

# for i in random.sample(glob.glob('abIR*'), 17):
#     shutil.move(i, 'test/abIR')

# for i in random.sample(glob.glob('abRSO*'), 17):
#     shutil.move(i, 'test/abRSO')

# for i in random.sample(glob.glob('abLSO*'), 17):
#     shutil.move(i, 'test/abLSO')

# for i in random.sample(glob.glob('abSO*'), 17):
#     shutil.move(i, 'test/abSO')





os.chdir('../../')
