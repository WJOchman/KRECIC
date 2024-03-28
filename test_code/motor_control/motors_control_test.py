import RPi.GPIO as GPIO
from time import sleep

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

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
pwm_a = GPIO.PWM(en1, 1000)

GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)
pwm_b = GPIO.PWM(en2, 1000)

pwm_a.start(50)
pwm_b.start(50)

def motor_forward():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    print("Motor moving forward")

def motor_backward():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    print("Motor moving backward")

def motor_stop():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    print("Motor stopped")

def set_speed(speed):
    pwm_a.ChangeDutyCycle(speed)
    pwm_b.ChangeDutyCycle(speed)

def cleanup_gpio():
    pwm_a.stop()
    pwm_b.stop()
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