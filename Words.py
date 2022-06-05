# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class WordlistManager:

    def __init__(self, name_file):
        self.name_file = name_file
        self.words_dictionary = {}

    def read_file(self):
        f = open(self.name_file, encoding='utf-8')
        while True:
            line = f.readline()
            if not line:
                break
            x = line.split(" ", 1)
            self.words_dictionary[x[1]] = x[0]
        f.close()

    def print_dict(self):
        for k, v in self.words_dictionary.items():
            print("{" + v + "} " + k)
