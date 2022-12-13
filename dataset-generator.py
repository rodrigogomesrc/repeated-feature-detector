import sys
import os
import random
import numpy as np

def get_images_file_paths(images_path):
    photo_paths = os.listdir(images_path)
    return [os.path.join(images_path, photo_path) for photo_path in photo_paths]

def resize_image(image, resolution):
    return cv2.resize(image, (resolution, resolution))

def create_non_matching_images(images_path, quantity, grid_size):
    random_indices = get_n_random_indices(quantity, len(images_path), repeat=False)
    images = [get_resized_image(images_path[random_index], 64) for random_index in random_indices]
    return create_images_collage(images, grid_size, 64)

def create_matching_images(images_path, quantity, grid_size):
    random_indices = get_n_random_indices(quantity, len(images_path), repeat=True)
    images = [get_resized_image(images_path[random_index], 64) for random_index in random_indices]
    return create_images_collage(images, grid_size, 64)


def create_images_collage(images, grid_size, resolution):
    if len(images) < 1:
        return None

    while len(images) < grid_size * grid_size:
        images.append(get_black_image(resolution))

    for i in range(grid_size):
        image_line = images[0]
        for j in range(1, grid_size):
            image_line = np.concatenate((image_line, images[i * grid_size + j]), axis=1)
        if i == 0:
            collage = image_line
        else:
            collage = np.concatenate((collage, image_line), axis=0)

    return collage


def get_black_image(resolution):
    return np.zeros((resolution, resolution, 3), dtype=np.uint8)


def get_n_random_indices(quantity, max_value, repeat=False):
    if repeat:
        return [random.randint(0, max_value) for _ in range(quantity)]
    else:
        return random.sample(range(max_value), quantity)
    

def get_resized_image(path, resolution):
    image = cv2.imread(path)
    return resize_image(image, resolution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dataset-generator.py <entry-images-path>")
        exit(1)

    images_path = sys.argv[1]
