import dearpygui.dearpygui as dpg
import pyttsx3 as ts




def save_callback():
    engine = ts.init()
    print(dpg.get_value(user))
    # engine.say(dpg.get_value(user))
    # engine.runAndWait()
    engine.say("hello {0}", dpg.get_value(user))
    engine.runAndWait()
    engine.stop()

    

def print_value(sender):
    print(dpg.get_value(sender))
    


    


dpg.create_context()

dpg.create_viewport()

dpg.setup_dearpygui()



with dpg.window(label="Assistant Eri"):


    # dpg.add_input_text(hint="Enter your name here", name="user")
    user = dpg.add_input_text( 
        label="string",
        hint="Enter name here")
    
    dpg.add_button(label="Say hello",
    callback=save_callback)





    dpg.add_text("Hello world")

    dpg.add_button(label="Save")

    dpg.add_input_text(label="string")

    dpg.add_slider_float(label="float")



dpg.show_viewport()

dpg.start_dearpygui()

dpg.destroy_context()
