from datetime import datetime as dt
from random import randint

fonts_list = ['Arial', 'Arial Bold', 'Arial Bold Italic', 'Arial Italic',
              'Comic', 'Comic Bold', 'Comic Italic',
              'Courier', 'Courier Bold', 'Courier Bold Italic', 'Courier Italic',
              'Georgia', 'Georgia Bold',
              'Times', 'Times Bold', 'Times Bold Italic', 'Times Italic',
              'Trebuchet', 'Trebuchet Bold Italic', 'Trebuchet Italic',
              'Verdana', 'Verdana Bold']

fonts_dict = {"arial": "arial",
              "times": "times",
              "comic": "comic",
              "trebuchet": "trebuc",
              "courier": "cour",
              "verdana": "verdana",
              "georgia": "georgia"}

fonts_reg = {i: fonts_dict[i] + ".ttf" for i in fonts_dict}
fonts_b = {i: fonts_dict[i] + "bd.ttf" for i in fonts_dict if i not in ["verdana", "georgia"]}
fonts_i = {i: fonts_dict[i] + "i.ttf" for i in fonts_dict if i != "trebuchet"}
fonts_bi = {i: fonts_dict[i] + "bi.ttf" for i in fonts_dict if i not in ["comic", "verdana", "georgia"]}

font_convert = {'Arial': "arial.ttf",
                'Arial Bold': "arialbd.ttf",
                'Arial Bold Italic': "arialbi.ttf",
                'Arial Italic': "ariali.ttf",
                'Comic': "comic.ttf",
                'Comic Bold': "comicbd.ttf",
                'Comic Italic': "comici.ttf",
                'Courier': "cour.ttf",
                'Courier Bold': "courbd.ttf",
                'Courier Bold Italic': "courbi.ttf",
                'Courier Italic': "couri.ttf",
                'Georgia': "georgia.ttf",
                'Georgia Bold': "georgiabd.ttf",
                'Times': "times.ttf",
                'Times Bold': "times",
                'Times Bold Italic': "timesbi.ttf",
                'Times Italic': "timesi.ttf",
                'Trebuchet': "trebuc.ttf",
                'Trebuchet Bold Italic': "trebucbi.ttf",
                'Trebuchet Italic': "trebuci.ttf",
                'Verdana': "verdana.ttf",
                'Verdana Bold': "verdanabd.ttf"}

watermark_button_text = "Image(s) save upon program exit."

about_text = """WaterMARKER v.1.0\n\n\
©2024, MIT License\n\n\
Andrew Blais\n\n\
https://github.com/andrewblais"""

indent = "    "

help_text = f"""\
Easy-Peasy...\n\n{indent}\
• 'Browse' image to watermark.\n\n\
{indent}• Adjust settings (optional).\n\n\
{indent}• Click 'Watermark IT' button.\n\n\
{indent}• Program automatically closes.\n\n\
{indent}• Check your directory for `watermark_it###.png` image."""

font_size_vals = [str(i) for i in range(8, 73, 4)]

opacity_list = [str(i) for i in range(0, 101, 5)]

rows_list = [str(i) for i in range(1, 101)]

columns_list = [str(i) for i in range(1, 51)]

file_num = f"{randint(0, 999):03d}"

dt_object = dt.now()

now_string = str(dt_object)

copyright_year = f"©{dt_object.year}"
