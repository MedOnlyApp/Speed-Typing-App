from tkinter import Tk, Label, ARC, Button, StringVar, Canvas, BOTH, IntVar, PhotoImage
from tkinter.ttk import Frame, Style
from customtkinter import CTkTextbox, CTkButton, CTkOptionMenu, CTkCanvas
# import keyboard as kb
from keyboard import press, press_and_release, release
from pynput import keyboard                   ## pynput for recording mouse and keyboard with mouse.listener and keyboard.listener
from threading import Thread
from ctypes import windll 
from pygetwindow import getActiveWindow

focusBorderImageData = '''
    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
    Ry/99NIz//oGrZpUUEAAOw==
'''

borderImageData = '''
    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
'''

paragraph = """We learned to see, at long last. Partway through the millennium, we figured out how to shape and polish glass so as to see far and to see small, and we dug into dead languages of previous millenniums to name our new aids to seeing telescope, microscope, spectroscope, spectrophotometer, spectroheliograph and, eventually, television. We figured out the art, the geometry and the semantics of perspective. No wonder our superheroes had X-ray vision; so did we. And infrared vision, and ultraviolet vision, and gamma-ray vision and nuclear magnetic resonant vision. We extended our sight far beyond the tiny spectrum our unaided eyes could handle, from violet to red. We looked out, and we looked inside. We saw where earth is and what humans are. We noticed quasars and we noticed viruses. Surprise! "In all falling rain, carried from gutters into water butts, animalcules are to be found. in all kinds of water, standing in the open air, animalcules can turn up" noted Anton van Leeuwenhoek, the first man to observe bacteria. We figured out some things about color and space"""
paragraph_index = 0
shift_key = False
previous_space = 0
word = ""

def is_caps_lock_on():   ## Check if the caps lock key is on
    ## Checks if Caps Lock is on in Windows
    ## windll from ctypes
    return windll.user32.GetKeyState(0x14) & 0x0001 != 0

