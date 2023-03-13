import dearpygui.dearpygui as dpg
dpg.create_context()

with dpg.viewport_menu_bar():
    with dpg.menu(label="File"):
        dpg.add_menu_item(label="New")
    dpg.add_menu_item(label="Edit")
    dpg.add_menu_item(label="View")

with dpg.window(pos=(100,100)):
    with dpg.menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="New")
        dpg.add_menu_item(label="Edit")
        dpg.add_menu_item(label="View")

    with dpg.child_window(width=200, height=200, menubar=True):
        with dpg.menu_bar():
            with dpg.menu(label="File"):
                dpg.add_menu_item(label="New")
            dpg.add_menu_item(label="Edit")
            dpg.add_menu_item(label="View")
   
dpg.create_viewport(width=800, height=600, title="Menubar types")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
