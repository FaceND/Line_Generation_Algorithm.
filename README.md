# Digital Differential Analyzer (DDA) & Bresenham Circle Algorithm (BCA)
DDA and BCA algorithms are essential tools in the field of computer graphics, 
offering different advantages for rendering lines and circles with varying degrees of complexity and precision. 
The choice between them depends on the specific requirements of the graphics task at hand.

## Table of Contents
- [Introduction](#introduction)
- [DDA Algorithm](#dda-algorithm)
- [BCA Algorithm](#bca-algorithm)
- [Example](#example)
- [Contribution](#contribution)
- [License](#license)

## Introduction
Drawing lines and circles are fundamental operations in computer graphics. 
While there are various algorithms available, the DDA and Bresenham's are among the most 
popular due to their efficiency.

## DDA Algorithm
> ### Description
**Digital Differential Analyzer (DDA)** is a fundamental method in computer graphics used for rendering lines and other linear shapes on a digital screen. 
It's a simple and straightforward approach for generating points along a line between two given coordinates. 
The DDA Algorithm calculates each pixel's position along the line by incrementing the x and y coordinates in small steps.

> ### Key Features
- **Simplicity**: DDA is easy to understand and implement, making it a great choice for beginners in computer graphics.
- **Straight Lines**: It is primarily used for drawing straight lines but can be extended for drawing other shapes by connecting line segments.
- **Efficiency**: DDA uses integer arithmetic and only requires additions and truncations, which makes it computationally efficient.

> ### Applications
The DDA algorithm is widely used in computer graphics, including rasterization of lines, generating digital images, and rendering vector graphics. 
It serves as the foundation for many graphics primitives and is essential in rendering 2D and 3D graphics.

## BCA Algorithm
> ### Description
**The Bresenham Circle Algorithm (BCA)** Bresenham's Circle Algorithm (BCA) is a highly efficient method used for drawing circles on a pixel grid. 
It was developed by Jack E. Bresenham and is an extension of Bresenham's line drawing algorithm. 
BCA is particularly valuable for applications where performance is critical.

> ### Key Features
- **Efficiency**: BCA is known for its speed and efficiency because it relies solely on integer calculations, avoiding costly floating-point operations.
- **Precision**: The algorithm produces highly accurate results, ensuring that each pixel plotted is as close as possible to the true circle.
- **Symmetry**: BCA takes advantage of the symmetry of circles, reducing calculations to only one-eighth of the circle and mirroring the results to complete the circle.

> ### Applications
Bresenham's Circle Algorithm is commonly used in computer graphics, image processing, and games for rendering circles, curved shapes, and circular objects. 
Its efficient and accurate nature makes it a preferred choice for graphics rendering when drawing circles or circular patterns.

## Example
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

## Contribution
Feel free to fork this repository, make changes, and submit pull requests. Any contributions, no matter how minor, are greatly appreciated!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
