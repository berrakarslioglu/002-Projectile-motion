# 🚀 Projectile Motion Graph Simulator

A Python program that calculates and visualizes the motion of a projectile launched from ground level.

## Features

- Calculates flight time
- Calculates maximum height
- Calculates horizontal range
- Visualizes the projectile trajectory
- Accepts user-defined initial speed and launch angle
- Displays the calculated results directly on the graph

## Physics

The simulation assumes:

- No air resistance
- Constant gravitational acceleration of `9.81 m/s²`
- Launch from ground level
- Two-dimensional projectile motion

The program uses the horizontal and vertical components of the initial velocity to calculate the projectile's position over time.

## Technologies

- Python
- `math`
- `matplotlib`

## Example Input

```text
Initial speed: 20
Launch angle: 45
```

## Example Results

```text
Flight time: 2.883 s
Maximum height: 10.194 m
Range: 40.775 m
```
<img width="899" height="542" alt="image" src="https://github.com/user-attachments/assets/0c853389-ff7a-4100-a389-cf72956236d0" />


The program also generates a trajectory graph showing the horizontal distance and height of the projectile.

## Future Improvements

- Trajectory animation
- Air resistance
- Initial height option
- Multiple launch angle comparison
