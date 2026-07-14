import math
g= 9.81
v= float (input("please enter the speed of the object "))
angle= float(input("please enter the angle of the object "))
angle_radian= math.radians(angle)
t=  (2*v*math.sin(angle_radian))/g
hmax = (v*math.sin(angle_radian))**2/ (2*g)
v_range =( v*math.cos(angle_radian)*t)
print(f""" Projectile Motion Simulator --------------------------- \
      Flight time: {t:.3f} s \
Maximum height: {hmax:.3f} m\
 Range: {v_range:.3f} m """)
