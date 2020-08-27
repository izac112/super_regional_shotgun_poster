import time

import PySimpleGUI as sg
from pynput.keyboard import Key, Controller as KeyboardController

# defines
kb = KeyboardController()

##Functions##
# presses enter
def chat_enter():
    kb.press(Key.enter)
    kb.release(Key.enter)


# adds the start of the regional
def chat_regional():
    for char in ":regional_indicator_":
        kb.press(char)
        kb.release(char)


# cleans string of white spaces
def chat_remove_space(string):
    return string.replace(" ", "")


# shotgun Posts
def chat_shotgun(string):
    for char in string:
        chat_regional()
        kb.press(char)
        # adds the : at the end to complete the regional
        kb.press(':')
        kb.release(':')
        chat_enter()


##Gui Stuff##
sg.theme('Purple') # theme
# all the stuff inside the window.
layout = \
    [
        [sg.Text('String to Type'), sg.InputText()],
        [sg.Text('Time Delay'), sg.InputText()],
        [sg.Button('Post'), sg.Button('Exit')]
    ]
# create the Window
window = sg.Window('Super Regional Shotgun Poster', layout)
# event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
        break
    print("'", values[0], "'", 'will be typed without the white spaces', )
    print('in', values[1], 'seconds')
    delay = int(values[1])
    time.sleep(delay)
    c_string = chat_remove_space(values[0])
    chat_shotgun(c_string)
window.close()
