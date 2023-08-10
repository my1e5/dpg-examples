import dearpygui.dearpygui as dpg
dpg.create_context()


def add():
    dpg.add_input_int(parent='input_group')

def remove():
    numbers_tags = dpg.get_item_children('input_group',1)
    if len(numbers_tags) > 1:
        dpg.delete_item(numbers_tags[-1])

def print_numbers():
    numbers = [dpg.get_value(tag) for tag in dpg.get_item_children('input_group',1)]
    print(numbers)


with dpg.window() as primary_window:

    with dpg.group(horizontal=True):
        dpg.add_button(label='Add number', callback=add)
        dpg.add_button(label='Remove last number', callback=remove)
        dpg.add_button(label="Print numbers", callback=print_numbers)

    with dpg.group(tag='input_group'):
        for _ in range(4):
            dpg.add_input_int()


dpg.set_primary_window(primary_window, True)    
dpg.create_viewport(width=400, height=100, title="No data binding")  
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()