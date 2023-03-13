import dearpygui.dearpygui as dpg
dpg.create_context()

def print_item_sizes(sender):
    print(f"On {sender} the window size is: {dpg.get_item_rect_size('window')}")
    print(f"On {sender} the text size is: {dpg.get_item_rect_size('text')}")

with dpg.window(autosize=True, tag='window'):
    dpg.add_input_text(width=400, height=200, multiline=True, tag='text')
    print_item_sizes('startup')

dpg.set_frame_callback(1, print_item_sizes)
dpg.set_frame_callback(2, print_item_sizes)
dpg.create_viewport(width=800, height=600, title="Get item size on startup")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

"""
$ python get_item_size_on_startup.py 
On startup the window size is: [0, 0]
On startup the text size is: [0, 0]
On 1 the window size is: [100, 100]
On 1 the text size is: [400, 200]
On 2 the window size is: [416, 235]
On 2 the text size is: [400, 200]
"""