'''
Find Angle MBC
Link: https://www.hackerrank.com/challenges/find-angle/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

ab = float(input())
bc = float(input())

ca = (ab**2 + bc**2)**0.5
mc = ca/2

'''
We know that, a triangle's area = 1/2 * a * b
Where:
Height (a): The height of the triangle
Base (b): The base of the triangle

Therefore, 
    0.5*ab*bc = 0.5*ca*mb
'''

mb = (ab*bc)/ca

'''
Let's say you have the lengths of the two sides:

Adjacent side (a): The side that is adjacent to the angle you want to find.
Opposite side (b): The side opposite to the angle you want to find.
The angle you're trying to find, let's call it theta, can be calculated using the arctan function (inverse tangent) as follows:

theta = arctan(b / a)
'''

'''
If you know all three side lengths of a triangle (not necessarily a right triangle), you can use the Law of Cosines to find the angles.

The Law of Cosines states:
c^2 = a^2 + b^2 - 2ab * cos(C)
'''

cos_MBC = (mb**2 + bc**2 - mc**2) / (2*mb*bc)

MBC_rad = math.acos(cos_MBC)

MBC_deg = round(math.degrees(MBC_rad))

print(f"{MBC_deg}\u00b0")