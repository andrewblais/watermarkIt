from tkinter import *
from tkinter import ttk, filedialog, messagebox

from modules.watermark_it_pil import PilImage
from static.watermark_it_data import *


class WatermarkItGui:
    """A simple GUI application for creating watermarked images using Tkinter.

    Attributes:
        root (Tk): The main Tkinter window.
        path_input (str): The path of the input image.
        path_output (str): The path for the watermarked image output.
        image_obj (PilImage): The PilImage object for creating watermarks.
        watermark_entry_var (StringVar): Tkinter StringVar for the watermark text.
        font_type_var (StringVar): Tkinter StringVar for the selected font type.
        font_color_var (IntVar): Tkinter IntVar for the selected font color (1 for white, 0 for black).
        font_size_var (IntVar): Tkinter IntVar for the selected font size.
        rows_var (IntVar): Tkinter IntVar for the selected number of rows in the watermark.
        columns_var (IntVar): Tkinter IntVar for the selected number of columns in the watermark.
        opacity_var (IntVar): Tkinter IntVar for the selected opacity percentage.

    Methods:
        browse_file(): Command for the 'Browse' button to select an input image.
        about_popup(): Command for the 'About' button to display information about the application.
        help_popup(): Command for the 'Help' button to display help information.
        watermark_it(): Command for the 'Create Watermark' button to create a watermarked image.
        setup_gui(): Configures and sets up the Tkinter GUI elements.
    """

    def __init__(self, root, gui_w: int = 475, gui_h: int = 895, move_x: int = 0, move_y: int = 0):
        """Initialize the WatermarkGui object with default values and set up the GUI.

        Args:
            root (Tk): The main Tkinter window.
        """
        self.root = root

        # Widgets
        self.browse_button = None
        self.watermark_button = None
        self.help_button = None
        self.about_button = None
        self.settings_label = None
        self.watermark_entry_label = None
        self.watermark_entry = None
        self.font_type_label = None
        self.font_color_label = None
        self.font_type_combo = None
        self.color_radiobutton_white = None
        self.color_radiobutton_black = None
        self.font_size_scale = None
        self.rows_scale = None
        self.columns_scale = None
        self.opacity_scale = None
        self.exit_button = None

        self.gui_w = gui_w
        self.gui_h = gui_h
        self.move_x = move_x
        self.move_y = move_y
        self.current_row = 0
        self.path_input = None
        self.path_output = None
        self.image_obj = None
        self.watermark_entry_var = StringVar()
        self.font_type_var = StringVar(value=fonts_list[3])
        self.font_color_var = IntVar(value=1)
        self.font_size_var = IntVar(value=40)
        self.rows_var = IntVar(value=20)
        self.columns_var = IntVar(value=6)
        self.opacity_var = IntVar(value=50)
        self.setup_gui()

    @staticmethod
    def about_popup():
        """Command for `About` button."""
        messagebox.showinfo("About WaterMARKER", about_text, icon="info")

    def browse_file(self):
        """Command for `Browse` button."""
        self.path_input = filedialog.askopenfile().name

    @staticmethod
    def convert_opacity(opacity_100):
        opacity_255 = round(255 * opacity_100 / 100)
        return opacity_255

    @staticmethod
    def color_to_tuple(color_var):
        return (255, 255, 255) if color_var else (0, 0, 0)

    @staticmethod
    def get_tk_font_name(font_name: str = "Arial Italic"):
        """Get Tkinter font name from readable user font name.

        Args:
            font_name (str, optional): Desired font name. Defaults to "arial".
        """
        return font_convert.get(font_name, "ariali.ttf")

    @staticmethod
    def help_popup():
        """Command for `Help` button."""
        messagebox.showinfo("WaterMARKER Help", help_text, icon="question")

    def increment_row(self):
        self.current_row += 1

    def setup_gui(self):
        self.root.title("Watermark IT")
        self.root.iconbitmap("static/water_icon.ico")
        self.root.geometry(f"{self.gui_w}x{self.gui_h}+{self.move_x}+{self.move_y}")
        self.root.minsize(self.gui_w, self.gui_h)
        self.root.maxsize(self.gui_w, self.gui_h)
        self.root.config(padx=10, pady=35)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        # Browse button:
        self.browse_button = Button(self.root,
                                    text="Browse",
                                    width=9,
                                    height=1,
                                    command=self.browse_file)
        self.browse_button.grid(row=self.current_row,
                                column=0,
                                columnspan=3,
                                pady=(0, 35))

        self.increment_row()

        # Watermark button:
        self.watermark_button = Button(self.root,
                                       text="Watermark IT",
                                       font=("Source Sans 3 Black", 16),
                                       cursor="spraycan",
                                       width=13,
                                       height=1,
                                       command=self.watermark_it)
        self.watermark_button.grid(row=self.current_row,
                                   column=0,
                                   columnspan=3,
                                   pady=(0, 0))

        self.increment_row()

        # Help button:
        self.help_button = Button(self.root,
                                  text="Help",
                                  cursor="question_arrow",
                                  width=8,
                                  height=1,
                                  command=self.help_popup)
        self.help_button.grid(row=self.current_row,
                              column=0,
                              padx=(65, 0),
                              pady=(35, 0))

        # About button:
        self.about_button = Button(self.root,
                                   text="About",
                                   width=8,
                                   height=1,
                                   command=self.about_popup)
        self.about_button.grid(row=self.current_row,
                               column=2,
                               padx=(0, 65),
                               pady=(35, 0))

        self.increment_row()

        # Settings label:
        self.settings_label = Label(self.root,
                                    text="Optional Settings:",
                                    font=("Source Sans 3 Black", 14))
        self.settings_label.grid(row=self.current_row,
                                 column=0,
                                 columnspan=3,
                                 pady=(60, 0))

        self.increment_row()

        # Watermark text label:
        self.watermark_entry_label = Label(self.root,
                                           text="Watermark text")
        self.watermark_entry_label.grid(row=self.current_row,
                                        column=0,
                                        columnspan=3,
                                        pady=(5, 0))

        self.increment_row()

        # Settings label:
        self.watermark_entry = Entry(self.root, textvariable=self.watermark_entry_var)
        self.watermark_entry.grid(row=self.current_row,
                                  column=0,
                                  columnspan=3,
                                  pady=(0, 17))
        self.watermark_entry.insert(0, copyright_year)

        self.increment_row()

        # Font-type label:
        self.font_type_label = Label(self.root,
                                     text="Font type")
        self.font_type_label.grid(row=self.current_row,
                                  column=0,
                                  padx=(80, 0),
                                  pady=(5, 0))

        # Font-color label:
        self.font_color_label = Label(self.root,
                                      text="Font color")
        self.font_color_label.grid(row=self.current_row,
                                   column=2,
                                   padx=(0, 80),
                                   pady=(5, 0))

        self.increment_row()

        # Font type combo:
        self.font_type_combo = ttk.Combobox(self.root,
                                            width=18,
                                            values=fonts_list,
                                            state="readonly",
                                            textvariable=self.font_type_var)
        self.font_type_combo.grid(row=self.current_row,
                                  column=0,
                                  padx=(80, 0))
        self.font_type_combo.current(3)

        # Color radiobutton white:
        self.color_radiobutton_white = Radiobutton(self.root,
                                                   text="White",
                                                   width=18,
                                                   value=1,
                                                   variable=self.font_color_var)
        self.color_radiobutton_white.grid(row=self.current_row,
                                          column=2,
                                          padx=(0, 80))

        self.increment_row()

        # Color radiobutton black:
        self.color_radiobutton_black = Radiobutton(self.root,
                                                   text="Black",
                                                   width=18,
                                                   value=0,
                                                   variable=self.font_color_var)
        self.color_radiobutton_black.grid(row=self.current_row,
                                          column=2,
                                          padx=(0, 80))

        self.increment_row()

        # Font size scale:
        self.font_size_scale = Scale(self.root,
                                     width=12,
                                     sliderlength=25,
                                     length=350,
                                     label="Font size",
                                     from_=8,
                                     to=72,
                                     resolution=4,
                                     orient=HORIZONTAL,
                                     variable=self.font_size_var)
        self.font_size_scale.grid(row=self.current_row,
                                  column=0,
                                  columnspan=3,
                                  pady=(17, 0))

        self.increment_row()

        # Rows scale:
        self.rows_scale = Scale(self.root,
                                width=12,
                                sliderlength=25,
                                length=350,
                                label="Rows",
                                from_=1,
                                to=100,
                                orient=HORIZONTAL,
                                variable=self.rows_var)
        self.rows_scale.grid(row=self.current_row,
                             column=0,
                             columnspan=3,
                             pady=(17, 0))

        self.increment_row()

        # Columns scale:
        self.columns_scale = Scale(self.root,
                                   width=12,
                                   sliderlength=25,
                                   length=350,
                                   label="Columns",
                                   from_=1,
                                   to=50,
                                   orient=HORIZONTAL,
                                   variable=self.columns_var)
        self.columns_scale.grid(row=self.current_row,
                                column=0,
                                columnspan=3,
                                pady=(17, 0))

        self.increment_row()

        # Opacity scale:
        self.opacity_scale = Scale(self.root,
                                   width=12,
                                   sliderlength=25,
                                   length=350,
                                   label="Opacity %",
                                   from_=0,
                                   to=100,
                                   resolution=5,
                                   orient=HORIZONTAL,
                                   variable=self.opacity_var)
        self.opacity_scale.grid(row=self.current_row,
                                column=0,
                                columnspan=3,
                                pady=(17, 0))

        self.increment_row()

        # Exit button:
        self.exit_button = Button(self.root,
                                  text="Make it\nSTOP!",
                                  cursor="trek",
                                  width=10,
                                  height=3,
                                  command=self.root.quit)
        self.exit_button.grid(row=self.current_row,
                              column=0,
                              columnspan=3,
                              pady=(65, 0))

    def watermark_it(self):
        """Command for `Create Watermark` button. Imports PILWatermark class. Creates watermark."""
        self.image_obj = PilImage(self.path_input)
        self.image_obj.text = self.watermark_entry.get()
        self.image_obj.font_name = self.get_tk_font_name(self.font_type_combo.get())
        self.image_obj.color = self.color_to_tuple(self.font_color_var.get())
        self.image_obj.font_size = self.font_size_scale.get()
        self.image_obj.rows = self.rows_scale.get()
        self.image_obj.cols = self.columns_scale.get()
        self.image_obj.alpha = self.convert_opacity(self.opacity_scale.get())
        self.image_obj.create_watermark()


if __name__ == "__main__":
    window = Tk()
    watermark_gui = WatermarkItGui(window, move_x=350, move_y=40)
    window.mainloop()
