"""Holds constant variable data across classifier model."""

# File Locations.
PATH_TO_CSV_MAP = './data/map.csv'
PATH_TO_MODEL = './damage-classifier-model.ckpt'
PATH_TO_DATA = './data'

# Image Constants.
WIDTH = 660
HEIGHT = 109
RGB = 3

# Data gather.
NUM_IMAGE_GRAB = 10000
GATHER_WIDTH = WIDTH
GATHER_HEIGHT = HEIGHT*5

# Hyper Parameters. 
LEARNING_RATE = 0.0001
TRAINING_EPOCHS = 10
BATCH_SIZE = 58
DISPLAY_STEP = 1

# Network Config Parameters. 
IMAGE_SIZE = WIDTH * HEIGHT * RGB
NUM_EXAMPLES = 58  # Number of images.
MAX_DAMAGE = 999  # Used as number of classes.
N_HIDDEN_1 = 109
N_HIDDEN_2 = 660
