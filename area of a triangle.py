'''
11)
Finding the Area of a Triangle
Problem Statement
Ajay, Binoy, and Chandru decide to test their geometry skills. They want to calculate the area of the triangle formed by their house coordinates. Given the coordinates of the 3 vertices of a triangle (x1,y1)(x_1, y_1)(x1​,y1​), (x2,y2)(x_2, y_2)(x2​,y2​), and (x3,y3)(x_3, y_3)(x3​,y3​), write a Python program to find the area of the triangle.
Formula
Area=1/2​∣x1​(y2​−y3​)+x2​(y3​−y1​)+x3​(y1​−y2​)∣
Input Format
Input consists of 6 integers. The first two integers correspond to (x1,y1)(x_1, y_1)(x1​,y1​). The next two integers correspond to (x2,y2)(x_2, y_2)(x2​,y2​). The last two integers correspond to (x3,y3)(x_3, y_3)(x3​,y3​).
Output Format
Refer to the Sample Input and Output for exact formatting specifications. [All floating point values are displayed correct to 2 decimal places]
Sample Input

0
0
4
0
0
3

Sample Output

The area of the triangle is 6.00
'''
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
'''
12)
 Finding the Slope of a Line
Problem Statement
Ajay and Binoy are curious about the slope of the line joining their houses. Given the coordinates of the 2 endpoints of a line (x1,y1)(x_1, y_1)(x1​,y1​) and (x2,y2)(x_2, y_2)(x2​,y2​), write a Python program to find the slope of the line.
Formula:
slope=x2​−x1/​y2​−y1​​
Input Format
Input consists of 4 integers. The first integer corresponds to x1x_1x1​. The second integer corresponds to y1y_1y1​. The third and fourth integers correspond to x2x_2x2​ and y2y_2y2​ respectively.
Output Format
Refer to the Sample Input and Output for exact formatting specifications. [All floating point values are displayed correct to 2 decimal places]
Sample Input

1
2
3
6

Sample Output

The slope of the line joining Ajay's house and Binoy's house is 2.00

'''
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x2 != x1:
    slope = (y2 - y1) / (x2 - x1)
    print(f"The slope of the line joining Ajay's house and Binoy's house is {slope:.2f}")
else:
    print("The line is vertical, slope is undefined")
'''

'''
