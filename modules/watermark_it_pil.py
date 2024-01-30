import os
from PIL import Image, ImageDraw, ImageFont
import random

from static.watermark_it_data import *


class PilImage:
    """A class for adding watermarks to images using PIL.

    Attributes:
        color (tuple): RGB color tuple for the watermark text.
        alpha (int): Alpha value for transparency in the watermark.
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
        self.alpha = 96
        self.font_size = 40
        self.font_name = "arial"
        self.rows = 20
        self.cols = 6

    def change_color(self, color: str = "white"):
        """Set the color of the watermark text.

        Args:
            color (str): Desired color of watermark text. Defaults to "white".
        """
        if not color or color != "black":
            self.color = (255, 255, 255)
        else:
            self.color = (0, 0, 0)

    def change_font_size(self, font_size: int):
        """Set the font size of watermark text.

        Args:
            :var font_size: Desired size of watermark text. :type: int, required
        """
        if font_size and type(font_size) is int and 8 <= font_size <= 72:
            self.font_size = font_size
        else:
            self.font_size = 40

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

    def change_font_name(self, font_name: str = "arial"):
        """Get Tkinter font name from readable user font name.

        Args:
            font_name (str, optional): Desired font name. Defaults to "arial".
        """
        if type(font_name) is str and font_name:
            font = fonts_reg[font_name]
        else:
            font = "arial"
        self.font_name = font

    def change_rows(self, rows: int):
        """Set the number of watermark rows.

        Args:
            :var rows: Number of watermark rows. type: int, required
        """
        if rows and type(rows) is int:
            self.rows = rows
        else:
            self.rows = 20

    def change_cols(self, cols: int):
        """Set the number of watermark rows.

        Args:
            :var cols: Number of watermark rows. type: int, required
        """
        if cols and type(cols) is int:
            self.cols = cols
        else:
            self.cols = 6

    def change_alpha(self, alpha: int):
        """Allows user to adjust opacity of watermark text.

        Args:
            :var alpha: Number of watermark rows. type: int, required
        """
        if type(alpha) is not int or not alpha:
            self.alpha = 128
        else:
            self.alpha = alpha

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
                              fill=(self.color[0], self.color[1], self.color[2], self.alpha))

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
    water = PilImage("../static/paris_test.jpg", "©2024")
    water.create_watermark()
