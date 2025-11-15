from engine import Engine
from gui import GUI

input = Engine.input_initialize()
gui = GUI()
gui.update_screen(input)

while input["running"] : 
    input = gui.update_input(input)
    input =  Engine.interpret_input(input)
    gui.update_screen(input)

GUI.quit()