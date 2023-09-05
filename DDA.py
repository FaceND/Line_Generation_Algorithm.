# DDA Algorithm [ straight line ]
import matplotlib.pyplot as plt

def dda_line_algorithm(x1, y1, x2, y2):
    """
    Compute the DDA line coordinates from (x1, y1) to (x2, y2)
    """
    points = []  # List to store the points on the line
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    x_increment = dx / steps if steps > 0 else 0
    y_increment = dy / steps if steps > 0 else 0

    x = float(x1)
    y = float(y1)

    for _ in range(steps + 1):
        points.append((round(x,2), round(y,2)))  # Add the current point to the list
        x += x_increment
        y += y_increment

    return points

def drawLine(x1, y1, x2, y2, show=False):
    points = dda_line_algorithm(x1, y1, x2, y2)
    if show:
        for x, y in points:      
            print(f'x: {x}    y: {y}')

    x_coordinates, y_coordinates = zip(*points)
    plt.plot(x_coordinates, y_coordinates, color='red')

    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("DDA Algorithm")
    plt.grid(True)
    plt.show()

    return points