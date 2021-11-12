def ClockSetHour():
    global hrs, hiddenfunctions
    basic.show_number(hrs)
    while hiddenfunctions == 1:
        if input.button_is_pressed(Button.A):
            hrs += -1
            basic.show_number(hrs)
        if input.button_is_pressed(Button.B):
            hrs += 1
            basic.show_number(hrs)
        if input.logo_is_pressed():
            hiddenfunctions = 2
            ClockSetMinute()
def a_test():
    global hiddenfunctions
    hiddenfunctions = 2
    basic.show_string("I am a test")

def on_button_pressed_a():
    global functions
    if not (functions == 0):
        functions += -1
        if functions < 1:
            functions = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def ClockSetMinute():
    global mins, hiddenfunctions, functions
    basic.show_number(mins)
    while hiddenfunctions == 2:
        if input.button_is_pressed(Button.A):
            mins += -1
            basic.show_number(mins)
        if input.button_is_pressed(Button.B):
            mins += 1
            basic.show_number(mins)
        if input.logo_is_pressed():
            hiddenfunctions = 0
            functions = 1
            Test()

def on_button_pressed_b():
    global functions
    if not (functions == 0):
        functions += 1
        if functions > 3:
            functions = 3
input.on_button_pressed(Button.B, on_button_pressed_b)

def Clock():
    if functions == 1:
        if mins < 10:
            basic.show_string("" + convert_to_text(hrs) + (":0" + convert_to_text(mins)))
        else:
            basic.show_string("" + convert_to_text(hrs) + (":" + convert_to_text(mins)))

def on_gesture_logo_down():
    global steps
    steps += 1
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def Test():
    basic.show_number(steps)
def setTimer():
    pass
secs = 0
mins = 0
hiddenfunctions = 0
hrs = 0
functions = 0
steps = 0
time = 0
timer = 0
steps = 0
basic.show_string("Eris")
music.play_tone(494, music.beat(BeatFraction.WHOLE))
music.play_tone(392, music.beat(BeatFraction.WHOLE))
basic.show_leds("""
    # # # # #
        # . . . #
        # # # # #
        # . . . #
        # # # # #
""")
basic.pause(3000)
steps = 0
functions = 1

def on_forever():
    global functions, hiddenfunctions
    if functions == 1 and hiddenfunctions == 0:
        if input.logo_is_pressed():
            functions = 0
            hiddenfunctions = 1
            ClockSetHour()
    if functions == 3 and hiddenfunctions == 0:
        if input.logo_is_pressed():
            functions = 0
            hiddenfunctions = 1
            setTimer()
basic.forever(on_forever)

def on_forever2():
    if functions == 1:
        Clock()
    if functions == 2:
        Test()
    if functions == 3:
        a_test()
basic.forever(on_forever2)

def on_forever3():
    global secs, mins, hrs
    basic.pause(1000)
    secs += 1
    if secs > 59:
        mins += 1
        secs = 0
        if mins > 59:
            hrs += 1
            mins = 0
            if hrs > 12:
                hrs = 1
basic.forever(on_forever3)
