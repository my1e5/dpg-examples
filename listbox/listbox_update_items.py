# Updating listbox after creation
# from https://github.com/DataExplorerUser/tools
import dearpygui.dearpygui as dpg
dpg.create_context()

def new_list_box_item():
    items = dpg.get_item_configuration("lbox")['items']
    items.append(str(len(items)+1))
    dpg.configure_item("lbox", items=items)

with dpg.window():
    dpg.add_listbox(items=['1', '2'], tag="lbox")
    dpg.add_button(label="New listbox item", callback=new_list_box_item)

dpg.create_viewport(width=600, height=400, title='Updating listbox items after creation')
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()