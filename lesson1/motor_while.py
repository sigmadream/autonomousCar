import xhat as hw

print('Press ctrl + c to terminate program')
while(True):
    hw.motor_one_speed(100)
    # hw.motor_two_speed(50)


hw.motor_clean()
