import os

# COMPUTER_NAME = os.environ['COMPUTERNAME']
COMPUTER_NAME = "Ubuntu@Azure"
print("Computer: ", COMPUTER_NAME)

WORKER_POOL_SIZE = 8

TARGET_VOXEL_MM = 1.00
MEAN_PIXEL_VALUE_NODULE = 41
LUNA_SUBSET_START_INDEX = 0
LUNA_SUBSET_END_INDEX = 10
SEGMENTER_IMG_SIZE = 320

BASE_DIR_SSD = "/home/ayokoyama/Project/DSB2017/kaggle_ndsb2017/"
# BASE_DIR_SSD = "E:/Workspace/Archaic/Holoeyes/kaggle_ndsb2017/"
BASE_DIR = "/home/ayokoyama/Project/DSB2017/kaggle_ndsb2017/"
# BASE_DIR = "E:/Workspace/Archaic/Holoeyes/kaggle_ndsb2017/"
EXTRA_DATA_DIR = "resources/"
NDSB3_RAW_SRC_DIR = BASE_DIR + "ndsb_raw/stage12/"
# NDSB3_RAW_SRC_DIR = "E:/Workspace/Archaic/Holoeyes/Data/DSB2017/stage1/"
LUNA16_RAW_SRC_DIR = BASE_DIR + "luna_raw/"
# LUNA16_RAW_SRC_DIR = "E:/Workspace/Archaic/Holoeyes/Data/LUNA16/"

NDSB3_EXTRACTED_IMAGE_DIR = BASE_DIR_SSD + "ndsb3_extracted_images/"
LUNA16_EXTRACTED_IMAGE_DIR = BASE_DIR_SSD + "luna16_extracted_images/"
NDSB3_NODULE_DETECTION_DIR = BASE_DIR_SSD + "ndsb3_nodule_predictions/"
