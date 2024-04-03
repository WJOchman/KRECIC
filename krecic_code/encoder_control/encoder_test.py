import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

in1 = 23
in2 = 24
en = 25

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)

pwm = GPIO.PWM(en, 1000)
pwm.start(0)

encoder = 22
GPIO.setup(encoder, GPIO.IN, pull_up_down=GPIO.PUD_UP)
encoder_count = 0

def encoder_callback(channel):
    global encoder_count
    encoder_count += 1

GPIO.add_event_detect(encoder, GPIO.RISING, callback=encoder_callback)

def motor_forward(speed_pct):
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    pwm.ChangeDutyCycle(speed_pct)

try:
    motor_forward(50)
    time.sleep(5)
    motor_forward(0)
    print("Encoder Count: ", encoder_count)

except KeyboardInterrupt:
    print("Program Stopped")

finally:
    pwm.stop()
    GPIO.cleanup()

