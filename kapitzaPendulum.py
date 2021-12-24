import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def kapitzaPendulum(t, x, y, g=9.8, a=0.1, v=120, l=1):
    x_out = -1 * (g + (a * (v**2) * np.cos(v*t))) * np.sin(x) / l - y
    return y, x_out

def drawOneTrajectory(startAngle=0.75*np.pi, g=9.8, a=0.1, v=120, l=1):
    trajectory = odeint(lambda y, t: np.array(kapitzaPendulum(t, y[0], y[1], g=g, a=a, v=v, l=l)),
            np.array([startAngle, 0]),
            np.linspace(0, 5, 1000))
    plt.plot(l * np.sin(trajectory[:, 0]), -l * np.cos(trajectory[:, 0]) - a * np.cos(v * np.linspace(0, 5, 1000)),
    color='blue', linewidth=0.5)

def drawTrajectories(numberOfTrajectories=200, g=9.8, a=0.1, v=120, l=1):
    plt.rcParams['figure.figsize'] = [12, 12]
    for x0 in np.linspace(-np.pi, np.pi, num=numberOfTrajectories, endpoint=False):
        drawOneTrajectory(startAngle=x0, g=g, a=a, v=v, l=l)
