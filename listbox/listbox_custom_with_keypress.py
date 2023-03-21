import string
import dearpygui.dearpygui as dpg
dpg.create_context()


ascii_dict = {ord(char): char for char in string.ascii_uppercase}


def print_selected(sender, app_data):
    children = dpg.get_item_children(item="custom_listbox")[1]
    print("Selected items:")
    for child in children:
        print(f"{dpg.get_item_label(child)}: {dpg.get_value(child)}")


def add_custom_listbox(items: list[str], tag: str, height: int, width: int = -1, scroll_offset: int = 0):

    with dpg.theme() as theme_item_selected:
        with dpg.theme_component(dpg.mvSelectable):
            dpg.add_theme_color(dpg.mvThemeCol_Header, (0,119,200,153))

    with dpg.theme() as theme_item_normal:
        with dpg.theme_component(dpg.mvSelectable):
            dpg.add_theme_color(dpg.mvThemeCol_Header, (51, 51, 55, 255))
            dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (51, 51, 55, 255))

    def _key_press_handler(sender, app_data, user_data):
        listbox_ids, items = user_data
        letter = ascii_dict.get(app_data)
        if letter and dpg.is_item_hovered(tag):
            start_index = next(i for i, item_id in enumerate(listbox_ids) if dpg.get_value(item_id))
            for idx, item in enumerate(items[start_index+1:]):
                if item.startswith(letter):
                    _selection(listbox_ids[start_index+1+idx], None, listbox_ids)
                    dpg.set_y_scroll(tag, max(0,dpg.get_item_pos(listbox_ids[start_index+1+idx])[1] - scroll_offset))
                    return
            for idx, item in enumerate(items[:start_index]):
                if item.startswith(letter):
                    _selection(listbox_ids[idx], None, listbox_ids)
                    dpg.set_y_scroll(tag, max(0,dpg.get_item_pos(listbox_ids[idx])[1] - scroll_offset))
                    return

    def _selection(sender, app_data, user_data):

        for item in user_data:
            dpg.set_value(item, False)
            dpg.bind_item_theme(item, theme_item_normal)
            
        dpg.set_value(sender, True)
        dpg.bind_item_theme(sender, theme_item_selected)



    with dpg.child_window(tag=tag, height=height, width=width):
        for item in items:
            dpg.add_selectable(label=item)

        listbox_ids = dpg.get_item_children(item=tag)[1]

        for child in listbox_ids:
            dpg.configure_item(child, callback=_selection, user_data=listbox_ids)
    
    _selection(listbox_ids[0], None, listbox_ids)
    
    with dpg.handler_registry():
        dpg.add_key_press_handler(callback=_key_press_handler, user_data=(listbox_ids, items))

   

with dpg.window(tag="primary_window"):

    dpg.add_text("Custom listbox using selectables and with key press enabled\n(only works when the listbox is hovered)")

    items = ['Apple', 'Apricot', 'Avocado', 'Banana', 'Broccoli', 'Carrot', 'Cherry', 'Cucumber', 'Grape', 'Kiwi', 'Lemon', 'Mango', 'Orange', 'Papaya', 'Peach', 'Pear', 'Pepper', 'Pineapple', 'Potato', 'Raspberry', 'Strawberry', 'Tomato', 'Watermelon']

    add_custom_listbox(items=items, tag="custom_listbox", height=200, scroll_offset=100)

    dpg.add_button(label="Print Selected in Custom Listbox", callback=print_selected)


dpg.set_primary_window("primary_window", True)
dpg.create_viewport(title='Custom listbox using selectables and with key press enabled', width=600, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

