import dearpygui.dearpygui as dpg
dpg.create_context()

with dpg.window(width=500, height=500, min_size=(200,200)) as window:
    with dpg.menu_bar():
        spacer = dpg.add_spacer()
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="New")
        with dpg.menu(label="Edit"):
            dpg.add_menu_item(label="Copy")
        with dpg.menu(label="View"):
            dpg.add_menu_item(label="Maximize")

def adjust_menu_bar_spacer():
    dpg.configure_item(spacer, width=dpg.get_item_width(window) - 150) # adjust 150 to fit your needs

with dpg.item_handler_registry() as item_handler_registry:
    dpg.add_item_resize_handler(callback=adjust_menu_bar_spacer)
dpg.bind_item_handler_registry(window, item_handler_registry)

dpg.create_viewport(width=800, height=600, title="Menubar right aligned")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
