# Credit @Quattro https://discord.com/channels/736279277242417272/1080603804812181605/1080603804812181605
import dearpygui.dearpygui as dpg
dpg.create_context()

"""As a workaround, using format="" you can disable the text in the slider, 
then you can add your own label next to the slider,
and change the value according to the step value.
""" 

STEP_SIZE = 2

with dpg.window():
    dpg.add_slider_int(
        tag="myslider",
        label=2*STEP_SIZE,
        default_value=2,
        min_value=0,
        max_value=5,
        format="",
        callback=lambda s, d: dpg.configure_item("myslider", label=d * STEP_SIZE),
    )

dpg.create_viewport(title="Slider with step size", width=400, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()