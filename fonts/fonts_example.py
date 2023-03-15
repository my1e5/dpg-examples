import dearpygui.dearpygui as dpg
dpg.create_context()

FONT_SCALE = 2
with dpg.font_registry():
    font_regular = dpg.add_font('Inter-Regular.ttf', 16*FONT_SCALE)
    font_medium = dpg.add_font('Inter-Medium.ttf', 16*FONT_SCALE)
    font_bold = dpg.add_font('Inter-Bold.ttf', 22*FONT_SCALE)
dpg.set_global_font_scale(1/FONT_SCALE)
dpg.bind_font(font_medium)

with dpg.window(width=700, height=500):
    dpg.add_text("Fonts example")
    dpg.bind_item_font(dpg.last_item(), font_bold)
    dpg.add_separator()
    dpg.add_text('''* If your fonts look a bit fuzzy it sometimes helps to multiply the font by a scaling factor (e.g. 2) 
  and then multiply the global font scale by 1/factor. I find it helps on high DPI displays to make the font look 'crisper'.

* On Windows this might help:
      import ctypes
      ctypes.windll.shcore.SetProcessDpiAwareness(2)

* If you have an integrated graphics card this might help:
      dpg.configure_app(auto_device=True)

* Another thing I find looks better is to use a medium weight font as the default font. 
  The Inter font is one of my favourites - see https://github.com/rsms/inter'''
    )
    dpg.add_separator()
    dpg.add_text('''* Here is some text in the regular font (Inter-Regular.ttf) for comparison.
  Depending on the screen it can look a bit more fuzzy compared to the medium weight font.

* Another thing to try is different font sizes. Experiment with different sizes and see what looks best.'''
    )
    dpg.bind_item_font(dpg.last_item(), font_regular)

dpg.create_viewport(title='Fonts example', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
