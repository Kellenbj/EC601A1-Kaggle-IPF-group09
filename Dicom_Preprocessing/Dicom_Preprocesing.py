import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import pydicom
#import scipy.ndimage
#import gdcm

#from skimage import measure
#from mpl_toolkits.mplot3d.art3d import Poly3DCollection
#from skimage.morphology import disk, opening, closing
#from tqdm import tqdm

#from IPython.display import HTML
#from PIL import Image

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

from os import listdir, mkdir

listdir('location of file')

basepath = 'location of file'
listdir(basepath)

#loading csv files
train = pd.read_csv(basepath + "train.csv")
test = pd.read_csv(basepath + "test.csv")

train.shape

train.head()

if basepath == "C:/Users/Poras/Desktop/osic-pulmonary-fibrosis-progression/":
    train["dcm_path"] = basepath + "train/" + train.Patient + "/"
else:
    train["dcm_path"] = basepath + "train/" + train.StudyInstanceUID + "/" + train.SeriesInstanceUID

def load_scans(dcm_path):
    if basepath == "../input/osic-pulmonary-fibrosis-progression/":
        # in this competition we have missing values in ImagePosition, this is why we are sorting by filename number
        files = listdir(dcm_path)
        file_nums = [np.int(file.split(".")[0]) for file in files]
        sorted_file_nums = np.sort(file_nums)[::-1]
        slices = [pydicom.dcmread(dcm_path + "/" + str(file_num) + ".dcm" ) for file_num in sorted_file_nums]
    else:
        # otherwise we sort by ImagePositionPatient (z-coordinate) or by SliceLocation
        slices = [pydicom.dcmread(dcm_path + "/" + file) for file in listdir(dcm_path)]
        slices.sort(key = lambda x: float(x.ImagePositionPatient[2]))
    return slices

example = train.dcm_path.values[0]
scans = load_scans(example)

scans[0]


fig, ax = plt.subplots(1,2,figsize=(20,5))
for n in range(10):
    image = scans[n].pixel_array.flatten()
    rescaled_image = image * scans[n].RescaleSlope + scans[n].RescaleIntercept
    sns.distplot(image.flatten(), ax=ax[0]);
    sns.distplot(rescaled_image.flatten(), ax=ax[1])
ax[0].set_title("Raw pixel array distributions for 10 examples")
ax[1].set_title("HU unit distributions for 10 examples");

def set_outside_scanner_to_air(raw_pixelarrays):
    # in OSIC we find outside-scanner-regions with raw-values of -2000.
    # Let's threshold between air (0) and this default (-2000) using -1000
    raw_pixelarrays[raw_pixelarrays <= -1000] = 0
    return raw_pixelarrays


def transform_to_hu(slices):
    images = np.stack([file.pixel_array for file in slices])
    images = images.astype(np.int16)

    images = set_outside_scanner_to_air(images)

    # convert to HU
    for n in range(len(slices)):

        intercept = slices[n].RescaleIntercept
        slope = slices[n].RescaleSlope

        if slope != 1:
            images[n] = slope * images[n].astype(np.float64)
            images[n] = images[n].astype(np.int16)

        images[n] += np.int16(intercept)

    return np.array(images, dtype=np.int16)

hu_scans = transform_to_hu(scans)

fig, ax = plt.subplots(1,4,figsize=(20,3))
ax[0].set_title("Original CT-scan")
ax[0].imshow(scans[0].pixel_array, cmap="bone")
ax[1].set_title("Pixelarray distribution");
sns.distplot(scans[0].pixel_array.flatten(), ax=ax[1]);

ax[2].set_title("CT-scan in HU")
ax[2].imshow(hu_scans[0], cmap="bone")
ax[3].set_title("HU values distribution");
sns.distplot(hu_scans[0].flatten(), ax=ax[3]);

for m in [0,2]:
    ax[m].grid(False)
