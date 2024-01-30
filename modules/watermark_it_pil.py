import os
from PIL import Image, ImageDraw, ImageFont
import random

from static.watermark_it_data import *


class PilImage:
    """A class for adding watermarks to images using PIL.
    Use with watermark_it_main.py's Tkinter GUI.

    Attributes:
        color (tuple): RGB color tuple for the watermark text.
        opacity (int): Alpha value for transparency in the watermark.
        font_size (int): Font size of the watermark text.
        font_name (str): Font type for the watermark text.
        rows (int): Number of rows for the watermark.
        cols (int): Number of columns for the watermark.
        text (str): Text content of the watermark.
        path_input (str): Input path of the image to watermark.
        path_output (str): Output path for the watermarked image.
    """

    def __init__(self, path: str, text: str = "©2024", path_output: str = "watermark_it"):
        """Initialize PilImage object with default values.

        Args:
            path (str): Input path of the image to watermark.
            text (str, optional): Text content of the watermark. Defaults to "©2024".
            path_output (str, optional): Output path for the watermarked image. Defaults to "watermark_it".
        """
        self.path_input = path
        self.text = text
        self.path_output = path_output
        self.color = (255, 255, 255)
        self.opacity = 96
        self.font_size = 40
        self.font_name = "arial"
        self.rows = 20
        self.cols = 6

    @staticmethod
    def __dict_vals_to_list(*args: dict):
        """Static and private method. Used to populate font list.

        Args:
            :var *args: Dictionary of readable_name(keys)/tk_name(values): :type: dict, required
        """
        res_list = list()
        for i in args:
            res_list.extend(list(i.values()))
        return res_list

    def draw_text(self, draw_obj: ImageDraw, base_size: tuple, font: ImageFont):
        """Draw watermark text on a PIL image.

        Args:
            draw_obj (ImageDraw): ImageDraw object for drawing on the image.
            base_size (tuple): Size of the base image.
            font (ImageFont): Font object for drawing text.
        """
        x = base_size[0]
        x_parts = base_size[0] // self.cols
        y_parts = base_size[1] // self.rows
        for col_ind in range(self.cols):
            y = base_size[1]
            x -= x_parts
            for row_ind in range(self.rows):
                y -= y_parts
                draw_obj.text((x, y),
                              self.text,
                              font=font,
                              fill=(self.color[0], self.color[1], self.color[2], self.opacity))

    def create_watermark(self):
        """Build PIL.Image object and overlay watermark with draw_text method."""
        with Image.open(self.path_input).convert("RGBA") as base:
            text_layer = Image.new("RGBA", base.size, (255, 255, 255, 0))
            font = ImageFont.truetype(self.font_name, self.font_size)
            draw_obj = ImageDraw.Draw(text_layer)
            now_str = [i for i in now_string if i.isdigit()]
            suffix = "".join(random.sample(now_str, k=4))
            self.draw_text(draw_obj, base.size, font)
            final = Image.alpha_composite(base, text_layer)

            input_dir = os.path.dirname(self.path_input)

            output_path = os.path.join(input_dir, f"watermark_it_{suffix}.png")
            final.convert("RGB").save(output_path, "PNG")
            quit()


if __name__ == "__main__":
    water = PilImage("../static/paris_test.jpg", "PIL Module")
    water.create_watermark()
