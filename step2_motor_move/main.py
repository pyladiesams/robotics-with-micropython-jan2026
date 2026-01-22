from machine import Pin, PWM
import time

# The signal pin connected to the servo (Yellow/Orange wire)
SERVO_PIN = 15 # TODO update to the correct pin for the servo

# The servo specifications from the datasheet
SERVO_FREQUENCY = 50

# the frequency of the servo is 50Hz, which means one cycle period is 1s/50 = 20ms
# the minimum duty cycle is 2.5% of the 20ms, which is 0.5ms
MIN_DUTY_PERCENT = 2.5
# the maximum duty cycle is 12.5% of the 20ms, which is 2.5ms
MAX_DUTY_PERCENT = 12.5

# The maximum duty value is 1023, which is the maximum value of the PWM signal, 100%
MAX_DUTY_VALUE = 1023

# Initialize the servo
servo = PWM(Pin(SERVO_PIN), freq=SERVO_FREQUENCY)
servo.duty(0)

def setAngle(angle):
    # Convert the angle to a duty percentage
    dutyPercent = MIN_DUTY_PERCENT + (angle / 180) * (MAX_DUTY_PERCENT - MIN_DUTY_PERCENT)
    # Convert the duty percentage to a duty value
    dutyValue = int((dutyPercent / 100) * MAX_DUTY_VALUE)
    servo.duty(dutyValue)
    # Wait for the servo to move to the new angle
    time.sleep(0.05)

# # If you have a 360° continuous rotation servo, use these functions instead:
# def turnLeft():
#     dutyValue = int((5.0 / 100) * MAX_DUTY_VALUE)
#     servo.duty(dutyValue)
#     time.sleep(0.05)

# def turnRight():
#     dutyValue = int((10.0 / 100) * MAX_DUTY_VALUE)
#     servo.duty(dutyValue)
#     time.sleep(0.05)

# def stop():
#     dutyValue = int((7.5 / 100) * MAX_DUTY_VALUE)
#     servo.duty(dutyValue)
#     time.sleep(0.05)

while True:
    setAngle(0)
    time.sleep(1)
    setAngle(90)
    time.sleep(0.5)
    setAngle(180)
    time.sleep(0.5)
