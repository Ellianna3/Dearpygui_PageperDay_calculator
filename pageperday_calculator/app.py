#  My DearPyGUI windowed app
import dearpygui.dearpygui as dpg

dpg.create_context()

#generate ids for all widgets we want to control
pages_id = dpg.generate_uuid()
pagesread_id = dpg.generate_uuid()
output_id = dpg.generate_uuid()
days_id = dpg.generate_uuid()

# callback functions
def get_pagenum():
    pagenum = dpg.get_value(pages_id)
    pagesread = dpg.get_value(pagesread_id)
    days = dpg.get_value(days_id)
    final = calculate_pages(pagenum, pagesread, days)
    output = get_output(pagenum, pagesread, days, final)
    dpg.set_value(output_id, output)

def calculate_pages(pn, pr, d):
    return int((pn - pr) / d)

def get_output(pn, pr, d, f):
    output = "With {} pages in the book". format(pn)
    output += "\nand {} pages already read". format(pr)
    output += "\nand {} days to read the book". format(d)
    output += "\nyou have to read {} pages a day to finish this \nbook on time!".format(f)
    return output


dpg.create_viewport(title='Page per Day Calculator', width=600, height=300)

with dpg.window(label="Page per Day Calculator", width = 350, height = 250):
    dpg.add_text("Welcome to the page per day calculator!")
    dpg.add_input_int(label = "How many pages are there?", width = 100, tag = pages_id)
    dpg.add_input_int(label = "How many pages have you read?", width = 100, tag = pagesread_id)
    dpg.add_input_int(label = "How many days until you have \nto be done reading this book?", width = 100, tag = days_id)
    dpg.add_button(label="Calculate!", callback = get_pagenum)
    dpg.add_text("", tag =output_id)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()