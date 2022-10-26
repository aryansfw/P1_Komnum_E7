import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

class Bolzano():
    def __init__(this, interval, iterasi, persamaan=None):
        this.persamaan = persamaan
        this.interval = interval
        this.iterasi = iterasi
        this.useF = f(1)
        (this.x, this.x1, this.x2, this.x3, this.y, this.y1, this.y2) = this.setup()
        (this.fig, this.ax, this.curve, this.xl, this.xr, this.xl_point, this.xr_point) = this.init_plot()
    
    def calc_func(this, x, x1, x2, x3):
        y = y1 = y2 = y3 = 0
        if this.useF:
            y = f(x)
            y1 = f(x1)
            y2 = f(x2)
            y3 = f(x3)
        else:
            n = len(this.persamaan)
            for i in range(0, n):
                coeff = this.persamaan[i]
                y += coeff * x**(n - i - 1)
                y1 += coeff * x1**(n - i - 1)
                y2 += coeff * x2**(n - i - 1)
                y3 += coeff * x3**(n - i - 1)
        
        return y, y1, y2, y3

    def setup(this):
        x1 = this.interval[0]
        x2 = this.interval[1]
        x3 = 1
        x = np.linspace(x1, x2)

        y, y1, y2, y3 = this.calc_func(x, x1, x2, x3)

        return x, x1, x2, x3, y, y1, y2
    
    def step(this, n):
        x1 = this.x1
        x2 = this.x2
        this.x3 = (x1 + x2) / 2

        fx, fx1, fx2, fx3 = this.calc_func(this.x, x1, x2, this.x3)

        print(f"{n + 1}  {x1:.5f} {x2:.5f} {this.x3:.5f} {fx1:.5f} {fx2:.5f} {fx3:.5f}")

        if (fx1 * fx3 > 0):
            this.x1 = this.x3
        elif (fx1 * fx3 < 0):
            this.x2 = this.x3

    def init_plot(this):
        fig = plt.figure()
        epsilon = 0.5
        ax = plt.axes(xlim=(this.x1 - epsilon, this.x2 + epsilon), ylim=(this.y1, this.y2))
        curve, = ax.plot([], [], color="blue", label="f(x)")
        xl, = ax.plot([], [], color="red")
        xr, = ax.plot([], [], color="red")
        xl_point, = ax.plot([], [], marker="o", color="red", markersize="2", label="x1")
        xr_point, = ax.plot([], [], marker="o", color="green", markersize="2", label="x2")
        return fig, ax, curve, xl, xr, xl_point, xr_point

    def clear_plot(this):
        this.xl_point.set_data([], [])
        this.xr_point.set_data([], [])
        this.xl.set_data([], [])
        this.xr.set_data([], [])
        return this.xl_point, this.xr_point, this.xl, this.xr

    def animate(this, it):
        this.step(it)
        this.xl_point.set_data([this.x1], [0])
        this.xr_point.set_data([this.x2], [0])
        this.xl.set_data([this.x1, this.x1], [this.y1, this.y2])
        this.xr.set_data([this.x2, this.x2], [this.y1, this.y2])
        this.curve.set_data(this.x, this.y)
        return this.xl, this.xr, this.curve, this.xl_point, this.xr_point
    
    def plot(this):
        print("No    x1      x2      x3      f(x1)   f(x2)   f(x3)")
        animation = FuncAnimation(this.fig, this.animate, this.iterasi, this.clear_plot, interval=250, blit=True, repeat=False)
        plt.axvline(x=0, c="black")
        plt.axhline(y=0, c="black")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid()
        plt.plot()
        plt.show()
        return this.x3

def prompt():
    persamaan = None
    if f(1) == None:
        persamaan = [float(x) for x in input("Input persamaan (Misal: x + 3x - 1 = 0 -> 1 3 -1): ").split()]
        assert len(persamaan) >= 2, "Harus berupa persamaan dengan minimal 1 x."

    interval = [float(x) for x in input("Input interval (Misal: x1 = 0, x2 = 1 -> 0 1): ").split()]
    assert len(interval) == 2, "Interval harus di antara 2 x."

    iterasi = int(input("Input banyak iterasi: "))

    return persamaan, interval, iterasi

# Biarkan fungsi ini return None jika ingin memasukkan fungsi di input
# Ubah return menjadi fungsi yang diinginkan (misal: x**2 + x + 1) jika ingin fungsi yang custom
def f(x):
    return None

if __name__ == "__main__":
    (persamaan, interval, iterasi) = prompt()

    bolzano = Bolzano(interval, iterasi, persamaan) 
    akar = bolzano.plot()

    print(f"x = {akar:.5f}")