def on_press(key):
    global index_int, paragraph_index, shift_key, previous_space, word, correct_words, incorrect_words, words_state
    print('{0} pressed'.format(key))

    ## if this window is not the active window then return
    try:
        if getActiveWindow().title != "Speed Typing": ## getActiveWindow from pygetwindow
            return
    except:
        return

    ## Get the current text box cursor index
    index_str = text_box.index("insert")
    index_int = int(index_str[2:])

    ## Get the names of all the tags in the text box
    tags_list = text_box.tag_names()

    if str(paragraph_index) not in tags_list: ## if this tag does not exist 
        ## create a tag in the current text box index and configure it
        text_box.tag_add(f"{paragraph_index}", index1=index_str)
        text_box.tag_config(f"{paragraph_index}", underline=True, underlinefg="#0049b2")
    else :      ## if the tag already exists 
        pass
    
    if len(format(key)) == 3 or format(key).startswith("<") and format(key).endswith(">"):     ## if a letter key was pressed
 
        if len(format(key)) == 3:
            letter = format(key)[1]
        elif format(key).startswith("<") and format(key).endswith(">"):
            number = int(format(key)[1:-1]) - 96
            if number > 10:
                letter = "."
            else :
                letter = str(number)

        if is_caps_lock_on() == True:  ## check if the caps lock key is on 
            if ord(letter) >= 97 and ord(letter) <= 122:
                ## if a letter key is pressed (a-z) then change the letter to upper case
                letter = letter.upper()
            elif shift_key == False:
                ## if a symbol key is pressed (, or ; or :) without the shift key first
                ## Press shift
                press("shift")
                ## then press and release the entered key
                press_and_release(letter)
                return
                
        if letter == paragraph[paragraph_index]:
            ## if the entered letter match the current letter in the text box --> Colorate the foreground of the letter with blue
            text_box.tag_config(f"{paragraph_index}", foreground="#0049b2", underline=False)
        else:
            ## if the entered letter does not match the current letter in the text box --> Colorate the foreground of the letter with red
            text_box.tag_config(f"{paragraph_index}", foreground="#b22300", underline=False)

        ## Create a tag for the next letter in the text box and underline it
        text_box.tag_add(f"{paragraph_index + 1}", index1=f"1.{index_int + 1}")
        text_box.tag_config(f"{paragraph_index + 1}", underline=True, underlinefg="#0049b2")

        paragraph_index += 1
        ## move the text box cursor to the next letter
        text_box.mark_set('insert', '1.{0}'.format(index_int + 1))
        ## Release shift key >>> this is needed when the caps lock key is on and the user input is a symbol like (caps lock + ,)-->(shift + ,)-->(.)
        release("shift")
        ## add this letter to the input_letters list
        input_letters.append(letter)
    elif format(key) == "Key.backspace": ## if backspace key was pressed
        ## Return the cursor to the previous letter in the text box 
        text_box.mark_set('insert', '1.{0}'.format(index_int - 1))
        ## Delete the last tag
        text_box.tag_delete(f"{paragraph_index}")
        paragraph_index -= 1
        text_box.tag_config(f"{paragraph_index}", foreground="#000000", underline=True, underlinefg="#0049b2")
        ## Remove the last letter from the input_letters list
        try:
            input_letters.pop()
        except:
            pass
    elif format(key) == "Key.space":   ## if the space key was pressed

        if paragraph[paragraph_index] == ' ':
            ## if the entered letter match the current letter in the text box --> Colorate the foreground of the letter with blue
            text_box.tag_config(f"{paragraph_index}", foreground="#0049b2", underline=False)
        else:
            ## if the entered letter does not match the current letter in the text box --> Colorate the foreground of the letter with red
            text_box.tag_config(f"{paragraph_index}", foreground="#b22300", underline=False)

        ## Create a tag for the next letter in the text box and underline it
        text_box.tag_add(f"{paragraph_index + 1}", index1=f"1.{index_int + 1}")
        text_box.tag_config(f"{paragraph_index + 1}", underline=True, underlinefg="#0049b2")

        paragraph_index += 1
        ## move the text box cursor to the next letter
        text_box.mark_set('insert', '1.{0}'.format(index_int + 1))
        ## add this space to the input_letters list
        input_letters.append(" ")

    ## This determens if the shift key is pressed or not
    if format(key) == "Key.shift" or format(key) == "Key.shift_r":
        shift_key = True
    else:
        shift_key = False

    if format(key) == "Key.backspace":
        if paragraph[paragraph_index + 1] == " ":
            ## Decrease the wpm/min frame by 1
            WPM_var.set(WPM_var.get() - 1)
            if words_state[-1] == True:
                correct_words -= 1
            else:
                incorrect_words -= 1
            ## Delete the state of the last word
            words_state.pop()
            ## Set the accuracy if the accuracy frame 
            ACCURACY_var.set(int((100 * correct_words) / len(words_state)))
    elif format(key) == "Key.space" or len(format(key)) == 3:
        if paragraph[paragraph_index - 1] == " ":
            ## find the index of the last space
            index = paragraph.rfind(" ", 0, paragraph_index - 1)
            ## Increase the wpm/min frame by 1
            WPM_var.set(WPM_var.get() + 1)
            if paragraph[index + 1:paragraph_index - 1] == "".join(input_letters[index + 1:paragraph_index - 1]):
                words_state.append(True)
                correct_words += 1
            else:
                words_state.append(False)
                incorrect_words += 1
            ## Set the accuracy if the accuracy frame 
            ACCURACY_var.set(int((100 * correct_words) / len(words_state)))

    ## Increase or decrease the char/min frame by 1
    CHPM_var.set(len(input_letters))
    return

def keyboard_listener():    ## keyboard information
    global listener_k
    with keyboard.Listener(on_press=on_press) as listener_k:
        ## start collecting keyboard presses and releases
        listener_k.join()  
    return

