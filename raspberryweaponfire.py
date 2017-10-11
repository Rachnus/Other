import socket
import time
import RPi.GPIO as GPIO

# Global Variables
GPIO_PIN = 12
HOST = '192.168.1.100'
PORT = 1738

BEEP_TIME = 0.1

# MAIN
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_PIN, GPIO.OUT)
GPIO.setwarnings(False)

g_hSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    g_hSock.bind((HOST, PORT))
except socket.error:
    print 'Bind failed'

g_hSock.listen(1)
print 'Socket listening to weapon fire'
(conn, addr) = g_hSock.accept()
print 'Connected'

# Waiting for beep
while True:
    data = conn.recv(1024)
    print "Fire"
    GPIO.output(GPIO_PIN, GPIO.HIGH)
    time.sleep(BEEP_TIME)
    GPIO.output(GPIO_PIN, GPIO.LOW)

# Close connection
conn.close()
GPIO.cleanup()