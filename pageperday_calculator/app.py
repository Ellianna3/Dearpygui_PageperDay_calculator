#  My DearPyGUI windowed app
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300)

with dpg.window(label="Page per day calculator", width = 600, height = 300):
    dpg.add_text("Welcome to the page per day calculator")
    dpg.add_input_int(label = "How many pages are there?")
    dpg.add_input_int(label = "How many pages have you read?")
    dpg.add_button(label="Calculate!")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()