"""Holds constant variable data across classifier model."""

# File Locations.
PATH_TO_CSV_MAP = './data/map.csv'
PATH_TO_MODEL = './'
MODEL_NAME = 'model.ckpt'
PATH_TO_DATA = './data'

# Image Constants (cropped images).
WIDTH = 660
HEIGHT = 109
RGB = 3
MAX_PIX_VAL = 255
IMAGE_SIZE = WIDTH * HEIGHT * RGB

# Data gather (full images).
NUM_IMAGE_GRAB = 10000
GATHER_WIDTH = WIDTH # 660.
GATHER_HEIGHT = HEIGHT*5 # 545.
NUM_FIELDS = 4  # Fields in the data.
SECPERFRAME = 0.3 # How fast to gather.
FULL_IMAGE_SIZE = GATHER_WIDTH * GATHER_HEIGHT * RGB

# Hyper Parameters. 
LEARNING_RATE = 0.001
TRAINING_EPOCHS = 200
BATCH_SIZE = 50
DISPLAY_STEP = 10

# Network Config Parameters. 
NUM_EXAMPLES = 168  # Number of images.
N_HIDDEN_1 = 109
N_HIDDEN_2 = 660
ONEHOT_SIZE = 2
NUM_INPUT_NEURONS = IMAGE_SIZE*2
NUM_OUTPUT_NEURONS = ONEHOT_SIZE
