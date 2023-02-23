import dearpygui.dearpygui as dpg
dpg.create_context()

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 100
ITEM_SPACING_X, ITEM_SPACING_Y = 8,4 # The default item spacing

with dpg.window() as primary_window:
    with dpg.child_window(height=-BUTTON_HEIGHT-ITEM_SPACING_Y):
        pass
    with dpg.group(horizontal=True):
        with dpg.child_window(width=-BUTTON_WIDTH-ITEM_SPACING_X):
            pass
        with dpg.child_window(border=False):
            dpg.add_button(label="Connect", width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

dpg.set_primary_window(primary_window, True)
dpg.create_viewport(width=600, height=400, title="Spacing Using Child Window Grid")
dpg.setup_dearpygui()  
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()