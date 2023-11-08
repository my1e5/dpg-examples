# see https://discord.com/channels/736279277242417272/1171570899888123934/1171570899888123934
# and see my1e6/dpg-examples/window/pop_to_window.py
import dearpygui.dearpygui as dpg
dpg.create_context()

def move_group(sender, app_data, user_data):
    group, window = user_data
    def close():
        dpg.move_item(group, parent=window)
        dpg.delete_item(new_window)
        dpg.show_item(sender)
    with dpg.window(on_close=close) as new_window:
        dpg.move_item(group, parent=new_window)    
    dpg.hide_item(sender)


with dpg.window() as main_window:

    with dpg.group() as my_group:
        with dpg.plot():
            dpg.add_plot_legend(location=dpg.mvPlot_Location_NorthEast)
            dpg.add_plot_axis(dpg.mvXAxis)
            with dpg.plot_axis(dpg.mvYAxis):
                dpg.add_line_series([0, 1, 2, 3, 4], [0, 3, 4, 1, 5], label="line1")
        
        with dpg.child_window(border=False, pos=(50,24), width=106, height=19): # The trick is you need to set the child window width and height to be exactly the size of the button. Any bigger and the extra space will cover the plot and prevent mouse inputs.
            dpg.add_button(label="Pop to window!", callback=move_group, user_data=(my_group, main_window))

dpg.set_primary_window(main_window, True)
dpg.create_viewport(title='Plot buttons', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()



