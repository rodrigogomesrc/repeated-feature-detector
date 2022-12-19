import cv2
import numpy as np
import sys


def divide_images_into_sections(image, n_sections):
    height, width, _ = image.shape
    height_section = height // n_sections
    width_section = width // n_sections
    sections = []
    for i in range(n_sections):
        for j in range(n_sections):
            sections.append(image[i * height_section: (i + 1) * height_section, j * width_section: (j + 1) * width_section, :])
    return sections


def match_template(image, template):
    
    bw_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bw_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(bw_image, bw_template, cv2.TM_SQDIFF_NORMED)
    min_val,_,_,_ = cv2.minMaxLoc(result)
    return min_val
    

def has_repeated_patterns(image, n_sections=4):
    sections = divide_images_into_sections(image, n_sections)
    matches = []
    for i in range(len(sections)):
        for j in range(i + 1, len(sections)):
            matches.append(match_template(sections[i], sections[j]))

    return min(matches) < 0.1


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 detector.py <image_path> <number_of_sections>")
        sys.exit(1)

    image_path = sys.argv[1]
    sections = int(sys.argv[2])
    image = cv2.imread(image_path)

    if image is None:
        print("Invalid image path.")
        sys.exit(1)

    if has_repeated_patterns(image, sections):
        print("Existe padrão repetido")

    else:
        print("Não existe padrão repetido")