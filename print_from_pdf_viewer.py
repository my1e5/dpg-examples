import webbrowser
import keyboard # pip install keyboard
from fpdf import FPDF # pip install fpdf
import dearpygui.dearpygui as dpg
dpg.create_context()

def generate_and_save_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page() 
    pdf.set_font("Arial", size = 15) 
    for line in text.splitlines():
        pdf.cell(110, 10, txt = line, ln = 1, align = 'L')
    pdf.output(filename)

def print_text_from_pdf_viewer():
    generate_and_save_pdf(dpg.get_value(text), dpg.get_value(filename)+".pdf")
    webbrowser.get().open(dpg.get_value(filename)+".pdf")
    keyboard.press_and_release('ctrl+p')

with dpg.window() as primary_window:
    filename = dpg.add_input_text(label="Filename", default_value="foo")
    text = dpg.add_input_text(label="Text", multiline=True, default_value="Hello World!")
    dpg.add_button(label="Print text\n(using default PDF viewer)", callback=print_text_from_pdf_viewer)

dpg.set_primary_window(primary_window, True)
dpg.create_viewport(width=200, height=200, title="Print from PDF Viewer")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()