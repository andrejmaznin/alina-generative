from random import randint, choice
from typing import Tuple

from PIL import Image
from PIL.Image import Transpose


def generate_image(
    size: Tuple[int, int],
    background_rgb: Tuple[int, int, int]
) -> Image:
    img = Image.new('RGB', size=size, color=background_rgb)
    methods = [
        Transpose.FLIP_LEFT_RIGHT,
        Transpose.FLIP_TOP_BOTTOM,
        Transpose.ROTATE_180,
        Transpose.TRANSPOSE
    ]

    for _ in range(5):
        form = Image.open(f'data/{randint(1, 67)}.png')

        big_flag = max(form.size) > 1400

        if big_flag:
            form = form.resize(size)

        form = form.transpose(choice(methods))

        form_size = form.size

        if not big_flag:
            img.paste(form, (randint(0, size[0] - form_size[0]), randint(0, size[1] - form_size[1])), form)
        else:
            img.paste(form, (0, 0), form)

    img.save('output.png')
