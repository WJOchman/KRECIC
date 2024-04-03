import RPi.GPIO as GPIO
from time import sleep

in1 = 23
in2 = 24
en = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
pwm = GPIO.PWM(en, 1000)
pwm.start(50)

def motor_forward():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    print("Motor moving forward")

def motor_backward():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    print("Motor moving backward")

def motor_stop():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    print("Motor stopped")

def set_speed(speed):
    pwm.ChangeDutyCycle(speed)

def cleanup_gpio():
    pwm.stop()
    GPIO.cleanup()
    print("GPIO Clean Up")

print("\n")
print("f-forward, b-backward, s-stop, l-low, m-medium, h-high, vh-very high e-exit")
print("\n")

try:
    while True:
        x = input("Enter command: ").lower()

        if x == 'f':
            print("Motor Forward")
            motor_forward()
        elif x == 'b':
            print("Motor Backward")
            motor_backward()
        elif x == 's':
            print("Motor Stop")
            motor_stop()
        elif x == 'l':
            print("Low Speed")
            set_speed(25)
        elif x == 'm':
            print("Medium Speed")
            set_speed(50)
        elif x == 'h':
            print("High Speed")
            set_speed(75)
        elif x == 'vh':
            print("Very High Speed")
            set_speed(100)
        elif x == 'e':
            print("GPIO Clean Up")
            cleanup_gpio()
            break
        else:
            print("Wrong Input!")
except KeyboardInterrupt:
    cleanup_gpio()