#!/usr/bin/python

from time import sleep
import sys

pause = 1
text = sys.argv[1]
morse = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
        "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
        "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
        "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
        "y": "-.--", "z": "--.."}

def led(state):
    led = open("/sys/kernel/debug/ec/ec0/io", "wb")
    led.seek(12)
    if state:
        led.write(b"\x8a")
    else:
        led.write(b"\x0a")
    led.flush()

while True:
    led(True)
    sleep(1)
    words = text.split(" ")
    for word in words:
        for lettre in word:
            encoded = morse[lettre] 
            for sign in encoded:
                if sign == ".":
                    led(True)
                    sleep(pause)
                else:
                    led(True)
                    sleep(3 * pause)
                led(False)
                sleep(pause)
            led(False)
            sleep(2 * pause)
        led(False)
        sleep(5 * pause)

