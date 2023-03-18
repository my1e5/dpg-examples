# Inspired by https://github.com/bandit-masked/raccoon/blob/main/src/gui/gui.py#L231
# and credit to @Atlamillias on Discord.
import dearpygui.dearpygui as dpg
dpg.create_context()

is_menu_bar_clicked = False

def mouse_drag_callback(_, app_data):
    if is_menu_bar_clicked:
        _, drag_delta_x, drag_delta_y = app_data
        viewport_pos_x, viewport_pos_y = dpg.get_viewport_pos()
        new_pos_x = viewport_pos_x + drag_delta_x
        new_pos_y = max(viewport_pos_y + drag_delta_y, 0)
        dpg.set_viewport_pos([new_pos_x, new_pos_y])

def mouse_click_callback():
    global is_menu_bar_clicked
    is_menu_bar_clicked = True if dpg.get_mouse_pos(local=False)[1] < 30 else False # 30 pixels is slightly more than the height of the default menu bar 

with dpg.handler_registry():
    dpg.add_mouse_drag_handler(button=0, threshold=0, callback=mouse_drag_callback)
    dpg.add_mouse_click_handler(button=0, callback=mouse_click_callback)

with dpg.window() as primary_window:
    dpg.add_text("Click and drag the menu bar to move this undecorated window.")
    with dpg.menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="New")
            dpg.add_menu_item(label="Open")
            dpg.add_menu_item(label="Save")
        with dpg.menu(label="View"):
            dpg.add_menu_item(label="Maximize viewport", callback=lambda: dpg.maximize_viewport())
            dpg.add_slider_float(label="Width", default_value=600, min_value=400, max_value=1000, callback=lambda _, app_data: dpg.set_viewport_width(app_data))
            dpg.add_slider_float(label="Height", default_value=600, min_value=400, max_value=1000, callback=lambda _, app_data: dpg.set_viewport_height(app_data))
        dpg.add_button(label="Close", callback=lambda: dpg.destroy_context())

dpg.set_primary_window(primary_window, True)
dpg.create_viewport(width=600, height=600, decorated=False)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()