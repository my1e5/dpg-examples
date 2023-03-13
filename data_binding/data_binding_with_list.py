import dearpygui.dearpygui as dpg
dpg.create_context()

numbers = [0, 0, 0, 0]

def update(_, app_data, user_data):
    numbers[user_data] = app_data

def remove():
    if len(numbers) > 1:
        numbers.pop()
        last_input = dpg.get_item_children('input_group',1)[-1]
        dpg.delete_item(last_input)

def add():
    numbers.append(0)
    dpg.add_input_int(parent='input_group', callback=update, user_data=len(numbers)-1)


with dpg.window() as primary_window:

    with dpg.group(horizontal=True):
        dpg.add_button(label='Add number', callback=add)
        dpg.add_button(label='Remove last number', callback=remove)
        dpg.add_button(label="Print numbers", callback=lambda: print(numbers))

    with dpg.group(tag='input_group'):
        for idx, number in enumerate(numbers):
            dpg.add_input_int(default_value=number, callback=update, user_data=idx)


dpg.set_primary_window(primary_window, True)    
dpg.create_viewport(width=400, height=100, title="Data binding with list")  
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()