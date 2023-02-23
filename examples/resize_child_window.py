import dearpygui.dearpygui as dpg
dpg.create_context()

def resize_height(sender, data):
    dpg.configure_item(dpg.get_item_parent(sender), height=data)

with dpg.window() as primary_window:
    with dpg.child_window(height=100) as child_window:
        dpg.add_slider_int(label="Resize Child Window", default_value=dpg.get_item_height(child_window), min_value=50, max_value=300, callback=resize_height)
    dpg.add_separator()
    with dpg.child_window():
        pass

dpg.set_primary_window(primary_window, True)
dpg.create_viewport(title='Resize Child Window', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()