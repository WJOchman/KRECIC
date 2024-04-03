import RPi.GPIO as GPIO
import time
import curses

in1 = 23
in2 = 24
en1 = 25

in3 = 17
in4 = 27
en2 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en1, GPIO.OUT)

GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)

pwm_a = GPIO.PWM(en1, 1000)
pwm_b = GPIO.PWM(en2, 1000)

pwm_a.start(0)
pwm_b.start(0)

def stop_motors():
    pwm_a.ChangeDutyCycle(0)
    pwm_b.ChangeDutyCycle(0)

def forward():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    pwm_a.ChangeDutyCycle(75)
    pwm_b.ChangeDutyCycle(75)

def backward():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    pwm_a.ChangeDutyCycle(75)
    pwm_b.ChangeDutyCycle(75)

def left():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    pwm_a.ChangeDutyCycle(75)
    pwm_b.ChangeDutyCycle(75)

def right():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    pwm_a.ChangeDutyCycle(75)
    pwm_b.ChangeDutyCycle(75)

def control(stdscr):
    stdscr.nodelay(True)
    stdscr.clear()

    while True:
        char = stdscr.getch()

        if char == ord('q'):
            break
        elif char == ord('w'):
            forward()
        elif char == ord('s'):
            backward()
        elif char == ord('a'):
            left()
        elif char == ord('d'):
            right()
        else:
            stop_motors()
        
        time.sleep(0.1)

try:
    curses.wrapper(control)
finally:
    pwm_a.stop()
    pwm_b.stop()
    GPIO.cleanup()