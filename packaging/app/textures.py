import dearpygui.dearpygui as dpg
from .utils import absolute_path
from .constants import BEACH_IMAGE_FILE, BEACH_IMAGE_TAG

def load_textures():
    width, height, channels, data = dpg.load_image(absolute_path(BEACH_IMAGE_FILE))
    with dpg.texture_registry():
        dpg.add_static_texture(width=width, height=height, default_value=data, tag=BEACH_IMAGE_TAG)