def return_to_main_motion(): ## Return to the main page motion
    x = 0
    def motion():
        nonlocal x
        x += 50
        ## Move the typing_test_frame horizontally until it gets out of the window then destroy it
        typing_test_frame.place(x=x,y=0)
        if x < 950:
            typing_test_frame.after(20, motion)
        else:
            typing_test_frame.destroy()
        return
    motion()
    return

def end_test_motion():      ## Last motion when the test is finished
    global paragraph_index
    ## Stop the keyboard listener
    listener_k.stop()

    ## new_width of the canvas
    new_width = 150
    def motion():   ## End test motion
        nonlocal new_width
        ## Add 50 to the canvas width to create a motion
        new_width += 50
        side_canvas.config(width=new_width) ## configure the new width

        if new_width < 750:     ## if the canvas width is less than 750
            ## wait 20 ms then call the motion function to increase the canvas width again width=750
            side_canvas.after(20, motion)
    
        return
    
    ## Create the last labels to show the test results
    Label(side_frame, text="Typing Test Complete!", background="#ffffff", font="Arial 19 bold").place(x=300,y=150)
    Label(side_frame, text="You typed the", background="#ffffff", font="Arial 15 bold").place(x=210,y=215)
    Label(side_frame, text=f"{test_name} Typing Test.", background="#ffffff", font="Arial 20 bold").place(x=350,y=210)
    text_label = CTkTextbox(side_frame, font=("Arial bold", 17), cursor="arrow", fg_color="#ffffff", text_color="#000000", width=400, height=50)
    text_label.place(x=270,y=270)
    text_label.insert(index='1.0',text=F"Your speed was {WPM_var.get()} wpm with {"{:02d}".format(ACCURACY_var.get())}% accuracy!")
    text_label.tag_add("1", "1.15", "1.20" if len(str(WPM_var.get())) == 1 else "1.21" if len(str(WPM_var.get())) == 2 else "1.22")
    text_label.tag_config("1", foreground= "#488206")
    start = "1.26" if len(str(WPM_var.get())) == 1 else "1.27" if len(str(WPM_var.get())) == 2 else "1.28"
    end = f"1.{int(start[2:]) + 2 if len(str(ACCURACY_var.get())) == 1 else int(start[2:]) + 3 if len(str(ACCURACY_var.get())) == 2 else int(start[2:]) + 4}" 
    text_label.tag_add("2", start, end)
    text_label.tag_config("2", foreground= "#488206")
    ## Disable the text box to be like a label
    text_label.configure(state="disabled")
    ## Bind the text_label to block_mouse to block text selection 
    text_label.bind("<B1-Motion>", block_mouse)
    text_label.bind("<Button-1>", block_mouse)
    ## Try again button
    CTkButton(side_frame, text="Try Again", font=("Arial bold", 15), command=try_again_command).place(x=350,y=350)

    motion()
    
    ## Reset the paragraph_index to 0
    paragraph_index = 0
    return

def block_mouse(event):     ## Block the mouse click and the mouse click and drag in the text box
    return "break"

