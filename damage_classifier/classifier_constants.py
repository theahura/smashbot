"""Holds constant variable data across classifier model."""

# File Locations.
PATH_TO_CSV_MAP = ''
PATH_TO_MODEL = ''

# Image Constants.
WIDTH = 1000
HEIGHT = 1000

# Hyper Parameters. 
LEARNING_RATE = 0.001
TRAINING_EPOCHS = 15
BATCH_SIZE = 100
DISPLAY_STEP = 1

# Network Config Parameters. 
IMAGE_SIZE = WIDTH * HEIGHT
NUM_EXAMPLES = 500  # Number of images.
MAX_DAMAGE = 999  # Used as number of classes.
N_HIDDEN_1 = 256
N_HIDDEN_2 = 256
