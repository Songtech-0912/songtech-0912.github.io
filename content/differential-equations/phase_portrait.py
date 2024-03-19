import numpy as np
import matplotlib.pyplot as plt

class VectorField:
    def __init__(self, f_x, f_y):
        # both of these are functions of two variables
        self.f_x = f_x
        self.f_y = f_y

    def generate_series(self, x0, x1, y0=-5, y1=5, samples=20):
        if not y0:
            y0 = x0
            y1 = x1
        x_data = np.linspace(x0, x1, samples)
        y_data = np.linspace(y0, y1, samples)
        x_grid, y_grid = np.meshgrid(x_data, y_data)
        self.x_grid = x_grid
        self.y_grid = y_grid

    def generate_vectors(self):
        u_grid = self.f_x(self.x_grid, self.y_grid)
        v_grid = self.f_y(self.x_grid, self.y_grid)
        self.u_grid = u_grid
        self.v_grid = v_grid

    def plot(self, cmap=plt.cm.jet):
        plt.xlabel("x")
        plt.ylabel("y")
        # compute magnitude
        M = np.hypot(self.u_grid, self.v_grid) + 15
        plt.streamplot(self.x_grid, self.y_grid, self.u_grid, self.v_grid, arrowsize=0)
        plt.quiver(self.x_grid, self.y_grid, self.u_grid, self.v_grid, M, cmap=cmap)
        plt.show()

if __name__ == "__main__":
    vf = VectorField(lambda x, y: y, lambda x, y: -x - y)
    vf.generate_series(-5, 5)
    vf.generate_vectors()
    vf.plot(cmap=plt.cm.viridis)
