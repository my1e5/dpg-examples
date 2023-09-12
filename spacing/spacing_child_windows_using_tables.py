import dearpygui.dearpygui as dpg
dpg.create_context()

child_window_tags = []

def resize_child_windows(sender, data):
    x,y = dpg.get_item_rect_size(data) # get the size of the 'main_window'
    for tag in child_window_tags:
        dpg.set_item_height(tag, y//2)

def add_layout():
    with dpg.table(header_row=False):
        dpg.add_table_column()
        dpg.add_table_column()
        with dpg.table_row():
            with dpg.child_window() as child1:
                child_window_tags.append(child1)
                dpg.add_button(label="Button")
            with dpg.child_window() as child2:
                child_window_tags.append(child2)
                dpg.add_slider_float(label="Slider")
    with dpg.child_window():
        pass
       
with dpg.window(tag='main_window'):
    with dpg.tab_bar(tag="tabs"):
        with dpg.tab(label="Home", tag="home_tab"):
            add_layout()
        with dpg.tab(label="Settings", tag="settings_tab"):
            add_layout()

with dpg.item_handler_registry() as registry:
    dpg.add_item_resize_handler(callback=resize_child_windows)
dpg.bind_item_handler_registry('main_window', registry)

dpg.create_viewport(width=1200, height=800, title='Spacing Child Windows Using Tables')
dpg.set_primary_window('main_window', True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context() 