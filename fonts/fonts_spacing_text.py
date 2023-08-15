import dearpygui.dearpygui as dpg
dpg.create_context()


TEXT_WIDTH = 140
INPUT_WIDTH = 80
TRANSPARENT = (0, 0, 0, 0)
FONT_SCALE = 2

with dpg.font_registry():
    font_sans = dpg.add_font('Inter-Medium.ttf', 16*FONT_SCALE)
    font_mono = dpg.add_font('FiraCode-Medium.ttf', 16*FONT_SCALE)
dpg.set_global_font_scale(1/FONT_SCALE)
dpg.bind_font(font_sans)


with dpg.theme() as button_text_theme:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign, 1)
        dpg.add_theme_color(dpg.mvThemeCol_Button, TRANSPARENT)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, TRANSPARENT)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive,TRANSPARENT)


def standard():
    dpg.add_input_float(label="Label", width=INPUT_WIDTH, step=0)
    dpg.add_input_float(label="Longer Label", width=INPUT_WIDTH, step=0)
    dpg.add_input_float(label="Even Longer Label", width=INPUT_WIDTH, step=0)


def f_string_padding():
    with dpg.group(horizontal=True):
        dpg.add_text(f"{'Label': <20}")
        dpg.add_input_float(width=INPUT_WIDTH, step=0)
    with dpg.group(horizontal=True):
        dpg.add_text(f"{'Longer Label': <20}")
        dpg.add_input_float(width=INPUT_WIDTH, step=0)
    with dpg.group(horizontal=True):
        dpg.add_text(f"{'Even Longer Label': <20}")
        dpg.add_input_float(width=INPUT_WIDTH, step=0)


def r_just():
    with dpg.group(horizontal=True):
        dpg.add_text("Label".rjust(20))
        dpg.add_input_float(width=INPUT_WIDTH, step=0)
    with dpg.group(horizontal=True):
        dpg.add_text("Longer Label".rjust(20))
        dpg.add_input_float(width=INPUT_WIDTH, step=0)
    with dpg.group(horizontal=True):
        dpg.add_text("Even Longer Label".rjust(20))
        dpg.add_input_float(width=INPUT_WIDTH, step=0)


def button_method():
    with dpg.group(horizontal=True):
        dpg.add_button(label="Label", width=TEXT_WIDTH)
        dpg.bind_item_theme(dpg.last_item(), button_text_theme)
        dpg.add_input_float(width=INPUT_WIDTH, step=0)
    with dpg.group(horizontal=True):
        dpg.add_button(label="Longer Label", width=TEXT_WIDTH)
        dpg.bind_item_theme(dpg.last_item(), button_text_theme)
        dpg.add_input_float(width=INPUT_WIDTH, step=0)
    with dpg.group(horizontal=True):
        dpg.add_button(label="Even Longer Label", width=TEXT_WIDTH)
        dpg.bind_item_theme(dpg.last_item(), button_text_theme)
        dpg.add_input_float(width=INPUT_WIDTH, step=0)


with dpg.window() as primary_window:
    with dpg.group(horizontal=True):

        with dpg.child_window(width=400):
            dpg.add_text("Sans Serif Font Example")
            for method in [standard, f_string_padding, r_just, button_method]:
                dpg.add_spacer(height=20)
                method()

        with dpg.child_window(width=400):
            dpg.bind_item_font(dpg.last_item(), font_mono)
            dpg.add_text("Monospaced Font Example")
            for method in [standard, f_string_padding, r_just, button_method]:
                dpg.add_spacer(height=20)
                method()


dpg.set_primary_window(primary_window, True)
dpg.create_viewport(width=900, height=600, title="Fonts Spacing Text")
dpg.setup_dearpygui()  
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()