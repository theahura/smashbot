"""API to handle image data and associated labels."""

import csv

import gtk.gdk
import numpy as np


class Data():

    def __init__(self, path):
        self.current_index = 0
        self.data = load_images_from_csv(path)

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
        csv_dict = {}
        with open(path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                csv_dict['%s%s.png' % (row['base'],
                                       row['name'])] = int(row['label'])

        return csv_dict

    def get_next_batch(self, size):
        """Returns the next batch of size of image, label pairs.

        Args:
            size: int, size of next batch
        """
        prev_index = self.current_index
        self.current_index += size
        return self.data[prev_index:self.current_index]

    def load_images_from_csv(self, path):
        """Loads all images and labels from csv map.

        Args:
            path: str, location of the csv map.
        Returns:
            [([pixel array], label)]
        """
        csv_dict = self._load_csv(path)

        data = []
        for path, label in csv_dict.iteritems():
            data.append((self._load_image(path), label))

        return data
