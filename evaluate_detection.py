from detector import has_repeated_patterns
import sys
import os
import cv2

def evaluate(path):
    images_evaluated = 0
    images_got_right = 0

    matching_folder = os.path.join(path, "matching")
    non_matching_folder = os.path.join(path, "non-matching")

    matching_images = os.listdir(matching_folder)
    non_matching_images = os.listdir(non_matching_folder)

    for image in matching_images:
        image_path = os.path.join(matching_folder, image)
        print("Evaluating image: {}".format(image_path))
        image = cv2.imread(image_path)
        if has_repeated_patterns(image):
            images_got_right += 1
        images_evaluated += 1

    for image in non_matching_images:
        image_path = os.path.join(non_matching_folder, image)
        print("Evaluating image: {}".format(image_path))
        image = cv2.imread(image_path)
        if not has_repeated_patterns(image):
            images_got_right += 1
        images_evaluated += 1

    print("Accuracy: {}%".format(images_got_right / images_evaluated * 100))


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 evaluate_detection.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    evaluate(folder_path)