import dearpygui.dearpygui as dpg
dpg.create_context()

'''
If you use a callback in directly in dpg.tab_bar, e.g.
    with dpg.tab_bar(tag='tab_bar', callback=tab_bar_callback):
then the callback is only called when the tab changes. If you want
it to be called whenever the tab bar is clicked, i.e. even when 
clicking the same tab, then here is a workaround.
'''

def tab_bar_callback():
    for child in dpg.get_item_children('tab_bar')[1]:
        if dpg.is_item_hovered(child):
            dpg.split_frame() # wait a frame for the tab to change
            print(f"{dpg.get_value('tab_bar')} clicked!")

with dpg.window():
    with dpg.tab_bar(tag='tab_bar'):
        with dpg.tab(label="T1", tag='T1'):
            dpg.add_button(label="button1")
        with dpg.tab(label="T2", tag='T2'):
            dpg.add_slider_double()
        with dpg.tab(label="T3", tag="T3"):
            pass

with dpg.handler_registry():
    dpg.add_mouse_click_handler(button=0, callback=tab_bar_callback)

dpg.create_viewport(width=800, height=600, title="Tab bar callback")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
