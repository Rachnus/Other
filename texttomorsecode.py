import RPi.GPIO as GPIO
import time
import sys

DEBUG = 1

# The delay after a - in seconds
g_fDashDelay = 0.12

# The delay after a . in seconds
g_fDotDelay = 0.08

# The length of a - beep in seconds
g_fDashLength = 0.12

# The length of a . beep in seconds
g_fDotLength = 0.08

# The delay after a letter in seconds
g_fLetterDelay = 0.1

# The delay after a space (/) in seconds
g_fSpaceDelay = 0.3

g_iGPIOPin = 12

# Define what letters translate to what code
g_cCharacterPatterns = {" ": "/",
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


# Function to convert text to morse code
def ConvertTextToMorse(pText):
    szMorse = ""
    for c in pText:
        if c != " ":
            c = c.upper()
        try:
            szMorse += g_cCharacterPatterns[c] + " "
        except:
            print c, "does not exist in the morse code!"
            sys.exit()
    szMorse = szMorse[:-1]
    if DEBUG:
        print szMorse
    return szMorse

# MAIN
GPIO.setmode(GPIO.BOARD)

GPIO.setup(g_iGPIOPin, GPIO.OUT)

szText = "testing"
szMorse = ConvertTextToMorse(szText)
if DEBUG:
    print szText

for c in szMorse:
    if DEBUG:
        print c

    if c == '-':
        GPIO.output(g_iGPIOPin, GPIO.HIGH)
        time.sleep(g_fDashLength)
        GPIO.output(g_iGPIOPin, GPIO.LOW)
        time.sleep(g_fDashDelay)
    elif c == '.':
        GPIO.output(g_iGPIOPin, GPIO.HIGH)
        time.sleep(g_fDotLength)
        GPIO.output(g_iGPIOPin, GPIO.LOW)
        time.sleep(g_fDotDelay)
    elif c == '/':
        time.sleep(g_fSpaceDelay)
    else:
        time.sleep(g_fLetterDelay)

GPIO.cleanup()