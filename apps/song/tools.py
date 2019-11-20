import os
import uuid


def get_songs_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.name, ext)
    return os.path.join("songs", filename)