import dearpygui.dearpygui as dpg
dpg.create_context()

with dpg.theme() as blank_button_theme: # To make a button look like text
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 0, 0, 0))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0, 0, 0, 0))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0, 0, 0, 0))

with dpg.window(width=600, height=400):                   
    with dpg.table(header_row=False):
        dpg.add_table_column()
        dpg.add_table_column()
        dpg.add_table_column()       
        with dpg.table_row():
            dpg.add_spacer()                 
            dpg.add_button(label="Username", width=-1)
            dpg.bind_item_theme(dpg.last_item(), blank_button_theme)        
            dpg.add_spacer()           
        with dpg.table_row():
            dpg.add_spacer()                 
            dpg.add_input_text(width=-1) 
            dpg.add_spacer()      

dpg.create_viewport(width=800, height=600, title="Spacing Using Tables")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()