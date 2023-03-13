import dearpygui.dearpygui as dpg
dpg.create_context()

numbers = {
    dpg.generate_uuid(): 0,
    dpg.generate_uuid(): 0,
    dpg.generate_uuid(): 0,
    dpg.generate_uuid(): 0,
}


def update(_, app_data, user_data):
    numbers[user_data] = app_data

def remove(_, app_data, user_data):
    if len(numbers) > 1:
        del numbers[user_data]
        dpg.delete_item(user_data)

def add(_, app_data, user_data):
    if user_data is None:
        number = 0
        tag = dpg.generate_uuid()
        numbers[tag] = number
    else:
        tag, number = user_data
    with dpg.group(horizontal=True, tag=tag, parent="input_group"):
        dpg.add_input_int(default_value=number, callback=update, user_data=tag)
        dpg.add_button(label=" X ", callback=remove, user_data=tag)
        with dpg.tooltip(parent=dpg.last_item()):
            dpg.add_text("Remove this input")


with dpg.window() as primary_window:
    with dpg.group(horizontal=True):
        dpg.add_button(label="Add number", callback=add)
        dpg.add_button(label="Print numbers", callback=lambda: print(numbers.values()))

    with dpg.group(tag="input_group"):
        for tag, number in numbers.items():
            add(None, None, (tag, number))


dpg.set_primary_window(primary_window, True)
dpg.create_viewport(width=400, height=300, title="Data binding with dict")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
