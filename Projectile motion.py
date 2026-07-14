import math
import matplotlib.pyplot as plt

g= 9.81
v= float (input("please enter the speed of the object "))
angle= float(input("please enter the angle of the object "))

angle_radian= math.radians(angle)
t=  (2*v*math.sin(angle_radian))/g
hmax = (v*math.sin(angle_radian))**2/ (2*g)
v_range =( v*math.cos(angle_radian)*t)
vx=v*math.cos(angle_radian)
vy=v*math.sin(angle_radian)


#print(f""" Projectile Motion Simulator --------------------------- \
 #     Flight time: {t:.3f} s \
#Maximum height: {hmax:.3f} m\
 #Range: {v_range:.3f} m """)

x_positions=[]
y_positions=[]

for i in range(int(t * 10) + 1):
    time = i * 0.1
    vx_status=vx*time
    vy_status= vy*time-((1/2)*g*time**2)
    x_positions.append(vx_status)
    y_positions.append(vy_status)

plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.text(
    v_range * 0.65,
    hmax * 0.85,
    f"Flight time: {t:.2f} s\nMaximum height: {hmax:.2f} m\nRange: {v_range:.2f} m"
)
plt.plot(x_positions,y_positions,
         color="pink",
         linewidth=2)
plt.show()

    
    


