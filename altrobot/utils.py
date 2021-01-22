#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json

stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')

from tensorflow.keras.models import model_from_json

sys.stderr = stderr


def banner():
    with open('resources/banner', 'r') as f:
        for line in f:
            print(line.splitlines()[0])


def load_model(model_name):
    with open(f'resources/keras_models/{model_name}.json') as f:
        return model_from_json(json.load(f))


def save_model(model, name):
    with open(f'resources/keras_models/{name}.json', 'w') as f:
        json.dump(model.to_json(), f)


def progress_bar(iteration, total, prefix = '', suffix = '', decimals = 2, length = 100, fill = '#'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + ' ' * (length - filled_length)
    # █

    print('\r%s [%s] %s%% %s' % (prefix, bar, percent, suffix), end = '\r')

    if iteration == total:
        print()
