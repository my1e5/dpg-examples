'''
If you are using a primary window, this will work. See combo_box_custom_2.py for a
version that works with floating windows.
'''

import dearpygui.dearpygui as dpg
dpg.create_context()

def show_options(sender):
    x,y = dpg.get_item_pos(sender)
    dpg.configure_item("options_window", pos=(x,y+20))
    dpg.configure_item("options_window", show=True)

with dpg.window(popup=True, show=False, tag="options_window"):
    dpg.add_checkbox(label="Option 1")
    dpg.add_checkbox(label="Option 2")
    dpg.add_checkbox(label="Option 3")
    
with dpg.window(width=500, height=300):
    dpg.set_primary_window(dpg.last_item(), True)
    dpg.add_button(label="Options     V", width=100, callback=show_options)

dpg.create_viewport(width=800, height=600, title='Custom combo box with primary window')
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
