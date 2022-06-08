#  My DearPyGUI windowed app
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Page per Day Calculator', width=600, height=300)

with dpg.window(label="Page per Day Calculator", width = 700, height = 200):
    dpg.add_text("Welcome to the page per day calculator!")
    dpg.add_input_int(label = "How many pages are there?")
    dpg.add_input_int(label = "How many pages have you read?")
    dpg.add_input_int(label = "How many days until you have \nto be done reading this book?")
    dpg.add_button(label="Calculate!")
    dpg.add_text(label = "This is where your results will pop up.")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()