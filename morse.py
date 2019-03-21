# The unit used here is 1 second. You can change this by replacing every time.sleep(1) to time.sleep({number of seconds})
# The length of a dot is 1 unit.
# A dash is 3 units.
# The space between parts of the same letter is one unit.
# The space between letters is 3 units.
# The space between words is 7 units.
#       A       . _             N       _ .
#       B       _ . . .         O       _ _ _
#       C       _ . _ .         P       . _ _ .
#       D       _ . .           Q       _ _ . _
#       E       .               R       . _ .
#       F       . . _ .         S       . . .
#       G       _ _ .           T       _
#       H       . . . .         U       . . _
#       I       . .             V       . . . _
#       J       . _ _ _         W       . _ _
#       K       _ . _           X       _ . . _
#       L       . _ . .         Y       _ . _ _
#       M       _ _             Z       _ _ . .


# . code:
# print(".")
# GPIO.output(18,GPIO.HIGH)
# time.sleep(1)
# GPIO.output(18,GPIO.LOW)
# time.sleep(1)


# - code:
# print("-")
# GPIO.output(18,GPIO.HIGH)
# time.sleep(3)
# GPIO.output(18,GPIO.LOW)
# time.sleep(1)


# Todays message:
# HI GUYS


import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.LOW)

# H ( . . . . )
print(".")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
GPIO.output(18,GPIO.LOW)
time.sleep(1)
print(".")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
GPIO.output(18,GPIO.LOW)
time.sleep(1)
print(".")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
GPIO.output(18,GPIO.LOW)
time.sleep(1)
print(".")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
GPIO.output(18,GPIO.LOW)

print(" ")
time.sleep(3)

# I ( . . )
print(".")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
GPIO.output(18,GPIO.LOW)
time.sleep(1)
print(".")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
GPIO.output(18,GPIO.LOW)
time.sleep(1)

# (space)

print(" ")
print(" ")
time.sleep(7)

# G ( - - . )
print("-")
GPIO.output(18,GPIO.HIGH)
time.sleep(3)
GPIO.output(18,GPIO.LOW)
time.sleep(1)
print("-")
GPIO.output(18,GPIO.HIGH)
time.sleep(3)
GPIO.output(18,GPIO.LOW)
time.sleep(1)
print(".")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
GPIO.output(18,GPIO.LOW)
time.sleep(1)

print(" ")
time.sleep(3)


# U ( . . _ )
print(".")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
GPIO.output(18,GPIO.LOW)
time.sleep(1)
print(".")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
GPIO.output(18,GPIO.LOW)
time.sleep(1)
print("-")
GPIO.output(18,GPIO.HIGH)
time.sleep(3)
GPIO.output(18,GPIO.LOW)
time.sleep(1)


print(" ")
time.sleep(3)

# Y ( _ . _ _ )
print("-")
GPIO.output(18,GPIO.HIGH)
time.sleep(3)
GPIO.output(18,GPIO.LOW)
time.sleep(1)
print(".")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
GPIO.output(18,GPIO.LOW)
time.sleep(1)
print("-")
GPIO.output(18,GPIO.HIGH)
time.sleep(3)
GPIO.output(18,GPIO.LOW)
time.sleep(1)
print("-")
GPIO.output(18,GPIO.HIGH)
time.sleep(3)
GPIO.output(18,GPIO.LOW)
time.sleep(1)


print(" ")
time.sleep(3)

# S ( . . . )
print(".")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
GPIO.output(18,GPIO.LOW)
time.sleep(1)
print(".")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
GPIO.output(18,GPIO.LOW)
time.sleep(1)
print(".")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
GPIO.output(18,GPIO.LOW)
time.sleep(1)