def draw_circle_gradually(canvas, x, y, radius, duration):  ## Draw the clock circle
    ## Start drawing from the 90 angle
    start_angle = 90
    end_angle = 90
    if duration == 60 / 2:      ## if it is the 30 seconds test
        angle = 0.58 * 2  ## the value of the Increased angle each time
    elif duration == 60:        ## if it is the 1 minute test
        angle = 0.58      ## the value of the Increased angle each time
    elif duration == 60 * 2:    ## if it is the 2 minutes test
        angle = 0.58 / 2  ## the value of the Increased angle each time
    elif duration == 60 * 3:    ## if it is the 3 minutes test
        angle = 0.58 / 3  ## the value of the Increased angle each time
    elif duration == 60 * 5:    ## if it is the 5 minutes test
        angle = 0.58 / 5  ## the value of the Increased angle each time
    elif duration == 60 * 10:   ## if it is the 10 minutes test
        angle = 0.58 / 10 ## the value of the Increased angle each time

    ## the number of time the draw_arc function is called
    occ = 0

    def draw_arc():    ## Drawing the circle
        nonlocal start_angle, end_angle, occ
        end_angle += angle  # Increase end_angle by angle degrees each time

        if occ % 10 == 0: ## After calling the draw_arc function 10 times, decrese the clock by 1 second
            time_var_2.set("{:02d}".format(int(time_var_2.get()) - 1))

        ## Draw the circle from the start_angle to the start_angle + added angle
        arc = canvas.create_arc(x - radius, y - radius, x + radius, y + radius,
                                start=start_angle, extent=10, style=ARC, outline="#ffffff", width=5)
        start_angle = end_angle

        if occ < 10 * duration - 1: ## if the circle is not finished
            occ += 1
            ## Wait 100 ms then call the draw_arc function
            canvas.after(100, draw_arc)  # Adjust delay for drawing speed
        else :                      ## if the circle is finished
            ## End the test with the end_test_motion
            end_test_motion()

    draw_arc()

def block_input(event):     ## Block the text input in the text box
    global drawing, test_name
    ## if the index of the text box is 0 and the drawing variable is false
    if index_int == 0 and drawing == False:
        ## Set the choosen test name in the test_name variable
        test_name = f"{time_var_2.get()} Seconds" if int(time_var_2.get()) > 10 else f"{time_var_2.get() / 60} Minite" if int(time_var_2.get()) == 60 else f"{time_var_2.get() / 60} Minites"
        ## set the choosen duration
        duration =  int(time_var_2.get())
        ## Start the clock
        draw_circle_gradually(side_canvas, 75, 75, 40, duration)

        drawing = True
        
    ## Block the input in the text box
    return "break"

def try_again_command():
    ## destroy the text_frame and the side_frame
    text_frame.destroy()
    side_frame.destroy()
    ## The "Try again" parameter helps create only a new text_frame and the side_frame without the typing_speed_frame and the header_frame
    typing_test_command(event="Try again")
    return

