import dearpygui.dearpygui as dpg

dpg.create_context()

from .textures import load_textures
from .fonts import load_fonts
from .gui import create_gui
from .constants import VIEWPORT_WIDTH, VIEWPORT_HEIGHT, VIEWPORT_TITLE


def run():
    load_textures()
    load_fonts()
    create_gui()
    dpg.create_viewport(width=VIEWPORT_WIDTH, height=VIEWPORT_HEIGHT, title=VIEWPORT_TITLE)
    dpg.show_viewport()
    dpg.setup_dearpygui()
    dpg.start_dearpygui()
    dpg.destroy_context()
