import pigpio
from time import sleep
#For now only test one motor on GPIO7 (Pin26) http://imagizer.imageshack.us/a/img577/3040/raspberrypirev2pinout.jpg
#Motor1A = 16
#Motor1B = 18
Motor1E = 7

#Define PWM here or use as a refrence
PWM = 128
Rate_of_change = 32
Direction = 1


#Motor2A = 19
#Motor2B = 21
#Motor2E = 23

pi = pigpio.pi()
#pi.set_mode(Motor1A, pigpio.OUTPUT)
#pi.set_mode(Motor1B, pigpio.OUTPUT)
pi.set_mode(Motor1E, pigpio.OUTPUT)
#pi.set_PWM_range(9,100)

for x in range(0, 5): #For five iterations http://www.raspberrypi.org/forums/viewtopic.php?f=33&t=88323
  
  gpioPWM(Motor1E, PWM) #Read up http://abyz.co.uk/rpi/pigpio/cif.html#gpioPWM
  PWM += (Direction * Rate_of_change)
  if PWM < 0 or PWM > 255:
    Direction = -Direction
  time.sleep(1)
#pi.write(Motor1A, 0)
#pi.write(Motor1B, 1)
#pi.write(Motor1E, 1)

pi.stop()