def typing_test_command(event):
    global typing_test_frame, text_box, text_frame, side_canvas, side_frame
    global input_letters, correct_words, incorrect_words, words_state, index_int, drawing, previous_key
    global ACCURACY_var, WPM_var, CHPM_var, time_var_2, time_var

    ## This list is for storing the typed letter in the keyboard
    input_letters = []
    ## This list is for storing the state of the words (True for correct, False for incorrect)
    words_state = []
    ## Variable for storing the number of correct words
    correct_words = 0
    ## Variable for storing the number of incorrect words
    incorrect_words = 0

    ## Start keyboard listener in a thread
    Thread(target=keyboard_listener).start()

    if event != "Try again":
        ## Background frame
        typing_test_frame = Frame(root)##, background="#ffffff")
        typing_test_frame.place(x=0,y=0)
        typing_test_canvas = CTkCanvas(typing_test_frame, background="#ffffff", width=1920, height=1080)
        typing_test_canvas.pack(fill="both", expand=True)

        ## Return Arrow frame and button
        return_arrow_frame = Frame(typing_test_frame, style="RoundedFrame", padding=10)
        return_arrow_frame.place(x=70, y=57)
        return_arrow_button = Button(return_arrow_frame, image=return_arrow_image, background="#ffffff", borderwidth=0, command=return_to_main_motion)
        return_arrow_button.pack(padx=5, pady=5)

        ## Header frame
        header_frame = Frame(typing_test_frame, style="RoundedFrame", padding=10)
        header_frame.place(x=250, y=50)
        ## Text type combobox
        text_var = StringVar()
        text_var.set("Beginner")
        text_combobox = CTkOptionMenu(header_frame, variable=text_var, values=["Beginner", "Intemediate", "Advanced"], width=160)
        text_combobox.grid(row=0,column=0, padx=10, pady=10)
        ## Time combobox
        time_var = StringVar()
        time_var.set("30 Seconds Test")
        time_combobox = CTkOptionMenu(header_frame, dropdown_hover_color="#e2e535", variable=time_var, values=["30 Seconds Test", "1 Minute Test", "2 Minutes Test", "3 Minutes Test", "5 Minutes Test", "10 Minutes Test"], width=160)
        time_combobox.grid(row=0,column=1, padx=30, pady=10)
        ## Start button
        start_test_button = CTkButton(header_frame, text='Start test', font=("Arial bold", 15), command=try_again_command)
        start_test_button.grid(row=0,column=2, padx=10, pady=10)

    ## Text frame
    text_frame = Frame(typing_test_frame, style="RoundedFrame", padding=10)
    text_frame.place(x=250,y=155)
    text_canvas = Canvas(text_frame, background="#ffffff", borderwidth=0, highlightthickness=0, width=560, height=450)
    text_canvas.pack()
    ## Text box
    text_box = CTkTextbox(text_frame, spacing2=20, fg_color="#ffffff", exportselection=0, text_color="#000000", border_width=0, font=("Courier New", 35), wrap="word", undo=True, width=550, height=430)
    text_box.place(x=5, y=10)
    ## insert the paragraph in the text box
    text_box.insert("1.0", paragraph)

    # Bind key events to block input
    text_box.bind("<Key>", block_input)
    text_box.bind("<Button-1>", block_mouse)
    text_box.bind("<B1-Motion>", block_mouse)

    ## add a tag on the first character
    text_box.tag_add(f"{paragraph_index}", "1.0")
    text_box.tag_config(f"{paragraph_index}", underline=True, underlinefg="#0049b2")

    text_box.focus()
    ## set the marker to the first caracter in the text box
    text_box.mark_set("insert", "1.0")
    ## the int index of the letters in the text box
    index_int = 0
    ## this variable is for the clock start
    drawing = False

    ## Side frame
    side_frame = Frame(typing_test_frame, style="RoundedFrame", padding=10)
    side_frame.place(x=60, y=155)
    side_canvas = Canvas(side_frame, background="#ffffff", borderwidth=0, highlightthickness=0, width=150, height=450)
    side_canvas.pack()

    time_var_2 = StringVar()
    time_var_2.set(int(time_var.get().split()[0]) if int(time_var.get().split()[0]) > 10 else int(time_var.get().split()[0]) * 60)
    time_label = Label(side_frame, background="#ffffff", textvariable=time_var_2, font=("Helvetica Bold", 20))
    time_label.place(x=56,y=55)
    side_canvas.create_oval(75 - 40, 75 - 40, 75 + 40, 75 + 40, outline="#d8f44c", width=5)

    ## words/min frame / Int Varaible / labels
    WPM_frame = Frame(side_frame, style="RoundedFrame", padding=10)
    WPM_frame.place(x=25,y=150)
    WPM_var = IntVar()
    WPM_var.set(0)
    WPM_label = Label(WPM_frame, textvariable=WPM_var, font=("Arial bold", 15), background="#ffffff")
    WPM_label.pack(padx=5)
    Label(WPM_frame, text="words/min", background="#ffffff").pack(padx=5)

    ## chars/min frame / Int Varaible / labels
    CHPM_frame = Frame(side_frame, style="RoundedFrame", padding=10)
    CHPM_frame.place(x=25,y=250)
    CHPM_var = IntVar()
    CHPM_var.set(0)
    CHPM_label = Label(CHPM_frame, textvariable=CHPM_var, font=("Arial bold", 15), background="#ffffff")
    CHPM_label.pack(padx=5)
    Label(CHPM_frame, text="chars/min", background="#ffffff").pack(padx=5)

    ## Accuracy frame / Int Varaible / labels
    ACCURACY_frame = Frame(side_frame, style="RoundedFrame", padding=10)
    ACCURACY_frame.place(x=25,y=350)
    ACCURACY_var = IntVar()
    ACCURACY_var.set(100)
    ACCURACY_label = Label(ACCURACY_frame, textvariable=ACCURACY_var, font=("Arial bold", 15), background="#ffffff")
    ACCURACY_label.pack(padx=5)
    Label(ACCURACY_frame, text="%accuracy", background="#ffffff").pack(padx=5)


    return

