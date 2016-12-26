"""Creates a TF model to make moves given last four frames of input.

Functions as main for training. Stores the model for future testing.
"""

import move_constants as mc
import tensorflow as tf
import numpy as np

import time


