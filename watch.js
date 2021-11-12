function ClockSetHour () {
    basic.showNumber(hrs)
    while (hiddenfunctions == 1) {
        if (input.buttonIsPressed(Button.A)) {
            hrs += -1
            basic.showNumber(hrs)
        }
        if (input.buttonIsPressed(Button.B)) {
            hrs += 1
            basic.showNumber(hrs)
        }
        if (input.logoIsPressed()) {
            hiddenfunctions = 2
            ClockSetMinute()
        }
    }
}
function a_test () {
    hiddenfunctions = 2
    basic.showString("I am a test")
}
input.onButtonPressed(Button.A, function () {
    if (!(functions == 0)) {
        functions += -1
        if (functions < 1) {
            functions = 1
        }
    }
})
function ClockSetMinute () {
    basic.showNumber(mins)
    while (hiddenfunctions == 2) {
        if (input.buttonIsPressed(Button.A)) {
            mins += -1
            basic.showNumber(mins)
        }
        if (input.buttonIsPressed(Button.B)) {
            mins += 1
            basic.showNumber(mins)
        }
        if (input.logoIsPressed()) {
            hiddenfunctions = 0
            functions = 1
            Test()
        }
    }
}
input.onButtonPressed(Button.B, function () {
    if (!(functions == 0)) {
        functions += 1
        if (functions > 3) {
            functions = 3
        }
    }
})
function Clock () {
    if (functions == 1) {
        if (mins < 10) {
            basic.showString("" + convertToText(hrs) + (":0" + convertToText(mins)))
        } else {
            basic.showString("" + convertToText(hrs) + (":" + convertToText(mins)))
        }
    }
}
input.onGesture(Gesture.LogoDown, function () {
    steps += 1
})
function Test () {
    basic.showNumber(steps)
}
function setTimer () {
	
}
let secs = 0
let mins = 0
let hiddenfunctions = 0
let hrs = 0
let functions = 0
let steps = 0
let time = 0
let timer = 0
steps = 0
basic.showString("Eris")
music.playTone(494, music.beat(BeatFraction.Whole))
music.playTone(392, music.beat(BeatFraction.Whole))
basic.showLeds(`
    # # # # #
    # . . . #
    # # # # #
    # . . . #
    # # # # #
    `)
basic.pause(3000)
steps = 0
functions = 1
basic.forever(function () {
    if (functions == 1 && hiddenfunctions == 0) {
        if (input.logoIsPressed()) {
            functions = 0
            hiddenfunctions = 1
            ClockSetHour()
        }
    }
    if (functions == 3 && hiddenfunctions == 0) {
        if (input.logoIsPressed()) {
            functions = 0
            hiddenfunctions = 1
            setTimer()
        }
    }
})
basic.forever(function () {
    if (functions == 1) {
        Clock()
    }
    if (functions == 2) {
        Test()
    }
    if (functions == 3) {
        a_test()
    }
})
basic.forever(function () {
    basic.pause(1000)
    secs += 1
    if (secs > 59) {
        mins += 1
        secs = 0
        if (mins > 59) {
            hrs += 1
            mins = 0
            if (hrs > 12) {
                hrs = 1
            }
        }
    }
})
