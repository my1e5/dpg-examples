import dearpygui.dearpygui as dpg
dpg.create_context()

def add_custom_listbox(items: list, width: int = 250, height: int = 70, parent: int | str = None, callback: callable = None):
    parent = parent or dpg.last_container() 

    with dpg.theme() as custom_listbox_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 0,0)
            dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign, 0, 0.5)

    with dpg.theme() as button_selected_theme:
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (0,119,200,153))

    with dpg.theme() as button_normal_theme:
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (51, 51, 55, 255))
    
    def custom_listbox_callback(sender):
        if callback:
            callback(dpg.get_item_parent(sender), dpg.get_item_label(sender))
        for button in dpg.get_item_children(dpg.get_item_parent(sender))[1]:
            dpg.bind_item_theme(button, button_normal_theme)
        dpg.bind_item_theme(sender, button_selected_theme)

    with dpg.child_window(height=height, width=width, border=False, parent=parent) as custom_listbox:
        for item in items:
            dpg.add_button(label=item, width=-1, callback=custom_listbox_callback)
    dpg.bind_item_theme(custom_listbox, custom_listbox_theme)

def print_callback(sender, data):
    print(sender, data)

with dpg.window() as primary_window:
    items = ["Apple", "Banana", "Cherry", "Kiwi", "Mango"]
    dpg.add_text("This is a listbox:")
    dpg.add_listbox(items=items, callback=print_callback)
    dpg.add_spacer(height=20)
    dpg.add_text("This is a custom listbox which is unselected by default:")
    add_custom_listbox(items=items, callback=print_callback)

dpg.set_primary_window(primary_window, True)
dpg.create_viewport(width=500, height=400, title="Custom Listbox")
dpg.show_viewport()
dpg.setup_dearpygui()
dpg.start_dearpygui()
dpg.destroy_context()