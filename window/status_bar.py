import dearpygui.dearpygui as dpg
dpg.create_context()

STATUS_BAR_HEIGHT = 20

with dpg.theme() as status_bar_theme:
    with dpg.theme_component():
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (42, 123, 207, 255))
        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 4, 0)

def resize_primary_window():
    x,y = dpg.get_item_rect_size(primary_window)
    dpg.configure_item(status_bar, width=x)
    dpg.configure_item(status_bar, pos=(0, y-STATUS_BAR_HEIGHT))

with dpg.window() as primary_window:
    dpg.set_primary_window(primary_window, True)
    with dpg.item_handler_registry() as registry:
        dpg.add_item_resize_handler(callback=resize_primary_window)
    dpg.bind_item_handler_registry(primary_window, registry)

    with dpg.menu_bar():
        with dpg.menu(label="View"):
            dpg.add_menu_item(label="Show/hide status bar", callback=lambda: dpg.configure_item(status_bar, show=not dpg.is_item_shown(status_bar)))

    with dpg.window():
        dpg.add_button(label="Hello world")

    with dpg.window(no_title_bar=True, no_move=True, no_resize=False) as status_bar:
        dpg.bind_item_theme(status_bar, status_bar_theme)
        with dpg.group(horizontal=True):
            dpg.add_text("Hello")
            dpg.add_button(label="world")

dpg.create_viewport(width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()