"""Holds constant variable data across classifier model."""

# File Locations.
PATH_TO_CSV_MAP = './data/map.csv'
PATH_TO_MODEL = './damage-classifier-model.ckpt'
PATH_TO_DATA = './data'

# Image Constants.
WIDTH = 660
HEIGHT = 530

# Data gather.
NUM_IMAGE_GRAB = 300

# Hyper Parameters. 
LEARNING_RATE = 0.001
TRAINING_EPOCHS = 15
BATCH_SIZE = 1
DISPLAY_STEP = 1

# Network Config Parameters. 
IMAGE_SIZE = WIDTH * HEIGHT * 3 # RGB.
NUM_EXAMPLES = 2  # Number of images.
MAX_DAMAGE = 999  # Used as number of classes.
N_HIDDEN_1 = 256
N_HIDDEN_2 = 256
