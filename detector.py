import cv2
import numpy as np
import sys


def divide_images_into_sections(image, n_sections):
    print(image.shape)
    height, width, _ = image.shape
    section_height = height // n_sections
    section_width = width // n_sections
    sections = []
    for i in range(n_sections):
        for j in range(n_sections):
            section = image[i * section_height:(i + 1) * section_height, j * section_width:(j + 1) * section_width, :]
            sections.append(section)

    return sections


def get_image_features(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (8, 8))
    image = np.float32(image)
    image = cv2.dct(image)
    image = image[:4, :4]
    image = image.flatten()
    image = image / np.sum(image)
    return image


def does_template_match(image, template):
    image_features = get_image_features(image)
    template_features = get_image_features(template)
    distance = np.linalg.norm(image_features - template_features)
    return distance < 0.1


def has_repeated_patterns(image):
    sections = divide_images_into_sections(image, 4)
    for i in range(len(sections)):
        for j in range(i + 1, len(sections)):
            if does_template_match(sections[i], sections[j]):
                return True

    return False


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 detector.py <image_path> <number_of_sections>")
        sys.exit(1)

    image_path = sys.argv[1]
    sections = int(sys.argv[2])
    image = cv2.imread(image_path)

    if has_repeated_patterns(image):
        print("The image contains repeated patterns.")

    else:
        print("The image does not contain repeated patterns.")