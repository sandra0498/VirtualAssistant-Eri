import dearpygui.dearpygui as dpg
from dearpygui.core import *
import pyttsx3 as ts
engine = ts.init()



def save_callback(name):
    engine.say(name)
    engine.runAndWait()

    



dpg.create_context()

dpg.create_viewport()

dpg.setup_dearpygui()



with dpg.window(label="Assistant Eri"):


    dpg.add_input_text(hint="Enter your name here", name="user")

    dpg.add_button(label="Say hello")

    dpg.add_text("Hello world")

    dpg.add_button(label="Save", callback=save_callback(user))

    dpg.add_input_text(label="string")

    dpg.add_slider_float(label="float")



dpg.show_viewport()

dpg.start_dearpygui()

dpg.destroy_context()
