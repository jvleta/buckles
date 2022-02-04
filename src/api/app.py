import numpy as np
import matplotlib.pyplot  as plt
from dataclasses import dataclass, asdict

@dataclass
class BuckledConfiguration(object):
    x: np.ndarray
    y: np.ndarray

def plot(config: BuckledConfiguration):
    plt.figure()
    plt.plot(config.x, config.y)
    plt.show()


class Beam(object):

    def getdata(self, num_points, mode_number=1):
        x = np.linspace(0, 1, num_points)
        y = np.sin(mode_number * np.pi * x)
        return BuckledConfiguration(x, y)

if __name__ == "__main__":
    beam = Beam()
    result = beam.getdata(100, 2)
    plot(result)
