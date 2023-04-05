

def turn(deg):
    gyro.reset_angle(0)
    if(deg > 0)
        while(gyro.angle > deg)
        right.run(5)
    elif(deg < 0)
        while(gyro.angle < deg)
        right.run(-5)