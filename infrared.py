switch_pin = 18

while True:
   if GPIO.input(switch_pin)==True:
     print("letter is in the way")
   else:
     print("no letter")
