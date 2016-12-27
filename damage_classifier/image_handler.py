"""API to handle image data and associated labels."""

import csv

import classifier_constants as cc
import gtk.gdk
import numpy as np
import pandas as pd

#debugging
from matplotlib import pyplot as plt

class Data():

    def __init__(self, path):
        self.current_index = 0
        self.data = self.load_images_from_csv(path)

    def _load_images(self, path):
        """Converts a png image to a pixel array, normalizes from 0 to 1.

        For two frames.

        Args:
            path: str, location of the frames in the form base_name1_name2
        Returns:
            np pixel array
        """
        # Get the frame paths.
        print path
        path_args = path.split('_')
        frame_curr_path = path_args[0] + '/' +  path_args[1] + '.png'
        frame_prev_path = path_args[0] + '/' + path_args[2] + '.png'

        # Get the frames.
        pb = gtk.gdk.pixbuf_new_from_file(frame_curr_path)
        pix = np.fromstring(pb.get_pixels(), dtype=np.uint8)[-1*cc.IMAGE_SIZE:]

        # Debugging
        # pix = pix.reshape(cc.HEIGHT, cc.WIDTH, 3)
        # plt.imshow(pix, interpolation='nearest')
        # plt.show()

        pb = gtk.gdk.pixbuf_new_from_file(frame_prev_path)
        pix = np.append(pix, np.fromstring(pb.get_pixels(),
                                           dtype=np.uint8)[-1*cc.IMAGE_SIZE:])

        return pix/cc.MAX_PIX_VAL

    def _load_csv(self, path):
        """Loads the csv map of images and labels. Get names of maps from csv.

        Args:
            path: str, location of the csv map.
        Returns:
            {filename : label}
        """
        csv_df = pd.read_csv(path)
        d = {'filepaths': csv_df['base'] + '_' + csv_df['frame_curr'].map(str) +
                '_' + csv_df['frame_prev'].map(str),
             'label': csv_df['onehot_index']}
        return pd.DataFrame(d)

    def _load_onehot(self, index):
        """Returns a one hot numpy array encoded from index.

        Args:
            index: which num to make one hot
        """
        onehot = np.zeros(cc.ONEHOT_SIZE, dtype=np.int)
        onehot.itemset(index, 1)
        return onehot

    def get_next_batch(self, size):
        """Returns the next batch of size of image, label pairs.

        Loops around if needed.

        Args:
            size: int, size of next batch
        """
        prev_index = self.current_index
        self.current_index += size
        if self.current_index >= len(self.data):
            self.current_index -= len(self.data)
            return pd.concat([self.data.iloc[prev_index:],
                              self.data.iloc[:self.current_index]])
        else:
            return self.data.iloc[prev_index:self.current_index]

    def load_images_from_csv(self, path):
        """Loads all images and labels from csv map.

        Args:
            path: str, location of the csv map.
        Returns:
            [([pixel array], label)]
        """

        print "Opening CSV from %s" % path
        csv_df = self._load_csv(path)

        d = {'data': csv_df['filepaths'].map(self._load_images),
             'label': csv_df['label'].map(self._load_onehot)}

        data_df = pd.DataFrame(d)

        print "Data size: %d" % len(data_df)

        return data_df
