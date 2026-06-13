# track position, velocity, and time
import numpy as np

g = -9.81 # downward, negative

def simulate_projectile(initial_x,
                        initial_y,
                        v0,
                        angle):

    rad = np.radians(angle)

    # velocity components
    v_x = v0 * np.cos(rad)
    v_y = v0 * np.sin(rad)

    x = initial_x
    y = initial_y

    t = 0
    dt = 0.01

    trajectory = []
    trajectory.append((t,x,y))

    while y >= 0:
        # store current state
        trajectory.append(x)
        trajectory.append(y)
        trajectory.append(t)

        # update position
        x += v_x * dt
        y += v_y * dt

        # update velocity
        v_y += g * dt
        
        # update time
        t += dt

    return x, y, t