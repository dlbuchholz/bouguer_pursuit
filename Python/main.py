from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy
from tail_recursive import tail_recursive


@dataclass
class Result:
    th0: float
    yh0: float


@dataclass
class Point:
    x: float
    y: float


N = 3 / 4  # const
pirate_plot_x = numpy.array([], dtype=float)
pirate_plot_y = numpy.array([], dtype=float)
merchant_plot_y = numpy.array([], dtype=float)
result = Result(0, 0)


# approx_p_course
# ---------------
# Recursive function which approximates course of a pirate ship tailing a merchant ship
#
# INPUT:
# k       | iterator
# t       | current time
# delta_t | time delta
# pos_h   | position of merchant ship
# pos_p   | position of pirate ship
# angle   | arctan angle of pirate ship towards merchant ship
# delta_x | delta
#
# OUTPUT: Result(th0, yh0) | time and y-coordinate of collision
@tail_recursive
def approx_p_course(k, t: float, delta_t, pos_h: Point, pos_p: Point, angle, delta_x, delta_y, epsilon):
    pos_h.y = k * N * delta_t
    t = k * delta_t

    try:
        distance = (pos_h.y - pos_p.y) / (1 - pos_p.x)
    except ZeroDivisionError:
        distance = numpy.pi / 2

    pos_p.x += delta_x
    pos_p.y += delta_y

    # update plot points
    global pirate_plot_x
    pirate_plot_x = numpy.append(pirate_plot_x, pos_p.x)
    global pirate_plot_y
    pirate_plot_y = numpy.append(pirate_plot_y, pos_p.y)
    global merchant_plot_y
    merchant_plot_y = numpy.append(merchant_plot_y, pos_h.y)

    # end function if pirate ship is way past the merchant ship and the distance between ships is never below the
    # threshold
    if pos_p.x > pos_h.x + 1:
        print("Distance is never below given epsilon threshold!")
        return None

    angle = numpy.arctan(distance)
    delta_x = delta_t * numpy.cos(angle)
    delta_y = delta_t * numpy.sin(angle)

    if (abs(pos_h.x - pos_p.x) < epsilon) and (abs(pos_h.y - pos_p.y) < epsilon):
        result.th0 = t
        result.yh0 = pos_h.y
    else:
        approx_p_course(k + 1, t, delta_t, pos_h, pos_p, angle, delta_x, delta_y, epsilon)


if __name__ == '__main__':
    position_merchants = Point(1, 0)
    position_pirates = Point(0, 0)
    t_delta_start = 0.04
    epsi = 0.15

    approx_p_course(0, 0, t_delta_start, position_merchants, position_pirates, 0, 0, 0, epsi)
    print(result)
    plt.plot(pirate_plot_x, pirate_plot_y, color='green', linestyle='dashed', linewidth=3,
             marker='.', markerfacecolor='blue', markersize=12)

    merchant_plot_x = merchant_plot_y.copy()
    merchant_plot_x.fill(1)
    plt.plot(merchant_plot_x, merchant_plot_y, color='orange', linestyle='dashed', linewidth=3,
             marker='.', markerfacecolor='red', markersize=12)                            # plot merchant ship

    plt.plot([1], [result.yh0], label="stars", color="purple", markersize=16, marker="*") # plot the position of yh0

    plt.ylim(0, 2)                   # y-axis range
    plt.xlim(0, 1.1)                 # x-axis range
    plt.xlabel('x - axis')           # naming the x axis
    plt.ylabel('y - axis')           # naming the y axis
    plt.title('Ships ships ships!')  # giving a title to my graph
    plt.show()                       # function to show the plot