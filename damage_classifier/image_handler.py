"""API to handle image data and associated labels."""

import csv

import gtk.gdk
import numpy as np
import pandas as pd


class Data():

    def __init__(self, path):
        self.current_index = 0
        self.data = self.load_images_from_csv(path)

    def _load_image(self, path):
        """Converts a png image to a pixel array.
        
        Args:
            path: str, location of png image
        Returns:
            np pixel array
        """
        pb = gtk.gdk.pixbuf_new_from_file(path)
        return np.fromstring(pb.get_pixels(), dtype=np.uint8)

    def _load_csv(self, path):
        """Loads the csv map of images and labels.
        
        Args:
            path: str, location of the csv map.
        Returns:
            {filename : label}
        """
        csv_df = pd.read_csv(path)
        d = {'filepath': csv_df['base'] + csv_df['name'].map(str) + '.png',
             'label': csv_df['label']}
        return pd.DataFrame(d)

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
            return self.data[prev_index:] + self.data[:self.current_index]
        else:
            return self.data[prev_index:self.current_index]

    def load_images_from_csv(self, path):
        """Loads all images and labels from csv map.

        Args:
            path: str, location of the csv map.
        Returns:
            [([pixel array], label)]
        """

        print "Opening CSV from %s" % path
        csv_df = self._load_csv(path)

        d = {'data': csv_df['filepath'].map(self._load_image),
             'label': csv_df['label']}

        data_df = pd.DataFrame(d)

        print "Data size: %d" % len(data_df)

        return data_df
