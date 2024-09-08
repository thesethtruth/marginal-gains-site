import os
from PIL import Image


def compress(image_file, quality, resize=None):

    filepath = os.path.join(os.getcwd(), image_file)
    image = Image.open(filepath)

    if resize is not None:
        image = image.resize(resize)

    image.save("image-file-compressed.png", "JPEG", optimize=True, quality=quality)
