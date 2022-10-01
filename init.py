import os

from config import result_storage_path
from detector import neural_network


def init():
    if not os.path.exists(result_storage_path):
        os.mkdir(result_storage_path)

    detector = neural_network()

    return detector


if __name__ == '__main__':
    init()
