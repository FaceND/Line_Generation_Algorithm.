# Bresenham’s Circle Algorithm
import PIL.Image, PIL.ImageDraw

def plot_circle_points(center, points):
    x_center, y_center = center
    translated_points = set()

    for x, y in points:
        translated_points.update([
            (x_center + x, y_center + y),
            (x_center - x, y_center + y),
            (x_center + x, y_center - y),
            (x_center - x, y_center - y),
            (x_center + y, y_center + x),
            (x_center - y, y_center + x),
            (x_center + y, y_center - x),
            (x_center - y, y_center - x)
        ])

    return translated_points

def bresenham_circle(radius):
    """
    Bresenham's circle algorithm to find points on the circle's circumference.
    """
    x = 0
    y = radius
    p = 3 - 2 * radius

    # Starting point on circle at end of radius.
    points = {(x, y)}

    # Until radius crosses line y=x, keep finding points.
    while x <= y:
        x += 1
        if p > 0:
            y -= 1
            p += 4 * (x - y) + 10
        else:
            p += 4 * x + 6

        points.add((x, y))

    return points

def drawCircle(radius, center=None, size=1000):
    """
    Draws a circle of given radius and center using PIL.
    """
    if center is None:
        center = (size//2, size//2)

    circle_graph = PIL.Image.new("RGB", (size, size), (255,255,255))
    draw = PIL.ImageDraw.Draw(circle_graph)

    raw_points = bresenham_circle(radius)
    actual_points = plot_circle_points(center, raw_points)

    for point in actual_points:
        draw.point(point, (0, 0, 0))

    circle_graph.show()