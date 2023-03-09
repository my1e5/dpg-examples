import string
import dearpygui.dearpygui as dpg
dpg.create_context()

ascii_dict = {ord(char): char for char in string.ascii_uppercase}

def is_pressed(sender, app_data):
    letter = ascii_dict.get(app_data)
    if letter:
        items = dpg.get_item_configuration('l_box')['items']
        start_index = items.index(dpg.get_value('l_box'))
        for item in items[start_index+1:]+items[:start_index]:
            if item.startswith(letter):
                dpg.set_value('l_box', item)
                break

with dpg.handler_registry():
    dpg.add_key_press_handler(callback=is_pressed)

with dpg.window(width=500, height=300):
    items = ['Apple', 'Apricot', 'Avocado', 'Banana', 'Orange']
    dpg.add_listbox(tag='l_box', items=items)

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()