import dearpygui.dearpygui as dpg
dpg.create_context()

with dpg.theme(tag='button_border_theme'):
    with dpg.theme_component():
        dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 0, 0, 0))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (255, 255, 255, 100))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0, 0, 0, 0))
        dpg.add_theme_color(dpg.mvThemeCol_Border, (255, 255, 255, 255))
        dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, (0, 0, 0, 0))
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 100)
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 2)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 8, 8)

with dpg.window(width=500, height=300):
    dpg.add_button(label="Button", width=100, tag="button")
    dpg.bind_item_theme("button", "button_border_theme")

dpg.create_viewport(width=800, height=600, title='Button Border Theme')
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()