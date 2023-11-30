import dearpygui.dearpygui as dpg
from .utils import absolute_path
from .constants import FONT_FILE, FONT_SIZE, FONT_TAG


def load_fonts():
    with dpg.font_registry():
        dpg.add_font(absolute_path(FONT_FILE), FONT_SIZE, tag=FONT_TAG)
