#import RPi.GPIO as GPIO
import time

DEBUG = 1

g_fDashDelay = 0.2
g_fDotDelay = 0.1

g_fDashLength = 0.2
g_fDotLength = 0.1

g_fSpaceLength = 0.5

g_cCharacterPatterns = {" ": " ",
                        "A": "-.",
                        "B": "-...",
                        "C": "-.-.",
                        "D": "-..",
                        "E": ".",
                        "F": "..-.",
                        "G": "--.",
                        "H": "....",
                        "I": "..",
                        "J": ".---",
                        "K": "-.-",
                        "L": ".-..",
                        "M": "--",
                        "N": "-.",
                        "O": "---",
                        "P": ".--.",
                        "Q": "--.-",
                        "R": ".-.",
                        "S": "...",
                        "T": "-",
                        "U": "..-",
                        "V": "...-",
                        "W": ".--",
                        "X": "-..-",
                        "Y": "-.--",
                        "Z": "--..",
                        "1": ".----",
                        "2": "..---",
                        "3": "...--",
                        "4": "....-",
                        "5": ".....",
                        "6": "-....",
                        "7": "--...",
                        "8": "---..",
                        "9": "----.",
                        "0": "-----"}


def ConvertTextToMorse(pText):
    szMorse = ""
    for c in pText:
        c = c.upper()
        try:
            szMorse += g_cCharacterPatterns[c]
        except:
            print c, "does not exist in the morse code!"
        #print g_cCharacterPatterns[c],
    print szMorse
    return szMorse
szMorse = ConvertTextToMorse("hello lol")


# MAIN
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

for c in szMorse:
    if DEBUG:
            print c

    if c == '-':
        GPIO.output(12, GPIO.HIGH)
        time.sleep(g_fDashLength)
        GPIO.output(12, GPIO.LOW)
        time.sleep(g_fDashDelay)
    elif c == '.':
        GPIO.output(12, GPIO.HIGH)
        time.sleep(g_fDotLength)
        GPIO.output(12, GPIO.LOW)
        time.sleep(g_fDotDelay)
    else:
        time.sleep(g_fSpaceLength)

GPIO.cleanup()