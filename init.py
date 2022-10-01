import os

from dotenv import load_dotenv


from detector import neural_network


load_dotenv(dotenv_path='.env')
result_storage_path = os.environ.get("result_storage_path")

def init():
    if not os.path.exists(result_storage_path):
        os.mkdir(result_storage_path)

    detector = neural_network()

    return detector


if __name__ == '__main__':
    init()
