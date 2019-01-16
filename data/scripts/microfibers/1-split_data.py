import os
import glob
import random

TRAIN_RATIO = 0.8

DATA_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir,
                                        os.path.pardir, os.path.pardir))
IMG_DIR = os.path.join(DATA_DIR, 'raw', 'microfibers')
METADATA_DIR = os.path.join(DATA_DIR, 'metadata', 'microfibers')

try:
    os.makedirs(METADATA_DIR)
except BaseException:
    pass

image_paths = glob.glob(os.path.join(IMG_DIR, '*_rgb.png'))
image_names = [p.split('/')[-1].split('_')[0] for p in image_paths]
random.seed(37)
random.shuffle(image_names)
index = int(TRAIN_RATIO * len(image_names))
train = image_names[:index]
val = image_names[index:]

for name, samples in [('training', train), ('validation', val)]:
    path = os.path.join(METADATA_DIR, '{}.lst'.format(name))
    with open(path, 'w') as f:
        f.writelines('\n'.join(samples))
