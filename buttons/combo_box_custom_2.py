'''
If you are not using a primary window, you need to check the position of the window
the button is in and add this on.
'''

import dearpygui.dearpygui as dpg
dpg.create_context()

def show_options(sender):
    wx, wy = dpg.get_item_pos("window")
    x,y = dpg.get_item_pos(sender)
    dpg.configure_item("options_window", pos=(wx+x,wy+y+20))
    dpg.configure_item("options_window", show=True)

with dpg.window(popup=True, show=False, tag="options_window"):
    dpg.add_checkbox(label="Option 1")
    dpg.add_checkbox(label="Option 2")
    dpg.add_checkbox(label="Option 3")
    
with dpg.window(width=500, height=300, tag="window"):
    dpg.add_button(label="Options     V", width=100, callback=show_options)

dpg.create_viewport(width=800, height=600, title='Custom combo box with floating window')
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
