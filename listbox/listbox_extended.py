# Credit @mangotuesday - https://discord.com/channels/736279277242417272/1078520923893805137/1085627890143600752

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=600)

# generic class that holds custom app data
class Data:
    def __init__(self):
        self.last_selected = None


def print_selected(sender, app_data):
    children = dpg.get_item_children(item="custom_listbox")[1]
    print("Selected items:")
    for child in children:
        print(f"{dpg.get_item_label(child)}: {dpg.get_value(child)}")


def add_custom_listbox(items: list[str], tag: str, height: int, width: int = -1):

    with dpg.theme() as theme_item_selected:
        with dpg.theme_component(dpg.mvSelectable):
            dpg.add_theme_color(dpg.mvThemeCol_Header, (0,119,200,153))

    with dpg.theme() as theme_item_normal:
        with dpg.theme_component(dpg.mvSelectable):
            dpg.add_theme_color(dpg.mvThemeCol_Header, (51, 51, 55, 255))

    def _selection(sender, app_data, user_data):

        # shift + left click = set True to all in range between previous selection and current
        # selection, inclusive
        if dpg.is_key_down(dpg.mvKey_Shift):
            # if it's the first selection (no previous selection exists), assign to the
            # previous selection, set current selection to True, and return
            if not d.last_selected:
                d.last_selected = sender
                dpg.set_value(sender, True)
                return

            prev_index = user_data.index(d.last_selected)
            cur_index = user_data.index(sender)

            if prev_index < cur_index:
                items_to_set_true = user_data[prev_index:cur_index + 1]
            else:
                items_to_set_true = user_data[cur_index:prev_index + 1]
            
            for item in items_to_set_true:
                dpg.set_value(item, True)

        # ctrl + left click = set True to current selection, preserve previous selections
        # unintuitive because of how underlying selectable works, but this will toggle the
        # item correctly
        elif dpg.is_key_down(dpg.mvKey_Control):
            dpg.set_value(sender, dpg.get_value(sender))

        # left click = erase previous selections, set True to current selection only
        else:
            for item in user_data:
                dpg.set_value(item, False)
            dpg.set_value(sender, True)

        for item in user_data:
            if dpg.get_value(item) is True:
                dpg.bind_item_theme(item, theme_item_selected)
            else:
                dpg.bind_item_theme(item, theme_item_normal)

        # store previous selection
        d.last_selected = sender

    with dpg.child_window(tag=tag, height=height, width=width):
        for item in items:
            dpg.add_selectable(label=item)

        listbox_ids = dpg.get_item_children(item=tag)[1]

        for child in listbox_ids:
            dpg.configure_item(child, callback=_selection, user_data=listbox_ids)

        # dpg.bind_item_theme(tag, theme_listbox_custom)

d = Data()

with dpg.window(tag="primary_window"):
    
    contents = [
        "hello world 1",
        "hello world 2",
        "hello world 3",
        "hello world 4",
        "hello world 5",
        "hello world 6",
        "hello world 7",
    ]

    dpg.add_text("Normal Listbox")
    dpg.add_listbox(items=contents)

    dpg.add_text("Custom Listbox w/ Sorta Extended Selection")
    dpg.add_text("(Try holding CTRL or SHIFT while selecting)")
    add_custom_listbox(items=contents, tag="custom_listbox", height=200)

    dpg.add_button(label="Print Selected in Custom Listbox", callback=print_selected)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("primary_window", True)
dpg.start_dearpygui()
dpg.destroy_context()