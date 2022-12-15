import sys
import os
import random
from dataset_generator import get_images_file_paths
from dataset_generator import create_directory_if_not_exists


def shuffle_datasets(dataset_path, new_dataset_path):
    shuffle_dataset(dataset_path, new_dataset_path, "matching")
    shuffle_dataset(dataset_path, new_dataset_path, "non-matching")


def shuffle_dataset(dataset_path, new_dataset_path, folder_name):
    files = get_images_file_paths(os.path.join(dataset_path, folder_name))
    random.shuffle(files)
    create_directory_if_not_exists(os.path.join(new_dataset_path, folder_name))

    for i, f in enumerate(files):
        new_file_name = "{}-{}.jpg".format(folder_name, i + 1)
        os.system("cp {} {}".format(f, os.path.join(new_dataset_path, folder_name, new_file_name)))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 shuffle-dataset.py <new-dataset-path>")
        exit(1)

    new_dataset_path = sys.argv[1]
    shuffle_datasets("generated-dataset", new_dataset_path)