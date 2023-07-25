import dearpygui.dearpygui as dpg
dpg.create_context()

def move_group(sender, app_data, user_data):
    group, window = user_data

    def close():
        dpg.move_item(group, parent=window)
        dpg.show_item(sender)

    with dpg.window(on_close=close) as new_window:
        dpg.move_item(group, parent=new_window)    
    dpg.hide_item(sender)


with dpg.window() as main_window:
    
    with dpg.child_window(width=120, height=80) as child_window:
        with dpg.group() as my_group:
            dpg.add_input_text(default_value="Hello world", width=100)
            dpg.add_slider_float(width=100)
    
    dpg.add_button(label="Pop to window!", callback=move_group, user_data=(my_group, child_window))


dpg.set_primary_window(main_window, True)
dpg.create_viewport(title='Pop to Window', width=500, height=300)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
