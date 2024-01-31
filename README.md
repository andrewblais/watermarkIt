# WatermarkIt Documentation

A Pythonic OOP project allowing the user take an image and save a watermarked copy.

Utilizes a Tkinter GUI and the PIL module on the backend.

Run via the `watermark_it_main.py` along with your favorite Python interpreter, or use the portable .exe installer!

---

I've got it working, basically, but more work needs to be done to ensure functionality and a good UX.

Windows portable .exe to be added shortly.

Next update will include (more) thorough error-checking and GUI improvements.

---

Public Domain files I used:

Icon file: https://commons.wikimedia.org/wiki/File:Pok%C3%A9mon_Water_Type_Icon.svg

Earth test image: https://commons.wikimedia.org/wiki/File:ISS046-E-36381_-_View_of_Earth.jpg

Paris test image: https://commons.wikimedia.org/wiki/File:Paris_-_Eiffelturm_und_Marsfeld2.jpg

---

### Documentation:

_Printed via `help(WatermarkItGui)`:_

```markdown
Help on class WatermarkItGui in module __main__:

class WatermarkItGui(builtins.object)
 |  WatermarkItGui(root, gui_w: int = 475, gui_h: int = 895, move_x: int = 0, move_y: int = 0)
 |  
 |  A simple GUI application for creating watermarked images with Tkinter(front) and PIL(back).
 |  
 |  Attributes:
 |      root (Tk): The main Tkinter window.
 |      path_input (str): The path of the input image.
 |      path_output (str): The path for the watermarked image output.
 |      image_obj (PilImage): The PilImage object for creating watermarks.
 |      watermark_entry_var (StringVar): Tkinter StringVar for the watermark text.
 |      font_type_var (StringVar): Tkinter StringVar for the selected font type.
 |      font_color_var (IntVar): Tkinter IntVar for the selected font color (1 for white, 0 for black).
 |      font_size_var (IntVar): Tkinter IntVar for the selected font size.
 |      rows_var (IntVar): Tkinter IntVar for the selected number of rows in the watermark.
 |      columns_var (IntVar): Tkinter IntVar for the selected number of columns in the watermark.
 |      opacity_var (IntVar): Tkinter IntVar for the selected opacity percentage.
 |  
 |  Methods:
 |      browse_file(): Command for the 'Browse' button to select an input image.
 |      about_popup(): Command for the 'About' button to display information about the application.
 |      help_popup(): Command for the 'Help' button to display help information.
 |      watermark_it(): Command for the 'Create Watermark' button to create a watermarked image.
 |      setup_gui(): Configures and sets up the Tkinter GUI elements.
 |  
 |  Methods defined here:
 |  
 |  __init__(self, root, gui_w: int = 475, gui_h: int = 895, move_x: int = 0, move_y: int = 0)
 |      Initialize the WatermarkGui object with default values and set up the GUI.
 |      
 |      Args:
 |          root (Tk): The main Tkinter window.
 |  
 |  browse_file(self)
 |      Command for `Browse` button.
 |  
 |  increment_row(self)
 |  
 |  setup_gui(self)
 |  
 |  watermark_it(self)
 |      Command for `Create Watermark` button. Imports PILWatermark class. Creates watermark.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  about_popup()
 |      Command for `About` button.
 |  
 |  color_to_tuple(color_var)
 |  
 |  convert_opacity(opacity_100)
 |  
 |  get_tk_font_name(font_name: str = 'Arial Italic')
 |      Get Tkinter font name from readable user font name.
 |      
 |      Args:
 |          font_name (str, optional): Desired font name. Defaults to "arial".
 |  
 |  help_popup()
 |      Command for `Help` button.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
```

_Printed via `help(PilImage)`:_

```markdown
Help on class PilImage in module __main__:

class PilImage(builtins.object)
 |  PilImage(path: str, text: str = '©2024', path_output: str = 'watermark_it')
 |  
 |  A class for adding watermarks to images using PIL.
 |  Use with watermark_it_main.py's Tkinter GUI.
 |  
 |  Attributes:
 |      color (tuple): RGB color tuple for the watermark text.
 |      opacity (int): Alpha value for transparency in the watermark.
 |      font_size (int): Font size of the watermark text.
 |      font_name (str): Font type for the watermark text.
 |      rows (int): Number of rows for the watermark.
 |      cols (int): Number of columns for the watermark.
 |      text (str): Text content of the watermark.
 |      path_input (str): Input path of the image to watermark.
 |      path_output (str): Output path for the watermarked image.
 |  
 |  Methods defined here:
 |  
 |  __init__(self, path: str, text: str = '©2024', path_output: str = 'watermark_it')
 |      Initialize PilImage object with default values.
 |      
 |      Args:
 |          path (str): Input path of the image to watermark.
 |          text (str, optional): Text content of the watermark. Defaults to "©2024".
 |          path_output (str, optional): Output path for the watermarked image. Defaults to "watermark_it".
 |  
 |  create_watermark(self)
 |      Build PIL.Image object and overlay watermark with draw_text method.
 |  
 |  draw_text(self, draw_obj: <module 'PIL.ImageDraw' from 'C:\\Users\\anb20\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\PIL\\ImageDraw.py'>, base_size: tuple, font: <module 'PIL.ImageFont' from 'C:\\Users\\anb20\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\PIL\\ImageFont.py'>)
 |      Draw watermark text on a PIL image.
 |      
 |      Args:
 |          draw_obj (ImageDraw): ImageDraw object for drawing on the image.
 |          base_size (tuple): Size of the base image.
 |          font (ImageFont): Font object for drawing text.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
```

---

#### _I created this project in completing Professional Portfolio Project: Assignment 4, "Image Watermarking Desktop

App" from [Angela Yu 100 Days of Code](https://www.udemy.com/course/100-days-of-code/):_

# Assignment: Image Watermarking Desktop App

## Day 85 - PPP, Assignment 4: Image Watermarking Desktop App

_A Desktop program where you can upload images and add a watermark._

### Assignment instructions

Using what you've learned about Tkinter, you will create a desktop application with a
Graphical User Interface (GUI) where you can upload an image and use Python to add a watermark
logo/text.

Normally, you would have to use an image editing software like Photoshop to add the watermark,
but your program is going to do it automatically.

Use case: e.g you want to start posting your photos to Instagram but you want to add your
website to all the photos, you can now use your software to add your website/logo automatically
to any image.

A similar online service is: https://watermarkly.com/

You might need:

https://pypi.org/project/Pillow/

https://docs.python.org/3/library/tkinter.html

...and some Googling.
