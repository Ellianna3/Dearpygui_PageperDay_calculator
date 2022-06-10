#  My DearPyGUI windowed app
import dearpygui.dearpygui as dpg

dpg.create_context()

#generate ids for all widgets we want to control
numpages_id = dpg.generate_uuid()
temp_id = dpg.generate_uuid()
output_id = dpg.generate_uuid()

def callback():
    print("Number of Pages ID: " + str(dpg.get_value(numpages_id)))

dpg.create_viewport(title='Page per Day Calculator', width=600, height=300)

with dpg.window(label="Page per Day Calculator", width = 700, height = 200):
    dpg.add_text("Welcome to the page per day calculator!")
    dpg.add_input_int(label = "How many pages are there?", width = 100, tag = numpages_id)
    dpg.add_input_int(label = "How many pages have you read?", width = 100, tag = temp_id)
    dpg.add_input_int(label = "How many days until you have \nto be done reading this book?", width = 100)
    dpg.add_button(label="Calculate!", callback = callback)
    dpg.add_text("", tag =output_id)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()