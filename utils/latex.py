from PIL import Image
import re
import numpy as np
from IPython.display import display, Math, Latex
import random
from matplotlib import pyplot as plt
from scipy.ndimage import rotate
import random

def crop_to_formula(image, padding = 30, max_width = 6, line_colors = [(240, 0, 0, 150),
                                                                        (0, 0, 0, 180),
                                                                        (30, 30, 30, 150)], max_lines = 5):
    # Image: 4 channel image with alpha.
    # Convert black pixels to white pixels.
    data = np.array(image)
    red, green, blue, alpha = data.T
    black_areas = (red < 10) & (blue < 10) & (green < 10)
    # Convert alpha to white.
    data[..., -1] = 255
    # Crop a box around the area that contains black pixels.
    coords = np.argwhere(black_areas)
    x0, y0 = coords.min(axis=0)
    x1, y1 = coords.max(axis=0) + 1
    # Add padding.
    x0 = max(0, x0 - padding)
    y0 = max(0, y0 - padding)
    x1 = min(image.width, x1 + padding)
    y1 = min(image.height, y1 + padding)

    # Image augmentation
    # Draw lines randomly
    image = data[y0:y1, x0:x1]
    mask = np.zeros_like(image)
    rotate_rads = np.random.random() * 10 - 5
    line_width = np.random.randint(1, max_width)
    for i in range(np.random.randint(1, max_lines)):
        center_coords = np.random.randint(0, mask.shape[0])
        # print(center_coords, max(0, center_coords - line_width // 2), min(mask.shape[0], center_coords + line_width // 2))
        mask[max(0, center_coords - line_width // 2):min(mask.shape[0], center_coords + line_width // 2), :] = 1
    line_color = random.choice(line_colors)
    # plt.imshow(mask * line_color)
    # plt.show()
    mask = rotate(mask, rotate_rads, reshape = False)
    image = image * (mask == 0) + mask * line_color

    image = Image.fromarray(image.astype('uint8'), 'RGBA')
    return image.convert('RGB')

def renderedLaTeXLabelstr2Formula(label: str):
    # We're matching \\label{...whatever} and removing it
    label = re.sub(r"\\label\{[^\}]*\}", "", label)
    # We match \, and remove it.
    label = re.sub(r"\\,", "", label)
    return label

def display_formula(latex: str):
    # Remove \mbox{...} - not supported by the inline MathJax renderer
    parsed_latex = re.sub(r"\\mbox\{[^\}]*\}", "", latex)
    display(Math(parsed_latex))