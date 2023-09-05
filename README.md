# Digital Differential Analyzer (DDA) & Bresenham Circle Algorithm (BCA)
This repository contains implementations and explanations for the DDA line drawing algorithm and the Bresenham Circle Algorithm. Both these algorithms are integral in computer graphics to draw primitives.

## Table of Contents
- [Introduction](#introduction)
- [DDA Algorithm](#dda-algorithm)
- [BCA Algorithm](#bca-algorithm)
- [Usage](#usage)
- [License](#license)
- [Contribution](#contribution)

## Introduction
Drawing lines and circles are fundamental operations in computer graphics. 
While there are various algorithms available, the DDA and Bresenham's are among the most 
popular due to their efficiency.

## DDA Algorithm
**Digital Differential Analyzer (DDA)** is an incremental scan-conversion method for rasterizing lines. 
The key idea behind the DDA algorithm is to incrementally plot points on the line between the start and end points.

> ### Key Features
- Floating point arithmetic makes it less efficient.
- Rounding operations can lead to inaccuracies.
- Simplicity makes it a good choice for hardware implementation.

## BCA Algorithm
**The Bresenham Circle Algorithm (BCA)** is an incremental circle generation algorithm which selects the nearest pixel position to complete the circle. 
BCA uses only integer addition and subtraction along with a test to know where to plot the next pixel.

> ### Key Features
- More efficient than traditional methods like using the equation of the circle due to the use of integer arithmetic.
- Produces a more accurate circle than the DDA algorithm.

## Usage
### DDA Example
```python
# Import the Digital Differential Analyzer (DDA) module
import DDA

# Define the coordinates of the first point (x1, y1) and the second point (x2, y2)
x1, y1 = 20, 20
x2, y2 = 60, 60

# Use the DDA module to draw a line between the two specified points
DDA.drawLine(x1, y1, x2, y2, show=True)
```
- `x1`, `y1`: The starting coordinates of the line.
- `x2`, `y2`: The ending coordinates of the line.
- `show` (optional): If set to True, it will display the intermediate points on the line.

### BCA Example
```python
# Import the Bresenham's Circle Algorithm (BCA) module
import BCA

# Define the radius of the circle
radius = 400

# Use the BCA module to draw a circle with the specified radius
BCA.drawCircle(radius, size=1000)
```
- `radius`: The radius of the circle.
- `center` (optional): The center coordinates of the circle. Defaults to the center of the image.
- `size` (optional): The size of the image canvas. Defaults to 1000x1000 pixels.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contribution
Feel free to fork this repository, make changes, and submit pull requests. Any contributions, no matter how minor, are greatly appreciated!