def main_window():  ## Create the main window

    ## Create a rounded frame and put a canvas, image and a label inside
    frame1 = Frame(root, style="RoundedFrame", padding=10)
    frame1.grid(row=0, column=0, padx=40, pady=200)
    canvas1 = Canvas(frame1, background="#ffffff", borderwidth=0, highlightthickness=0, height=250, width=200)
    canvas1.pack(fill=BOTH, expand=True)
    image_label = Label(frame1, image=typing_test_image, borderwidth=0, highlightthickness=0)
    image_label.place(x=0,y=0)
    text_label = Label(frame1, text="Speed Typing Test", font=("Arial bold", 15), borderwidth=0, highlightthickness=0, background="#ffffff")
    text_label.place(x=10,y=220)

    ## Bind the frame, image and label to the typing_test_command 
    frame1.bind("<Button-1>", typing_test_command)
    image_label.bind("<Button-1>", typing_test_command)
    text_label.bind("<Button-1>", typing_test_command)

    ## Create a second rounded frame 
    frame2 = Frame(root, style="RoundedFrame", padding=10)
    frame2.grid(row=0, column=1, padx=40, pady=200)
    canvas2 = Canvas(frame2, background="#ffffff", borderwidth=0, highlightthickness=0, height=250, width=200)
    canvas2.pack(fill=BOTH, expand=True)

    ## Create a third rounded frame 
    frame3 = Frame(root, style="RoundedFrame", padding=10)
    frame3.grid(row=0, column=2, padx=40, pady=200)
    canvas3 = Canvas(frame3, background="#ffffff", borderwidth=0, highlightthickness=0, height=250, width=200)
    canvas3.pack(fill=BOTH, expand=True)

    return

def Exit():  ## Close window action
    print("this is exit function !")
    try:  ## Stop the keybord listener if it is ON
        listener_k.stop()
    except:
        pass
    ## Close the window
    root.destroy()
    return

def main():
    global root, main_frame
    global typing_test_image, return_arrow_image

    ## create a window
    root = Tk()
    ## Disable horizontale resize
    root.resizable(False, True)
    ## Name the window
    root.title("Speed Typing")
    ## Set the window size and position
    root.geometry("900x700+200+50")
    ## Set the window background color
    root.configure(background="white")
    ## Set the program icon
    root.iconbitmap('src/typing.ico')
    ## Create a new style for the frames
    style = Style()
    borderImage = PhotoImage("borderImage", data=borderImageData)
    focusBorderImage = PhotoImage("focusBorderImage", data=focusBorderImageData)
    style.element_create("RoundedFrame", "image", borderImage, ("focus", focusBorderImage), border=16, sticky="nsew")
    style.layout("RoundedFrame", [("RoundedFrame", {"sticky": "nsew"})])

    ## Define the images
    typing_test_image = PhotoImage(file="src/typing_test.png")
    return_arrow_image = PhotoImage(file="src/return-arrow.png")

    ## Create the main window
    main_window()

    ## assign a function to the window close command
    root.wm_protocol("WM_DELETE_WINDOW", Exit)

    ## Loop the window
    root.mainloop()


    return

if __name__ == "__main__":
    main()


## pyinstaller --onefile --windowed --icon=typing.ico Programe.py --name "Speed Typing"