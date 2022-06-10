#  My DearPyGUI windowed app
import dearpygui.dearpygui as dpg

dpg.create_context()

#generate ids for all widgets we want to control
pages_id = dpg.generate_uuid()
pagesread_id = dpg.generate_uuid()
output_id = dpg.generate_uuid()

def callback():
    output = "Number of Pages Value: " + str(dpg.get_value(pages_id))
    dpg.set_value(output_id, output)

dpg.create_viewport(title='Page per Day Calculator', width=600, height=300)

with dpg.window(label="Page per Day Calculator", width = 400, height = 200):
    dpg.add_text("Welcome to the page per day calculator!")
    dpg.add_input_int(label = "How many pages are there?", width = 100, tag = pages_id)
    dpg.add_input_int(label = "How many pages have you read?", width = 100, tag = pagesread_id)
    dpg.add_input_int(label = "How many days until you have \nto be done reading this book?", width = 100)
    dpg.add_button(label="Calculate!", callback = callback)
    dpg.add_text("", tag =output_id)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()